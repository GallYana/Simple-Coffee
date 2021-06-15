from django.contrib import admin
from .models import Question, Answer
from .models import Result
from .models import Quiz

class AnswerInline(admin.TabularInline):
    model = Answer

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
admin.site.register(Result)
admin.site.register(Quiz)