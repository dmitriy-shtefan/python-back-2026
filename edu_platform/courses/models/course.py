from django.db import models
import datetime

class Course(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField(blank=True)
    lessons_number = models.IntegerField()

    is_active = models.BooleanField(default=True)

    start_date = models.DateField(default=datetime.date.today)

    updated_at = models.DateTimeField(auto_now=True)   # оновлення дати та часу при кожній зміні курсу
    created_at = models.DateTimeField(auto_now_add=True)   # при створенні курсу зберегти дату та час

    def __str__(self):
        return "## " + self.title + " " + str(self.lessons_number) + " ##"