from Location.models import Location
from Location.serializers import LocationSerializer


# Create a new location
@staticmethod
def createLocation(latitude, longitude, type):
    location = Location(latitude=latitude, longitude=longitude, type=type)
    location.save()
    serializer = LocationSerializer(location, many=False)
    return serializer