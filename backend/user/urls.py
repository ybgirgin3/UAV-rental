from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_protect
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView
)



urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('register/', views.RegisterView.as_view(), name='auth_register'),
    path('logout/', csrf_protect(views.LogoutView.as_view()), name ='logout')
]