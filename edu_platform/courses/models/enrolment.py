from django.db import models
from django.conf import settings

from . import Course


class Enrolment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="enrolments")
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="enrolments")

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.student.username) + " -> " + str(self.course.title)