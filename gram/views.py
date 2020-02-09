from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import 
from django.core.mail import send_mail
from .models import Profile, Comment, Post
# Create your views here.

@login_required(login_url='/login/')
def Index(request):
    current_user = request.user
    posts = Post.get_posts()
    comments = Comment.get_comments()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            