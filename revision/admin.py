from django.contrib import admin
from .models import StudentProfile, Question


@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'course', 'is_approved', 'mpesa_code')
    list_filter = ('course', 'is_approved')


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('course', 'question_text')
    list_filter = ('course',)