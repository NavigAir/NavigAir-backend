from User.models import User
from User.serializers import UserSerializer


# Get a certain user
@staticmethod
def getUser(mail):
    user = User.objects.get(mail=mail)
    serializer = UserSerializer(user)
    return serializer

# List all Users
@staticmethod
def listUsers():
    users = User.objects.all()
    data = UserSerializer(users, many=True)
    return data