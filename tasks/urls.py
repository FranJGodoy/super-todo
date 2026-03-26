from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),  # /tasks
    path('create/', views.task_create, name='task_create'),
    path('<int:id>/delete/', views.task_delete, name='task_delete'),
    path('<int:id>/toggle/', views.task_toggle, name='task_toggle'),
    path('<slug:slug>/', views.task_detail, name='task_detail'),
    path('task/<int:id>/edit/', views.task_edit, name='task_edit'),
]
