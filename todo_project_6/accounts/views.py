from django.contrib import auth, messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from . forms import  CreateUserForm
# Create your views here.

def login(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        # find out if any such user is present
        # login the user
        # send that user to there dashboard
        # password in admin it saved as a hash we cant compare it by our logic so use the inbuilt methods
        # that django provides

        user=authenticate(request,username=username,password=password)# does't log the user just this method checks any such username exists
                                                                # if exists check if the password matches
                                                                #if exist it give me back the user object
                                                                #it return user object if exist or null for not exist
        if user is not None:  #some user is available to us
            auth_login(request,user)
            return  redirect('dashboard')
        else:
            messages.error(request,"user or password is incorrect")
    return render(request,'accounts/login.html')

def register(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    if request.method=="POST":
        form=CreateUserForm(data=request.POST)
        if form.is_valid():
            user=form.save()
            #login and authenticate this user
            return redirect('login')

    else:
        form=CreateUserForm()
    return render(request,'accounts/register.html',{
        'form':form
    })

def logout(request):
    auth_logout(request)
    return redirect('login')