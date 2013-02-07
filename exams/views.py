# coding: utf-8
import datetime
from django.utils import timezone
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from exams.models import UserExam, Question, Answer, UserExamAnswers

@login_required
def user_exams(request):
    user_exam_list = UserExam.objects.filter(user__id=request.user.id).order_by('-id')
    context = RequestContext(request, {'user_exam_list': user_exam_list,})
    return render_to_response('exams/user_exams.html', context)

@login_required
def start_exam(request, exam_id):
    user_exam = UserExam.objects.get(pk=exam_id)
    if request.user.id == user_exam.user.id:
        if not user_exam.has_expired():
            if not user_exam.start_time:
                user_exam.start_time = timezone.now()
                user_exam.save()
                return redirect('/prova/%s/' % user_exam.id)
            else:
                messages.add_message(request, messages.ERROR, 'Esta prova já foi inicializada.')
        else:
            messages.add_message(request, messages.ERROR, 'Não foi possível iniciar a prova pois o prazo expirou.')
    else:
        messages.add_message(request, messages.ERROR, 'Usuário sem permissão para acessar prova.')

    context = RequestContext(request)
    return redirect('/')

@login_required
def end_exam(request, exam_id):
    user_exam = UserExam.objects.get(pk=exam_id)
    if request.user.id == user_exam.user.id:
        if user_exam.get_progress() == '100%':
            if not user_exam.has_expired():
                if not user_exam.end_time:
                    user_exam.end_time = timezone.now()
                    user_exam.save()
                    messages.add_message(request, messages.SUCCESS, 'Prova enviada com sucesso!')
                    return redirect('/')
                else:
                    messages.add_message(request, messages.ERROR, 'Esta prova já foi finalizada.')
            else:
                messages.add_message(request, messages.ERROR, 'Não foi possível enviar a prova pois o prazo expirou.')
        else:
            messages.add_message(request, messages.ERROR, 'É necessário responder todas as perguntas antes de enviar!')
    else:
        messages.add_message(request, messages.ERROR, 'Usuário sem permissão para acessar prova.')

    context = RequestContext(request)
    return redirect('/')    

@login_required
def exam(request, exam_id):
    user_exam = UserExam.objects.get(pk=exam_id)
    if (request.user.id == user_exam.user.id):
        context = RequestContext(request, { 'user_exam': user_exam })
        return render_to_response('exams/exam.html', context)
    else:
        messages.add_message(request, messages.ERROR, 'Usuário sem permissão para acessar prova.')
        context = RequestContext(request)
        return redirect('/')

@login_required
def question(request, exam_id, question_id):
    user_exam = UserExam.objects.get(pk=exam_id)

    if (request.user.id == user_exam.user.id):
        question = Question.objects.get(pk=question_id)
        #question = user_exam.exam.questions.all().filter(id=question_id)
        #questions = user_exam.exam.questions.all()
        #question = Question.objects.get(pk=questions[question_index])
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

        return render_to_response('exams/question.html', context)
    else:
        messages.add_message(request, messages.ERROR, 'Usuário sem permissão para acessar prova.')
        context = RequestContext(request)
        return render_to_response('exams/exam.html', context)

@login_required
def send_answer(request):
    if request.method == 'POST':
        user_exam_id = request.POST['user-exam-id']
        question_id = request.POST['question-id']
        answer_id = request.POST['rb-answer']

        user_exam_answer = UserExamAnswers.objects.filter(user_exam__id=user_exam_id, question__id=question_id)
        user_exam_answer.delete()

        user_exam_answer = UserExamAnswers(user_exam=UserExam(id=user_exam_id), question=Question(id=question_id), closed_answer=Answer(id=answer_id))
        user_exam_answer.save()

        return HttpResponse('OK')