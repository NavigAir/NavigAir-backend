from django.http import JsonResponse
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import api_view

from User.models import User
from User.services.creators import createUser
from User.services.deleters import deleteUser
from User.services.exists import existsUser
from User.services.getters import getUser, listUsers
from User.services.setters import putUser


@swagger_auto_schema(
    method = 'get',
    operation_description="Get all users",
    responses={
        200: 'OK: Operation successful',
        500: 'INTERNAL_SERVER_ERROR: Internal error'
    },
)
@api_view(['GET'])
def userList(request):
    try:
        data = listUsers()
        return JsonResponse(data.data, status=status.HTTP_200_OK, safe=False)
    except Exception:
        return JsonResponse({'error': 'Internal error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@swagger_auto_schema(
    method='get',
    operation_description="Get a certain user",
    manual_parameters=[
        openapi.Parameter('mail', openapi.IN_QUERY, description="User's mail", type=openapi.TYPE_STRING),
    ]
)
@swagger_auto_schema(
    method='post',
    operation_description="Add a new user",
    manual_parameters=[
    openapi.Parameter('name', openapi.IN_QUERY, description="User's name", type=openapi.TYPE_STRING, required=True),
    openapi.Parameter('age', openapi.IN_QUERY, description="User's age", type=openapi.TYPE_INTEGER, required=True),
    openapi.Parameter('visual', openapi.IN_QUERY, description="User's visual limitation", type=openapi.TYPE_INTEGER, required=True),
    openapi.Parameter('mail', openapi.IN_QUERY, description="User's mail", type=openapi.TYPE_STRING, required=True),
    openapi.Parameter('pwd', openapi.IN_QUERY, description="User's password", type=openapi.TYPE_STRING, required=True),
    openapi.Parameter('dni', openapi.IN_QUERY, description="User's dni", type=openapi.TYPE_STRING, required=True),
    openapi.Parameter('passport', openapi.IN_QUERY, description="User's passport", type=openapi.TYPE_STRING, required=True),
    openapi.Parameter('address', openapi.IN_QUERY, description="User's address", type=openapi.TYPE_STRING),
    openapi.Parameter('birthday', openapi.IN_QUERY, description="User's birthday", type=openapi.TYPE_STRING),
    openapi.Parameter('assigned_flight', openapi.IN_QUERY, description="User's flight", type=openapi.TYPE_STRING)
    ],
    responses={
        200: openapi.Response('User Created Successfully'),
        400: 'User already exists or invalid parameters',
        404: 'User does not exist'
    }
)
@swagger_auto_schema(
    method='put',
    operation_description="Update an existing user",
    manual_parameters=[
        openapi.Parameter('name', openapi.IN_QUERY, description="User's name", type=openapi.TYPE_STRING, required=True),
        openapi.Parameter('age', openapi.IN_QUERY, description="User's age", type=openapi.TYPE_INTEGER, required=True),
        openapi.Parameter('visual', openapi.IN_QUERY, description="User's visual limitation",
                          type=openapi.TYPE_INTEGER, required=True),
        openapi.Parameter('mail', openapi.IN_QUERY, description="User's mail", type=openapi.TYPE_STRING, required=True),
        openapi.Parameter('pwd', openapi.IN_QUERY, description="User's password", type=openapi.TYPE_STRING,
                          required=True),
        openapi.Parameter('dni', openapi.IN_QUERY, description="User's dni", type=openapi.TYPE_STRING, required=True),
        openapi.Parameter('passport', openapi.IN_QUERY, description="User's passport", type=openapi.TYPE_STRING,
                          required=True),
        openapi.Parameter('address', openapi.IN_QUERY, description="User's address", type=openapi.TYPE_STRING),
        openapi.Parameter('birthday', openapi.IN_QUERY, description="User's birthday", type=openapi.TYPE_STRING),
        openapi.Parameter('assigned_flight', openapi.IN_QUERY, description="User's flight", type=openapi.TYPE_STRING)
    ],
    responses={
        200: openapi.Response('User Updated Successfully'),
        400: 'User not exists or invalid parameters',
    }
)
@swagger_auto_schema(
    method='delete',
    operation_description="Delete an existing user",
    manual_parameters=[
    openapi.Parameter('mail', openapi.IN_QUERY, description="User's mail", type=openapi.TYPE_STRING)
    ],
    responses={
        204: 'User deleted successfully',
        404: 'User not exists',
    }
)
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def users(request):
    if request.method == "GET":
        mail = request.query_params.get('mail')
        try:
            serializer = getUser(mail)
            return JsonResponse(data=serializer.data, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return JsonResponse({'error': 'User does not exist'}, status=status.HTTP_404_NOT_FOUND)
    elif request.method == "POST":
        name = request.query_params.get('name')
        age = request.query_params.get('age')
        visual = request.query_params.get('visual')
        mail = request.query_params.get('mail')
        pwd = request.query_params.get('pwd')
        passport = request.query_params.get('passport')
        address = request.query_params.get('address')
        birthday = request.query_params.get('birthday')
        if existsUser(mail):
            return JsonResponse({"error": "User already exists."},
                                status=status.HTTP_400_BAD_REQUEST)
        serializer = createUser(name, age, visual, mail, pwd, dni, passport, address, birthday, assigned_flight)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "PUT":
        age = request.query_params.get('age')
        visual = request.query_params.get('visual')
        mail = request.query_params.get('mail')
        dni = request.query_params.get('dni')
        passport = request.query_params.get('passport')
        address = request.query_params.get('address')
        birthday = request.query_params.get('birthday')
        try:
            serializer = putUser(age, visual, mail, dni, passport, address, birthday)
            return JsonResponse(serializer.data, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return JsonResponse({"error": "User not exists."},
                                status=status.HTTP_400_BAD_REQUEST)
    else:
        mail = request.query_params.get('mail')
        try:
            deleteUser(mail)
            return JsonResponse({'message': 'User deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except User.DoesNotExist:
            return JsonResponse({'error': 'User not exists'}, status=status.HTTP_404_NOT_FOUND)
