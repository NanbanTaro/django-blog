from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    params = {
        'title': 'テストページ',
        'message': 'テストページです。'
    }
    return render(request, 'blog/index.html', params)

def detail(request):
    params = {
        'title': '詳細ページ',
        'message': '詳細ページです。'
    }
    return render(request, 'blog/detail.html', params)
