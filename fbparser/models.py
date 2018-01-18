from django.db import models

class FeedPost(models.Model):
    facebook_post_id = models.IntegerField(verbose_name="ID поста на Facebook")
    title = models.TextField(verbose_name="Название", default="")
    content = models.TextField(verbose_name="Контент поста")
    desc = models.TextField(verbose_name="Краткое описание", default='')
    date = models.DateTimeField(verbose_name="Дата")
    is_published = models.BooleanField(default=False, verbose_name="Публиковать в Яндекс.Дзен?")

    def __str__(self):
        return self.content[0:50]

    def facebookpost(self):
        return 'https://www.facebook.com/moveax3/posts/'+str(self.facebook_post_id)

    class Meta:
        verbose_name = "Пост со страницы пользователя"
        verbose_name_plural = "Посты со страницы пользователя"
