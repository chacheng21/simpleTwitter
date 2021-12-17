from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tweet(models.Model):
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, )
    likes = models.ManyToManyField(User, default=None, blank=True, related_name='likes', editable=False)

LIKE_CHOICES = {
    ('Like', 'Like'),
    ('Unlike', 'Unlike')
}

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'user')
    tweet = models.ForeignKey(Tweet, on_delete = models.CASCADE, related_name = 'tweet')
    value = models.CharField(choices=LIKE_CHOICES, default='Like', max_length=10)

class Tag(models.Model):
    tag = models.TextField()
    tweets = models.ManyToManyField(Tweet, default=None, blank=True, related_name='hashtag', editable=False)
