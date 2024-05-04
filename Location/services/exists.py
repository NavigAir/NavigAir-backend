from Location.models import Location

@staticmethod
def existsLocation(latitude, longitude):
    return Location.objects.filter(latitude=latitude, longitude=longitude).exists()