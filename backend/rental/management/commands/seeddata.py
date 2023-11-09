from django.core.management.base import BaseCommand
from rental.models import UAV, Category, Reservation
from user.models import User
import random

class Command(BaseCommand):
    help = 'Seed data into the database'

    def handle(self, *args, **options):
        pass
        data_to_category = [
                {
                    "name": "Heavy Duty"
                }
        ]
        
        for item_data in data_to_category:
            try:
                Category.objects.create(**item_data)
                print('count of cat', Category.objects.count(), [{item.id, item.name} for item in Category.objects.all()])
            except Exception as e:
                print('ERROR WHILE WRITING CATEG count', Category.objects.count(), e)
            


        data_to_uav = [
                {
                    "name": "Bayraktar1",
                    "description": "Best Performance",
                    "brand": "Baykar",
                    "weight": "300000",
                    "hourly_rate": 10000,
                    "is_available": True,
                    "category": Category.objects.get(pk=random.choice([item.id for item in Category.objects.all()])),
                }
        ]

        for item_data in data_to_uav:
            UAV.objects.create(**item_data) 
            
        
        data_to_reservation = [
            {
                "customer": User.objects.get(pk=random.choice([item.id for item in User.objects.all()])),
                "uav": UAV.objects.get(pk=random.choice([item.id for item in UAV.objects.all()])),
                "issue_date": '2023-10-10',
                "return_date": '2023-11-11',
                "is_deleted": False 
            }
        ]
        for item_data in data_to_reservation:
            Reservation.objects.create(**item_data)