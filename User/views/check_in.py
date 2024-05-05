import json

from django.http import JsonResponse
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import api_view

from User.models import CheckIn
from User.services.creators import createCheckIn
from User.services.deleters import deleteCheckIn
from User.services.exists import existsCheckIn
from User.services.getters import getCheckIn
from User.services.setters import putCheckIn


@swagger_auto_schema(
    method='get',
    operation_description="Get a certain check-in",
    manual_parameters=[
        openapi.Parameter('mail', openapi.IN_QUERY, description="User's mail", type=openapi.TYPE_STRING, required=True),
        openapi.Parameter('id', openapi.IN_QUERY, description="Flight's id", type=openapi.TYPE_STRING, required=True),
    ]
)
@swagger_auto_schema(
    method='post',
    operation_description="Add a new check-in",
    manual_parameters=[
    openapi.Parameter('mail', openapi.IN_QUERY, description="User's mail", type=openapi.TYPE_STRING, required=True),
    openapi.Parameter('id', openapi.IN_QUERY, description="Flight's id", type=openapi.TYPE_STRING, required=True),
    ],
    responses={
        200: openapi.Response('Check-in Created Successfully'),
        400: 'Check-in already exists or invalid parameters',
        404: 'Check-in does not exist'
    }
)
@swagger_auto_schema(
    method='put',
    operation_description="Update an existing check-in",
    manual_parameters=[
    openapi.Parameter('mail', openapi.IN_QUERY, description="User's mail", type=openapi.TYPE_STRING, required=True),
    openapi.Parameter('id', openapi.IN_QUERY, description="Flight's id", type=openapi.TYPE_STRING, required=True),
    openapi.Parameter('seat', openapi.IN_QUERY, description="Check-in seat", type=openapi.TYPE_STRING, required=True),
    openapi.Parameter('fast_track', openapi.IN_QUERY, description="Check-in fast track", type=openapi.TYPE_BOOLEAN, required=True),
    openapi.Parameter('priority', openapi.IN_QUERY, description="Check-in priority", type=openapi.TYPE_BOOLEAN, required=True),
    openapi.Parameter('bags', openapi.IN_QUERY, description="Check-in bags", type=openapi.TYPE_INTEGER, required=True)
    ],
    responses={
        200: openapi.Response('Check-in Updated Successfully'),
        400: 'Check-in not exists or invalid parameters',
    }
)
@swagger_auto_schema(
    method='delete',
    operation_description="Delete an existing check-in",
    manual_parameters=[
        openapi.Parameter('mail', openapi.IN_QUERY, description="User's mail", type=openapi.TYPE_STRING, required=True),
        openapi.Parameter('id', openapi.IN_QUERY, description="Flight's id", type=openapi.TYPE_STRING, required=True),
    ],
    responses={
        204: 'Check-in deleted successfully',
        404: 'Check-in not exists',
    }
)
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def checkIns(request):
    if request.method == "GET":
        mail = request.query_params.get('mail')
        id = request.query_params.get('id')
        try:
            serializer = getCheckIn(mail, id)
            return JsonResponse(data=serializer.data, status=status.HTTP_200_OK)
        except CheckIn.DoesNotExist:
            return JsonResponse({'error': 'CheckIn does not exist'}, status=status.HTTP_404_NOT_FOUND)
    elif request.method == "POST":
        data = json.loads(request.body)
        mail = data.get('mail')
        id = data.get('id')
        if existsCheckIn(mail, id):
            return JsonResponse({"error": "CheckIn already exists."},
                                status=status.HTTP_400_BAD_REQUEST)
        serializer = createCheckIn(mail, id)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "PUT":
        data = json.loads(request.body)
        mail = data.get('mail')
        id = data.get('id')
        seat = data.get('seat')
        fast_track = data.get('fast_track')
        priority = data.get('priority')
        bags = data.get('bags')
        try:
            serializer = putCheckIn(mail, id, seat, fast_track, priority, bags)
            return JsonResponse(serializer.data, status=status.HTTP_200_OK)
        except CheckIn.DoesNotExist:
            return JsonResponse({"error": "CheckIn not exists."},
                                status=status.HTTP_400_BAD_REQUEST)
    else:
        mail = request.query_params.get('mail')
        id = request.query_params.get('id')
        try:
            deleteCheckIn(mail, id)
            return JsonResponse({'message': 'CheckIn deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except CheckIn.DoesNotExist:
            return JsonResponse({'error': 'CheckIn not exists'}, status=status.HTTP_404_NOT_FOUND)
