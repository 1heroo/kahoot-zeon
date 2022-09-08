from django.contrib import admin
from .models import *
from nested_inline.admin import *


class PlayerAdmin(admin.ModelAdmin):
    # displaying some fields in object list
    list_display = ('first_name', 'last_name', 'get_group', 'email', 'phone_number', 'rank', 'final_score', 'passed_tests')
    list_display_links = ('first_name', 'last_name', 'email')
    search_fields = ('first_name', 'phone_number', 'last_name', )
    list_editable = ('passed_tests', )
    list_filter = ('groups', )
    ordering = ('rank', )

    def get_group(self, obj):
        return "\n".join([p.name for p in obj.groups.all()])


# class AnswerInline(NestedStackedInline):
#     model = Answer
#     extra = 4
#

class AnswerInline(NestedStackedInline):
    model = Answer
    extra = 4
    max_num = 4


class AnswerAdmin(admin.ModelAdmin):
    list_display = ('option', 'is_correct')
    list_display_links = ('option', )
    list_editable = ('is_correct', )


class QuestionsAdmin(admin.ModelAdmin):
    inlines = (AnswerInline, )
    list_display = ('question_name', 'is_active')
    list_display_links = ('question_name', )

    # def get_player(self, obj):
    #     return "\n".join([p.first_name for p in obj.is_done_by_players.all()])


class QuizAdmin(admin.ModelAdmin):
    list_display = ('quiz_topic', 'question_amount', 'player_passed_amount')
    list_display_links = ('quiz_topic', )
    filter_horizontal = ('question', )


class LeaderBoardAdmin(admin.ModelAdmin):
    # displaying some fields in object list
    list_display = ('first_name', 'last_name', 'get_group', 'email', 'phone_number', 'rank', 'final_score')
    list_display_links = ('first_name', 'last_name', 'email')
    search_fields = ('first_name', 'phone_number', 'last_name',)
    list_filter = ('groups',)
    ordering = ('rank',)

    def get_group(self, obj):
        return "\n".join([p.name for p in obj.groups.all()])


admin.site.register(Player, PlayerAdmin)
admin.site.register(LeaderBoard, LeaderBoardAdmin)
admin.site.register(Quiz, QuizAdmin)
admin.site.register(Questions, QuestionsAdmin)
admin.site.register(Answer, AnswerAdmin)
