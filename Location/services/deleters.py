from Location.models import Location, BoardingDoor


# Delete a certain location
@staticmethod
def deleteLocation(latitude, longitude):
    location = Location.objects.get(latitude=latitude, longitude=longitude)
    location.delete()

# Delete a certain boarding door
@staticmethod
def deleteBoardingDoor(latitude, longitude):
    boarding_door = BoardingDoor.objects.get(latitude=latitude, longitude=longitude)
    boarding_door.delete()