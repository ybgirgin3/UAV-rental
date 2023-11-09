from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """User Model
    Represents a user in the application, inheriting from the default AbstractUser of Django.

    Attributes:
        username (str): The username of the user.
        email (str): The email address of the user.
        password (str): The password of the user.
        phone (str): The phone number of the user.
        is_active (bool): Indicates whether the user is active.

    Methods:
        profile(): Retrieves the user's profile.

    Example:
        user = User(username="john_doe", email="john@example.com", password="password123", phone="1234567890", is_active=True)
        user.profile()  # Returns the user's profile object
    """
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
    """Profile Model
    Represents additional user profile information.

    Attributes:
        user (OneToOneField): The user associated with this profile.
        full_name (str): The full name of the user.
        bio (str): A short bio or description of the user (optional).
        image (ImageField): User's profile image.
        verified (bool): Indicates whether the profile is verified.

    Example:
        profile = Profile(user=user_instance, full_name="John Doe", bio="A software developer", verified=True)
        profile.save()
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=1000)
    bio = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to='user_images', default='default.jpg')
    verified = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.full_name
    
def create_user_profile(sender, instance, created, **kwargs):
    """Signal Handler: Create User Profile
    Creates a user profile when a new user is created.

    Args:
        sender: The sender of the signal.
        instance: The user instance.
        created (bool): Indicates if the user is being created.

    Example:
        post_save.connect(create_user_profile, sender=User)
    """
    if created:
        Profile.objects.create(user=instance)

def save_user_profile(sender, instance, **kwargs):
    """Signal Handler: Save User Profile
    Saves the user profile.

    Args:
        sender: The sender of the signal.
        instance: The user instance.

    Example:
        post_save.connect(save_user_profile, sender=User)
    """
    instance.profile.save()

post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)