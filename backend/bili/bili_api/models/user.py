from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.template.defaultfilters import slugify

# Create your models here.


class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.first_name + ' ' +  self.last_name


class PhoneNumber(models.Model):
    user = models.ForeignKey(Person, on_delete=models.CASCADE)
    phone_regex=RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    number = models.CharField(max_length=15, validators=[phone_regex], blank=True)

    def __str__(self):
        return self.number

class Address(models.Model):
    address = models.CharField(max_length=150)
    region = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    user = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        return self.address + ' ' + self.region + ' ' + self.city
