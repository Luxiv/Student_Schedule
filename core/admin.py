from django.contrib import admin
from .models import Teacher, Subject, TimeSlot, Class, Lesson, Day


admin.site.register(Subject)
admin.site.register(Teacher)
admin.site.register(TimeSlot)
admin.site.register(Class)
admin.site.register(Lesson)
# admin.site.register(StudyWeek)
admin.site.register(Day)
