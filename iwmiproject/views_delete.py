from django.shortcuts import render, render_to_response,get_object_or_404,redirect,RequestContext, HttpResponseRedirect
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.core.context_processors import csrf
from datetime import datetime, date
from .models import Weed,LandClearance,FertilizerManagement,LabourManagament,SystemUser,PlotCrop,Region,District,Village,Remark,SaleHarvestedCrop,OtherWaterUsage,ResidualHandling,Service,Spaire,CropVarieties,BedPlot,SoilProperty,PlotIrrigationEvent,ApplicationCalibration,YieldFarmLevel,YieldRowBedLevel,YieldPlantLevel,ConsumedCrops,TissueNutrientAnalysis,CropMonitoringPlantHeight,GravimetricSoilMoisture,TDRMeasurement,SoilMoistureProfiler,Country,Soil,Weed,WaterliftingCalibrations,TechnologyFailure,Technology,TechnologyManagement,FertilizerManagement,PesticideManagement,Pesticide,Fertilizer,SystemUser,Farm,LandPreparation,NurseryIrrigationEvent,Nursery,BedNursery,Crop,SeedManagement,LandClearance,LabourManagament,WaterManagement,TDRMeasurement,GravimetricSoilMoisture,Plot,PlotManagement,People,Furrow,BedPlot,PlantingMethod
from iwmiproject.forms import LandClearance_Form,LabourManagement_Form,Remark_Form,PlotManagementForm,PlotForm,CropVarietiesForm,BedPlotForm,FurrowForm,WaterManagementForm,PlotCropForm
from .generic import timedifference
import math

from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger
from django.shortcuts import render
from .functions import pick_currency


def delete_landclearance_specific_detail(request,plotID,personID,date):
   print('no')
   if not request.user.is_authenticated():
      return HttpResponseRedirect(reverse('signup:login'))
   plot_land_clearance_instance = LandClearance.objects.get(farm=personID,plotID=Plot.objects.get(plotID=plotID,farm=personID),date=date)
   
   plot_land_clearance_instance.delete()
   
   message='deleted'
   return render(request,'iwmiproject/delete.html',locals())
   
def delete_land_clearance_detail(request,plotID,personID):
   print('yes')
   if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('signup:login'))
   user_instance = SystemUser.objects.get(user=request.user)
   
   if user_instance.role == 'RA' or user_instance.role == 'ST':
      user_village = user_instance.village
      plot_landclearance_queryset_list = LandClearance.objects.filter(enteredpersonel=user_instance,farm=personID,plotID=Plot.objects.get(plotID=plotID,farm=personID)).select_related()
   elif user_instance.role == 'ALL':
      user_country = user_instance.country
      plot_landclearance_queryset_list = LandClearance.objects.filter(farm=personID,plotID=Plot.objects.get(plotID=plotID,farm=personID)).select_related() 
   elif user_instance.role == 'RS':
      researcher_country = user_instance.country
      plot_landclearance_queryset_list = LandClearance.objects.filter(farm__farmID__village__district__region__country=researcher_country).select_related() 
   paginator = Paginator(plot_landclearance_queryset_list, 20)
      
   page = request.GET.get('page')
   try:
      plot_landclearance_queryset = paginator.page(page)
   except PageNotAnInteger:
      plot_landclearance_queryset = paginator.page(1)
   except EmptyPage:
      plot_landclearance_queryset = paginator.page(paginator.num_pages)
      
   context ={
         'object_list':plot_landclearance_queryset,
         'title':"List",
         'user_instance':user_instance
      }
   return render(request,'iwmiproject/iwmiproject_delete/delete_landclearance_detail_display.html',context)


def delete_landpreparation_specific_detail(request,plotID,personID,date):
   if not request.user.is_authenticated():
      return HttpResponseRedirect(reverse('signup:login'))
   plot_landpreparation_instance = LandPreparation.objects.get(farm=personID,plotID=Plot.objects.get(plotID=plotID,farm=personID),date=date)
   
   plot_landpreparation_instance.delete()
   
   message='deleted'
   return render(request,'iwmiproject/delete.html',locals())
   
def delete_landpreparation_detail(request,plotID,personID):
   if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('signup:login'))
   user_instance = SystemUser.objects.get(user=request.user)
   
   if user_instance.role == 'RA' or user_instance.role == 'ST':
      user_village = user_instance.village
      plot_landpreparation_queryset_list = LandPreparation.objects.filter(enteredpersonel=user_instance,farm=personID,plotID=Plot.objects.get(plotID=plotID,farm=personID)).select_related()
   elif user_instance.role == 'ALL':
      user_country = user_instance.country
      plot_landpreparation_queryset_list = LandPreparation.objects.filter(farm=personID,plotID=Plot.objects.get(plotID=plotID,farm=personID)).select_related() 
   elif user_instance.role == 'RS':
      researcher_country = user_instance.country
      plot_landpreparation_queryset_list = LandPreparation.objects.filter(farm__farmID__village__district__region__country=researcher_country).select_related() 
   paginator = Paginator(plot_landpreparation_queryset_list, 20)
      
   page = request.GET.get('page')
   try:
      plot_landpreparation_queryset = paginator.page(page)
   except PageNotAnInteger:
      plot_landpreparation_queryset = paginator.page(1)
   except EmptyPage:
      plot_landpreparation_queryset = paginator.page(paginator.num_pages)
      
   context ={
         'object_list':plot_landpreparation_queryset,
         'title':"List",
         'user_instance':user_instance
      }
   return render(request,'iwmiproject/iwmiproject_delete/delete_landpreparation_detail_display.html',context)


      
def delete_fertilizermanagement_specific_detail(request,plotID,personID,date):
   if not request.user.is_authenticated():
      return HttpResponseRedirect(reverse('signup:login'))
   plot_fertilizermanagement_instance = FertilizerManagement.objects.get(farm=personID,plotID=Plot.objects.get(plotID=plotID,farm=personID),date=date)
   
   plot_fertilizermanagement_instance.delete()
   
   message='deleted'
   return render(request,'iwmiproject/delete.html',locals())

def delete_fertilizermanagement_detail(request,plotID,personID):
   if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('signup:login'))
   user_instance = SystemUser.objects.get(user=request.user)
   
   if user_instance.role == 'RA' or user_instance.role == 'ST':
      user_village = user_instance.village
      plot_fertilizermanagement_queryset_list = FertilizerManagement.objects.filter(enteredpersonel=user_instance,farm=personID,plotID=Plot.objects.get(plotID=plotID,farm=personID)).select_related()
   elif user_instance.role == 'ALL':
      user_country = user_instance.country
      plot_fertilizermanagement_queryset_list = FertilizerManagement.objects.filter(farm=personID,plotID=Plot.objects.get(plotID=plotID,farm=personID)).select_related() 
   elif user_instance.role == 'RS':
      researcher_country = user_instance.country
      plot_fertilizermanagement_queryset_list = FertilizerManagement.objects.filter(farm__farmID__village__district__region__country=researcher_country).select_related() 
   paginator = Paginator(plot_fertilizermanagement_queryset_list, 20)
      
   page = request.GET.get('page')
   try:
      plot_fertilizermanagement_queryset = paginator.page(page)
   except PageNotAnInteger:
      plot_fertilizermanagement_queryset = paginator.page(1)
   except EmptyPage:
      plot_fertilizermanagement_queryset = paginator.page(paginator.num_pages)
      
   context ={
         'object_list':plot_fertilizermanagement_queryset,
         'title':"List",
         'user_instance':user_instance
      }
   return render(request,'iwmiproject/iwmiproject_delete/delete_fertilizermanagement_detail_display.html',context)


def delete_pesticidemanagement_specific_detail(request,plotID,personID,date):
   if not request.user.is_authenticated():
      return HttpResponseRedirect(reverse('signup:login'))
   plot_pesticidemanagement_instance = PesticideManagement.objects.get(farm=personID,plotID=Plot.objects.get(plotID=plotID,farm=personID),date=date)
   
   plot_pesticidemanagement_instance.delete()
   message='deleted'
   return render(request,'iwmiproject/delete.html',locals())

def delete_pesticidemanagement_detail(request,plotID,personID):
   if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('signup:login'))
   user_instance = SystemUser.objects.get(user=request.user)
   
   if user_instance.role == 'RA' or user_instance.role == 'ST':
      user_village = user_instance.village
      plot_pesticidemanagement_queryset_list = PesticideManagement.objects.filter(enteredpersonel=user_instance,farm=personID,plotID=Plot.objects.get(plotID=plotID,farm=personID)).select_related()
   elif user_instance.role == 'ALL':
      user_country = user_instance.country
      plot_pesticidemanagement_queryset_list = PesticideManagement.objects.filter(farm=personID,plotID=Plot.objects.get(plotID=plotID,farm=personID)).select_related() 
   elif user_instance.role == 'RS':
      researcher_country = user_instance.country
      plot_pesticidemanagement_queryset_list = PesticideManagement.objects.filter(farm__farmID__village__district__region__country=researcher_country).select_related() 
   paginator = Paginator(plot_pesticidemanagement_queryset_list, 20)
      
   page = request.GET.get('page')
   try:
      plot_pesticidemanagement_queryset = paginator.page(page)
   except PageNotAnInteger:
      plot_pesticidemanagement_queryset = paginator.page(1)
   except EmptyPage:
      plot_pesticidemanagement_queryset = paginator.page(paginator.num_pages)
      
   context ={
         'object_list':plot_pesticidemanagement_queryset,
         'title':"List",
         'user_instance':user_instance
      }
   return render(request,'iwmiproject/iwmiproject_delete/delete_pesticidemanagement_detail_display.html',context)


def delete_weeding_specific_detail(request,plotID,personID,date):
   if not request.user.is_authenticated():
      return HttpResponseRedirect(reverse('signup:login'))
   plot_weed_instance = Weed.objects.get(farm=personID,plotID=Plot.objects.get(plotID=plotID,farm=personID),date=date)
   
   plot_weed_instance.delete()
   
   message='deleted'
   return render(request,'iwmiproject/delete.html',locals())


def delete_weeding_detail(request,plotID,personID):
   if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('signup:login'))
   user_instance = SystemUser.objects.get(user=request.user)
   
   if user_instance.role == 'RA' or user_instance.role == 'ST':
      user_village = user_instance.village
      plot_weeding_queryset_list = Weed.objects.filter(enteredpersonel=user_instance,farm=personID,plotID=Plot.objects.get(plotID=plotID,farm=personID)).select_related()
   elif user_instance.role == 'ALL':
      user_country = user_instance.country
      plot_weeding_queryset_list = Weed.objects.filter(farm=personID,plotID=Plot.objects.get(plotID=plotID,farm=personID)).select_related() 
   elif user_instance.role == 'RS':
      researcher_country = user_instance.country
      plot_weeding_queryset_list = Weed.objects.filter(farm__farmID__village__district__region__country=researcher_country).select_related() 
   paginator = Paginator(plot_weeding_queryset_list, 20)
      
   page = request.GET.get('page')
   try:
      plot_weeding_queryset = paginator.page(page)
   except PageNotAnInteger:
      plot_weeding_queryset = paginator.page(1)
   except EmptyPage:
      plot_weeding_queryset = paginator.page(paginator.num_pages)
      
   context ={
         'object_list':plot_weeding_queryset,
         'title':"List",
         'user_instance':user_instance
      }
   return render(request,'iwmiproject/iwmiproject_delete/delete_weeding_detail_display.html',context)

