from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group
from django.db import models


class Player(AbstractUser):
    phone_number = models.IntegerField(blank=True, default=555)
    final_score = models.IntegerField(default=0)
    rank = models.IntegerField(default=999, blank=True)
    passed_questions = models.IntegerField(default=0)
    passed_tests = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        ordering = ['rank']


class Answer(models.Model):
    option_1 = models.CharField(max_length=50, blank=True)
    option_2 = models.CharField(max_length=50, blank=True)
    option_3 = models.CharField(max_length=50, blank=True)
    option_4 = models.CharField(max_length=50, blank=True)
    correct_answer = models.TextField(max_length=50)
    timer = models.IntegerField(default=20)
    score_for_answering = models.IntegerField(default=100)

    def __str__(self):
        return f'{self.correct_answer}'


class Questions(models.Model):
    question_name = models.CharField(max_length=50)
    question = models.TextField(max_length=150)
    image = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_active = models.BooleanField(default=True)
    correct_answer = models.OneToOneField(Answer, on_delete=models.CASCADE)
    is_done_by_players = models.ManyToManyField(Player, blank=True)

    class Meta:
        verbose_name = 'Question'
        ordering = ['pk']

    def __str__(self):
        return f'{self.question_name}'


class Quiz(models.Model):
    quiz_topic = models.CharField(max_length=50)
    group = models.ForeignKey(Group, on_delete=models.PROTECT, null=True)
    question = models.ManyToManyField(Questions)
    is_done_by_players = models.ManyToManyField(Player, blank=True)
    is_active = models.BooleanField(default=True)
    question_amount = models.IntegerField(default=0)
    player_passed_amount = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.quiz_topic}'

    class Meta:
        verbose_name_plural = 'Quizzes'
        ordering = ['pk']