from django.shortcuts import render
from .models import Restaurant
from django.shortcuts import settings

# Create your views here.


def homepage(request):

    restaurant = Restaurant.objects.first()
    phone_number = getattr(settings, "RESTAURANT_PHONE", "Not Available")
    
    return render(request, "homepage.html", {"restaurant": restaurant})

    def about(request):

        restaurant = Restaurant.objects.first()

        return render(request, "about.html", {"restaurant": restaurant})