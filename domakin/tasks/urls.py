from django.urls import path
from .views import tasks_view, TaskCreateView, task_complete_view

urlpatterns = [
    path("", tasks_view, name="tasks"),
    path("create/", TaskCreateView.as_view(), name="create_task"),
    path("<int:pk>/complete/", task_complete_view, name="complete_task"),
]
