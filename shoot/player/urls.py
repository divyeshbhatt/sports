from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.PlayerCreate, name='player-create'),
    path('delete/<int:pk>/', views.PlayerDelete, name='player-delete'),
    path('update/<int:pk>/', views.PlayerUpdate, name='player-update'),
]
