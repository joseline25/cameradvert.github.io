from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),


    path('users/', views.users_list, name='users_list'),
    path('users/<slug>/', views.profile_view, name='profile_view'),
    path('friends/', views.friend_list, name='friend_list'),
    path('users/friend-request/send/<int:id>/', views.send_friend_request, name='send_friend_request'),
    path('users/friend-request/cancel/<int:id>/', views.cancel_friend_request, name='cancel_friend_request'),
    path('users/friend-request/accept/<int:id>/', views.accept_friend_request, name='accept_friend_request'),
    path('users/friend-request/delete/<int:id>/', views.delete_friend_request, name='delete_friend_request'),
    path('users/friend/delete/<int:id>/', views.delete_friend, name='delete_friend'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('my-profile/', views.my_profile, name='my_profile'),
    path('search_users/', views.search_users, name='search_users'),
    

]

