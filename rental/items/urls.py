from items import views as items_views
from django.urls import path

app_name = 'items'
urlpatterns = [
    path('', items_views.home, name='items-home'),
    path('items/', items_views.list_items, name='list-items'),
    path('items/<int:item_id>/', items_views.view_item, name='view-item'),
]
