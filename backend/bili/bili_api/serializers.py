from rest_framework import serializers

from .models.user import (Person, Address, PhoneNumber)
from .models.ads import (Ad, AdImage, Favourite)
from .models.categories import (MainCategory, SubCategory)
from django.contrib.auth.models import User




class PhoneNumberListSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='phone-detail')
    person = serializers.HyperlinkedIdentityField(view_name='profile-detail', lookup_field='user_username')
    class Meta:
        model = PhoneNumber
        fields = ('url','number','person')

class PhoneNumberDetailSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='phone-detail')
    # person = serializers.StringRelatedField(view_name='profile-detail')

    class Meta:
        model = PhoneNumber
        fields = ('number','url')

# class CreatePhoneNumberSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = PhoneNumber
#         lookup_field = 'number'


class AddressListSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='address-detail')
    person = serializers.HyperlinkedIdentityField(view_name='profile-detail',
    lookup_field='username')
    class Meta:
        model = Address
        fields = ('url', 'person', 'address', 'region', 'city')

class AddressDetailSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='address-detail')
    person = serializers.HyperlinkedIdentityField(view_name='profile-detail',
    lookup_field='username')
    class Meta:
        model = Address
        fields = ('url', 'person', 'address', 'region', 'city')


# class AdSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Ad


# class RegisterSerializer(serializers.ModelSerializer):
#     url = serializers.HyperlinkedIdentityField(
#         view_name='person-detail',
#         lookup_field='username'
#     )
#     class Meta:
#         model = Person
#         fields = ('url', 'username', 'first_name', 'last_name', 'email')


class ProfileListSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
    view_name='profile-detail',
    lookup_field='username'
    )
    class Meta:
        model = Person
        fields = ('url','username', 'first_name', 'last_name', 'email')

class ProfileDetailSerializer(serializers.HyperlinkedModelSerializer):
    # url = serializers.HyperlinkedIdentityField(
    #     view_name='person-detail',
    #     lookup_field='username')

    phone_numbers = serializers.HyperlinkedRelatedField(view_name='phone-detail',read_only=True, many=True)
    addresses = serializers.HyperlinkedRelatedField(view_name='address-detail', read_only=True, many=True)
    ads = serializers.HyperlinkedRelatedField(view_name='ad-detail', lookup_field='slug', read_only=True, many=True)
    class Meta:
        model = Person
        fields = ('first_name', 'last_name', 'email', 'phone_numbers', 'addresses',
        'favourites', 'ads')
        extra_kwargs={
            'phone_numbers':{'read_only':'True'},
            'addresses':{'read_only':'True'}
        }



class AdListSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='ad-detail', lookup_field='slug')
    # person = serializers.HyperlinkedIdentityField(view_name='profile-detail')

    class Meta:
        model = Ad
        fields = ('url', 'title' , 'description' , 'price', 'published', 'active_from',
        'slug', 'spotlight',)

class AdDetailSerializer(serializers.HyperlinkedModelSerializer):
    # person = serializers.HyperlinkedIdentityField(view_name='profile-detail')

    class Meta:
        model = Ad
        fields = ('title' , 'description' , 'price', 'published', 'active_from',
        'slug', 'spotlight')

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
