from .models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class UserSerializer(serializers.ModelSerializer):
    """User Serializer
    Serializes User model data.

    Attributes:
        Meta: Configuration options for the serializer.

    Example:
        serializer = UserSerializer(user_instance)
        data = serializer.data
    """
    class Meta:
        model = User
        fields = [
        "email",
        "password",
        "phone",
        "username",
        ]
        extra_kwargs = {
            'password': {
                'write_only': True
                }
            }
        
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    """TokenObtainPairSerializer
    Implements JWT (Json Web Token) for Authentication and creates Access Token and Refresh Token.

    Example:
        serializer = MyTokenObtainPairSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        token = serializer.validated_data
    """
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        
        # These are claims, you can add custom claims
        token['full_name'] = user.profile.full_name
        token['username'] = user.username
        token['email'] = user.email
        token['bio'] = user.profile.bio
        token['image'] = str(user.profile.image)
        token['verified'] = user.profile.verified
        # ...
        return token


class RegisterSerializer(serializers.ModelSerializer):
    """RegisterSerializer
    Implements user registration.

    Attributes:
        password (CharField): User's password.
        password2 (CharField): User's password confirmation.

    Example:
        serializer = RegisterSerializer(data=data)
        if serializer.is_valid():
            user = serializer.save()
    """
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'password2')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email']

        )

        user.set_password(validated_data['password'])
        user.save()

        return user