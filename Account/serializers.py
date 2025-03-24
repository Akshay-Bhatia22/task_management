from rest_framework.views import APIView
from .models import UserAccount
from rest_framework.serializers import ModelSerializer

class AccountSerializer(ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ['id', 'email', 'password', 'name', 'mobile', 'gender', 'position']

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
