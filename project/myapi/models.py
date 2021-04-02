from django.db import models

# Create your models here.
class City(models.Model):
    ID = models.IntegerField(primary_key=True, max_length=11)
    name = models.CharField(max_length=35)
    CountryCode = models.CharField(max_length=3)
    Disctrict = models.CharField(max_length=20)
    Population = models.IntegerField(max_length=11)
    def __str__(self):
        return self.name

class Country(models.Model):
    Code = models.CharField(primary_key=True, max_length=3)
    Name = models.CharField(max_length=35)
    Continent = models.CharField(max_length=20)
    Region = models.CharField(max_length=26)
    SurfaceArea = models.FloatField(max_length=10)
    Population = models.IntegerField(max_length=11)
    Captital = models.IntegerField(max_length=11)
    def __str__(self):
        return self.Name

class CountryLanguage(models.Model):
    CountryCode = models.CharField(primary_key=True, max_length=3)
    Language = models.CharField(max_length=30)
    IsOfficial = models.BooleanField()
    Percentage = models.FloatField(max_length=20)
    def __str__(self):
        return self.Language