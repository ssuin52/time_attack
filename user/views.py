
from django.shortcuts import render, redirect
from .models import UserModel
from django.contrib.auth.decorators import login_required
from django.contrib import auth



# Create your views here.
def sign_up_view(request):
    if request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return redirect('/')
        else:
            return render(request, 'user/signup.html')
    elif request.method == 'POST':
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        phone = request.POST.get('phone','')
        address = request.POST.get('address','')
        UserModel.objects.create_user(username=username, password=password, phone=phone, address=address)
        return redirect('/login')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        
        me = auth.authenticate(request, username=username, password=password)
        if me is not None:
            auth.login(request, me)
            return redirect('/')
        else:
            return render(request,'user/home.html')
        
    elif request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return redirect('/')
        else:
            return render(request, 'user/login.html')

@login_required   
def home_view(request):
    user = request.user.is_authenticated
    if user:
        return redirect('/')
    else:
        return redirect('/login')

@login_required        
def logout(request):
    auth.logout(request)
    return redirect('/')