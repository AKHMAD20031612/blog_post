from django.shortcuts import render
from django.views.generic import TemplateView
posts = [
    {
        'author': 'akhmad',
        'title': 'blogpost1',
        'content': 'kun.uz',
        'pub_date': 'December 16, 2003',
    },
    {
        'author': 'sardor',
        'title': 'blogpost2',
        'content': 'daryo.uz',
        'pub_date': 'january 1, 2002',
    },
]


def home(request):
    contexts = {
        'posts': posts
    }
    return render(request, 'blogpost/home.html', contexts)


def about(request):
    return render(request, 'blogpost/about.html', {'title': 'About'})
