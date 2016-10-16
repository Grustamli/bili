from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

# Create your models here.


class Person(models.Model):
    user = models.OneToOneField(User)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)


class PhoneNumber(models.Model):
    user = models.ForeignKey(Person)
    phone_regex=RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    number = models.CharField(max_length=15, validators=[phone_regex], blank=True)


class Address(models.Model):
    address = models.CharField(max_length=150)
    region = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    user = models.ForeignKey(Person)

class Ad(models.Model):
    user = models.ForeignKey(Person)
    title = models.CharField(max_length=250, blank=False)
    description = models.TextField()
