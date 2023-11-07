from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'firstname',
            'middlename',
            'lastname',
            'email',
            'password'
        ]
        extra_kwargs = {
            'password': {
                'write_only': True
                }
            }