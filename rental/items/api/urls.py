from items.api import views as api_views
from django.urls import path


urlpatterns = [
    path('', api_views.getRoutes, name='api-routes'),
    path('items/', api_views.ItemListView.as_view(), name='api-items'),
    path('items/<str:pk>/', api_views.ItemDetailView.as_view(), name='api-items-detail'),
    path('example/', api_views.ExampleView.as_view(), name='api-example'),
]