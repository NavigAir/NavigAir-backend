from User.models import User

@staticmethod
def existsUser(mail):
    return User.objects.filter(mail=mail).exists()