from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime
from webber.models import Post

from django.http import HttpResponse
from django.contrib import auth


def judge(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        auth.login(request, user)
        return HttpResponseRedirect('/board/')
    else:
        return render(request, 'login.html', locals())


def login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('http://127.0.0.1:8080/#/bord')


def board(request):
    judge(request)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/login/')

