from django.contrib import admin
from .models import Subject, Question, Score

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'subject')

@admin.register(Score)
class ScoreAdmin(admin.ModelAdmin):
    list_display = ('student_name', 'subject', 'score')
