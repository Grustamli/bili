from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .serializers import (
                        ProfileListSerializer,
                        ProfileDetailSerializer,
                        PhoneNumberListSerializer,
                        PhoneNumberDetailSerializer,
                        AddressListSerializer,
                        AddressDetailSerializer,
                        AdListSerializer,
                        AdDetailSerializer
                        )

from .models.user import (Person,
                        PhoneNumber,
                        Address,
                        )

from .models.ads import (Ad,
                        )
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.response import Response

# Create your views here.
# class UserViewSet(generics.ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer()


# class RegisterViewSet(viewsets.ModelViewSet):
#     queryset = Person.objects.all()
#     serializer_class = RegisterSerializer
    # lookup_field = 'username'
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

# class PhoneViewSet(viewsets.ModelViewSet):
#     queryset = PhoneNumber.objects.all()
#     serializer_class = PhoneNumberSerializer
#
# class AddressViewSet(viewsets.ModelViewSet):
#     queryset = Address.objects.all()
#     serializer_class = AddressSerializer

# class ProfileViewSet(viewsets.ModelViewSet):
#     queryset = Person.objects.all()
#     serializer_class = ProfileSerializer
#

class ProfileListView(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = ProfileListSerializer

class ProfileDetailView(generics.RetrieveDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = ProfileDetailSerializer
    lookup_field = 'username'

# class AdViewSet(viewsets.ModelViewSet):
#     queryset = Ad.objects.all()
#     serializer_class = AdSerializer

class PhoneNumberListView(generics.ListCreateAPIView):
    queryset = PhoneNumber.objects.all()
    serializer_class = PhoneNumberListSerializer

class PhoneNumberDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PhoneNumber.objects.all()
    serializer_class = PhoneNumberDetailSerializer


class AddressListView(generics.ListCreateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressListSerializer

class AddressDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressDetailSerializer


class AdListView(generics.ListCreateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdListSerializer
    lookup_field='slug'


class AdDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdDetailSerializer
    lookup_field='slug'
