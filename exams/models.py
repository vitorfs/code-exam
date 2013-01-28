from django.db import models

class QuestionSubject(models.Model):
    subject = models.CharField(max_length=50)

    def __unicode__(self):
        return self.subject

    class Meta:
        verbose_name = "Assunto de Questão"
        verbose_name_plural = "Assuntos de Questões"

class QuestionDificulty(models.Model):
    dificulty = models.CharField(max_length=50)
    weight = models.IntegerField()

    def __unicode__(self):
        return self.dificulty

    class Meta:
        verbose_name = "Dificuldade de Questão"
        verbose_name_plural = "Dificuldades de Questões"

class QuestionType(models.Model):
    type = models.CharField(max_length=30)

    def __unicode__(self):
        return self.type

    class Meta:
        verbose_name = "Tipo de Questão"
        verbose_name_plural = "Tipos de Questões"

class Question(models.Model):
    question = models.CharField(max_length=200)
    example = models.CharField(max_length=2000)
    subject = models.ForeignKey(QuestionSubject)
    type = models.ForeignKey(QuestionType)
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
        verbose_name = "Assunto de Prova"
        verbose_name_plural = "Assuntos de Provas"

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