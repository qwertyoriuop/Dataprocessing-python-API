from rest_framework import serializers
from .models import City
from .models import Country
from .models import CountryLanguage

class CitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = City
        fields = ('ID','name', 'CountryCode', 'Disctrict', 'Population')

class CountrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Country
        fields = ('Code','Name', 'Continent', 'Region', 'SurfaceArea', 'Population', 'Captital')

class CountryLanguageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CountryLanguage
        fields = ('CountryCode','Language', 'IsOfficial', 'Percentage')