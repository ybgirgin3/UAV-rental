from django.contrib import admin
from .models import UAV, Reservation, Customer

# Register your models here.

admin.site.register(UAV)
admin.site.register(Customer)
admin.site.register(Reservation)
