from items.api import views as api_views
from django.urls import path


urlpatterns = [
    path('', api_views.getRoutes, name='api-routes'),
    path('info/', api_views.InfoView.as_view(), name='api-info'),
    path('token/', api_views.CustomAuthToken.as_view(), name='api-token'),

    path('items/', api_views.ItemListView.as_view(), name='api-items'),
    path('user-items/', api_views.UserItemListView.as_view(), name='api-useritems'),
    path('items/<str:pk>/', api_views.ItemDetailView.as_view(), name='api-items-detail'),

    path('rents/', api_views.ItemRentListView.as_view(), name='api-rents'),
    path('rents/<str:pk>/', api_views.ItemRentDetailView.as_view(), name='api-rents-detail'),

    path('users/', api_views.UserListView.as_view(), name='api-users'),
    path('users/<str:pk>', api_views.UserDetailView.as_view(), name='api-users-detail'),
    path('users/<str:pk>/info', api_views.UserNameView.as_view(), name='api-users-info'),
    path('students/', api_views.StudentsListView.as_view({'get': 'list'}), name='api-students'),
]
