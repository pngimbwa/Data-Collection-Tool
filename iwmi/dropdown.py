

from iwmi.models import Country, Region, Village, District,Crop,Farm,WaterSources,WaterSourceCategory
from django import template
from django.core.context_processors import csrf
from django.core import serializers
from django.http import Http404, HttpResponse 
from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect
register = template.Library()
import json

@register.inclusion_tag("farmer/addfarmer.html")
def country_select(request):
    countries = Country.objects.all().order_by('name')
    return render(request,'farmer/addfarmer.html',locals())
        
def region_select(request,country):
    country_obj = Country.objects.get(name=country)
    regions = Region.objects.all().filter(country=country_obj).order_by('region')
    json_models = serializers.serialize("json", regions)
    print('hello')
    return HttpResponse(json_models, content_type="application/javascript")

def district_select(request,region):
    region_obj = Region.objects.get(region=region)
    districts = District.objects.all().filter(region=region).order_by('district')
    json_models = serializers.serialize("json", districts)
    return HttpResponse(json_models, content_type="application/javascript")

def village_select(request,district):
    district_obj = District.objects.get(district=district)
    villages = Village.objects.all().filter(district=district_obj).order_by('village')
    json_models = serializers.serialize("json",villages)
    return HttpResponse(json_models, content_type="application/javascript")

def farmer_select(request,village):
    #district_obj = District.objects.get(district=district)
    farmers = Farmer.objects.all().filter(village=village).order_by('first_name')
    json_models = serializers.serialize("json",farmers)
    return HttpResponse(json_models, content_type="application/javascript")

def crop_select(request,category):
    #category_obj = Crop.objects.get(category=category)
    crops = Crop.objects.all().filter(category=category).order_by('name')
    json_models = serializers.serialize("json",crops)
    return HttpResponse(json_models, content_type="application/javascript")

def plot_select(request,farm):
    plots= Farm.objects.get(farm=farm).__int__()
    return HttpResponse(json.dumps(plots), content_type="application/json")
 
def pumping_source_select(request,watersource):
    pumping_sources= WaterSourceCategory.objects.filter(watersourcetype=watersource).order_by('category')
    json_models = serializers.serialize("json",pumping_sources)
    return HttpResponse(json_models, content_type="application/javascript")
'''
def water_application_select(request,farmerID):
    water_applications= PlotManagement.objects.get(farm=farmerID)
    json_models = serializers.serialize("json",water_applications)
    return HttpResponse(json_models, content_type="application/javascript")
'''
    
    
    
    
    