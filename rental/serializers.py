from rest_framework import serializers, status, response
from .models import UAV, Customer, Reservation, Category

class UAVSerializer(serializers.ModelSerializer):
    """
        Serializer for UAVs
    """
    class Meta:
        model = UAV
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class AvailableUAVSerializer(serializers.ModelSerializer):
    class Meta:
        model = UAV
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):
    """
        Serializer for Customer
    """
    class Meta:
        model = Customer
        fields = '__all__'


class ReservationSerializer(serializers.ModelSerializer):
    """
        Serializer for Reservation
    """
    class Meta:
        model = Reservation
        fields = '__all__'


class UAVDetailsReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UAV
        fields = '__all__'
        current_active_bookings = ReservationSerializer(many=True)

