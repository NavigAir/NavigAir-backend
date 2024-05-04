from Flight.models import Flight, Boarding
from Flight.serializers import FlightSerializer, BoardingSerializer
from Location.models import Location


# Get a certain flight
@staticmethod
def getFlight(id):
    flight = Flight.objects.get(id=id)
    serializer = FlightSerializer(flight)
    return serializer

@staticmethod
def getBoarding(id, latitude, longitude):
    location = Location.objects.get(latitude=latitude, longitude=longitude)
    boarding = Boarding.objects.get(boarding_door_id=location.id, flight_id=id)
    serializer = BoardingSerializer(boarding)
    return serializer

# List all flights
@staticmethod
def listFlights():
    flights = Flight.objects.all()
    data = FlightSerializer(flights, many=True)
    return data