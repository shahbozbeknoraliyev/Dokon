from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import *
from django.views import View
from django.contrib.auth import authenticate,login,logout
class LoginView(View):
    def get(self,request):
        return render (request,"home.html")
    def post(self,request):
        foydalanuvchi=authenticate(username=request.POST.get('l'),
                                   password=request.POST.get('p'))
        if foydalanuvchi:
            login(request,foydalanuvchi)
            return redirect("/bolim/")
        return redirect('/')
class LogoutView(View):
    def get(self,request):
        logout(request)
        return redirect('/')

class