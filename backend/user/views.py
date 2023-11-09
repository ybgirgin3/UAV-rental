from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import MyTokenObtainPairSerializer, RegisterSerializer

User = get_user_model()


class RegisterView(generics.CreateAPIView):
    """RegisterView
    Allows users to register by creating a new account.

    Attributes:
        queryset: The queryset of User objects.
        permission_classes: The permissions required for this view.
        serializer_class: The serializer class used for registration.

    Example:
        To register a new user, make a POST request with user data.
    """
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class LogoutView(APIView):
    """LogoutView
    Allows users to log out by blacklisting their refresh token.

    Attributes:
        permission_classes: The permissions required for this view.

    Example:
        To log out, make a POST request with a refresh token.
    """
    permission_classes = (IsAuthenticated,)
    def post(self, request):
        try:
            refresh_token = request.data['refresh_token']
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)

