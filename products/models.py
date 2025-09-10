from django.db import models

# Create your models here.
class Item(models.Model):
    item_name = models.CharField(max_length=150)
    item_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.item_name)


class MenuItem(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self):
        return f"{self.name} -{self.price}"

class Restaurant(models.Model):
    name = models.CharField(max_length=100, default="My Restaurant" )
    address = models.CharField(max_length=300, default="123 new street delhi")


    def __str__(self):
        return self.name