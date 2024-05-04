from Flight.models import Flight
from Flight.serializers import FlightSerializer

# Get a certain flight
@staticmethod
def getFlight(id):
    flight = Flight.objects.get(id=id)
    serializer = FlightSerializer(flight)
    return serializer

# List all flights
@staticmethod
def listFlights():
    flights = Flight.objects.all()
    data = FlightSerializer(flights, many=True)
    return data