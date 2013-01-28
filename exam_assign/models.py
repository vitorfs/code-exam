from django.db import models
from django.contrib.auth.models import User
from exams.models import Exam, Question, Answer

class UserExam(models.Model):
    user = models.ForeignKey(User)
    exam = models.ForeignKey(Exam)
    expire_date = models.DateTimeField()
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)

    def __unicode__(self):
         return u"%s %s" % (self.user, self.exam)

    class Meta:
        verbose_name = "Prova de Usuário"
        verbose_name_plural = "Provas de Usuários"

class UserExamAnswers(models.Model):
    user_exam = models.ForeignKey(UserExam)
    question = models.ForeignKey(Question)
    closed_answer = models.ForeignKey(Answer)
    open_answer = models.CharField(max_length=2000)