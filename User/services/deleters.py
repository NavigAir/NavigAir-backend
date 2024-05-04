from User.models import User

# Delete a certain user
@staticmethod
def deleteUser(mail):
    user = User.objects.get(mail=mail)
    user.delete()