from django.db import models


class UAV(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    hourly_rate = models.DecimalField(max_digits=12, decimal_places=2)
    is_available = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f'{self.name}: {self.description}'


class Customer(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    
    def __str__(self) -> str:
        return f'{self.firstname} {self.lastname}'


class Reservation(models.Model):
    uav = models.ForeignKey(UAV, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return super().__str__()


