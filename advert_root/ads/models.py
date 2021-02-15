from django.db import models
#from card.profiles.models import *
from django.contrib.auth.models import User
from user_auth.models import Profile

# Create your models here.

# trouver le moyen d'importer les modèles de profiles dans forums



class Thread(models.Model):
    subject = models.CharField(max_length=300)
    creator = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    imagepost = models.ImageField(upload_to='upload/', blank=True, null=True)
    interest_count = models.IntegerField(blank=True, default=0)
    interested = models.ManyToManyField(User, blank=True, related_name='interested_users')


    def number_of_interested(self):
        return self.interested.count()
    

    @property
    def image_url(self):
        if self.imagepost and hasattr(self.imagepost, 'url'):
            return self.imagepost.url


    def __str__(self):
        return str(self.subject)



class Comment(models.Model):
    text = models.TextField()
    thread_id = models.ForeignKey('Thread', related_name='thread', on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)




    def __str__(self):
        return str(self.thread_id)