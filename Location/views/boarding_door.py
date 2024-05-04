from django.http import JsonResponse
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import api_view

from Location.models import Location
from Location.services.creators import createBoardingDoor
from Location.services.deleters import deleteBoardingDoor
from Location.services.exists import existsBoardingDoor
from Location.services.getters import listBoardingDoors, getBoardingDoor
from Location.services.setters import putBoardingDoor


@swagger_auto_schema(
    method = 'get',
    operation_description="Get all boarding doors",
    responses={
        200: 'OK: Operation successful',
        500: 'INTERNAL_SERVER_ERROR: Internal error'
    },
)
@api_view(['GET'])
def boardingDoorList(request):
    try:
        data = listBoardingDoors()
        return JsonResponse(data.data, status=status.HTTP_200_OK, safe=False)
    except Exception:
        return JsonResponse({'error': 'Internal error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@swagger_auto_schema(
    method='get',
    operation_description="Get the boarding door from a certain latitude and longitude",
    manual_parameters=[
        openapi.Parameter('latitude', openapi.IN_QUERY, description="Latitude of the location", type=openapi.TYPE_STRING),
        openapi.Parameter('longitude', openapi.IN_QUERY, description="Longitude of the location", type=openapi.TYPE_STRING),
    ]
)
@swagger_auto_schema(
    method='post',
    operation_description="Add a new boarding door",
    manual_parameters=[
    openapi.Parameter('latitude', openapi.IN_QUERY, description="Latitude of the location", type=openapi.TYPE_STRING, required=True),
    openapi.Parameter('longitude', openapi.IN_QUERY, description="Longitude of the location", type=openapi.TYPE_STRING, required=True),
    openapi.Parameter('type', openapi.IN_QUERY, description="Type of the location", type=openapi.TYPE_STRING, required=True, enum=['security_control', 'wc', 'boarding_door']),
    openapi.Parameter('code', openapi.IN_QUERY, description="Code of the boarding door", type=openapi.TYPE_STRING, required=True),
    openapi.Parameter('finger', openapi.IN_QUERY, description="Check if the boarding door has a finger", type=openapi.TYPE_BOOLEAN, required=True)
    ],
    responses={
        200: openapi.Response('Boarding Door Created Successfully'),
        400: 'Location already exists or invalid parameters',
        404: 'Location does not exist'
    }
)
@swagger_auto_schema(
    method='put',
    operation_description="Update an existing boarding door",
    manual_parameters=[
        openapi.Parameter('latitude', openapi.IN_QUERY, description="Latitude of the location",
                          type=openapi.TYPE_STRING, required=True),
        openapi.Parameter('longitude', openapi.IN_QUERY, description="Longitude of the location",
                          type=openapi.TYPE_STRING, required=True),
        openapi.Parameter('type', openapi.IN_QUERY, description="Type of the location", type=openapi.TYPE_STRING,
                          required=True, enum=['security_control', 'wc', 'boarding_door']),
        openapi.Parameter('code', openapi.IN_QUERY, description="Code of the boarding door", type=openapi.TYPE_STRING,
                          required=True),
        openapi.Parameter('finger', openapi.IN_QUERY, description="Check if the boarding door has a finger",
                          type=openapi.TYPE_BOOLEAN, required=True)
    ],
    responses={
        200: openapi.Response('Boarding Door Updated Successfully'),
        400: 'Location not exists or invalid parameters',
    }
)
@swagger_auto_schema(
    method='delete',
    operation_description="Delete an existing boarding door",
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
def boardingDoors(request):
    if request.method == "GET":
        latitude = request.query_params.get('latitude')
        longitude = request.query_params.get('longitude')
        try:
            serializer = getBoardingDoor(latitude, longitude)
            return JsonResponse(data=serializer.data, status=status.HTTP_200_OK)
        except Location.DoesNotExist:
            return JsonResponse({'error': 'Location does not exist'}, status=status.HTTP_404_NOT_FOUND)
    elif request.method == "POST":
        latitude = request.query_params.get('latitude')
        longitude = request.query_params.get('longitude')
        type = request.query_params.get('type')
        code = request.query_params.get('code')
        finger = request.query_params.get('finger')
        if existsBoardingDoor(latitude, longitude):
            return JsonResponse({"error": "Location for this user already exists."},
                                status=status.HTTP_400_BAD_REQUEST)
        serializer = createBoardingDoor(latitude, longitude, type, code, finger)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "PUT":
        latitude = request.query_params.get('latitude')
        longitude = request.query_params.get('longitude')
        type = request.query_params.get('type')
        code = request.query_params.get('code')
        finger = request.query_params.get('finger')
        try:
            serializer = putBoardingDoor(latitude, longitude, type, code, finger)
            return JsonResponse(serializer.data, status=status.HTTP_200_OK)
        except Location.DoesNotExist:
            return JsonResponse({"error": "Location not exists."},
                                status=status.HTTP_400_BAD_REQUEST)
    else:
        latitude = request.query_params.get('latitude')
        longitude = request.query_params.get('longitude')
        try:
            deleteBoardingDoor(latitude, longitude)
            return JsonResponse({'message': 'Location deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except Location.DoesNotExist:
            return JsonResponse({'error': 'Location not exists'}, status=status.HTTP_404_NOT_FOUND)
