from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


# viewsets
from rental.views import UAVViewSet, CustomerViewSet, ReservationViewSet

router = routers.DefaultRouter()
router.register(r'uav', UAVViewSet)
router.register(r'customer', CustomerViewSet)
router.register(r'reservation', ReservationViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
