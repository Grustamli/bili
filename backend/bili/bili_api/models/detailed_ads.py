from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.template.defaultfilters import slugify
from .ads import Ad

# Creating models for categories
class Property(models.Model):
    TYPE_CHOICES=(
        ('OFFICE', 'Office place'),
        ('HOME', (
            ('FlAT', 'Flat'),
            ('HOUSE', 'House'),
            )
        ),
        ('LAND', 'Land'),
        ('COMMERCIAL', 'Commercial'),
        ('UNKNOWN', 'Unknown')
    )
    STATUS_CHOICES=(
    ('RENT', 'Rent'),
    ('SALE', 'Sale'),
    ('SHARE', 'Share')
    )
    PAYMENT_CHOICES=(
    ('DAILY', 'Daily'),
    ('WEEKLY', 'Weekly'),
    ('MONTHLY','Monthly')
    )
    ad = models.OneToOneField(Ad,related_name='property')
    kind = models.CharField(max_length=10, choices=TYPE_CHOICES)
    status = models.CharField(max_length=7, choices=STATUS_CHOICES)
    no_bed_room = models.IntegerField(blank=True, null=True)
    area = models.DecimalField(max_digits=9, decimal_places=3, blank=True, null=True)
    payment = models.CharField(max_length=7, choices=PAYMENT_CHOICES, default=PAYMENT_CHOICES[2][1])
    def __str__(self):
        return self.ad.title
