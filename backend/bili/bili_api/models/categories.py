from django.db import models


class MainCategory(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    main_category = models.ForeignKey(MainCategory, related_name='subcategories')
    name = models.CharField(max_length=20)
    parent_category = models.ForeignKey('self', related_name='subcategories', blank=True, null=True)

    def __str__(self):
        return self.name
