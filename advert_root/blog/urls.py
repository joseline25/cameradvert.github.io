from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('details/<int:id>', views.details, name='details'),
    path('category/<str:category>', views.category, name='category'),
    path('addpost', views.addpost, name='addpost'),

]

