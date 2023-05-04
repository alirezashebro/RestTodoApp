from django.urls import path
from .views import TaskListApiView

urlpatterns = [
    path("get_tasks/", TaskListApiView.as_view(), name="get_tasks"),
]
