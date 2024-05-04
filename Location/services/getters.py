import requests

from BackendNavigair.settings import GOOGLE_MAPS_API_KEY


# Calculate the distance between two coordinates
@staticmethod
def calculateDistance(origin_lat, origin_long, destination_lat, destination_long):
    base_url = "https://maps.googleapis.com/maps/api/distancematrix/json"

    origins = f"{origin_lat},{origin_long}"
    destinations = f"{destination_lat},{destination_long}"
    params = {
        "origins": origins,
        "destinations": destinations,
        "key": GOOGLE_MAPS_API_KEY
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    if data['status'] == 'OK' and data['rows']:
        elements = data['rows'][0]['elements'][0]
        if elements['status'] == 'OK':
            result = elements['distance']['text']
        else:
            result = Exception
    else:
        result = Exception
    return result

# Get the walking optimal rute between two coordinates
@staticmethod
def calculateRoute(origin_lat, origin_long, destination_lat, destination_long):
    origins = f"{origin_lat},{origin_long}"
    destinations = f"{destination_lat},{destination_long}"
    url = f'https://maps.googleapis.com/maps/api/directions/json?origin={origins}&destination={destinations}&mode=walking&key={GOOGLE_MAPS_API_KEY}'
    response = requests.get(url)
    data = response.json()
    return data

# Get the surrounding places based on a text
@staticmethod
def getNearbyPlaces(latitude, longitude, string):
    url_base = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
    parametros = {
        'location': f'{latitude},{longitude}',
        'radius': 500,  # Radio en metros
        'type': string,
        'key': GOOGLE_MAPS_API_KEY
    }
    respuesta = requests.get(url_base, params=parametros)
    if respuesta.status_code == 200:
        return respuesta.json()
    else:
        return Exception