from django.shortcuts import render
from django.contrib.auth.models import User, auth
from rest_framework.decorators import api_view
from django.contrib import messages
from django.shortcuts import redirect,render
# Create your views here.

@api_view(['GET','POST'])
def login(request):
    if request.method=='GET':
        return render(request,'login.jinja')
    else:
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Invalid Credentials")
            return redirect('/auth/login')
@api_view(['GET','POST'])
def signup(request):
    if request.method=='GET':
        return render(request,'signup.jinja')
    else:
        firstName=request.POST['firstName']
        lastName=request.POST['lastName']
        email=request.POST['email']
        username=request.POST['username']
        password=request.POST['password']
        if not User.objects.filter(username=username).exists() or not User.objects.filter(email=email).exists():
            user=User.objects.create_user(first_name=firstName,email=email,password=password,last_name=lastName,username=username)
            user.save()
            messages.info(request,'Now Pleaes login with your credentials')
            return redirect('/auth/login')
        else:
            messages.info(request,'Username or Email Exists')
            return redirect('/auth/signup')
        return redirect('/')

@api_view(['GET'])
def logout(request):
    auth.logout(request)
    return redirect('/')