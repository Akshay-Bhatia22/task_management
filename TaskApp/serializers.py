from .models import Task
from rest_framework.serializers import ModelSerializer
from Account.models import UserAccount

class TaskSerializer(ModelSerializer):

    class Meta:
        model = Task
        fields = ["id","name", "description", "task_type", "created_at", "created_by", "completed_at", "status", "assignee"]
        # for optional field in POST request
        extra_kwargs = {
            "assignee": {"required": False}
        }
    
    def create(self, validated_data):
        request = self.context.get('request')
        if request and request.user:
            validated_data['created_by'] = UserAccount.objects.get(id=request.user.id)
        return super().create(validated_data)
