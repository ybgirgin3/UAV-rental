from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser


# class User(models.Model):
class User(AbstractUser):
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    phone = models.CharField(max_length=12)
    is_active = models.BooleanField(default=True)

    def profile(self):
        profile = Profile.objects.get(user=self)

    def __str__(self) -> str:
        return f'{self.username}'

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=1000)
    bio = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to='user_images', default='default.jpg')
    verified = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.full_name
    
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)