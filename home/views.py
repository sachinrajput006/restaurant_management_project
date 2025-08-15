from django.shortcuts import render
from .models import Restaurant

# Create your views here.


def homepage(request):
    restaurant = Restaurant.objects.first()
    return render(request, "homepage.html", {"restaurant": restaurant})

    def about(request):
        restaurant = Restaurant.objects.first()
        return render(request, "about.html", {"restaurant": restaurant})