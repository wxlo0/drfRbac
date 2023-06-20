"""
@Created on 2023/6/13 21:15
@Author: clyde.liu
@Des: 
"""

from django.urls import path
from . import views

urlpatterns = [
    path('register', views.RegisterAPIView.as_view()),
    path('login', views.LoginAPIView.as_view()),
]

