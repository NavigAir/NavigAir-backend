import requests

from BackendNavigair.settings import GOOGLE_MAPS_API_KEY
from Location.models import Location, BoardingDoor
from Location.serializers import LocationSerializer, BoardingDoorSerializer


# Convert coordinates into an address
@staticmethod
def convertCoordinatesToAddress(latitude, longitude):
    base_url = "https://maps.googleapis.com/maps/api/geocode/json"
    params = {
        "latlng": f"{latitude},{longitude}",
        "key": GOOGLE_MAPS_API_KEY
    }
    response = requests.get(base_url, params=params)
    data = response.json()

    if data['status'] == 'OK':
        result = data['results'][0]['formatted_address']
    else:
        result = Exception
    return result

# Convert an address into coordinates
@staticmethod
def convertAddressToCoordinates(address):
    base_url = "https://maps.googleapis.com/maps/api/geocode/json"
    params = {
        "address": address,
        "key": GOOGLE_MAPS_API_KEY
    }
    response = requests.get(base_url, params=params)
    data = response.json()

    if data['status'] == 'OK':
        latitude = data['results'][0]['geometry']['location']['lat']
        longitude = data['results'][0]['geometry']['location']['lng']
        result = [latitude, longitude]
    else:
        result = Exception
    return result

# Modify a location
@staticmethod
def putLocation(latitude, longitude, type):
    location = Location.objects.get(latitude=latitude, longitude=longitude)
    location.type = type
    location.save()
    serializer = LocationSerializer(location, many=False)
    return serializer

# Modify a boarding door
@staticmethod
def putBoardingDoor(latitude, longitude, type, code, finger):
    if finger == "true":
        f = True
    else:
        f = False
    boarding_door = BoardingDoor.objects.get(latitude=latitude, longitude=longitude)
    boarding_door.type = type
    boarding_door.code = code
    boarding_door.finger = f
    boarding_door.save()
    serializer = BoardingDoorSerializer(boarding_door, many=False)
    return serializer