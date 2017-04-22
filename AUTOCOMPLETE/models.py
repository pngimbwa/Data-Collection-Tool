from django.db import models
from django.contrib.auth.models import User #help us to access User object
import uuid
from geoposition.fields import GeopositionField

# Create your models here.
class Country(models.Model):
    name = models.CharField('Name',primary_key=True,max_length=50)
    
    class Meta:
        ordering =['name']
        
    def __str__(self):
        return '{}'.format(self.name)

class Person(models.Model):
    personID=models.CharField(max_length=100, blank=True, unique=True, default=uuid.uuid4().hex[:6].upper())
    name = models.CharField('Name',primary_key=True,max_length=50)
    birth_country = models.ForeignKey(Country, verbose_name="country")
    
    class Meta:
        ordering =['name']
        
    def __str__(self):
        return '{}'.format(self.name)

class CompanyStation(models.Model):
    name = models.CharField('Name',primary_key=True,max_length=50)
    countries = models.ManyToManyField(Country, verbose_name="country")
    
    class Meta:
        ordering =['name']
        
    def __str__(self):
        return '{}'.format(self.name)
    
    
class Car(models.Model):
    name = models.CharField(max_length=255)
    #price = models.DecimalField(max_digits=5, decimal_places=2)
    photo = models.ImageField(upload_to='cars', null=True, blank=True)
    
    class Meta:
        ordering =['name']
        
    def __str__(self):
        return '{}'.format(self.name)
    
class PointOfInterest(models.Model):
    name = models.CharField(max_length=100)
    position = GeopositionField()
    
    class Meta:
        ordering =['name']
        
    def __str__(self):
        return '{}'.format(self.name)
    