# views.py
from rest_framework import viewsets

from .serializers import CitySerializer
from .serializers import CountrySerializer
from .serializers import CountryLanguageSerializer
from .models import City
from .models import Country
from .models import CountryLanguage


class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all().order_by('name')
    serializer_class = CitySerializer

class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all().order_by('Name')
    serializer_class = CountrySerializer
    
class CountryLanguageViewSet(viewsets.ModelViewSet):
    queryset = CountryLanguage.objects.all().order_by('Language')
    serializer_class = CountryLanguageSerializer