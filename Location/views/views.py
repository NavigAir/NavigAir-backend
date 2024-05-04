from django.http import JsonResponse
from django.shortcuts import render
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import api_view

from Location.services.getters import calculateDistance, calculateRoute, getNearbyPlaces
from Location.services.setters import convertAddressToCoordinates, convertCoordinatesToAddress


# Create your views here.
@swagger_auto_schema(
    method='put',
    operation_description="Converts a given address to geographic coordinates using a PUT request.",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        required=['address'],
        properties={
            'address': openapi.Schema(type=openapi.TYPE_STRING, description='Full address to be converted.')
        }
    ),
    responses={
        status.HTTP_200_OK: openapi.Response(
            description="Geographic coordinates of the provided address.",
            examples={
                "application/json": {
                    "latitude": 12.345678,
                    "longitude": 98.765432
                }
            }
        ),
        status.HTTP_400_BAD_REQUEST: openapi.Response(
            description="Address parameter is missing.",
            examples={
                "application/json": {"error": "Address is required"}
            }
        ),
        status.HTTP_500_INTERNAL_SERVER_ERROR: openapi.Response(
            description="An error occurred during the conversion process.",
            examples={
                "application/json": {"error": "Internal error"}
            }
        )
    }
)
@api_view(['PUT'])
def addressConverter(request):
    address = request.data.get('address')
    if address is None:
        return JsonResponse({'error': 'Address is required'}, status=status.HTTP_400_BAD_REQUEST)
    try:
        coordinates = convertAddressToCoordinates(address)
    except Exception:
        return JsonResponse({'error': 'Internal error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return JsonResponse(coordinates, status=status.HTTP_200_OK, safe=False)

@swagger_auto_schema(
    method='put',
    operation_description="Converts a given address to geographic coordinates using a PUT request.",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        required=['latitude', 'longitude'],
        properties={
            'latitude': openapi.Schema(type=openapi.TYPE_STRING, description='Latitude to be converted.'),
            'longitude': openapi.Schema(type=openapi.TYPE_STRING, description='Longitude to be converted.')
        }
    ),
    responses={
        status.HTTP_200_OK: openapi.Response(
            description="Address corresponding to the provided coordinates.",
            examples={
                "application/json": {
                    "formatted_address": "123 Main St, City, Country",
                    "comarca": "County",
                    "region": "Region",
                    "country": "Country"
                }
            }
        ),
        status.HTTP_400_BAD_REQUEST: openapi.Response(
            description="Latitude and/or longitude parameter is missing.",
            examples={
                "application/json": {"error": "Latitude and longitude are required"}
            }
        ),
        status.HTTP_500_INTERNAL_SERVER_ERROR: openapi.Response(
            description="An error occurred during the conversion process.",
            examples={
                "application/json": {"error": "Internal error"}
            }
        )
    }
)
@api_view(['PUT'])
def coordinatesConverter(request):
    latitude = request.data.get('latitude')
    longitude = request.data.get('longitude')
    if None in [latitude, longitude]:
        return JsonResponse({'error': 'Latitude and longitude are required'}, status=status.HTTP_400_BAD_REQUEST)
    try:
        address = convertCoordinatesToAddress(latitude, longitude)
    except Exception:
        return JsonResponse({'error': 'Internal error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return JsonResponse(address, status=status.HTTP_200_OK, safe=False)

@swagger_auto_schema(
    method='get',
    operation_description="Calculates the distance between two sets of geographic coordinates.",
    manual_parameters=[
        openapi.Parameter('origin_lat', openapi.IN_QUERY, description="Latitude of the origin point.", type=openapi.TYPE_STRING),
        openapi.Parameter('origin_long', openapi.IN_QUERY, description="Longitude of the origin point.", type=openapi.TYPE_STRING),
        openapi.Parameter('destination_lat', openapi.IN_QUERY, description="Latitude of the destination point.", type=openapi.TYPE_STRING),
        openapi.Parameter('destination_long', openapi.IN_QUERY, description="Longitude of the destination point.", type=openapi.TYPE_STRING),
    ],
    responses={
        status.HTTP_200_OK: openapi.Response(
            description="Distance between the origin and destination points in kilometers.",
            schema=openapi.Schema(type=openapi.TYPE_NUMBER)
        ),
        status.HTTP_400_BAD_REQUEST: openapi.Response(
            description="One or more required parameters are missing.",
            examples={
                "application/json": {"error": "Origin_lat, origin_long, destination_lat, and destination_long are required"}
            }
        ),
        status.HTTP_500_INTERNAL_SERVER_ERROR: openapi.Response(
            description="An internal server error occurred.",
            examples={
                "application/json": {"error": "Internal error"}
            }
        )
    }
)
@api_view(['GET'])
def calculateDistanceBetweenCoordinates(request):
    origin_lat = request.query_params.get('origin_lat')
    origin_long = request.query_params.get('origin_long')
    destination_lat = request.query_params.get('destination_lat')
    destination_long = request.query_params.get('destination_long')

    if None in [origin_lat, origin_long, destination_lat, destination_long]:
        return JsonResponse({'error': 'Origin_lat, origin_long, destination_lat and destination_long are required'},
                            status=status.HTTP_400_BAD_REQUEST)
    try:
        distance = calculateDistance(origin_lat, origin_long, destination_lat, destination_long)
    except Exception:
        return JsonResponse({'error': 'Internal error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return JsonResponse(distance, status=status.HTTP_200_OK, safe=False)

@swagger_auto_schema(
    method='get',
    operation_description="Calculates the optimal route between two sets of geographic coordinates.",
    manual_parameters=[
        openapi.Parameter('origin_lat', openapi.IN_QUERY, description="Latitude of the origin point.", type=openapi.TYPE_STRING),
        openapi.Parameter('origin_long', openapi.IN_QUERY, description="Longitude of the origin point.", type=openapi.TYPE_STRING),
        openapi.Parameter('destination_lat', openapi.IN_QUERY, description="Latitude of the destination point.", type=openapi.TYPE_STRING),
        openapi.Parameter('destination_long', openapi.IN_QUERY, description="Longitude of the destination point.", type=openapi.TYPE_STRING),
    ],
    responses={
        status.HTTP_200_OK: openapi.Response(
            description="Distance between the origin and destination points in kilometers.",
            schema=openapi.Schema(type=openapi.TYPE_NUMBER)
        ),
        status.HTTP_400_BAD_REQUEST: openapi.Response(
            description="One or more required parameters are missing.",
            examples={
                "application/json": {"error": "Origin_lat, origin_long, destination_lat, and destination_long are required"}
            }
        ),
        status.HTTP_500_INTERNAL_SERVER_ERROR: openapi.Response(
            description="An internal server error occurred.",
            examples={
                "application/json": {"error": "Internal error"}
            }
        )
    }
)
@api_view(['GET'])
def calculateRouteBetweenCoordinates(request):
    origin_lat = request.query_params.get('origin_lat')
    origin_long = request.query_params.get('origin_long')
    destination_lat = request.query_params.get('destination_lat')
    destination_long = request.query_params.get('destination_long')

    if None in [origin_lat, origin_long, destination_lat, destination_long]:
        return JsonResponse({'error': 'Origin_lat, origin_long, destination_lat and destination_long are required'},
                            status=status.HTTP_400_BAD_REQUEST)

    try:
        route = calculateRoute(origin_lat, origin_long, destination_lat, destination_long)
    except Exception:
        return JsonResponse({'error': 'Internal error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return JsonResponse(route, status=status.HTTP_200_OK, safe=False)

@swagger_auto_schema(
    method='get',
    operation_description="Retrieve nearby places based on text input, latitude, and longitude",
    manual_parameters=[
        openapi.Parameter('latitude', openapi.IN_QUERY, description="Latitude of the location", type=openapi.TYPE_STRING),
        openapi.Parameter('longitude', openapi.IN_QUERY, description="Longitude of the location", type=openapi.TYPE_STRING),
        openapi.Parameter('string', openapi.IN_QUERY, description="Search string for places", type=openapi.TYPE_STRING)
    ],
    responses={
        200: openapi.Response('Successful Response', openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'results': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Schema(type=openapi.TYPE_OBJECT)),
                'status': openapi.Schema(type=openapi.TYPE_STRING)
            }
        )),
        400: 'String, latitude and longitude are required',
        500: 'Internal error'
    }
)

@api_view(['GET'])
def getNearbyPlacesByText(request):
    latitude = request.query_params.get('latitude')
    longitude = request.query_params.get('longitude')
    string = request.query_params.get('string')

    if None in [latitude, longitude]:
        return JsonResponse({'error': 'String, latitude and longitude are required'},
                            status=status.HTTP_400_BAD_REQUEST)
    try:
        places = getNearbyPlaces(latitude, longitude, string)
    except Exception:
        return JsonResponse({'error': 'Internal error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return JsonResponse(places, status=status.HTTP_200_OK, safe=False)