from User.models import User, CheckIn

@staticmethod
def existsUser(mail):
    return User.objects.filter(mail=mail).exists()

@staticmethod
def existsCheckIn(mail, id):
    user = User.objects.get(mail=mail)
    return CheckIn.objects.filter(user=user.id, flight_id=id).exists()