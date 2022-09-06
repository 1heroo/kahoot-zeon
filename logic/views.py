from django.forms import model_to_dict

from .permissions import *
from .serializers import *
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from django.contrib.auth.models import Group
from rest_framework import viewsets, views, generics
from.services import *
from rest_framework.filters import SearchFilter
from django.http import HttpResponse


class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    # def get_queryset(self):
    #     pk = self.kwargs.get('pk')
    #     if not pk:
    #         return LogicConfig.objects.all()
    #     return LogicConfig.objects.filter(pk=pk

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


class ListAPIView(views.APIView):
    # class to receive an answer from player
    def post(self, request):
        data = request.data
        data = proceed_data(data)
        rating_algo()
        passed_tests_calculating()
        return Response({'info': f'{data}'})


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


def refresh_rating_data(request):
    # procedures to refresh some data
    rating_algo()
    passed_tests_calculating()
    return HttpResponse('Data refreshed')
