from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class UserProfile(models.Model):
    # Link to the built-in User model
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Extra fields

    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)


    def __str__(self):
        return self.user.username