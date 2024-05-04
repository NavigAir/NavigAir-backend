from rest_framework import serializers

from User.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['name', 'age', 'visual_percentage', 'mail', 'pwd', 'dni', 'passport', 'address', 'birthday']