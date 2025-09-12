from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Item, MenuItem
from .serializers import ItemSerializer
from django.http import JsonResponse

'''
NOTE: Conside this as a reference and follow this same coding structure or format to work on you tasks
'''

# Create your views here.
class ItemView(APIView):

    def get(self, request):
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_menu_item(request, pk):
    try: if pk == 1:
        return Response({"id": 1, "name": "Pizza", "price": "10.99"})

        else:
            raise ValueError ("Menu item not found")

    except ValueError as e:
        return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)

    except Exception as e:
        return Response({"error": f"Unexpected error: {str(e)}*},
        status=status.HTTP_500INTERNAL_SERVER_ERROR)


def list_menu_items(request):
    # Hardcoded list of menu items(mock data for now)

    menu_items = [
        {"id": 1, "name": "Pizza", "price": 9.99},
        {"id": 2, "name": "Burger", "price": 5.98},
        {"id": 3, "name": "Pasta", "price": 8.98},
    ]

    return JsonResponse(menu_items, safe=False)


def menu_view(request):
    items = MenuItem.objects.all()
    return render(request, "menu.html", {"items": items})

    