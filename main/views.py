from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import UserForm, UserProfileForm
from courses.models import *

def p_account(request):
    s = User.objects.filter(id=request.user.id)
    information = UserProfile.objects.filter(user=request.user)
    return render(request, 'main/personalaccount.html', {'information': information, 's': s})

def p_account_edit(request):
    if request.method == "POST":
        form = UserProfileForm(request.POST)
        
        print(request.POST)
        if form.is_valid():
            form.save()
            return redirect('p_account')
        else:
            return render(request, 'main/personalaccount.html', { 'form': form })
    else:
        form = UserForm()
        return render(request, 'main/personalaccount.html', { 'form': form })

def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'main/login.html', {'invalid':True})
    else:
        return render(request, 'main/login.html', {'invalid':False})

def user_logout(request):
    logout(request)
    return redirect('login')

def user_registration(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            mainCycle = UserProfile()
            mainCycle.user = user
            mainCycle.save()
            user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'main/registration.html', {'invalid':True, 'form': form})
    else:
        form = UserForm()
        return render(request, 'main/registration.html', {'invalid':False, 'form': form})

def index(request):
    posts = News.objects.filter(is_published=True).order_by('-created_date')
    user = User.objects.filter(id=request.user.id)
    if len(user) > 0:
        mainCycle = UserProfile.objects.filter(user=request.user)[0]
        chels = UserProfile.objects.filter(user=request.user)
        for chel in chels:
            courses = Course.objects.filter(role=chel.role)
        context = {
        'posts': posts,
        'user':user[0], 
        'mainCycle':mainCycle,
        'courses': courses
        }
        return render(request, 'main/index.html', context=context)
    else:
         return redirect('login')

def menu(request):
    products = AboutProduct.objects.all()
    return render(request, 'main/about.html', {'products': products})

def library(request):
    return render(request, 'main/library.html')