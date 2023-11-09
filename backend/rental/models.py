from django.db import models
# from django.contrib.auth.models import User
from user.models import User

class Category(models.Model):
    """Category Model
    Represents a category for UAVs.

    Attributes:
        name (str): The name of the category.

    Methods:
        __str__: Returns the category's name as a string.

    Example:
        category = Category(name="Quadcopters")
        print(category)  # Output: "Quadcopters"
    """
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name

class UAV(models.Model):
    """UAV Model
    Represents a UAV (Unmanned Aerial Vehicle) with its details.

    Attributes:
        name (str): The name of the UAV.
        description (str): A description of the UAV.
        category (Category): The category to which the UAV belongs.
        brand (str): The brand or manufacturer of the UAV.
        weight (str): The weight of the UAV.
        hourly_rate (Decimal): The hourly rental rate for the UAV.
        is_available (bool): Indicates if the UAV is available for rental.

    Methods:
        __str__: Returns a string representation of the UAV.

    Example:
        uav = UAV(name="Drone X", description="A high-performance drone", category=category, brand="XYZ Co.", weight="2kg", hourly_rate=25.00, is_available=True)
        print(uav)  # Output: "Drone X: A high-performance drone"
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


class Reservation(models.Model):
    """Reservation Model
    Represents a reservation of a UAV by a customer.

    Attributes:
        uav (UAV): The UAV being reserved.
        customer (User): The customer making the reservation.
        issue_date (Date): The date the reservation is made.
        return_date (Date): The date the UAV is expected to be returned.
        is_deleted (bool): Indicates if the reservation is deleted or active.

    Methods:
        __str__: Returns a string representation of the reservation.

    Example:
        reservation = Reservation(uav=uav, customer=user, issue_date="2023-11-10", return_date="2023-11-15", is_deleted=False)
        print(reservation)  # Output: "Drone X: John Doe, expires at: 2023-11-15"
    """
    uav = models.ForeignKey(UAV, on_delete=models.CASCADE)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    issue_date = models.DateField()
    return_date = models.DateField()
    is_deleted = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'{self.uav}: {self.customer}, expires at: {self.return_date}'
