from django.shortcuts import render, redirect
from django.views import View
from django.contrib import auth
from django.contrib.auth import authenticate
from .models import User

class Register(View):

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('/')
        return render(request, 'accounts/register.html')
    
    def post(self, request):
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(email=email, password=password).exists():
            # Send message already exist user
            return render(request, 'accounts/register.html')

        user = User.objects.create_user(email=email, password=password)
        user.save()

        return render(request, 'accounts/login.html')


class Login(View):

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('/')
        return render(request, 'accounts/login.html')
    
    def post(self, request):
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(email=email, password=password)
        if user:
            auth.login(request, user)
            return redirect('/')
        return render(request, 'accounts/login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')