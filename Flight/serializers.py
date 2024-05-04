from rest_framework import serializers

from Flight.models import Flight


class FlightSerializer(serializers.ModelSerializer):

    class Meta:
        model = Flight
        fields = ['id', 'origin', 'destination', 'departure_time', 'arrival_time', 'date', 'company', 'plane']