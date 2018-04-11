from django.urls import path, include
from . import views

urlpatterns = [
    path('create/', views.Participation, name='participation-create'),
    path('create/match/<int:id>/', views.ParticipationofEvents, name='match-add'),
    path('score/<int:id>/', views.EventScore, name='event-score'),
]
