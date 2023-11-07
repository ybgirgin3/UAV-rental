from rest_framework import serializers, status, response
from .models import UAV, Customer, Reservation

class UAVSerializer(serializers.ModelSerializer):
    """
        Serializer for UAVs
    """
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

    def create(self, validated_data):
        # get the associated UAV from the data
        uav = validated_data.get('uav')
        
        # set the is_available field to the UAV to false
        uav.is_available = False
        uav.save()
        
        # create the reservation
        reservation_transaction: Reservation = Reservation.objects.create(**validated_data)
        
        return reservation_transaction


    
 
    
        