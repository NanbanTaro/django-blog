from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

title = '開発者ブログ'

def index(request):
    posts = Post.objects.all()
    params = {
        'title': title,
        'posts': posts
    }
    return render(request, 'blog/index.html', params)

def detail(request, post_id):
    post = Post.objects.get(id=post_id)
    params = {
        'title': title,
        'id': post_id,
        'post': post
    }
    return render(request, 'blog/detail.html', params)

def introduction(request):
    params = {
        'title': title,
    }
    return render(request, 'blog/introduction.html', params)
