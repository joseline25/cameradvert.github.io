import autoslug
from django.db import models
from django.contrib.auth.models import User
#from ads.models import Thread
from autoslug import AutoSlugField
from django.db.models.signals import post_save
from django.conf import settings
import os


# Create your models here.


Profiles_Choices = (
    ("Per",'Personal'),
    ("Pro",'Professional'),
    ("Ent",'Enterprise'),
    ("PME",'Small Business'),
    ("Bus",'Business'),
    ("Org",'Organization'),
    ("Mag",'Magazine'),
)

class Profile(models.Model):
    type = models.CharField(max_length=50, choices=Profiles_Choices, default="Per")
    picture = models.ImageField(upload_to='upload/', blank=True, null=True )
    profile_bio = models.TextField(null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    location = models.CharField(max_length=100, null=True, blank=True)
    slug = autoslug.AutoSlugField(populate_from='user', null=True)
    created = models.DateTimeField(auto_now=True)
    #ad = models.ManyToManyField(Thread, related_name='interrested')
    friends = models.ManyToManyField("Profile", blank=True, related_name='profile_friends')



    def __str__(self):
        return self.user.username

    def get_absolute_url(self):

    	return "/user_auth/{}".format(self.slug)


def post_save_user_model_receiver(sender, instance, created, *args, **kwargs):
    if created:
        try:
            Profile.objects.create(user=instance)
        except:
            pass
        


post_save.connect(post_save_user_model_receiver, sender=settings.AUTH_USER_MODEL)


class FriendRequest(models.Model):
	to_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='to_user', on_delete=models.CASCADE)
	from_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='from_user', on_delete=models.CASCADE)
	timestamp = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return "From {}, to {}".format(self.from_user.username, self.to_user.username)






	
