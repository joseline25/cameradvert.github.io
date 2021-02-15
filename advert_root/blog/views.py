from django.shortcuts import render, redirect

from .forms import *
from .models import *


# Create your views here.

# the first view : display the list of all your post

def index(request):
    posts = Post.objects.all().order_by('-created_on')
    context = {'posts': posts}
    return render(request, 'indexblog.html', context)

# the second view : display the full post with comments plus a form to allow users to input new comments

def details(request, id):
    post = Post.objects.get(id=id)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(author=form.cleaned_data["author"], body=form.cleaned_data["body"], post=post)
            comment.save()
    comments = Comment.objects.filter(post=post)
    context = {'post': post,
               'comments': comments,
               'form': form}
    return  render(request, 'details.html', context)


#  the third view will display all the posts of a specific category

def category(request, category):
    posts = Post.objects.filter(categories__name__contains=category).order_by('-created_on')
    context = {'category': category,
               'posts': posts}
    return render(request, 'category.html', context)


# The fourth view add a new post


def addpost(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {'form': form}
    return render(request, 'indexblog.html', context)