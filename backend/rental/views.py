"""
    ViewSets:
        The main bridges between Backend and UI
        
        - Get objects from DB using Model and serialize with it's own serializer
        - return data
"""

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import UAV, Reservation, Category
from .serializers import (
    UAVSerializer,
    ReservationSerializer,
    CategorySerializer
)


class CategoryViewSet(viewsets.ModelViewSet):
    """Category ViewSet
    Provides CRUD operations for Category objects.

    Attributes:
        queryset (QuerySet): The queryset of Category objects.
        serializer_class: The serializer class to be used.

    Example:
        category_viewset = CategoryViewSet.as_view({'get': 'list'})
        response = category_viewset(request)
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class UAVViewSet(viewsets.ModelViewSet):
    """UAV ViewSet
    Provides CRUD operations for UAV (Unmanned Aerial Vehicle) objects.

    Attributes:
        queryset (QuerySet): The queryset of UAV objects.
        serializer_class: The serializer class to be used.

    Example:
        uav_viewset = UAVViewSet.as_view({'get': 'list'})
        response = uav_viewset(request)
    """
    queryset = UAV.objects.all()
    serializer_class = UAVSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Additional view methods for create, retrieve, update, partial update, and delete
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            # Custom logic for partial data validation and updating
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ReservationViewSet(viewsets.ModelViewSet):
    """Reservation ViewSet
    Provides CRUD operations for Reservation objects.

    Attributes:
        queryset (QuerySet): The queryset of Reservation objects.
        serializer_class: The serializer class to be used.

    Example:
        reservation_viewset = ReservationViewSet.as_view({'get': 'list'})
        response = reservation_viewset(request)
    """
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            # get uav and make it unavailable
            uav = UAV.objects.get(pk=serializer.data.get('uav'))
            uav.is_available = False
            uav.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            # Custom logic for partial data validation and updating
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        print('instance', instance)
        if instance:
            try:
                uav = UAV.objects.get(id=instance.uav.id)
                # print('uav in delete', uav)
                uav.is_available = True
                uav.save()

                instance.is_deleted = True
                instance.save()

                return Response(status=status.HTTP_204_NO_CONTENT)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            raise('object not found')