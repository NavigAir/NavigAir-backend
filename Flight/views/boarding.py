from django.http import JsonResponse
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import api_view

from Flight.models import Flight, Boarding
from Flight.services.creators import createFlight, createBoarding
from Flight.services.deleters import deleteFlight, deleteBoarding
from Flight.services.exists import existsFlight, existsBoarding
from Flight.services.getters import listFlights, getFlight, getBoarding
from Flight.services.setters import putFlight, putBoarding


@swagger_auto_schema(
    method='get',
    operation_description="Get a certain boarding",
    manual_parameters=[
        openapi.Parameter('id', openapi.IN_QUERY, description="Flight's id", type=openapi.TYPE_STRING, required=True),
        openapi.Parameter('latitude', openapi.IN_QUERY, description="Boarding door latitude", type=openapi.TYPE_STRING, required=True),
        openapi.Parameter('longitude', openapi.IN_QUERY, description="Boarding door longitude", type=openapi.TYPE_STRING, required=True)
    ]
)
@swagger_auto_schema(
    method='post',
    operation_description="Add a new boarding",
    manual_parameters=[
        openapi.Parameter('id', openapi.IN_QUERY, description="Flight's id", type=openapi.TYPE_STRING, required=True),
        openapi.Parameter('latitude', openapi.IN_QUERY, description="Boarding door latitude", type=openapi.TYPE_STRING, required=True),
        openapi.Parameter('longitude', openapi.IN_QUERY, description="Boarding door longitude",
                          type=openapi.TYPE_STRING, required=True),
        openapi.Parameter('opening_time', openapi.IN_QUERY, description="Boarding's opening_time", type=openapi.TYPE_STRING, required=True),
        openapi.Parameter('last_call', openapi.IN_QUERY, description="Boarding's last call", type=openapi.TYPE_STRING, required=True),
        openapi.Parameter('opened', openapi.IN_QUERY, description="If boarding is opened", type=openapi.TYPE_BOOLEAN, required=True),
    ],
    responses={
        200: openapi.Response('Boarding Created Successfully'),
        400: 'Boarding already exists or invalid parameters',
        404: 'Boarding does not exist'
    }
)
@swagger_auto_schema(
    method='put',
    operation_description="Update an existing boarding",
    manual_parameters=[
        openapi.Parameter('id', openapi.IN_QUERY, description="Flight's id", type=openapi.TYPE_STRING, required=True),
        openapi.Parameter('latitude', openapi.IN_QUERY, description="Boarding door latitude", type=openapi.TYPE_STRING,
                          required=True),
        openapi.Parameter('longitude', openapi.IN_QUERY, description="Boarding door longitude",
                          type=openapi.TYPE_STRING, required=True),
        openapi.Parameter('opening_time', openapi.IN_QUERY, description="Boarding's opening_time",
                          type=openapi.TYPE_STRING, required=True),
        openapi.Parameter('last_call', openapi.IN_QUERY, description="Boarding's last call", type=openapi.TYPE_STRING,
                          required=True),
        openapi.Parameter('opened', openapi.IN_QUERY, description="If boarding is opened", type=openapi.TYPE_BOOLEAN,
                          required=True)
    ],
    responses={
        200: openapi.Response('Boarding Updated Successfully'),
        400: 'Boarding not exists or invalid parameters',
    }
)
@swagger_auto_schema(
    method='delete',
    operation_description="Delete an existing Boarding",
    manual_parameters=[
        openapi.Parameter('id', openapi.IN_QUERY, description="Flight's id", type=openapi.TYPE_STRING, required=True),
        openapi.Parameter('latitude', openapi.IN_QUERY, description="Boarding door latitude", type=openapi.TYPE_STRING,
                          required=True),
        openapi.Parameter('longitude', openapi.IN_QUERY, description="Boarding door longitude",
                          type=openapi.TYPE_STRING, required=True)
    ],
    responses={
        204: 'Boarding deleted successfully',
        404: 'Boarding not exists',
    }
)
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def boardings(request):
    if request.method == "GET":
        id = request.query_params.get('id')
        latitude = request.query_params.get('latitude')
        longitude = request.query_params.get('longitude')
        try:
            serializer = getBoarding(id, latitude, longitude)
            return JsonResponse(data=serializer.data, status=status.HTTP_200_OK)
        except Boarding.DoesNotExist:
            return JsonResponse({'error': 'Boarding does not exist'}, status=status.HTTP_404_NOT_FOUND)
    elif request.method == "POST":
        id = request.query_params.get('id')
        latitude = request.query_params.get('latitude')
        longitude = request.query_params.get('longitude')
        opening_time = request.query_params.get('opening_time')
        last_call = request.query_params.get('last_call')
        opened = request.query_params.get('opened')
        if existsBoarding(id, latitude, longitude):
            return JsonResponse({"error": "Boarding already exists."},
                                status=status.HTTP_400_BAD_REQUEST)
        serializer = createBoarding(id, latitude, longitude, opening_time, last_call, opened)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "PUT":
        id = request.query_params.get('id')
        latitude = request.query_params.get('latitude')
        longitude = request.query_params.get('longitude')
        opening_time = request.query_params.get('opening_time')
        last_call = request.query_params.get('last_call')
        opened = request.query_params.get('opened')
        try:
            serializer = putBoarding(id, latitude, longitude, opening_time, last_call, opened)
            return JsonResponse(serializer.data, status=status.HTTP_200_OK)
        except Boarding.DoesNotExist:
            return JsonResponse({"error": "Boarding not exists."},
                                status=status.HTTP_400_BAD_REQUEST)
    else:
        id = request.query_params.get('id')
        latitude = request.query_params.get('latitude')
        longitude = request.query_params.get('longitude')
        try:
            deleteBoarding(id, latitude, longitude)
            return JsonResponse({'message': 'Boarding deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except Boarding.DoesNotExist:
            return JsonResponse({'error': 'Boarding not exists'}, status=status.HTTP_404_NOT_FOUND)
