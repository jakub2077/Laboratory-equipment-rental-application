from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.permissions import DjangoModelPermissions, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics

from django.http import JsonResponse

from items.api.serializers import ItemSerializer
from items.models import Item


def getRoutes(request):
    """
    Get all routes in API 
    """
    routes = [
        'GET /api/items',
        'GET /api/items/:id',
        #'POST /api-token-auth',
    ]
    return JsonResponse(routes, safe=False)


class ExampleView(APIView):
    authentication_classes = [BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = {
            'user': str(request.user),  # `django.contrib.auth.User` instance.
            'email': str(request.user.email),
            'auth': str(request.auth),  # None
            'staff': str(request.user.is_staff),
        }
        return Response(content)


class ItemListView(generics.ListCreateAPIView):
    """
    List all items, or create a new item
    """
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [DjangoModelPermissions]
    authentication_classes = [BasicAuthentication, TokenAuthentication]


class ItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retreive, update or delete an item instance
    """ 
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [DjangoModelPermissions]
    authentication_classes = [BasicAuthentication, TokenAuthentication]
