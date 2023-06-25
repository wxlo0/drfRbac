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
    path('list', views.UserListAPIView.as_view()),
    path('role/list', views.RoleListAPIView.as_view()),
    path('role/change/<pk>', views.ChangeUserRoleAPIView.as_view()),
    path('role/update/<pk>', views.RoleUpdateAPIView.as_view()),
    path('permissions/list', views.PermissionsListAPIView.as_view()),
    path('role/permissions/list/<role_id>', views.RolePermissionsListAPIView.as_view()),
]

