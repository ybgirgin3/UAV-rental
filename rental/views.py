from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import UAV, Customer, Reservation
from .serializers import (
    UAVSerializer,
    CustomerSerializer,
    ReservationSerializer
)


class UAVViewSet(viewsets.ModelViewSet):
    queryset = UAV.objects.all()
    serializer_class = UAVSerializer
    
    @action(detail=False, methods=['GET'])
    def list_available(self, request):
        """
            list only available UAVs
        """
        available_uavs = UAV.objects.filter(is_available=True)
        serializer = UAVSerializer(available_uavs, many=True)
        return Response(serializer.data)


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
