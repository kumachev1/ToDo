from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('task/create/', views.task_create, name='task_create'),
    path('task/edit/<int:pk>/', views.task_edit, name='task_edit'),
    path('task/delete/<int:pk>/', views.task_delete, name='task_delete'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/register/', views.register, name='register'),
    path('accounts/logout/', views.user_logout, name='user_logout'),
]
