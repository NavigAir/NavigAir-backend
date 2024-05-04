# Modify a user
from User.models import User, CheckIn
from User.serializers import UserSerializer, CheckInSerializer


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

@staticmethod
def putCheckIn(mail, id, seat, fast_track, priority, bags):
    if fast_track == "true":
        ft = True
    else:
        ft = False

    if priority == "true":
        p = True
    else:
        p = False
    user = User.objects.get(mail=mail)
    check_in = CheckIn.objects.get(user_id=user.id, flight_id=id)
    check_in.seat = seat
    check_in.fast_track = ft
    check_in.priority = p
    check_in.bags = bags
    check_in.save()
    serializer = CheckInSerializer(check_in, many=False)
    return serializer