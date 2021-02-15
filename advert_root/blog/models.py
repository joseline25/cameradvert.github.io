from django.db import models
from django.contrib.auth.models import User
from user_auth.models import Profile



# Create your models here.
from user_auth.models import Profile


class Category(models.Model):
    name = models.CharField(max_length=20)


    def __str__(self):
        return str(self.name)

class Post(models.Model):
    title = models.CharField(max_length=300)
    body = models.TextField()
    imagepost = models.ImageField(upload_to='upload/', blank=True, null=True)
    created_on = models.DateTimeField(auto_now=True)
    last_modified = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, related_name='post_likes', blank=True)
    categories = models.ManyToManyField('Category', related_name='posts')
    creator = models.ForeignKey(Profile, related_name='post_creator', on_delete=models.CASCADE, null=True)


    def __str__(self):
        return str(self.title)+',  ' + str(self.imagepost)


class Comment(models.Model):
    author = models.CharField(max_length=50)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return str(self.author)+',  ' + str(self.body)