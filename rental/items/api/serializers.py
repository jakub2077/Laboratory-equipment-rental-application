from items.models import Item
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
            'date_rented',
            'date_returned',
            ]
   