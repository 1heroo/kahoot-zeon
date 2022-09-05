"""kahoot URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from rest_framework import routers
from django.urls import path, include
from logic.views import *
from .yasg import urlpatterns as swagger


router = routers.DefaultRouter()
router.register(r'player', PlayerViewSet, basename='player')
router.register(r'group', GroupViewSet, basename='group')
router.register(r'quiz', QuizViewSet, basename='quiz')
router.register(r'answers', AnswerViewSet, basename='answer')

# print(router.urls)
# print(include('rest_framework.urls'))

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api/v1/', include('rest_framework.urls')),
    path('getting/', ListAPIView.as_view()),
    path('refresh-data/', refresh_rating_data, name='refresh')
]
urlpatterns += swagger

