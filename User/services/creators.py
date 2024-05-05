from User.models import User, CheckIn
from User.serializers import UserSerializer, CheckInSerializer
import random

# Create a new location
@staticmethod
def createUser(name, age, visual, mail, pwd, passport, address, birthday):
    user = User(name=name, age=age, visual_percentage=visual, mail=mail, pwd=pwd, passport=passport, address=address, birthday=birthday, assigned_flight=None)
    user.save()
    serializer = UserSerializer(user, many=False)
    return serializer

@staticmethod
def createCheckIn(mail, id):
    number = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33']
    letter = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    bool = [True, False]
    seat = number[random.randint(0, 32)]+letter[random.randint(0, 6)]
    user = User.objects.get(mail=mail)
    check_in = CheckIn(user_id=user.id, flight_id=id, seat=seat, fast_track=bool[random.randint(0,1)], priority=bool[random.randint(0,1)], bags=random.randint(1,5))
    check_in.save()
    serializer = CheckInSerializer(check_in, many=False)
    return serializer