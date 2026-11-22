from django.contrib import admin
from courses.models import Course, Lesson, Enrolment

admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(Enrolment)