from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.template.defaultfilters import slugify
from .user import Person

class Ad(models.Model):
    user = models.ForeignKey(Person, on_delete=models.CASCADE)
    title = models.CharField(max_length=250, blank=False)
    description = models.TextField()
    price = models.CharField(max_length=25,)
    published = models.DateTimeField(auto_now=True)
    active_since = models.DateField(blank=True, null=True)
    slug = models.SlugField(blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(Ad, self).save(*args, **kwargs)



class AdImage(models.Model):
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)
    def user_directory_path(instance, filename):
        # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
        user = str(instance.ad.user.id) + '-' + instance.ad.user.first_name + '-' + instance.ad.user.last_name
        ad_name = instance.ad.title
        return 'ads/images/{0}/{1}/{2}'.format(user,ad_name,filename)


    image = models.ImageField(upload_to=user_directory_path)
    def __str__(self):
        return self.ad.title

class Favourites(models.Model):
    user = models.ForeignKey(Person, on_delete=models.CASCADE)
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'ad')
