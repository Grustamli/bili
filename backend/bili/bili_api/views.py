from django.shortcuts import get_object_or_404
from .serializers import (UserSerializer,
                        PersonSerializer,
                        ProfileSerializer,
                        PhoneNumberSerializer,
                        )

from .models.user import (Person,
                        PhoneNumber,
                        )
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.response import Response

# Create your views here.
# class UserViewSet(generics.ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer()


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    # def list(self, request):
    #     queryset = Person.objects.all()
    #     serializer = PersonSerializer(queryset, many=True, context={'request': request})
    #     return Response(serializer.data)
    #
    # def retrieve(self, request, pk=None):
    #     queryset = Person.objects.all()
    #     person = get_object_or_404(queryset, pk=pk)
    #     serializer = PersonSerializer(person, context={'request': request})
    #     return Response(serializer.data)

class PhoneViewSet(viewsets.ModelViewSet):
    queryset = PhoneNumber.objects.all()
    serializer_class = PhoneNumberSerializer
