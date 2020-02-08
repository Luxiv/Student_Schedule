from django.shortcuts import render
from .models import Lesson, Class
from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404


class StudentsScheduleView(TemplateView):
    template_name = 'student.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['lessons'] = Lesson.objects.all()
        context['name'] = 'admin'
        return context

class IndexView(TemplateView):
    template_name = 'index.html'

class TeachersScheduleView(TemplateView):
    template_name = 'teacher.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['lessons'] = Lesson.objects.all()
        context['name'] = 'admin'
        return context

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
