from django.contrib import admin

# Register your models here.
from .models import Menu, Order, OrderItem

# Inline admin for Order Items (so items show inside order)
class OrderItemInline(admin.TabularInline):

    model = OrderItem
    extra = 1 # how many empty rows to show by default

# Menu Model Admin
@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "price")
    search_fields = ("name", "category")
    list_filter = ("category",)


# Order Models Admin 

class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "customer", "total_amount", "status", "created_at")
    list_filter = ("status", "created_at")
    search_fields = ("customer__username",)
    inlines = [OrderItemInline] # shows items inside Order

# OrderItem Model Admin (optional, since it's already inline)
@admin.register(OrderItem)
class OrderItemInline(admin.ModelAdmin):
    list_display = ("order", "menu_item", "quantity")