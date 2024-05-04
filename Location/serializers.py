from rest_framework import serializers

from Location.models import Location, BoardingDoor


class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location
        fields = ['latitude', 'longitude', 'type']

class BoardingDoorSerializer(serializers.ModelSerializer):
    location = LocationSerializer(read_only=True)
    class Meta:
        model = BoardingDoor
        fields = ['location', 'code', 'finger']