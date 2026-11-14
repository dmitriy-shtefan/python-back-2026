from django.urls import path
from . import views

urlpatterns = [
    path("index/", views.index, name="index"),
    path("profile/", views.profile, name="profile"),
    path("courses_list/", views.courses_list, name="courses_list"),
    path("contacts/", views.contacts, name="contacts"),
    path("lessons/<int:lesson_id>/", views.lesson_detail, name="lesson_detail"),
    path("100/", views.course_100, name="course_100"),
    path("old-contacts/", views.old_contacts, name="old_contacts"),
]
