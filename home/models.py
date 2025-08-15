from django.db import models

# Create your models here.

class Restaurant(models.Model):
    name = models.CharField(max_length = 100)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="restaurant_images/", blank=True, null=True)

    def __str__(self):
        return self.name