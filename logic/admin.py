from django.contrib import admin
from .models import *


# Register your models here.


class PlayerAdmin(admin.ModelAdmin):
    # displaying some fields in object list
    list_display = ('id', 'first_name', 'last_name', 'email', 'phone_number', 'rank', 'final_score', 'is_active')
    list_display_links = ('id', 'first_name', 'last_name', 'email')
    search_fields = ('first_name', 'phone_number', 'last_name', )
    list_editable = ('is_active', )
    list_filter = ('groups', )
    ordering = ('rank', )


class QuizAdmin(admin.ModelAdmin):
    list_display = ('pk', 'quiz_topic', 'question_amount', 'player_passed_amount', 'group')
    list_display_links = ('pk', 'quiz_topic')
    filter_horizontal = ('question', )
    list_editable = ('group',)


class QuestionsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'question_name', 'is_active', )
    list_display_links = ('pk', 'question_name')


class AnswerAdmin(admin.ModelAdmin):
    list_display = ('pk', 'correct_answer', 'timer')
    list_display_links = ('pk', 'correct_answer', )
    list_editable = ('timer', )


admin.site.register(Player, PlayerAdmin)
admin.site.register(Quiz, QuizAdmin)
admin.site.register(Questions, QuestionsAdmin)
admin.site.register(Answer, AnswerAdmin)
