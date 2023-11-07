from rest_framework import serializers, status, response
from .models import UAV, Reservation, Category
# from django.contrib.auth.models import User
from user.models import User


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

# class CustomerSerializer(serializers.ModelSerializer):
#     """
#         Serializer for Customer
#     """
#     class Meta:
#         model = Customer
#         fields = '__all__'


class ReservationSerializer(serializers.ModelSerializer):
    """
        Serializer for Reservation
    """
    customer = serializers.PrimaryKeyRelatedField(queryset=User.objects.filter(is_active=True))
    uav = serializers.PrimaryKeyRelatedField(queryset=UAV.objects.filter(is_available=True))
    class Meta:
        model = Reservation
        fields = '__all__'


class UAVDetailsReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UAV
        fields = '__all__'
        current_active_bookings = ReservationSerializer(many=True)

