from User.models import User, CheckIn


# Delete a certain user
@staticmethod
def deleteUser(mail):
    user = User.objects.get(mail=mail)
    user.delete()

@staticmethod
def deleteCheckIn(mail, id):
    user = User.objects.get(mail=mail)
    check_in = CheckIn.objects.get(user_id=user.id, flight_id=id)
    check_in.delete()
