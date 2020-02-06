
from django.contrib import admin
from django.urls import path
from .views import StudentsScheduleView, IndexView


urlpatterns = [
    path('', IndexView.as_view()),
    path('schedule/students/', StudentsScheduleView.as_view(), name='schedule_students'),
]
