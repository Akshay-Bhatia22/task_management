from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from TaskApp.models import Task
from Account.models import UserAccount
from .serializers import TaskSerializer
from django.contrib.auth.password_validation import validate_password

# Create your views here.
class CreateTaskView(CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = TaskSerializer

class AssignTaskView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = TaskSerializer

    def patch(self, request, id):
        task = Task.objects.get(id=id)
        user = UserAccount.objects.get(id=request.data.get("user"))
        print(task)
        # TODO multiple users 
        if task and user:
            task.assignee.add(user)
            return Response("message", status=status.HTTP_200_OK)
        return Response("message", status=status.HTTP_200_OK)
        
