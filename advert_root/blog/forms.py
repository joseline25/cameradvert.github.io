from django import forms
from .models import *

class CommentForm(forms.Form):
    author = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': "form-control",
                                                                          'placeholder': "Enter your name"}))
    body = forms.CharField(widget=forms.Textarea(attrs={'class': "class-control", 'placeholder': "Leave a comment!"}))




class PostForm(forms.ModelForm):
    title = forms.CharField(max_length=300, widget=forms.TextInput(attrs={'class': "form-control",
                                                                          'placeholder': "Title of the new post!"}))

    body = forms.CharField(widget=forms.Textarea(attrs={'class': "class-control", 'placeholder': "Content"}))

    class Meta:
        model = Post
        exclude = ["likes", "creator"]