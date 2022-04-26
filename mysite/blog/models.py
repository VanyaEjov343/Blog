from django.db import models

# Create your models here.



class Post(models.Model):
    title = models.CharField(max_length=200)
    datetime = models.DateTimeField(u'Дата публикации')
    content = models.TextField(max_length=10000)
    
    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/blog/%i/" %self.id
