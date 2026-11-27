from django.urls import path

from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("found/", views.found, name="found"),
    path("pickup/", views.pickup, name="pickup"),
    path("lost/report/", views.report_lost, name="report_lost"),
]
