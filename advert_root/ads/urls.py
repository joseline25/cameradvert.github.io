from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.indexforum, name='indexforum'),
    path('newthread/', views.newthread, name='newthread'),
    path('newcomment/<int:id>', views.newcomment, name='newcomment'),
    path('searchbar/', views.searchbar, name='searchbar'),
    path('interested/<int:id>', LikeView, name='interested'),
    path('delete/<int:id>', views.delete, name='delete'),
]

#path('interested/<int:id>', views.interested, name='interested'),