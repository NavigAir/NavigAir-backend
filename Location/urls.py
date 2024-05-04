from django.urls import path
from Location.views import views, location

urlpatterns = [
    path('', location.locationList, name='list_locations'),
    path('unit', location.locations, name='locations'),
    path('address/coordinates', views.addressConverter, name='address_to_coordinates_converter'),
    path('coordinates/address', views.coordinatesConverter, name='coordinates_to_address_converter'),
    path('distance', views.calculateDistanceBetweenCoordinates, name='calculate_distance'),
    path('routes', views.calculateRouteBetweenCoordinates, name='calculate_route'),
    path('places', views.getNearbyPlacesByText, name='nearby_places')
]