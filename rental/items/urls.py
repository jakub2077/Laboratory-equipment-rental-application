from items import views as items_views
from django.urls import path

app_name = 'items'
urlpatterns = [
    path('', items_views.home, name='items-home'),
    path('items/', items_views.ItemListView.as_view(), name='items-list'),
    path('items/<int:pk>/', items_views.ItemDetailView.as_view(), name='items-detail'),
    path('items/<int:pk>/update/', items_views.ItemUpdateView.as_view(), name='items-update'),
    path('items/create/', items_views.ItemCreateView.as_view(), name='items-create'),
    path('items/user/', items_views.UserItemListView.as_view(), name='items-user'),
    path('rents/', items_views.ItemRentListView.as_view(), name='rents-list'),
    path('rents/create/', items_views.ItemRentCreateView.as_view(), name='rents-create'),
    path('rents/<int:pk>/update/', items_views.ItemRentUpdateView.as_view(), name='rents-update'),
    #path('create/', items_views.createrent, name='rents-creates'),

]

