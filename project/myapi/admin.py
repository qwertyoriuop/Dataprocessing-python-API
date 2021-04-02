from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import City
from .models import Country
from .models import CountryLanguage
admin.site.register(City)
admin.site.register(Country)
admin.site.register(CountryLanguage)