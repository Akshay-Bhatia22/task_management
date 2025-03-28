from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, UpdateAPIView, ListAPIView
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from TaskApp.models import Task
from Account.models import UserAccount
from .serializers import TaskSerializer
from django.contrib.auth.password_validation import validate_password

# for simple CRUD of tasks
class TaskView(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = TaskSerializer

    def get_queryset(self):
        # allows only tasks to be updated created by the login user
        return Task.objects.filter(created_by=self.request.user.id)

# for assigning/ removing a task to one or more users
class AssignTaskView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = TaskSerializer

    def patch(self, request, id):
        task = Task.objects.get(id=id)
        if not task:
            return Response("Task not found", status=status.HTTP_400_BAD_REQUEST)
        
        # check if supplied users exist
        valid_users = UserAccount.objects.filter(id__in=request.data.get("user"))
        user_ids = list(valid_users.values_list("id", flat=True))

        if request.data.get("operation") == "remove":
            task.assignee.remove(*user_ids)
            return Response(f"Assignee user ids {user_ids} deleted succesfully", status=status.HTTP_200_OK)

        # add to assignee if operation not specified
        task.assignee.add(*user_ids)
        return Response(f"Assigned user ids {user_ids} succesfully", status=status.HTTP_200_OK)

# to view tasks assigned to user 
class AssigneeTaskView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = TaskSerializer

    def get_queryset(self):
        # getting id from url parameter
        assignee_id = self.kwargs["id"]
        return Task.objects.filter(assignee=assignee_id)