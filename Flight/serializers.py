from rest_framework import serializers

from Flight.models import Flight, Boarding
from Location.serializers import BoardingDoorSerializer


class FlightSerializer(serializers.ModelSerializer):

    class Meta:
        model = Flight
        fields = ['id', 'origin', 'destination', 'departure_time', 'arrival_time', 'date', 'company', 'plane']

class BoardingSerializer(serializers.ModelSerializer):
    boarding_door = BoardingDoorSerializer(read_only=True)
    flight = FlightSerializer(read_only=True)
    class Meta:
        model = Boarding
        fields = ['flight', 'boarding_door', 'opening_time', 'last_call', 'opened']