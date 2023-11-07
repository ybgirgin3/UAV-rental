from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name

class UAV(models.Model):
    """
        UAV Model
    """
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.CharField(max_length=100)
    weight = models.CharField(max_length=10)
    hourly_rate = models.DecimalField(max_digits=12, decimal_places=2)
    is_available = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f'{self.name}: {self.description}'


class Customer(models.Model):
    """
        Customer Model
    """
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self) -> str:
        return f'{self.firstname} {self.lastname}'


class Reservation(models.Model):
    """
        Reservation Model
    """
    uav = models.ForeignKey(UAV, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    issue_date = models.DateField()
    return_date = models.DateField()

    def __str__(self) -> str:
        return f'{self.uav}: {self.customer}, expires at: {self.end_time}'
