from Flight.models import Flight

# Delete a certain flight
@staticmethod
def deleteFlight(id):
    flight = Flight.objects.get(id=id)
    flight.delete()