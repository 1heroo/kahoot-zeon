from .models import *
from django.contrib.auth.hashers import make_password
# the function 'make_password' is being used in other views.py

quiz_data = Quiz.objects.all()
players_data = Player.objects.all()


def proceed_data(json_data):
    """
    This is an algorithm to fill in the field in the 'Player' model
    if the player answered correctly.
    If he answered this question earlier,
    the player will not receive a point

    :param json_data: this data contains:
    player id,
    question id,
    answer id,
    player answer,
    in what time the player answered
    """
    player_id = json_data['player_id']
    answer_id = json_data['answer_id']
    answered_time = json_data['time']
    question_id = json_data['question_id']

    player_objects = Player.objects.get(pk=player_id)
    answer_objects = Answer.objects.get(pk=answer_id)
    question_objects = Questions.objects.get(pk=question_id)

    question_score = question_objects.score_for_answering
    question_timer = question_objects.timer

    is_answered = answer_objects.is_correct
    final_score = player_objects.final_score

    if player_objects in question_objects.is_done_by_players.all():
        return "Sorry, but you have already answered!"

    res = 0
    if is_answered:
        if answered_time == 1:
            res = question_score - (question_score / question_timer * answered_time) + (question_score / question_timer)
        else:
            res = question_score - (question_score / question_timer * answered_time)

        final_score = final_score + res
        question_objects.is_done_by_players.add(player_objects)
        question_objects.save()

        player_objects.final_score = final_score
        player_objects.passed_questions += 1
    player_objects.save()
    return res


def rating_algo():
    """
    This algo gives us a leaderboard by amount of scores
    """
    model = Player.objects.all()
    final_scores_and_id_list = sorted([
        (item.final_score, item.id)
        for item in model
    ], reverse=True)

    for index, item in enumerate(final_scores_and_id_list):
        player = Player.objects.get(pk=item[1])
        player.rank = index + 1 if item[0] > 0 else 0
        player.save()


def passed_tests_calculating():
    """
    This algorithm checks which questions the player answered
    from the entire test, if everything is answered correctly,
    then adds a score to the "passed_tests" field for a particular player
    """
    player_passed_question = 0
    for player in players_data:
        for quiz in quiz_data:
            all_questions = quiz.question.all()
            quiz_size = len(all_questions)
            for question in all_questions:
                player_passed_question += 1 if player in question.is_done_by_players.all() else 0
                player.passed_questions = player_passed_question
                player.save()

            if player_passed_question == quiz_size and player not in quiz.is_done_by_players.all():
                quiz.is_done_by_players.add(player)
                player.passed_tests += 1
                player.save()
            quiz.player_passed_amount = len(quiz.is_done_by_players.all())
            quiz.question_amount = quiz_size
            quiz.save()
        player_passed_question = 0


def update_player_info():
    player_info = ''

    for player in players_data:
        player_info += f'{player}: \n'
        for quiz in quiz_data:
            all_questions = quiz.question.all()

            if player in quiz.is_done_by_players.all():
                player_info += f'      {quiz}: \n'

            for question in all_questions:
                if player in question.is_done_by_players.all():
                    player_info += f'            {question}: Answered Correctly! \n'

        player_info += f'Answered {player.passed_questions} questions\nPassed {player.passed_tests} tests'
        player.detail = player_info
        player.save()
        player_info = ''








