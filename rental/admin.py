from django.contrib import admin
from .models import UAV, Reservation, Category

# Register your models here.

admin.site.register(UAV)
admin.site.register(Category)
admin.site.register(Reservation)