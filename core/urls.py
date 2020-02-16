
from django.contrib import admin
from django.urls import path
from .views import IndexView, StudentGroupsView, StudentGroupView, TachersListView, TeacherView


urlpatterns = [
    path('', IndexView.as_view(), name='index'),

    path('student/groups/', StudentGroupsView.as_view(), name='student_groups'),
    path('student/groups/<str:name>/', StudentGroupView.as_view(), name='student_group'),

    path('teacher/names/', TachersListView.as_view(), name='teachers_list'),
    path('teacher/name/<str:name>/', TeacherView.as_view(), name='teacher'),

]
