from rest_framework import serializers
from .models import UAV, Customer, Reservation

class UAVSerializer(serializers.ModelSerializer):
    class Meta:
        model = UAV
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'