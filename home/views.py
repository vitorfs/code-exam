# coding: utf-8
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from exams.models import UserExam
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as django_login, logout as django_logout

def homepage(request):
    if request.user.is_authenticated():
        user_exam_list = UserExam.objects.filter(user__id=request.user.id)
        context = RequestContext(request, {'user_exam_list': user_exam_list,})
        return render_to_response('index.html', context)
    else:
        return redirect('/login/')

def prova(request, exam_id):
    user_exam = UserExam.objects.get(pk=int(exam_id))
    context = RequestContext(request, { 'user_exam': user_exam })
    return render_to_response('home/exam.html', context)


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
                context = RequestContext(request, {'message': 'Conta inativa',})
                return render_to_response('home/login.html', context)
        else:
            context = RequestContext(request, {'message': 'Usuário ou senha inválido',})
            return render_to_response('home/login.html', context)
    else:
        context = RequestContext(request)
        return render_to_response('home/login.html', context)

def logout(request):
    django_logout(request)
    return redirect('/login/')