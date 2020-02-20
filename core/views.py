from django.shortcuts import render
from .models import Lesson, Class, Teacher, Day
from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404


class IndexView(TemplateView):
    template_name = 'index.html'

'''
0867 44 6:43-ЛІКАРНЯ 7:20 ДУДАЄВА
2131 26
'''

class StudentGroupsView(TemplateView):
    template_name = 'groups.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['student_groups'] = Class.objects.all()
        context['name'] = 'admin'
        return context

class StudentGroupView(TemplateView):
    template_name = 'group.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['student_group'] = get_object_or_404(Class, name=self.kwargs['name'])
        lessons = Lesson.objects.filter(class_name=context['student_group'])
        context['lessons'] = lessons
        return context

class TachersListView(TemplateView):
    template_name = 'teachers.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['teachers_list'] = Teacher.objects.all()
        context['name'] = 'admin'
        return context

class TeacherView(TemplateView):
    template_name = 'teacher.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['teacher'] = get_object_or_404(Teacher, name=self.kwargs['name'])
        lessons = Lesson.objects.filter(teacher=context['teacher'])
        context['lessons'] = lessons
        return context

class WeekDayView(TemplateView):
    template_name = 'week_day.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['day_of_week'] = get_object_or_404(Day, name=self.kwargs['name'])
        lessons = Lesson.objects.filter(day_of_week=context['day_of_week'])
        context['lessons'] = lessons
        return context
