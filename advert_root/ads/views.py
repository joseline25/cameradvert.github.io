from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import DetailView

from .models import *
from .forms import *

# Create your views here.
#.discussion_set.all()

def indexforum(request):
    threads = Thread.objects.all()
    count = threads.count()
    discussions = []
    for i in threads:
        discussions.append(i)
    context = {'forums': threads,
               'count': count,
               'discussions': discussions
              }
    return render(request, 'indexforum.html', context)


def newthread(request):
    form = createThread()
    if request.method == 'POST':
        form = createThread(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('indexforum')
    context = {'form': form}
    return render(request, 'newthread.html', context)


def newcomment(request, id):
    form = createComment()
    comments = Comment.objects.filter(thread_id=id)
    user = request.user
    thread = Thread.objects.get(id=id)
    print(user)
    if request.method == 'POST':
        form = createComment(request.POST)
        if form.is_valid():
            thread = Thread.objects.get(id=id)
            coment = Comment(text=form.cleaned_data.get('text'), thread_id=thread, user_id=request.user)
            coment.save()
            return redirect('newcomment', id)
    context = {'form': form, 'comments': comments, 'user':user, 'thread':thread}
    return render(request, 'newcomment.html', context)


def searchbar(request):
    if request.method == 'POST':
        search = request.POST.get('search')
        posts = Thread.objects.filter(subject__contains=search).order_by('creator')
        return render(request, 'searchbar.html', {'posts': posts})


"""
def interested(request, id):
    ads = Thread.objects.get(id=id)
    user= User.objects.get(id=request.user.id)
    ads.interested.add(user)
    print(ads.interested)
    return redirect("interested",  id)

    #return HttpResponseRedirect(reverse('details', args=[str(id)]))
"""

def LikeView(request, id):
    ads = get_object_or_404(Thread, id=request.POST.get('thread_id'))
    ads.interested.add(request.user)
    return HttpResponseRedirect(reverse('indexforum',args=[str(id)]))

class BlogPostDetailView(DetailView):
    model = Thread
    # template_name = detail.html
    # context_object_name = 'object'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        interested_connected = get_object_or_404(Thread, id=self.kwargs['pk'])
        liked = False
        if interested_connected.interested.filter(id=self.request.user.id).exists():
            liked = True
        data['number_interested'] = interested_connected.number_of_interested()
        data['post_interest'] = liked
        return data


def delete(request, id):
    element_to_delete = Thread.objects.get(id=id)
    element_to_delete.delete()
    return redirect('indexforum')