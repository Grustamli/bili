from rest_framework import serializers

from .models.user import Person
from django.contrib.auth.models import User



class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')



class ProfileSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Person
        fields = ('first_name', 'last_name', 'email', 'phone_numbers', 'addresses')
