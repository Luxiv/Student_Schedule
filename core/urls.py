
from django.contrib import admin
from django.urls import path
from .views import ScheduleView


urlpatterns = [
    path('', ScheduleView.as_view()),
]
