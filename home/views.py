from django.shortcuts import render
from .models import Restaurant

# Create your views here.


def homepage(request):
    restaurant = Restaurant.objects.first()
    context = {
        "restaurant_name":restaurant.restaurant_name if restaurant else "My Restaurant"

    }

    return render(request, "homepage.html", context)