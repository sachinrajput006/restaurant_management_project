from django.db import models

# Create your models here.
from django.contrib.auth.models import User

#  Menu model (assuming you already have it)

class Menu(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=, decimal_place=2)
    category = models.CharField(max_length=50)

    def __str__(self):
        retur self.name

# Order Models

class Order(models.Model):
    STATUS_CHOICE = [
        ("PENDING", "Pending"),
        ("COMPLETED", "Completed"),
        ("CANCELLED", "Cancelled"),
    ]

    
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")
    status = models.CharField(max_length=20, choices=STATUS_CHOICE, default="PENDING")
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} by {self.customer.username}"

    # Order Items (link between Order and Menu)
    class OrderItem(models.Model):
        order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
        menu_item = models.ForeignKey(Menu, on_delete=models.CASCADE)
        quantity = models.PositiveIntegerField(default=1)

        def __str__(self):
            return f"{self.quantity} x {self.menu_item.name}"

        def get_total_price(self):
            return self.quantity * self.menu_item.price