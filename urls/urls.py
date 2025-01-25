from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register/', views.register),
    path('log-in/', views.loginPage),
    path('dashboard/', views.dashboard),
    path('logout/', views.logout_user),
    path('delete/', views.delete_user)
]