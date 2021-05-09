from django.shortcuts import render
from .models import News
from .models import AboutProduct

def post_list(request):
    posts = News.objects.all()
    return render(request, 'main/post_list.html', {'posts': posts})

def index(request):
    posts = News.objects.all()
    return render(request, 'main/index.html', {'posts': posts})

def about(request):
    products = AboutProduct.objects.all()
    return render(request, 'main/about.html', {'products': products})

def library(request):
    return render(request, 'main/library.html')

def account(request):
    return render(request, 'main/personalaccount.html')