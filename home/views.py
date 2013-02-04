# coding: utf-8
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from exams.models import UserExam, Question, Answer, UserExamAnswers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as django_login, logout as django_logout

def homepage(request):
    if request.user.is_authenticated():
        user_exam_list = UserExam.objects.filter(user__id=request.user.id)
        context = RequestContext(request, {'user_exam_list': user_exam_list,})
        return render_to_response('index.html', context)
    else:
        return redirect('/login/')

def exam(request, exam_id):
    user_exam = UserExam.objects.get(pk=exam_id)
    if (request.user.id == user_exam.user.id):
        context = RequestContext(request, { 'user_exam': user_exam })
        return render_to_response('home/exam.html', context)
    else:
        context = RequestContext(request, {'message_severity': 'error', 'message': 'Usuário sem permissão para acessar prova.'})
        return render_to_response('home/exam.html', context)

def question(request, exam_id, question_id):
    user_exam = UserExam.objects.get(pk=exam_id)
    if (request.user.id == user_exam.user.id):
        question = Question.objects.get(pk=question_id)
        answers = Answer.objects.filter(question__id=question_id)
        try:
            user_answer = UserExamAnswers.objects.get(user_exam__id=exam_id, question__id=question_id)
        except:
            user_answer = None
        context = RequestContext(request, { 'user_exam': user_exam, 
            'question': question, 
            'answers': answers, 
            'user_answer': user_answer, 
            })
        return render_to_response('home/question.html', context)
    else:
        context = RequestContext(request, {'message_severity': 'error', 'message': 'Usuário sem permissão para acessar prova.'})
        return render_to_response('home/exam.html', context)

def send_answer(request):
    if request.method == 'POST':
        user_exam_id = request.POST['user-exam-id']
        question_id = request.POST['question-id']
        answer_id = request.POST['rb-answer']

        user_exam_answer = UserExamAnswers.objects.filter(user_exam__id=user_exam_id, question__id=question_id)
        user_exam_answer.delete()

        user_exam_answer = UserExamAnswers(user_exam=UserExam(id=user_exam_id), question=Question(id=question_id), closed_answer=Answer(id=answer_id))
        user_exam_answer.save()

        return HttpResponse('sucesso')

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