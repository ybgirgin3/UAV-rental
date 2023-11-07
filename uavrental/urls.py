from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


# viewsets
from rental.views import UAVViewSet, CustomerViewSet, ReservationViewSet

router = routers.DefaultRouter(trailing_slash=True)
router.register(r'uav', UAVViewSet)
router.register(r'customer', CustomerViewSet)
router.register(r'reservation', ReservationViewSet)

urlpatterns = [
    # admin panel
    path('admin/', admin.site.urls),

    ## MAIN API 
    path('api/', include(router.urls)),
    # custom
    # path('api/uav/<int:pk>/delete/', UAVViewSet.as_view({'delete': 'destroy'}, name='uav-delete')),
    

    # authentication
    path('api-auth/', include('rest_framework.urls')),
    # path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
