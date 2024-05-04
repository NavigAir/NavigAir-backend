from django.http import JsonResponse
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import api_view

from Location.models import Location
from Location.services.creators import createLocation
from Location.services.deleters import deleteLocation
from Location.services.exists import existsLocation
from Location.services.getters import listLocations, getLocation
from Location.services.setters import putLocation


@swagger_auto_schema(
    method = 'get',
    operation_description="Get all locations",
    responses={
        200: 'OK: Operation successful',
        500: 'INTERNAL_SERVER_ERROR: Internal error'
    },
)
@api_view(['GET'])
def locationList(request):
    try:
        data = listLocations()
        return JsonResponse(data.data, status=status.HTTP_200_OK, safe=False)
    except Exception:
        return JsonResponse({'error': 'Internal error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@swagger_auto_schema(
    method='get',
    operation_description="Get the location from a certain latitude and longitude",
    manual_parameters=[
        openapi.Parameter('latitude', openapi.IN_QUERY, description="Latitude of the location", type=openapi.TYPE_STRING),
        openapi.Parameter('longitude', openapi.IN_QUERY, description="Longitude of the location", type=openapi.TYPE_STRING),
    ]
)
@swagger_auto_schema(
    method='post',
    operation_description="Add a new location",
    manual_parameters=[
    openapi.Parameter('latitude', openapi.IN_QUERY, description="Latitude of the location", type=openapi.TYPE_STRING, required=True),
    openapi.Parameter('longitude', openapi.IN_QUERY, description="Longitude of the location", type=openapi.TYPE_STRING, required=True),
    openapi.Parameter('type', openapi.IN_QUERY, description="Type of the location", type=openapi.TYPE_STRING, required=True, enum=['security_control', 'wc', 'boarding_door']),
    ],
    responses={
        200: openapi.Response('Location Created Successfully'),
        400: 'Location already exists or invalid parameters',
        404: 'Location does not exist'
    }
)
@swagger_auto_schema(
    method='put',
    operation_description="Update an existing location",
    manual_parameters=[
        openapi.Parameter('latitude', openapi.IN_QUERY, description="Latitude of the location", type=openapi.TYPE_STRING, required=True),
        openapi.Parameter('longitude', openapi.IN_QUERY, description="Longitude of the location", type=openapi.TYPE_STRING, required=True),
        openapi.Parameter('type', openapi.IN_QUERY, description="Type of the location", type=openapi.TYPE_STRING, required=True, enum=['security_control', 'wc', 'boarding_door']),
    ],
    responses={
        200: openapi.Response('Location Updated Successfully'),
        400: 'Location not exists or invalid parameters',
    }
)
@swagger_auto_schema(
    method='delete',
    operation_description="Delete an existing location",
    manual_parameters=[
    openapi.Parameter('latitude', openapi.IN_QUERY, description="Latitude of the location", type=openapi.TYPE_STRING, required=True),
    openapi.Parameter('longitude', openapi.IN_QUERY, description="Longitude of the location", type=openapi.TYPE_STRING, required=True),
    ],
    responses={
        204: 'Location deleted successfully',
        404: 'Location not exists',
    }
)
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def locations(request):
    if request.method == "GET":
        latitude = request.query_params.get('latitude')
        longitude = request.query_params.get('longitude')
        try:
            serializer = getLocation(latitude, longitude)
            return JsonResponse(data=serializer.data, status=status.HTTP_200_OK)
        except Location.DoesNotExist:
            return JsonResponse({'error': 'Location does not exist'}, status=status.HTTP_404_NOT_FOUND)
    elif request.method == "POST":
        latitude = request.query_params.get('latitude')
        longitude = request.query_params.get('longitude')
        type = request.query_params.get('type')
        if existsLocation(latitude, longitude):
            return JsonResponse({"error": "Location for this user already exists."},
                                status=status.HTTP_400_BAD_REQUEST)
        serializer = createLocation(latitude, longitude, type)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "PUT":
        latitude = request.query_params.get('latitude')
        longitude = request.query_params.get('longitude')
        type = request.query_params.get('type')
        try:
            serializer = putLocation(latitude, longitude, type)
            return JsonResponse(serializer.data, status=status.HTTP_200_OK)
        except Location.DoesNotExist:
            return JsonResponse({"error": "Location not exists."},
                                status=status.HTTP_400_BAD_REQUEST)
    else:
        latitude = request.query_params.get('latitude')
        longitude = request.query_params.get('longitude')
        try:
            deleteLocation(latitude, longitude)
            return JsonResponse({'message': 'Location deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except Location.DoesNotExist:
            return JsonResponse({'error': 'Location not exists'}, status=status.HTTP_404_NOT_FOUND)
