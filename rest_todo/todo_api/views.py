from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Task
from .serializers import TodoSerializer

# Create your views here.
class TaskListApiView(APIView):
    def get(self, request):
        tasks = Task.objects.all()
        serializer = TodoSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
