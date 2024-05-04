from Flight.models import Flight, Boarding
from Location.models import Location


# Delete a certain flight
@staticmethod
def deleteFlight(id):
    flight = Flight.objects.get(id=id)
    flight.delete()

@staticmethod
def deleteBoarding(id, latitude, longitude):
    location = Location.objects.get(latitude=latitude, longitude=longitude)
    boarding = Boarding.objects.get(boarding_door_id=location.id, flight_id=id)
    boarding.delete()