from django.db import models


class Subject(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=256)
    subjects = models.ManyToManyField(Subject)

    def __str__(self):
        return self.name


class Class(models.Model):
    name = models.CharField(max_length=5)

    def __str__(self):
        return self.name


class TimeSlot(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()
    lesson_number = models.IntegerField(null=True)

    def __str__(self):
        return f'{self.start_time.isoformat()} - {self.end_time.isoformat()}'


class Day(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Lesson(models.Model):
    day_of_week = models.ForeignKey(Day, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)
    class_name = models.ForeignKey(Class, on_delete=models.CASCADE)
    time_slot = models.ForeignKey(TimeSlot, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.day_of_week.name}: {self.class_name.name} {self.subject.name}'
