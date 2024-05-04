from Flight.models import Flight, Boarding
from Location.models import Location


@staticmethod
def existsFlight(id):
    return Flight.objects.filter(id=id).exists()

@staticmethod
def existsBoarding(id, latitude, longitude):
    location = Location.objects.get(latitude=latitude, longitude=longitude)
    return Boarding.objects.filter(boarding_door_id=location.id, flight_id=id).exists()