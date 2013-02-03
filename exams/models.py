import datetime
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

class QuestionSubject(models.Model):
    subject = models.CharField(max_length=50)

    def __unicode__(self):
        return self.subject

    class Meta:
        verbose_name = "Tópico Questão"
        verbose_name_plural = "Tópicos Questões"

class QuestionDificulty(models.Model):
    dificulty = models.CharField(max_length=50)
    weight = models.IntegerField()

    def __unicode__(self):
        return self.dificulty

    class Meta:
        verbose_name = "Dificuldade Questão"
        verbose_name_plural = "Dificuldades Questões"

class Question(models.Model):
    QUESTION_TYPES = (
        (u'O', u'Open'),
        (u'C', u'Closed'),
    )

    question = models.CharField(max_length=200)
    example = models.TextField(max_length=2000)
    subject = models.ForeignKey(QuestionSubject)
    type = models.CharField(max_length=1, choices=QUESTION_TYPES)
    dificulty = models.ForeignKey(QuestionDificulty)
    image = models.CharField(max_length=200, blank=True)
    active = models.BooleanField()

    def __unicode__(self):
        return self.question

    class Meta:
        verbose_name = "Questão"
        verbose_name_plural = "Questões"

class Answer(models.Model):
    question = models.ForeignKey(Question)
    answer = models.CharField(max_length=200)
    correct = models.BooleanField()
    letter = models.CharField(max_length=1)

    def __unicode__(self):
        return self.answer

    class Meta:
        verbose_name = "Resposta"
        verbose_name_plural = "Respostas"

class ExamSubject(models.Model):
    subject = models.CharField(max_length=50)

    def __unicode__(self):
        return self.subject

    class Meta:
        verbose_name = "Tópico Prova"
        verbose_name_plural = "Tópicos Provas"

class Exam(models.Model):
    name = models.CharField(max_length=50)
    expire_date = models.DateTimeField()
    subject = models.ForeignKey(ExamSubject)
    questions = models.ManyToManyField(Question)
    duration = models.IntegerField()

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "Prova"
        verbose_name_plural = "Provas"

class UserExam(models.Model):
    user = models.ForeignKey(User)
    exam = models.ForeignKey(Exam)
    expire_date = models.DateTimeField()
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)

    def __unicode__(self):
         return u"%s %s" % (self.user, self.exam)

    def has_finished(self):
        if self.end_time:
            return True
        else:
            return False
    has_finished.boolean = True
    has_finished.short_description = 'Concluiu a Prova?'

    def has_expired(self):
        return timezone.now() > self.expire_date
    has_expired.boolean = True
    has_expired.short_description = 'Prazo Expirou?'

    class Meta:
        verbose_name = "Aplicar Prova"
        verbose_name_plural = "Aplicar Provas"

class UserExamAnswers(models.Model):
    user_exam = models.ForeignKey(UserExam)
    question = models.ForeignKey(Question)
    closed_answer = models.ForeignKey(Answer)
    open_answer = models.CharField(max_length=2000)