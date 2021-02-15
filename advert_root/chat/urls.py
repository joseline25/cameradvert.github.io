from django.urls import path
from .views import *


urlpatterns = [
   	path('', inbox, name='inbox'),
   	path('directs/<username>', directs, name='directs'),
   	path('new/', usersearch, name='usersearch'),
   	path('new/<username>', newconversation, name='newconversation'),
   	path('send/', senddirect, name='send_direct'),

]