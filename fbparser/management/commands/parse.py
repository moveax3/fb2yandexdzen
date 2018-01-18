import ipdb
from django.core.management.base import BaseCommand, CommandError
from fbparser.models import FeedPost
from fbparser.userfeedparser import FacebookUserFeedParser
from django.conf import settings
from bs4 import BeautifulSoup
import datetime

class Command(BaseCommand):
    help = 'Parse facebook user page'

    def add_arguments(self, parser):
        parser.add_argument("command")

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Start parsing process...'))
        user_feed_parser = FacebookUserFeedParser(settings.FACEBOOK_USER, settings.FACEBOOK_PASSWORD, settings.FACEBOOK_PROFILE)
        for post in reversed(user_feed_parser.result):
            try:
                FeedPost.objects.get(facebook_post_id=int(post['fbid']))
                self.stdout.write(self.style.SUCCESS('Post elready saved'))
            except:
                soup = BeautifulSoup(post['fbpost'].replace('</p> ,<p>', '</p><p>'), 'html.parser')
                post_content = ''
                for tag in soup.findAll('p'):
                    post_content += '<p>'+tag.text+'</p>'
                post_date = datetime.datetime.now()
                post_title = ' '.join(soup.text.split(' ')[0:5]).replace('[', '')
                post_description = ' '.join(soup.text.split(' ')[0:10]).replace('[', '')
                newpost = FeedPost(facebook_post_id=int(post['fbid']), title=post_title, content=post_content, desc=post_description, date=post_date)
                newpost.save()
                self.stdout.write(self.style.SUCCESS('Success save post with id: '+post['fbid']))

        self.stdout.write(self.style.SUCCESS('Parsing process success'))
