"""Определяет схемы URL для learning_logs."""

from django.urls import path
from . import views


app_name = 'learning_logs'
urlpatterns = [
    # Домашняя страница❻
    path('', views.index, name='index'),
    # Страница со списком всех тем.
    path('topics/', views.topics, name='topics'),
    # Страница с подробной информацией по отдельной теме
    path('topics/<int:topic_id>/', views.topic, name='topic'),
]