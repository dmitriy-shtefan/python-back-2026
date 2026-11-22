from django.db import models
from . import Course

class Lesson(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField(blank=True)

    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    updated_at = models.DateTimeField(auto_now=True)   # оновлення дати та часу при кожній зміні курсу
    created_at = models.DateTimeField(auto_now_add=True)   # при створенні курсу зберегти дату та час

    def __str__(self):
        return self.title