from django.db import models


class User(models.Model):
    firstname = models.CharField(max_length=100)
    middlename = models.CharField(max_length=100, blank=True, null=True, default='')
    lastname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    phone = models.CharField(max_length=12)
    is_active = models.BooleanField(default=True)
    
    def __str__(self) -> str:
        return f'{self.firstname} {self.middlename} {self.lastname}'