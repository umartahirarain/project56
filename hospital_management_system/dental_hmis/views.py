from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='login')
def HomePage(request):
    return render (request,'404.html')


def LoginPage(request):
    if request.method=='POST':
        email=request.POST.get('email')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=email,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return render (request,'404.html')

    return render (request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')


