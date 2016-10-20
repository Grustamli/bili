from django.contrib import admin
from .models.user import Person
from .models.categories import MainCategory
from .models.ads import AdImage, Ad
# Register your models here.

admin.site.register([MainCategory,
                    Person,
                    AdImage,
                    Ad,
                    ])
