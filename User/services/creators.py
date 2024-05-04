from User.models import User
from User.serializers import UserSerializer


# Create a new location
@staticmethod
def createUser(name, age, visual, mail, pwd, dni, passport, address, birthday):
    user = User(name=name, age=age, visual_percentage=visual, mail=mail, pwd=pwd, dni=dni, passport=passport, address=address, birthday=birthday)
    user.save()
    serializer = UserSerializer(user, many=False)
    return serializer