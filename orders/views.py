from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import response

@api_view(["GET"])
def get_menu(request):
    """
    API endpoint to retrieve the restaurant's menu.
    Hardcoded menu data for now.

    """

    menu = [
        {
            "name": "Margherita Pizza",
            "description": "Clasic pizza with fresh tomatoes, mozzarella cheese, and basil.",
            "price": 250

        },
        {
            "name": "Veggie Burger",
            "description": "Grilled veggie patty with lecture, tomato, and vegan mayo.",
            "price": 850
        },
        {
            "name": "Pasta Alfredo",
            "description": "Creamy white sauce pasta with mushrooms and herbs.",
            "price": 850
        }

    

    ]

    return Response(menu)