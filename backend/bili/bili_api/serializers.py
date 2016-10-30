from rest_framework import serializers

from .models.user import (Person, Address, PhoneNumber)
from .models.ads import (Ad, AdImage, Favourite)
from .models.categories import (MainCategory, SubCategory)
from django.contrib.auth.models import User




class PhoneNumberSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PhoneNumber



class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = ('url','username','email', 'password')
        extra_kwargs = {'password': {'write_only': True}}


class PersonSerializer(serializers.HyperlinkedModelSerializer):
    phone_numbers = PhoneNumberSerializer(many=True)
    addresses = AddressSerializer(many=True)
    class Meta:
        model = Person
        fields = ('first_name', 'last_name', 'email', 'phone_numbers', 'addresses')

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = ('first_name', 'last_name', 'email', 'phone_numbers', 'addresses',
        'favourites', 'ads')


class AddressSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Address


class AdDisplaySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ad
        fields = ('person', 'title' , 'description' , 'price', 'published', 'active_from',
        'slug', 'category', 'spotlight', 'images')


class AdImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AdImage



class FavouriteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Favourite


# can implement later
class CategoryListSerializer(serializers.ModelSerializer):
    subcategories = serializers.StringRelatedField(many=True)
    main_category = serializers.StringRelatedField()
    class Meta:
        model = SubCategory
        fields = ('main_category','name','subcategories')
