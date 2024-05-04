from Location.models import Location, BoardingDoor


@staticmethod
def existsLocation(latitude, longitude):
    return Location.objects.filter(latitude=latitude, longitude=longitude).exists()

@staticmethod
def existsBoardingDoor(latitude, longitude):
    return BoardingDoor.objects.filter(latitude=latitude, longitude=longitude).exists()