from Flight.models import Flight
from Flight.serializers import FlightSerializer

@staticmethod
def putFlight(id, origin, destination, departure_time, arrival_time, date, company, plane):
    flight = Flight.objects.get(id=id)
    flight.origin = origin
    flight.destination = destination
    flight.departure_time = departure_time
    flight.arrival_time = arrival_time
    flight.date = date
    flight.company = company
    flight.plane = plane
    flight.save()
    serializer = FlightSerializer(flight, many=False)
    return serializer