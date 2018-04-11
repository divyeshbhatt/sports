from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.LoginView, name='login'),
    path('register/', views.Registration, name='register'),
    path('logout/', views.UserLogout, name='logout'),
]
