from django.urls import path

from . import views

urlpatterns = [
    path('', views.home),
    path('about/', views.about),
    path('contacts/', views.contacts),
    path('context/', views.context_demo),
    path('profile/', views.profile),
    path('casino/', views.old_games),
    path('games/', views.games),
    path('games/<int:pk>/', views.detail),
]
