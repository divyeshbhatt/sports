from django.urls import path, include
from . import views

urlpatterns = [
    path('create/', views.CompetitionCreate, name='competition-create'),
    path('update/<int:pk>/', views.CompetitionUpdate, name='competition-update'),
    path('delete/<int:pk>/', views.CompetitionDelete, name='competition-delete'),
    
    path('match/create/', views.MatchCreate, name='match-create'),
    path('match/update/<int:pk>/', views.MatchUpdate, name='match-update'),
    path('match/delete/<int:pk>/', views.MatchDelete, name='match-delete'),
]
