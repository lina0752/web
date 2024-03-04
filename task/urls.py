from django.urls import path
from .views import task_list, create_task, edit_task, delete_task

urlpatterns = [
    path('task/', task_list, name='task_list'),
    path('task/create/', create_task, name='create_task'),
    path('<int:pk>/edit/', edit_task, name='edit_task'),
    path('<int:pk>/delete/', delete_task, name='delete_task'),
]
