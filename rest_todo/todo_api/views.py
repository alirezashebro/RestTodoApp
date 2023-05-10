from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Task
from .serializers import TodoSerializer
from django.core.exceptions import ValidationError

import json

# Create your views here.
class TaskListApiView(APIView):
    def get(self, request):
        tasks = Task.objects.all()
        serializer = TodoSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        try:
            request_body = json.loads(request.body.decode())
            if 'title' and 'done' in request_body:
                title = request_body['title']
                done = request_body['done']
                try:
                    Task.objects.create(title=title, done=done)
                    return Response({"detail" : "task created successfully."}, status=status.HTTP_200_OK)
                except ValidationError:
                    return Response({"error": "some thing were wrong in your request."}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({"error": "title or done not found in your request."}, status=status.HTTP_400_BAD_REQUEST)
        except json.JSONDecodeError:
            return Response({"error": "wrong request body."}, status=status.HTTP_400_BAD_REQUEST)
