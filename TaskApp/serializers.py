from .models import Task
from rest_framework.serializers import ModelSerializer

class TaskSerializer(ModelSerializer):

    class Meta:
        model = Task
        fields = ["name", "description", "task_type", "completed_at", "status", "assignee"]