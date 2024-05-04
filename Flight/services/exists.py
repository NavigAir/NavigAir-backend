from Flight.models import Flight

@staticmethod
def existsFlight(id):
    return Flight.objects.filter(id=id).exists()