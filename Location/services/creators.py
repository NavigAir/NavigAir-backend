from Location.models import Location, BoardingDoor
from Location.serializers import LocationSerializer, BoardingDoorSerializer


# Create a new location
@staticmethod
def createLocation(latitude, longitude, type):
    location = Location(latitude=latitude, longitude=longitude, type=type)
    location.save()
    serializer = LocationSerializer(location, many=False)
    return serializer

# Create a new location
@staticmethod
def createBoardingDoor(latitude, longitude, type, code, finger):
    if finger == "true":
        f = True
    else:
        f = False
    boarding_door = BoardingDoor(latitude=latitude, longitude=longitude, type=type, code=code, finger=f)
    boarding_door.save()
    serializer = BoardingDoorSerializer(boarding_door, many=False)
    return serializer