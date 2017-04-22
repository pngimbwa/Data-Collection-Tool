from dal import autocomplete
from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.contrib.auth.forms import AuthenticationForm
from .models import Country,Person,CompanyStation,PointOfInterest
from django.contrib import admin
from django.forms import ModelForm
from django import forms
from django.forms import Select

class CountryForm(forms.Form):
    name =  forms.ModelChoiceField(queryset = Country.objects.all(),widget=Select(attrs={'class': 'form-control seleckpicker'}),empty_label="Select Country")
    
class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('__all__')
        widgets = {
            'birth_country': autocomplete.ModelSelect2(url='country-autocomplete')
        }

class CompanyStationForm(forms.ModelForm):
    class Meta:
        model = CompanyStation
        fields = ('__all__')
        widgets = {
            'countries': autocomplete.ModelSelect2Multiple(url='country-autocomplete')
        }

class CarForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '#name','class':'form-control'}))
    photo = forms.ImageField()
    

class PointOfInterestForm(forms.ModelForm):
    class Meta:
        model = PointOfInterest
        fields = ('__all__')
