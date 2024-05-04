# Modify a user
from User.models import User
from User.serializers import UserSerializer


@staticmethod
def putUser(age, visual, mail, dni, passport, address, birthday):
    user = User.objects.get(mail=mail)
    user.age = age
    user.visual_percentage = visual
    user.dni = dni
    user.passport = passport
    user.address = address
    user.birthday = birthday
    user.save()
    serializer = UserSerializer(user, many=False)
    return serializer