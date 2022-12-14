from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Player(AbstractUser):
    phone_number = PhoneNumberField(blank=True)
    final_score = models.IntegerField(default=0)
    rank = models.IntegerField(default=999, blank=True)
    passed_questions = models.IntegerField(default=0)
    passed_tests = models.IntegerField(default=0)
    detail = models.TextField(blank=True, default="No activity yet")

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'LeaderBoard'
        verbose_name_plural = 'Leaderboard'
        ordering = ['rank']


class Answer(models.Model):
    option = models.CharField(max_length=50, blank=True)
    is_correct = models.BooleanField(default=False)
    level = models.ForeignKey("Questions", blank=True, on_delete=models.SET_NULL, null=True)


    def __str__(self):
        return f'{self.option}'


class Questions(models.Model):
    question_name = models.CharField(max_length=50)
    question = models.TextField(max_length=150)
    image = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_active = models.BooleanField(default=True)
    timer = models.IntegerField(default=20)
    score_for_answering = models.IntegerField(default=100)

    is_done_by_players = models.ManyToManyField(Player, blank=True)

    class Meta:
        verbose_name = 'Question'
        ordering = ['pk']

    def __str__(self):
        return f'{self.question_name}'


class Quiz(models.Model):
    quiz_topic = models.CharField(max_length=50)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True)
    question = models.ManyToManyField(Questions, blank=True)
    is_done_by_players = models.ManyToManyField(Player, blank=True)
    is_active = models.BooleanField(default=True)
    question_amount = models.IntegerField(default=0)
    player_passed_amount = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.quiz_topic}'

    class Meta:
        verbose_name_plural = 'Quizzes'
        ordering = ['pk']


class LeaderBoard(Player):
    class Meta(Player.Meta):
        verbose_name = 'User'
        verbose_name_plural = "Users"
        ordering = ["first_name"]
        proxy = True


class AnswerPOST(models.Model):
    player_id = models.IntegerField(blank=True)
    question_id = models.IntegerField(blank=True)
    answer_id = models.IntegerField(blank=True)
    time = models.IntegerField(blank=True)