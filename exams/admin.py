from exams.models import Exam, Question, Answer, ExamSubject, QuestionSubject, QuestionDificulty, UserExam
from django.contrib import admin

class AnswerInline(admin.TabularInline):
    model = Answer
    fields = ['letter', 'answer', 'correct']
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question','subject','type','dificulty','active']
    list_filter = ['type','dificulty','active']
    inlines = [AnswerInline]
    search_fields = ['question', 'subject__subject']

class UserExamAdmin(admin.ModelAdmin):
    fields = ['user', 'exam', 'expire_date']
    list_display = ['id', 'user', 'exam', 'expire_date', 'has_finished', 'has_expired']
    list_filter = ['expire_date']
    date_hierarchy = 'expire_date'
    search_fields = ['user__username', 'user__first_name', 'user__last_name', 'exam__name']

class ExamAdmin(admin.ModelAdmin):
    list_display = ['name', 'expire_date', 'subject', 'duration']
    date_hierarchy = 'expire_date'
    search_fields = ['name']
    list_filter = ['expire_date', 'subject']

admin.site.register(Exam, ExamAdmin)
admin.site.register(ExamSubject)
admin.site.register(Question, QuestionAdmin)
admin.site.register(QuestionSubject)
admin.site.register(QuestionDificulty)
admin.site.register(UserExam, UserExamAdmin)