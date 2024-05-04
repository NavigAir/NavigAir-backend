from Flight.models import Flight, Boarding
from Flight.serializers import FlightSerializer, BoardingSerializer
from Location.models import Location


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

@staticmethod
def putBoarding(id, latitude, longitude, opening_time, last_call, opened):
    location = Location.objects.get(latitude=latitude, longitude=longitude)
    if opened == "true":
        o = True
    else:
        o = False
    boarding = Boarding.objects.get(boarding_door_id=location.id, flight_id=id)
    boarding.opening_time = opening_time
    boarding.last_call = last_call
    boarding.opened = o
    boarding.save()
    serializer = BoardingSerializer(boarding, many=False)
    return serializer