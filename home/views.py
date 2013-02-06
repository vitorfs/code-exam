# coding: utf-8
from django.contrib import messages
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from exams.models import UserExam
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as django_login, logout as django_logout

def home(request):
    context = RequestContext(request)
    return render_to_response('home/index.html', context)

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                django_login(request, user)
                return redirect('/')
            else:
                messages.add_message(request, messages.ERROR, 'Sua conta foi desativada.')
                context = RequestContext(request)
                return render_to_response('home/login.html', context)
        else:
            messages.add_message(request, messages.ERROR, 'Usuário ou senha inválido.')
            context = RequestContext(request)
            return render_to_response('home/login.html', context)
    else:
        context = RequestContext(request)
        return render_to_response('home/login.html', context)

def logout(request):
    django_logout(request)
    return redirect('/login/')