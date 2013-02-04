# coding: utf-8
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from exams.models import UserExam, Question, Answer, UserExamAnswers

def exam(request, exam_id):
    user_exam = UserExam.objects.get(pk=exam_id)
    if (request.user.id == user_exam.user.id):
        context = RequestContext(request, { 'user_exam': user_exam })
        return render_to_response('exams/exam.html', context)
    else:
        messages.add_message(request, messages.ERROR, 'Usuário sem permissão para acessar prova.')
        context = RequestContext(request)
        return redirect('/')

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

        return render_to_response('exams/question.html', context)
    else:
        messages.add_message(request, messages.ERROR, 'Usuário sem permissão para acessar prova.')
        context = RequestContext(request)
        return render_to_response('exams/exam.html', context)

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