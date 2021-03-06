from django.db import models
from django.urls import reverse

class Post(models.Model):
  title=models.CharField(u'案號',max_length=200)
  author=models.ForeignKey('auth.User',on_delete=models.CASCADE)
  body=models.TextField(u'內文')
  pubdate = models.DateTimeField(u'發佈時間',null=True)

  def __str__(self):
    return self.title

  def get_absolute_url(self):
    return reverse("post:post_detail",args={str(self.id)})