from Location.models import Location

# Delete a certain user's location
@staticmethod
def deleteLocation(latitude, longitude):
    location = Location.objects.get(latitude=latitude, longitude=longitude)
    location.delete()