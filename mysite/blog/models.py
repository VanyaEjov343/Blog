from django.db import models






class Post(models.Model):
    title = models.CharField(max_length=200)
    datetime = models.DateTimeField(u'Дата публикации')
    content = models.TextField(max_length=10000)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/blog/%i/" %self.id

class UserFollowing(models.Model):
    user_id = models.ForeignKey('User', on_delete=models.PROTECT, related_name='following')
    following_user_id = models.ForeignKey('User', on_delete=models.PROTECT, related_name='followers')
    created = models.DateTimeField(auto_now_add=True)

