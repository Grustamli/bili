from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.template.defaultfilters import slugify
from .user import Person
from .categories import SubCategory
import datetime

class Ad(models.Model):
    user = models.ForeignKey(Person, on_delete=models.CASCADE)
    title = models.CharField(max_length=250, blank=False)
    description = models.TextField()
    price = models.IntegerField(default=0)
    published = models.DateTimeField('publish date', auto_now_add=True)
    active_from = models.DateField(blank=True, null=True)
    slug = models.SlugField(blank=True)
    category = models.ForeignKey(SubCategory, related_name='ads')
    spotlight = models.NullBooleanField()
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(Ad, self).save(*args, **kwargs)



class AdImage(models.Model):
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE, related_name='images')
    def user_directory_path(instance, filename):
        ad_name = instance.ad.title
        return 'ads/{0}/{1}'.format(ad_name,filename)


    image = models.ImageField(upload_to=user_directory_path)
    def __str__(self):
        return self.ad.title

class Favourite(models.Model):
    user = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='favourites')
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'ad')
