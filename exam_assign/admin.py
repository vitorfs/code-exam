from exam_assign.models import UserExam
from django.contrib import admin

class UserExamAdmin(admin.ModelAdmin):
    fields = ['user', 'exam', 'expire_date']

admin.site.register(UserExam, UserExamAdmin)