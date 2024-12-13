from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('trip/<int:pk>/edit/', views.update_trip, name='update_trip'),
    path('trip/<int:pk>/delete/', views.confirm_delete_trip, name='delete_trip'),
    path('trip_list/', views.trip_list, name='trip_list'),
    path('create/', views.create_trip, name='create_trip'),
]
