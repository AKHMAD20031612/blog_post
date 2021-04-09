from django.shortcuts import render
from .models import Post
# from django.views.generic import TemplateView


def home(request):
    contexts = {
        'posts': Post.objects.all()
    }
    return render(request, 'blogpost/home.html', contexts)


def about(request):
    return render(request, 'blogpost/about.html', {'title': 'About'})
