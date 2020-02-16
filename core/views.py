from django.shortcuts import render
from .models import Lesson, Class, Teacher
from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404




class IndexView(TemplateView):
    template_name = 'index.html'


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
