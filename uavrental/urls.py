from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


# viewsets
from rental.views import UAVViewSet, CategoryViewSet, ReservationViewSet
# from user.views import UserProfileView#, RegistrationView
# from user.urls import urlpatterns as user_urlpatterns

router = routers.DefaultRouter()
router.register(r'uav', UAVViewSet)
router.register(r'category', CategoryViewSet)
# router.register(r'customer', UserProfileView)
# router.register(r'create-customer', RegistrationView)
router.register(r'reservation', ReservationViewSet)


urlpatterns = [
    # admin panel
    path('admin/', admin.site.urls),

    ## MAIN API 
    path('api/', include(router.urls)),

    # path('user', include('user.urls')),
    

    # authentication
    path('api-auth/', include('rest_framework.urls')),
    # path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # path('auth/', include('user.urls')),

]

# urlpatterns += user_urlpatterns