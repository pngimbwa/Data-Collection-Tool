from dal import autocomplete

from django.shortcuts import render, render_to_response,get_object_or_404,redirect,RequestContext, HttpResponseRedirect
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.core.context_processors import csrf
from datetime import datetime, date
import math

from AUTOCOMPLETE.models import Country
from .models import Country, Car
from .forms import CarForm,PointOfInterestForm
class CountryAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated():
            return Country.objects.none()

        qs = Country.objects.all()

        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs
    
def car(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('signup:login'))
      
    if request.method == 'POST': 
        carform = CarForm(request.POST, request.FILES)
      
        if carform.is_valid():
            name = carform.cleaned_data['name']
            photo = carform.cleaned_data['photo']
            
            try:
                Car.objects.get(name=name,photo=photo)
            except:
                car_instance = Car(name=name,photo=photo)
                car_instance.save()
            else:
                message='The picture already exist'
                return render (request,'AUTOCOMPLETE/car.html',locals())
            message='saved'
            return render(request,'AUTOCOMPLETE/saved.html',locals())
        
        else:
            context = {'carform':carform}
            return render (request,'AUTOCOMPLETE/car.html',locals())
      
    else:
        carform = CarForm()
        return render (request,'AUTOCOMPLETE/car.html',locals())
    
    
def location(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('signup:login'))
    if request.method == 'POST':
        pointofinterestform = PointOfInterestForm(request.POST)
        if pointofinterestform.is_valid():
            name = carform.cleaned_data['name']
            position = carform.cleaned_data['position']
        else:
                context = {'pointofinterestform':pointofinterestform}
                return render (request,'AUTOCOMPLETE/location.html',locals())
    else:
        pointofinterestform = PointOfInterestForm()
        return render (request,'AUTOCOMPLETE/location.html',locals())