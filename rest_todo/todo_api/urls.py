from django.urls import path
from .views import TaskListApiView

urlpatterns = [
    path("", TaskListApiView.as_view()),
]
