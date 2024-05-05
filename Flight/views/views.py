import json

from django.http import JsonResponse
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import api_view

from Flight.models import Flight
from Flight.services.creators import createFlight
from Flight.services.deleters import deleteFlight
from Flight.services.exists import existsFlight
from Flight.services.getters import listFlights, getFlight
from Flight.services.setters import putFlight


@swagger_auto_schema(
    method = 'get',
    operation_description="Get all flights",
    responses={
        200: 'OK: Operation successful',
        500: 'INTERNAL_SERVER_ERROR: Internal error'
    },
)
@api_view(['GET'])
def flightList(request):
    try:
        data = listFlights()
        return JsonResponse(data.data, status=status.HTTP_200_OK, safe=False)
    except Exception:
        return JsonResponse({'error': 'Internal error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@swagger_auto_schema(
    method='get',
    operation_description="Get a certain flight",
    manual_parameters=[
        openapi.Parameter('id', openapi.IN_QUERY, description="Flight's id", type=openapi.TYPE_STRING)
    ]
)
@swagger_auto_schema(
    method='post',
    operation_description="Add a new flight",
    manual_parameters=[
    openapi.Parameter('id', openapi.IN_QUERY, description="Flight's id", type=openapi.TYPE_STRING, required=True),
    openapi.Parameter('origin', openapi.IN_QUERY, description="Flight's origin", type=openapi.TYPE_STRING, required=True),
    openapi.Parameter('destination', openapi.IN_QUERY, description="Flight's visual destination", type=openapi.TYPE_STRING, required=True),
    openapi.Parameter('departure_time', openapi.IN_QUERY, description="Flight's departure_time", type=openapi.TYPE_STRING, required=True),
    openapi.Parameter('arrival_time', openapi.IN_QUERY, description="Flight's arrival_time", type=openapi.TYPE_STRING, required=True),
    openapi.Parameter('date', openapi.IN_QUERY, description="Flight's date", type=openapi.TYPE_STRING, required=True),
    openapi.Parameter('company', openapi.IN_QUERY, description="Flight's company", type=openapi.TYPE_STRING, required=True),
    openapi.Parameter('plane', openapi.IN_QUERY, description="Flight's plane", type=openapi.TYPE_STRING, required=True)
    ],
    responses={
        200: openapi.Response('Flight Created Successfully'),
        400: 'Flight already exists or invalid parameters',
        404: 'Flight does not exist'
    }
)
@swagger_auto_schema(
    method='put',
    operation_description="Update an existing flight",
    manual_parameters=[
        openapi.Parameter('id', openapi.IN_QUERY, description="Flight's id", type=openapi.TYPE_STRING, required=True),
        openapi.Parameter('origin', openapi.IN_QUERY, description="Flight's origin", type=openapi.TYPE_STRING,
                          required=True),
        openapi.Parameter('destination', openapi.IN_QUERY, description="Flight's visual destination",
                          type=openapi.TYPE_STRING, required=True),
        openapi.Parameter('departure_time', openapi.IN_QUERY, description="Flight's departure_time",
                          type=openapi.TYPE_STRING, required=True),
        openapi.Parameter('arrival_time', openapi.IN_QUERY, description="Flight's arrival_time",
                          type=openapi.TYPE_STRING, required=True),
        openapi.Parameter('date', openapi.IN_QUERY, description="Flight's date", type=openapi.TYPE_STRING,
                          required=True),
        openapi.Parameter('company', openapi.IN_QUERY, description="Flight's company", type=openapi.TYPE_STRING,
                          required=True),
        openapi.Parameter('plane', openapi.IN_QUERY, description="Flight's plane", type=openapi.TYPE_STRING,
                          required=True)
    ],
    responses={
        200: openapi.Response('Flight Updated Successfully'),
        400: 'User not exists or invalid parameters',
    }
)
@swagger_auto_schema(
    method='delete',
    operation_description="Delete an existing flight",
    manual_parameters=[
        openapi.Parameter('id', openapi.IN_QUERY, description="Flight's id", type=openapi.TYPE_STRING)
    ],
    responses={
        204: 'Flight deleted successfully',
        404: 'Flight not exists',
    }
)
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def flights(request):
    if request.method == "GET":
        id = request.query_params.get('id')
        try:
            serializer = getFlight(id)
            return JsonResponse(data=serializer.data, status=status.HTTP_200_OK)
        except Flight.DoesNotExist:
            return JsonResponse({'error': 'Flight does not exist'}, status=status.HTTP_404_NOT_FOUND)
    elif request.method == "POST":
        data = json.loads(request.body)
        id = data.get('id')
        origin = data.get('origin')
        destination = data.get('destination')
        departure_time = data.get('departure_time')
        arrival_time = data.get('arrival_time')
        date = data.get('date')
        company = data.get('company')
        plane = data.get('plane')
        if existsFlight(id):
            return JsonResponse({"error": "Flight already exists."},
                                status=status.HTTP_400_BAD_REQUEST)
        serializer = createFlight(id, origin, destination, departure_time, arrival_time, date, company, plane)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "PUT":
        data = json.loads(request.body)
        id = data.get('id')
        origin = data.get('origin')
        destination = data.get('destination')
        departure_time = data.get('departure_time')
        arrival_time = data.get('arrival_time')
        date = data.get('date')
        company = data.get('company')
        plane = data.get('plane')
        try:
            serializer = putFlight(id, origin, destination, departure_time, arrival_time, date, company, plane)
            return JsonResponse(serializer.data, status=status.HTTP_200_OK)
        except Flight.DoesNotExist:
            return JsonResponse({"error": "Flight not exists."},
                                status=status.HTTP_400_BAD_REQUEST)
    else:
        id = request.query_params.get('id')
        try:
            deleteFlight(id)
            return JsonResponse({'message': 'Flight deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except Flight.DoesNotExist:
            return JsonResponse({'error': 'Flight not exists'}, status=status.HTTP_404_NOT_FOUND)
