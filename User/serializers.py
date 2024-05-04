from rest_framework import serializers

from Flight.serializers import FlightSerializer
from User.models import User, CheckIn


class UserSerializer(serializers.ModelSerializer):
    assigned_flight = FlightSerializer(read_only=True)

    class Meta:
        model = User
        fields = ['name', 'age', 'visual_percentage', 'mail', 'pwd', 'dni', 'passport', 'address', 'birthday', 'assigned_flight']

class CheckInSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    flight = FlightSerializer(read_only=True)

    class Meta:
        model = CheckIn
        fields = ['user', 'flight', 'seat', 'fast_track', 'priority', 'bags']