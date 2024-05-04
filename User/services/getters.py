from User.models import User, CheckIn
from User.serializers import UserSerializer, CheckInSerializer


# Get a certain user
@staticmethod
def getUser(mail):
    user = User.objects.get(mail=mail)
    serializer = UserSerializer(user)
    return serializer

@staticmethod
def getCheckIn(mail, id):
    user = User.objects.get(mail=mail)
    check_in = CheckIn.objects.get(user_id=user.id, flight_id=id)
    serializer = CheckInSerializer(check_in)
    return serializer

# List all Users
@staticmethod
def listUsers():
    users = User.objects.all()
    data = UserSerializer(users, many=True)
    return data