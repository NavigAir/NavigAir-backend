from Flight.models import Flight, Boarding
from Flight.serializers import FlightSerializer, BoardingSerializer
from Location.models import Location


# Create a new location
@staticmethod
def createFlight(id, origin, destination, departure_time, arrival_time, date, company, plane):
    flight = Flight(id=id, origin=origin, destination=destination, departure_time=departure_time, arrival_time=arrival_time, date=date, company=company, plane=plane)
    flight.save()
    serializer = FlightSerializer(flight, many=False)
    return serializer

@staticmethod
def createBoarding(id, latitude, longitude, opening_time, last_call, opened):
    location = Location.objects.get(latitude=latitude, longitude=longitude)
    if opened == "true":
        o = True
    else:
        o = False
    boarding = Boarding(flight_id=id, boarding_door_id=location.id, opening_time=opening_time, last_call=last_call, opened=o)
    boarding.save()
    serializer = BoardingSerializer(boarding, many=False)
    return serializer