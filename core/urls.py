
from django.contrib import admin
from django.urls import path
from .views import StudentsScheduleView, IndexView, TeachersScheduleView, StudentGroupsView, StudentGroupView


urlpatterns = [
    path('', IndexView.as_view()),
    path('student/groups/', StudentGroupsView.as_view(), name='student_groups'),
    path('student/groups/<str:name>/', StudentGroupView.as_view(), name='student_group'),
    path('schedule/students/', StudentsScheduleView.as_view(), name='schedule_students'),
    path('schedule/teachers/', TeachersScheduleView.as_view(), name='schedule_teacher'),
]
