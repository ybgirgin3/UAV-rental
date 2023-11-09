from rest_framework import serializers, status, response
from .models import UAV, Reservation, Category
# from django.contrib.auth.models import User
from user.models import User


class UAVSerializer(serializers.ModelSerializer):
    """UAV Serializer
    Serializes UAV (Unmanned Aerial Vehicle) data.

    Attributes:
        Meta: Configuration options for the serializer.

    Example:
        serializer = UAVSerializer(uav_instance)
        data = serializer.data
    """
    class Meta:
        model = UAV
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    """Category Serializer
    Serializes Category data.

    Attributes:
        Meta: Configuration options for the serializer.

    Example:
        serializer = CategorySerializer(category_instance)
        data = serializer.data
    """
    class Meta:
        model = Category
        fields = '__all__'

class AvailableUAVSerializer(serializers.ModelSerializer):
    """Available UAV Serializer
    Serializes UAV data for available UAVs.

    Attributes:
        Meta: Configuration options for the serializer.

    Example:
        serializer = AvailableUAVSerializer(uav_instance)
        data = serializer.data
    """
    class Meta:
        model = UAV
        fields = '__all__'


class ReservationSerializer(serializers.ModelSerializer):
    """Reservation Serializer
    Serializes Reservation data.

    Attributes:
        customer (serializers.PrimaryKeyRelatedField): Represents the customer making the reservation.
        uav (serializers.PrimaryKeyRelatedField): Represents the UAV being reserved.

    Example:
        serializer = ReservationSerializer(reservation_instance)
        data = serializer.data
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

