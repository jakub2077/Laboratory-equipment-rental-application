from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.permissions import DjangoModelPermissions, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, viewsets
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken


from django.http import JsonResponse
from django.contrib.auth.models import User

from items.models import Item,ItemRent
from items.api.serializers import ItemSerializer, UserSerializer, ItemRentSerializer
from items.api.permissons import AdminPermission, TeacherPermission

def getRoutes(request):
    """
    Get all routes in API 
    """
    routes = [
        'GET /api/info',
        'GET /api/token'
        'GET /api/items',
        'GET /api/items/:id',
        'GET /api/users',
        'GET /api/users/:id',
        'GET /api/students',
        #'POST /api-token-auth',
    ]
    return JsonResponse(routes, safe=False)


class InfoView(APIView):
    """
    Info view returning base information about request user 
    """
    authentication_classes = [BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = {
            'user': str(request.user),  # `django.contrib.auth.User` instance.
            'first_name': str(request.user.first_name),
            'last_name': str(request.user.last_name),
            'email': str(request.user.email),
            'role': list(request.user.groups.values_list('name',flat=True)),
            'token': str(Token.objects.get(user=request.user)),
            'auth': str(request.auth),  # None
        }
        return Response(content)


class CustomAuthToken(ObtainAuthToken):
    """
    Obtain token and user info
    """
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'user': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
            'role': list(user.groups.values_list('name',flat=True)),
        })


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


class ItemRentListView(generics.ListCreateAPIView):
    """
    List all items, or create a new ItemRent instance
    """
    queryset = ItemRent.objects.all()
    serializer_class = ItemRentSerializer
    permission_classes = [DjangoModelPermissions]
    authentication_classes = [BasicAuthentication, TokenAuthentication]


class ItemRentDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retreive, update or delete an ItemRent instance
    """ 
    queryset = ItemRent.objects.all()
    serializer_class = ItemRentSerializer
    permission_classes = [DjangoModelPermissions]
    authentication_classes = [BasicAuthentication, TokenAuthentication]


class UserListView(generics.ListCreateAPIView):
    """
    List or create users
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AdminPermission]
    authentication_classes = [BasicAuthentication, TokenAuthentication]


class UserDetailView(generics.RetrieveUpdateAPIView):
    """
    Retrieve or update user
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AdminPermission]
    authentication_classes = [BasicAuthentication, TokenAuthentication]

        
class StudentsListView(viewsets.ReadOnlyModelViewSet):
    """
    List all students
    """
    queryset = User.objects.filter(groups__name='Student')
    serializer_class = UserSerializer
    permission_classes = [TeacherPermission]
    authentication_classes = [BasicAuthentication, TokenAuthentication]