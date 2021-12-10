from django.contrib import admin
from .models import Item



class ItemAdmin(admin.ModelAdmin):
    list_display = [
        'pk', 
        'description', 
        'status'
        ]

    list_filter = [
        'status', 
        'university_number',
        'building_number',
        'faculty_number',
        'room_number',
        'rented_by',
        ]
    
admin.site.register(Item, ItemAdmin)