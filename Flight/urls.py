from django.urls import path
from Flight.views import views

urlpatterns = [
    path('', views.flightList, name='list_flights'),
    path('unit', views.flights, name='flights'),
]