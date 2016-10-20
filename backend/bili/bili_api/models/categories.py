from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.template.defaultfilters import slugify
from .ads import Ad

# Creating models for categories
class MainCategory(models.Model):
    name = models.CharField(max_length=50)
