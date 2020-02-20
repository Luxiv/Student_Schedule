
from django.contrib import admin
from django.urls import path
from .views import IndexView, StudentGroupsView, StudentGroupView, TachersListView, TeacherView, WeekDayView


urlpatterns = [
    path('', IndexView.as_view(), name='index'),

    path('groups/', StudentGroupsView.as_view(), name='student_groups'),
    path('groups/<str:name>/', StudentGroupView.as_view(), name='student_group'),
    path('groups/day/<str:name>/', WeekDayView.as_view(), name='day_of_week'),

    path('teachers/', TachersListView.as_view(), name='teachers_list'),
    path('teachers/<str:name>/', TeacherView.as_view(), name='teacher'),




]
