from django.shortcuts import render
from .models import Lesson
from django.views.generic import TemplateView


class ScheduleView(TemplateView):
    template_name = 'core.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['lessons'] = Lesson.objects.all()
        context['name'] = 'admin'
        return context
