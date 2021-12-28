from items.models import Item,ItemRent
from django.contrib.auth.models import User
from rest_framework import serializers

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = [
            'university_number',
            'building_number',
            'faculty_number',
            'room_number',
            'item_number',
            'description',
            'status',
            'rented_by',
            ]

class ItemRentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemRent
        fields = [
            'item_id',
            'user_id',
            'rent_date',
            'return_date',
            'is_archived',
            ]
   
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=[
            'id',
            'username',
            'email',
            'first_name',
            'last_name',
            'last_login',
            'groups',
        ]
        