from rest_framework import serializers

from .models.user import (Person, Address, PhoneNumber)
from .models.ads import (Ad, AdImage, Favourite)
from .models.categories import (MainCategory, SubCategory)
from django.contrib.auth.models import User



class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')



class ProfileSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Person
        fields = ('user', 'first_name', 'last_name', 'email', 'phone_numbers', 'addresses',
        'favourites')


class AddressSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Address


class PhoneNumberSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PhoneNumber



# Serializers for ads

class AdDisplaySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ad
        fields = ('user', 'title' , 'description' , 'price', 'published', 'active_from',
        'slug', 'category', 'spotlight', 'images')


class AdImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AdImage



class FavouriteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Favourite


class CategoryListSerializer(serializers.ModelSerializer):
    subcategories = serializers.StringRelatedField(many=True)
    main_category = serializers.StringRelatedField()
    class Meta:
        model = SubCategory
        fields = ('main_category','name','subcategories')
