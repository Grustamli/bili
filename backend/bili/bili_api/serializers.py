from rest_framework import serializers

from .models.user import (Person, Address, PhoneNumber)
from .models.ads import (Ad, AdImage, Favourite)
from .models.categories import (MainCategory, SubCategory)
from django.contrib.auth.models import User




class PhoneNumberListSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='phone-detail')
    person = serializers.HyperlinkedRelatedField(view_name='profile-detail',
            queryset=Person.objects.all(),
            lookup_field='username')
    class Meta:
        model = PhoneNumber
        fields = ('url','number','person')

class PhoneNumberDetailSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='phone-detail')
    person = serializers.HyperlinkedRelatedField(view_name='profile-detail',
            lookup_field='username',
            read_only=True)

    class Meta:
        model = PhoneNumber
        fields = ('url','number', 'person')

# class CreatePhoneNumberSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = PhoneNumber
#         lookup_field = 'number'


class AddressListSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='address-detail')
    person = serializers.HyperlinkedRelatedField(view_name='profile-detail',
            queryset=Person.objects.all(),
            lookup_field='username')
    class Meta:
        model = Address
        fields = ('url', 'person', 'address', 'region', 'city')

class AddressDetailSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='address-detail')
    person = serializers.HyperlinkedRelatedField(view_name='profile-detail',
            lookup_field='username', read_only=True)
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

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    class Meta:
        model = Person
        fields = ('url','username','password','first_name', 'last_name', 'email')
        # extra_kwargs={
        #     'password':{'write_only':'True'}
        # }

class ProfileDetailSerializer(serializers.HyperlinkedModelSerializer):
    # url = serializers.HyperlinkedIdentityField(
    #     view_name='person-detail',
    #     lookup_field='username')

    phone_numbers = serializers.HyperlinkedRelatedField(view_name='phone-detail',read_only=True, many=True)
    addresses = serializers.HyperlinkedRelatedField(view_name='address-detail', read_only=True, many=True)
    ads = serializers.HyperlinkedRelatedField(view_name='ad-detail', lookup_field='slug', read_only=True, many=True)
    favourites = serializers.HyperlinkedRelatedField(view_name='favourite-detail', read_only=True, many=True)

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr == 'password':
                instance.set_password(value)
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance

    class Meta:
        model = Person
        fields = ('username','password','first_name', 'last_name', 'email', 'phone_numbers', 'addresses',
        'favourites', 'ads')
        extra_kwargs={
            'phone_numbers':{'read_only':'True'},
            'addresses':{'read_only':'True'},
            'password':{'write_only':'True'}
        }



class AdListSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='ad-detail', lookup_field='slug')
    person = serializers.HyperlinkedRelatedField(view_name='profile-detail',
            queryset=Person.objects.all(),
            lookup_field='username')
    class Meta:
        model = Ad
        fields = ('url', 'person', 'title' , 'description' , 'price', 'published', 'active_from',
        'slug', 'spotlight',)


class AdDetailSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='ad-detail', lookup_field='slug')
    person = serializers.HyperlinkedRelatedField(view_name='profile-detail',
            lookup_field='username',
            read_only=True)
    images = serializers.HyperlinkedRelatedField(view_name='adimage-detail', read_only=True, many=True)

    class Meta:
        model = Ad
        fields = ('url','person', 'title' , 'description' , 'price', 'published', 'active_from',
        'spotlight', 'images')



class AdImageListSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='adimage-detail')
    ad = serializers.HyperlinkedRelatedField(view_name='ad-detail',
            queryset=Ad.objects.all(),
            lookup_field='slug')

    class Meta:
        model= AdImage
        fields = ('url', 'ad', 'image')


class AdImageDetailSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='adimage-detail')
    ad = serializers.HyperlinkedRelatedField(view_name='ad-detail',
            lookup_field='slug',
            read_only=True)
    class Meta:
        model= AdImage
        fields = ('url', 'ad', 'image')



class FavouriteListSerializer(serializers.HyperlinkedModelSerializer):
    person = serializers.HyperlinkedRelatedField(view_name='profile-detail',
            queryset=Person.objects.all(),
            lookup_field='username')
    ad = serializers.HyperlinkedRelatedField(view_name='ad-detail',
            queryset=Ad.objects.all(),
            lookup_field='slug')
    url = serializers.HyperlinkedIdentityField(view_name='favourite-detail')
    class Meta:
        model= Favourite
        fields = ('url', 'person', 'ad')


class FavouriteDetailSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='favourite-detail')
    person = serializers.HyperlinkedRelatedField(view_name='profile-detail',
            lookup_field='username',
            read_only=True)
    ad = serializers.HyperlinkedRelatedField(view_name='ad-detail',
            lookup_field='slug',
            read_only=True)
    class Meta:
        model= Favourite
        fields = ('url', 'person', 'ad')



# can implement later
class CategorySerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='category-detail')
    subcategories = serializers.StringRelatedField(many=True)
    main_category = serializers.StringRelatedField()
    class Meta:
        model = SubCategory
        fields = ('url','main_category','name','subcategories')
