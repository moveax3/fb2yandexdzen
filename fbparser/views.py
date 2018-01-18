from django.shortcuts import render
from .models import FeedPost

def yandex_dzen(request):
    return render(
        request,
        'dzen.xml',
        {'posts': FeedPost.objects.filter(is_published=True).order_by('-date')},
        content_type='text/xml',
     )
