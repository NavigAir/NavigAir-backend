from User.models import User, CheckIn
from User.serializers import UserSerializer, CheckInSerializer


# Create a new location
@staticmethod
def createUser(name, age, visual, mail, pwd, passport, address, birthday):
    user = User(name=name, age=age, visual_percentage=visual, mail=mail, pwd=pwd, passport=passport, address=address, birthday=birthday)
    user.save()
    serializer = UserSerializer(user, many=False)
    return serializer

@staticmethod
def createCheckIn(mail, id, seat, fast_track, priority, bags):
    if fast_track == "true":
        ft = True
    else:
        ft = False

    if priority == "true":
        p = True
    else:
        p = False
    user = User.objects.get(mail=mail)
    check_in = CheckIn(user_id=user.id, flight_id=id, seat=seat, fast_track=ft, priority=p, bags=bags)
    check_in.save()
    serializer = CheckInSerializer(check_in, many=False)
    return serializer