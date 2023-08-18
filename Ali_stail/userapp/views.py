from django.contrib.auth import authenticate, logout, login
from django.shortcuts import render, redirect
from django.views import View
from .models import *


class LoginView(View):
    def get(self, request):
        return render(request, 'page-user-login.html')
    def post(self, request):
        user = authenticate(
            username = request.POST.get('l'),
            password = request.POST.get('p')
        )
        if user is None:
            return redirect('login')
        login(request, user)
        return redirect('home')
        # return render(request, 'page-user-login.html')

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/')

class RegisterView(View):
    def get(self, request):
        return render(request, 'page-user-register.html')
    def post(self, request):
        if request.POST.get('p')==request.POST.get('pt'):
            user = User.objects.create_user(
                username=request.POST.get('fn'),
                password=request.POST.get('p'),
                email=request.POST.get('email')
            )
            Profil.objects.create(
                ism = request.POST.get('fn'),
                jins = request.POST.get('jins'),
                shahar = request.POST.get('shahar'),
                viloyat = request.POST.get('viloyat'),
                user = user
            )
            return redirect('/home')

class ProfAddView(View):
    def get(self, request):
        content={
            'userInfo': Profil.objects.get(user=request.user)
        }
        return render(request, 'page-profile-main.html', content)

