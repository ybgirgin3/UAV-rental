from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static


# viewsets
from rental.views import UAVViewSet, CategoryViewSet, ReservationViewSet

router = routers.DefaultRouter()
router.register(r'uav', UAVViewSet)
router.register(r'category', CategoryViewSet)
router.register(r'reservation', ReservationViewSet)


urlpatterns = [
    # admin panel
    path('admin/', admin.site.urls),

    # main api 
    path('api/', include(router.urls)),

    # auth
    path('auth/', include('user.urls'))

]

urlpatterns +=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)