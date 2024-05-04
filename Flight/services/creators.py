from Flight.models import Flight
from Flight.serializers import FlightSerializer


# Create a new location
@staticmethod
def createFlight(id, origin, destination, departure_time, arrival_time, date, company, plane):
    flight = Flight(id=id, origin=origin, destination=destination, departure_time=departure_time, arrival_time=arrival_time, date=date, company=company, plane=plane)
    flight.save()
    serializer = FlightSerializer(flight, many=False)
    return serializer