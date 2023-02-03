from django.shortcuts import render,redirect
from django.contrib.auth.models import User 
from .models import *
from django.contrib.auth import authenticate , login , logout
#create login page

def User_login(e):
    if e.method == 'POST':
        username = e.POST['username']
        password = e.POST['password']
        user = authenticate(e,username=username,password=password)
        if user is not None:
            login(e,user)
            return render(e,"auth/login.html",{
                "user":user,
            })
        else:
            return render(e,'auth/login.html',{})
    else: 
        return render(e,"auth/login.html",{
                
            })

def Logout(e):
    logout(e)
    return redirect("login")