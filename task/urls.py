from django.urls import path
from .views import TaskListView,TaskDetailView



urlpatterns = [
    path('tasks/', TaskListView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='user-task-detail')
]

