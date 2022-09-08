from django.forms import model_to_dict
from rest_framework.viewsets import GenericViewSet

from .permissions import *
from .serializers import *
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from django.contrib.auth.models import Group
from rest_framework import viewsets, views, generics, mixins
from.services import *
from rest_framework.filters import SearchFilter
from django.http import HttpResponse


class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    serializer_class = serializer_class
    filter_backends = (SearchFilter, )

    @action(methods=['post'], detail=False)
    def registration(self, request, pk=None):
        data = request.data
        new_player = Player.objects.create(
            username=data['username'],
            first_name=data['first_name'],
            last_name=data['last_name'],
            phone_number=data['phone_number'],
            email=data['email'],
            password=make_password(data['password'])

        )
        # print(csrf_token)
        return Response({
            f"{new_player.first_name}": 'Successfully added'
        })


class HandleAnswer(views.APIView):
    # class to receive an answer from player
    pass


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class QuestionsViewSet(viewsets.ModelViewSet):
    queryset = Questions.objects.all()
    serializer_class = QuestionsSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class AnswerPOSTAPICreate(generics.CreateAPIView):
    queryset = AnswerPOST.objects.all()
    serializer_class = AnswerPOSTSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        data = proceed_data(data)
        return Response({'Info': f'Added {data} scores to user'})


def refresh_rating_data(request):
    # procedures to refresh some data
    rating_algo()
    passed_tests_calculating()
    update_player_info()
    return HttpResponse(f'Data refreshed')
