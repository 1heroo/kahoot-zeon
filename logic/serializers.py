from rest_framework import serializers
from .models import *
from datetime import datetime


class PlayerSerializer(serializers.ModelSerializer):
    # #  user = serializers.HiddenField(default=serializers.CurrentUserDefault)
    # last_login = serializers.HiddenField(default=datetime.now())
    # is_superuser = serializers.HiddenField(default=False)
    # is_staff = serializers.HiddenField(default=False)
    # is_active = serializers.HiddenField(default=True)
    # date_joined = serializers.HiddenField(default=datetime.now())
    # user_permissions = serializers.HiddenField(default=None)
    # final_score = serializers.HiddenField(default=0)
    # rank = serializers.HiddenField(default=0)
    # passed_tests = serializers.HiddenField(default=0)
    # passed_questions = serializers.HiddenField(default=0)
    # group = serializers.HiddenField(default=None)

    class Meta:

        model = Player
        fields = ('id', 'first_name', 'last_name', 'groups', 'phone_number', 'username', 'rank', 'final_score')


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = '__all__'


class QuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields = "__all__"


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'
