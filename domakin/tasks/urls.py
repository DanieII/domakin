from django.urls import path
from .views import TaskListView, TaskCreateView

urlpatterns = [
    path("", TaskListView.as_view(), name="tasks"),
    path("create/", TaskCreateView.as_view(), name="create_task"),
]
