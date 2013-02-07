from django.conf.urls import patterns, include, url

urlpatterns = patterns('exams.views',
    url(r'^(?P<exam_id>\d+)/$', 'exam'),
    url(r'^(?P<exam_id>\d+)/questao/(?P<question_id>\d+)/$', 'question'),
    url(r'^enviar-resposta/$', 'send_answer'),
    url(r'^(?P<exam_id>\d+)/iniciar/$', 'start_exam'),
    url(r'^(?P<exam_id>\d+)/enviar/$', 'end_exam'),
)