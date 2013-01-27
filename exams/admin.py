from exams.models import Exam, Question, Answer, ExamSubject, QuestionSubject, QuestionDificulty, QuestionType
from django.contrib import admin

admin.site.register(Exam)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(ExamSubject)
admin.site.register(QuestionSubject)
admin.site.register(QuestionDificulty)
admin.site.register(QuestionType)