from django.shortcuts import render
from django.http import HttpResponse

title = '開発者ブログ'

def index(request):
    params = {
        'title': title,
        'message': 'テストページです。'
    }
    return render(request, 'blog/index.html', params)

def detail(request):
    params = {
        'title': title,
        'message': '詳細ページです。'
    }
    return render(request, 'blog/detail.html', params)

def introduction(request):
    params = {
        'title': title,
    }
    return render(request, 'blog/introduction.html', params)
