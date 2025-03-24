from .models import Task
from rest_framework.serializers import ModelSerializer, ValidationError

class TaskSerializer(ModelSerializer):

    class Meta:
        model = Task
        fields = ["name", "description", "task_type", "completed_at", "status"]


    # def update(self, instance, validated_data):
    #         request = self.context.get("request")  # Get request object

    #         if request and request.method == "PATCH":
    #             # Restrict PATCH to only certain fields
    #             allowed_fields = {"assignee"}  # Only 'name' can be updated
    #             disallowed_fields = [field for field in validated_data if field not in allowed_fields]

    #             if disallowed_fields:
    #                 raise ValidationError(
    #                     {"error": f"Only assignee can be updated through this request."}
    #                 )

    #         # Apply updates normally
    #         for field, value in validated_data.items():
    #             setattr(instance, field, value)
            
    #         instance.save()
    #         return instance
