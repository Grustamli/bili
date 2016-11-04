from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import (api_view, permission_classes)
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.permissions import (IsAdminUser, IsAuthenticatedOrReadOnly)

from .serializers import (
                        ProfileListSerializer,
                        ProfileDetailSerializer,
                        PhoneNumberListSerializer,
                        PhoneNumberDetailSerializer,
                        AddressListSerializer,
                        AddressDetailSerializer,
                        AdListSerializer,
                        AdDetailSerializer,
                        AdImageListSerializer,
                        AdImageDetailSerializer,
                        FavouriteListSerializer,
                        FavouriteDetailSerializer,
                        CategorySerializer,
                        )

from .models.user import (
                        Person,
                        PhoneNumber,
                        Address,
                        )

from .models.ads import (
                        Ad,
                        AdImage,
                        Favourite
                        )

from .models.categories import SubCategory


from .permissions import (
                        IsOwnProfileOrReadOnly,
                        IsOwnerOrReadOnly,
                        IsAdOwnerOrReadOnly,
                        IsOwner,
                        CanOnlyCreate
                        )

@api_view(['GET'])
# @permission_classes((IsAdminUser,))
def api_root(request, format=None):
    return Response({
        'profiles': reverse('profile-list', request=request, format=format),
        'phonenumbers': reverse('phone-list', request=request, format=format),
        'addresses': reverse('address-list', request=request, format=format),
        'ads': reverse('ad-list', request=request, format=format),
        'ad-images': reverse('adimage-list', request=request, format=format),
        'favourites': reverse('favourite-list', request=request, format=format),
        'categories': reverse('category-list', request=request, format=format),

    })

class ProfileListView(generics.ListAPIView):
    queryset = Person.objects.all()
    serializer_class = ProfileListSerializer
    permission_classes=(IsAdminUser,)

class ProfileCreateView(generics.CreateAPIView):
    queryset = Person.objects.all()
    serializer_class = ProfileListSerializer

class ProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = ProfileDetailSerializer
    lookup_field = 'username'
    permission_classes = (IsOwnProfileOrReadOnly,)


class PhoneNumberListView(generics.ListAPIView):
    queryset = PhoneNumber.objects.all()
    serializer_class = PhoneNumberListSerializer
    permission_classes = (IsAdminUser,)


class PhoneNumberCreateView(generics.CreateAPIView):
    queryset = PhoneNumber.objects.all()
    serializer_class = PhoneNumberListSerializer

class PhoneNumberDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PhoneNumber.objects.all()
    serializer_class = PhoneNumberDetailSerializer
    permission_classes = (IsOwnerOrReadOnly,)


class AddressListView(generics.ListAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressListSerializer
    permission_classes = (IsAdminUser,)


class AddressCreateView(generics.CreateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressListSerializer


class AddressDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressDetailSerializer
    permission_classes = (IsOwnerOrReadOnly,)


class AdListView(generics.ListAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdListSerializer
    lookup_field='slug'


class AdCreateView(generics.CreateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdListSerializer
    lookup_field='slug'


class AdDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdDetailSerializer
    lookup_field='slug'
    permission_classes = (IsOwnerOrReadOnly,)


class AdImageListView(generics.ListAPIView):
    queryset = AdImage.objects.all()
    serializer_class = AdImageListSerializer
    permission_classes = (IsAdminUser,)

class AdImageCreateView(generics.CreateAPIView):
    queryset = AdImage.objects.all()
    serializer_class = AdImageListSerializer


class AdImageDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AdImage.objects.all()
    serializer_class = AdImageDetailSerializer
    permission_classes = (IsAdOwnerOrReadOnly,)

class FavoriteListView(generics.ListAPIView):
    queryset = Favourite.objects.all()
    serializer_class = FavouriteListSerializer
    permission_classes = (IsAdminUser,)

class FavoriteCreateView(generics.CreateAPIView):
    queryset = Favourite.objects.all()
    serializer_class = FavouriteListSerializer


class FavouriteDetailView(generics.RetrieveDestroyAPIView):
    queryset = Favourite.objects.all()
    serializer_class = FavouriteDetailSerializer
    permission_classes = (IsOwner,)


class CategoryListView(generics.ListAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = CategorySerializer

class CategoryDetailView(generics.RetrieveAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = CategorySerializer
