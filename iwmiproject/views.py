from django.shortcuts import render, render_to_response,get_object_or_404,redirect,RequestContext, HttpResponseRedirect,HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.core.context_processors import csrf
from datetime import datetime, date
#from iwmi.models import Country, Crop,CropCategory
from .models import MyTestModel,FertilizerSpecification,PlotCrop,Remark,SaleHarvestedCrop,OtherWaterUsage,ResidualHandling,Service,Spaire,CropVarieties,BedPlot,SoilProperty,PlotIrrigationEvent,ApplicationCalibration,YieldFarmLevel,YieldRowBedLevel,YieldPlantLevel,ConsumedCrops,TissueNutrientAnalysis,CropMonitoringPlantHeight,GravimetricSoilMoisture,TDRMeasurement,SoilMoistureProfiler,Country,Soil,Weed,WaterliftingCalibrations,TechnologyFailure,Technology,TechnologyManagement,FertilizerManagement,PesticideManagement,Pesticide,Fertilizer,SystemUser,Farm,LandPreparation,NurseryIrrigationEvent,Nursery,BedNursery,Crop,Seed,SeedManagement,LandClearance,LabourManagament,WaterManagement,TDRMeasurement,GravimetricSoilMoisture,Plot,PlotManagement,People,Furrow,BedPlot,PlantingMethod
from iwmiproject.forms import  UploadFileForm, FertilizerSpecificationForm,RemarkForm,PlantingMethodForm,HarvestedCropSaleForm,OtherWaterUsageForm,ResidueHandlingForm,ConsumedCropbyHouseholdForm,TransplantingForm,NurseryIrrigationForm,ApplicationCalibrationForm,CropMonitoringPlantHeightForm,ServiceRepaireForm,WeedingForm,FarmInfoForm,NurseryForm,FertilizerApplicationForm,PesticideApplicationForm,WaterLiftingCalibrationForm,FarmIrrigationForm,SoilForm,SoilMoistureMeasurementForm,TissueNutrientAnalysisForm,TechnologyFailureForm,FarmYieldLevelForm,BedYieldLevelForm,PlantLevelYieldForm,LandPreparationForm,LandCleareanceForm
#from dal import autocomplete
from .functions import personID_generator, pick_currency, DegreeConverter
from .generic import timedifference
import math
import django_excel as excel
from data_importer.importers import CSVImporter

import csv
import codecs
from io import StringIO,TextIOWrapper



   
'''
class CountryAutocomplete(autocomplete.Select2QuerySetView):
   def get_queryset(self):
      # Don't forget to filter out results depending on the visitor !
      if not self.request.user.is_authenticated():
         return Country.objects.none()

      qs = Country.objects.all()

      if self.q:
         qs = qs.filter(name__istartswith=self.q)

      return qs
'''

def farmer(request):
   if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('signup:login'))
   return render(request,'iwmiproject/farmer.html',locals())

def weeding(request):
   if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('signup:login'))
   
   if request.method == 'POST': 
      weedingform= WeedingForm(request.POST)

      if weedingform.is_valid():
         date = weedingform.cleaned_data['date']
         farm = weedingform.cleaned_data['farm']
         weed_activities = weedingform.cleaned_data['weed_activities']
         plot = weedingform.cleaned_data['plot']

         labour = weedingform.cleaned_data['labour']
         hired_female_number = weedingform.cleaned_data['hired_female_number']
         hired_male_number = weedingform.cleaned_data['hired_male_number']
         family_female_number = weedingform.cleaned_data['family_female_number']
         family_male_number = weedingform.cleaned_data['family_male_number']
         wage = weedingform.cleaned_data['wage']
         #currency = weedingform.cleaned_data['currency']

         family_female_time = weedingform.cleaned_data['family_female_time']
         family_male_time = weedingform.cleaned_data['family_male_time']
         hired_female_time = weedingform.cleaned_data['hired_female_time']
         hired_male_time = weedingform.cleaned_data['hired_male_time']

         user_instance = SystemUser.objects.get(user=request.user)
         currency = pick_currency(user_instance)
         
         try:
            Weed.objects.get(farm=farm,date=date,plotID=Plot.objects.get(plotID=plot),weed_activities=weed_activities)
         except Weed.DoesNotExist:
            weed_instance = Weed(farm=farm,date=date,plotID=Plot.objects.get(plotID=plot),weed_activities=weed_activities,enteredpersonel= SystemUser.objects.get(user=request.user))
            weed_instance.save()
         else:
            message = 'Looks like information already exist'
            user_instance = SystemUser.objects.get(user=request.user)
            currency = pick_currency(user_instance)
            if user_instance.role == 'RA' or user_instance.role == 'ST':user_village = user_instance.village
            elif user_instance.role == 'ALL':user_country = user_instance.country
            elif user_instance.role == 'RS':researcher = user_instance.country
            return render (request,'iwmiproject/weeding.html',locals())
            
         if labour == 'Family':
            if not wage:
               LabourManagament_instance = LabourManagament(date=date,family_female_time=family_female_time,family_male_time=family_male_time,farm=farm,areaID=plot,areadescription='Plot',labour=labour,family_female_number=family_female_number,family_male_number=family_male_number,activity='Weeding',wage=0,price_unit='',enteredpersonel=SystemUser.objects.get(user=request.user))
            
            else:
               LabourManagament_instance = LabourManagament(date=date,family_female_time=family_female_time,family_male_time=family_male_time,farm=farm,areaID=plot,areadescription='Plot',labour=labour,family_female_number=family_female_number,family_male_number=family_male_number,activity='Weeding',wage=wage,price_unit=currency,enteredpersonel=SystemUser.objects.get(user=request.user))
         
         elif labour == 'Hired':
            LabourManagament_instance = LabourManagament(date=date,hired_female_time=hired_female_time,hired_male_time=hired_male_time,farm=farm,areaID=plot,areadescription='Plot',labour=labour,hired_female_number=hired_female_number,hired_male_number=hired_male_number,activity='Weeding',wage=wage,price_unit=currency,enteredpersonel=SystemUser.objects.get(user=request.user))
         
         elif labour == 'FamilyHired':
            LabourManagament_instance = LabourManagament(date=date,family_female_time=family_female_time,family_male_time=family_male_time,hired_female_time=hired_female_time,hired_male_time=hired_male_time,farm=farm,areaID=plot,areadescription='Plot',labour=labour,hired_female_number=hired_female_number,hired_male_number=hired_male_number,family_female_number=family_female_number,family_male_number=family_male_number,activity='Weeding',wage=wage,price_unit=currency,enteredpersonel=SystemUser.objects.get(user=request.user))
         
         
         LabourManagament_instance.save()
         
         message='saved'
         return render(request,'iwmiproject/saved.html',locals())
        
      else:
         user_instance = SystemUser.objects.get(user=request.user)
         currency = pick_currency(user_instance)
         if user_instance.role == 'RA' or user_instance.role == 'ST':user_village = user_instance.village
         elif user_instance.role == 'ALL':user_country = user_instance.country
         elif user_instance.role == 'RS':researcher = user_instance.country
         return render(request,'iwmiproject/weeding.html',locals())
   else:
      user_instance = SystemUser.objects.get(user=request.user)
      currency = pick_currency(user_instance)
      if user_instance.role == 'RA' or user_instance.role == 'ST':user_village = user_instance.village
      elif user_instance.role == 'ALL':user_country = user_instance.country
      elif user_instance.role == 'RS':researcher = user_instance.country
      weedingform= WeedingForm()
      return render(request,'iwmiproject/weeding.html',locals())
   
   

def nursery(request):
   if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('signup:login'))
      
   if request.method == 'POST': 
      nurseryform = NurseryForm(request.POST)
      if nurseryform.is_valid():
         date = nurseryform.cleaned_data['date']
         nurseryID = nurseryform.cleaned_data['nurseryID']
         area = nurseryform.cleaned_data['area']
         farm = nurseryform.cleaned_data['farm']
         #crop = nurseryform.cleaned_data['crop']
         date_bed_preparation = nurseryform.cleaned_data['date_bed_preparation']
         #date_trasplanting = nurseryform.cleaned_data['date_trasplanting']
         bed_length = nurseryform.cleaned_data['bed_length']
         bed_width = nurseryform.cleaned_data['bed_width']
         bednumber = nurseryform.cleaned_data['bednumber']
         seed_per_bed = nurseryform.cleaned_data['seed_per_bed']
         #seedrate = nurseryform.cleaned_data['seedrate']
         seedprice = nurseryform.cleaned_data['seedprice']
         seed_spacing_within_a_bed = nurseryform.cleaned_data['seed_spacing_within_a_bed']
         seed_spacing_btn_bed = nurseryform.cleaned_data['seed_spacing_btn_bed']
         seedtype = nurseryform.cleaned_data['seedtype']
         seeding_date = nurseryform.cleaned_data['seeding_date']
         quantity = nurseryform.cleaned_data['quantity']
         labour = nurseryform.cleaned_data['labour']
         hired_female_number = nurseryform.cleaned_data['hired_female_number']
         hired_male_number = nurseryform.cleaned_data['hired_male_number']
         family_female_number = nurseryform.cleaned_data['family_female_number']
         family_male_number = nurseryform.cleaned_data['family_male_number']
         #labour_time_taken = nurseryform.cleaned_data['labour_time_taken']
         wage = nurseryform.cleaned_data['wage']
         #currency = nurseryform.cleaned_data['currency']
         
         family_female_time = nurseryform.cleaned_data['family_female_time']
         family_male_time = nurseryform.cleaned_data['family_male_time']
         hired_female_time = nurseryform.cleaned_data['hired_female_time']
         hired_male_time = nurseryform.cleaned_data['hired_male_time']
      

         user_instance = SystemUser.objects.get(user=request.user)
         currency = pick_currency(user_instance)
         
         seedrate =area/quantity
         bedarea = bed_width*bed_length
         planting_density_per_bed = bedarea/seed_per_bed
         total_cost = seedprice * quantity
         try:Seed.objects.get(name=seedtype)
         except Seed.DoesNotExist:
            seed_instance = Seed(name=seedtype)
            seed_instance.save()
            
         nursery_instance = Nursery(NurseryID=nurseryID,area=area,farm=Farm.objects.get(farmID=farm),seed=Seed.objects.get(name=seedtype),date_bed_preparation=date_bed_preparation,enteredpersonel= SystemUser.objects.get(user=request.user))
         nursery_instance.save()
         seedmanagement_instance = SeedManagement(date=seeding_date,nursery=Nursery.objects.get(NurseryID=nurseryID),seed=Seed.objects.get(name=seedtype),quantity=quantity,price_per_unit=seedprice,total_cost=total_cost,currency=currency,enteredpersonel= SystemUser.objects.get(user=request.user))
      
         bednursery_instance = BedNursery(length=bed_length,width=bed_width,area=bedarea,nursery=Nursery.objects.get(NurseryID=nurseryID),numbers=bednumber,seed_spacing_within_a_bed=seed_spacing_within_a_bed,seed_spacing_btn_bed=seed_spacing_btn_bed,planting_density_per_bed=planting_density_per_bed,seedrate=seedrate,enteredpersonel=SystemUser.objects.get(user=request.user))
         
         if labour == 'Family':
            if not wage:
               LabourManagament_instance = LabourManagament(date=date,family_female_time=family_female_time,family_male_time=family_male_time,farm=Farm.objects.get(farmID=farm),areaID=nurseryID,areadescription='Nursery',labour=labour,family_female_number=family_female_number,family_male_number=family_male_number,activity='Nurserying',wage=0,price_unit='',enteredpersonel=SystemUser.objects.get(user=request.user))
            else:
               LabourManagament_instance = LabourManagament(date=date,hired_female_time=hired_female_time,hired_male_time=hired_male_time,farm=Farm.objects.get(farmID=farm),areaID=nurseryID,areadescription='Nursery',labour=labour,family_female_number=family_female_number,family_male_number=family_male_number,activity='Nurserying',wage=wage,price_unit=currency,enteredpersonel=SystemUser.objects.get(user=request.user))
         
         elif labour == 'Hired':
            LabourManagament_instance = LabourManagament(date=date,hired_female_time=hired_female_time,hired_male_time=hired_male_time,farm=Farm.objects.get(farmID=farm),areaID=nurseryID,areadescription='Nursery',labour=labour,hired_female_number=hired_female_number,hired_male_number=hired_male_number,activity='Nurserying',wage=wage,price_unit=currency,enteredpersonel=SystemUser.objects.get(user=request.user))
         
         elif labour == 'FamilyHired':
            LabourManagament_instance = LabourManagament(date=date,family_female_time=family_female_time,family_male_time=family_male_time,hired_female_time=hired_female_time,hired_male_time=hired_male_time,farm=Farm.objects.get(farmID=farm),areaID=nurseryID,areadescription='Nursery',labour=labour,hired_female_number=hired_female_number,hired_male_number=hired_male_number,family_female_number=family_female_number,family_male_number=family_male_number,activity='Nurserying',wage=wage,price_unit=currency,enteredpersonel=SystemUser.objects.get(user=request.user))

         seedmanagement_instance.save()
         
         bednursery_instance.save()
         LabourManagament_instance.save()
         
         message='saved'
         return render(request,'iwmiproject/saved.html',locals())
        
      else:
         user_instance = SystemUser.objects.get(user=request.user)
         currency = pick_currency(user_instance)
         if user_instance.role == 'RA' or user_instance.role == 'ST':user_village = user_instance.village
         elif user_instance.role == 'ALL':user_country = user_instance.country
         elif user_instance.role == 'RS':researcher = user_instance.country
         return render(request,'iwmiproject/nursery.html',locals())
      
   else:
      user_instance = SystemUser.objects.get(user=request.user)
      currency = pick_currency(user_instance)
      if user_instance.role == 'RA' or user_instance.role == 'ST':user_village = user_instance.village
      elif user_instance.role == 'ALL':user_country = user_instance.country
      elif user_instance.role == 'RS':researcher = user_instance.country
      nurseryform = NurseryForm()
      return render(request,'iwmiproject/nursery.html',locals())
   
def nurseryirrigation(request):
   if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('signup:login'))
      
   if request.method == 'POST': 
      nurseryirrigationform = NurseryIrrigationForm(request.POST)
      if nurseryirrigationform.is_valid():
         date = nurseryirrigationform.cleaned_data['date']
         climate = nurseryirrigationform.cleaned_data['climate']
         farm = nurseryirrigationform.cleaned_data['farm']
         nurseryID = nurseryirrigationform.cleaned_data['nurseryID']
         time_started = nurseryirrigationform.cleaned_data['time_started']
         time_ended = nurseryirrigationform.cleaned_data['time_ended']
         total_time = nurseryirrigationform.cleaned_data['total_time']
         irrigation_depth = nurseryirrigationform.cleaned_data['irrigation_depth']
         #event = nurseryirrigationform.cleaned_data['event']
         bucket_volume = nurseryirrigationform.cleaned_data['bucket_volume']
         bucket_numbers = nurseryirrigationform.cleaned_data['bucket_numbers']
         total_volume = nurseryirrigationform.cleaned_data['total_volume']
         labour = nurseryirrigationform.cleaned_data['labour']
         hired_female_number = nurseryirrigationform.cleaned_data['hired_female_number']
         hired_male_number = nurseryirrigationform.cleaned_data['hired_male_number']
         family_female_number = nurseryirrigationform.cleaned_data['family_female_number']
         family_male_number = nurseryirrigationform.cleaned_data['family_male_number']
         #labour_time_taken = nurseryirrigationform.cleaned_data['labour_time_taken']
         #currency = nurseryirrigationform.cleaned_data['currency']
         wage  = nurseryirrigationform.cleaned_data['wage']
        
         family_female_time = nurseryirrigationform.cleaned_data['family_female_time']
         family_male_time = nurseryirrigationform.cleaned_data['family_male_time']
         hired_female_time = nurseryirrigationform.cleaned_data['hired_female_time']
         hired_male_time = nurseryirrigationform.cleaned_data['hired_male_time']
         
         user_instance = SystemUser.objects.get(user=request.user)
         currency = pick_currency(user_instance)
         
         print('time_ended:{}'.format(time_ended))
         #family_female_time=family_female_time,family_male_time=family_male_time
         #hired_female_time=hired_female_time,hired_male_time=hired_male_time
         #family_female_time=family_female_time,family_male_time=family_male_time,hired_female_time=hired_female_time,hired_male_time=hired_male_time
         try:
            NurseryIrrigationEvent.objects.get(date=date,nursery=Nursery.objects.get(NurseryID=nurseryID),time_started=time_started,time_ended=time_ended)
         except NurseryIrrigationEvent.DoesNotExist:
            events =[i.event for i in NurseryIrrigationEvent.objects.all().filter(nursery=Nursery.objects.get(NurseryID=nurseryID))]
            if not events:current_event = 1
            else:current_event = max(events) + 1
            nurseryirrigationevent_instance = NurseryIrrigationEvent(date=date,nursery=Nursery.objects.get(NurseryID=nurseryID),time_started=time_started,irrigation_depth=irrigation_depth,time_ended=time_ended,total_time=total_time,event=current_event,quantity=bucket_numbers,total_volume=total_volume,climate=climate,enteredpersonel=SystemUser.objects.get(user=request.user))
            nurseryirrigationevent_instance.save()
         else:
            message = "Looks like the event on {} from {} to {} on Nursery '{}' is already recorded.!\
                      Go edit link if you want to update information".format(date,time_started,time_ended,nurseryID)
            user_instance = SystemUser.objects.get(user=request.user)
            currency = pick_currency(user_instance)
            if user_instance.role == 'RA' or user_instance.role == 'ST':user_village = user_instance.village
            elif user_instance.role == 'ALL':user_country = user_instance.country
            elif user_instance.role == 'RS':researcher = user_instance.country
            return render(request,'iwmiproject/nurseryirrigation.html',locals())
         
         if labour == 'Family':
            if not wage:
               LabourManagament_instance = LabourManagament(date=date,family_female_time=family_female_time,family_male_time=family_male_time,farm=Farm.objects.get(farmID=farm),areaID=nurseryID,areadescription='Nursery',labour=labour,family_female_number=family_female_number,family_male_number=family_male_number,activity='Nursery irrigation',wage=0,price_unit='',enteredpersonel=SystemUser.objects.get(user=request.user))
            else:
               LabourManagament_instance = LabourManagament(date=date,family_female_time=family_female_time,family_male_time=family_male_time,farm=Farm.objects.get(farmID=farm),areaID=nurseryID,areadescription='Nursery',labour=labour,family_female_number=family_female_number,family_male_number=family_male_number,activity='Nursery irrigation',wage=wage,price_unit=currency,enteredpersonel=SystemUser.objects.get(user=request.user))
         elif labour == 'Hired':
            LabourManagament_instance = LabourManagament(date=date,hired_female_time=hired_female_time,hired_male_time=hired_male_time,farm=Farm.objects.get(farmID=farm),areaID=nurseryID,areadescription='Nursery',labour=labour,hired_female_number=hired_female_number,hired_male_number=hired_male_number,activity='Nursery irrigation',wage=wage,price_unit=currency,enteredpersonel=SystemUser.objects.get(user=request.user))
         elif labour == 'FamilyHired':
            LabourManagament_instance = LabourManagament(date=date,family_female_time=family_female_time,family_male_time=family_male_time,hired_female_time=hired_female_time,hired_male_time=hired_male_time,farm=Farm.objects.get(farmID=farm),areaID=nurseryID,areadescription='Nursery',labour=labour,hired_female_number=hired_female_number,hired_male_number=hired_male_number,family_female_number=family_female_number,family_male_number=family_male_number,activity='Nurserying',wage=wage,price_unit=currency,enteredpersonel=SystemUser.objects.get(user=request.user))

         LabourManagament_instance.save()
         message='saved'
         return render(request,'iwmiproject/saved.html',locals())
      else:
         user_instance = SystemUser.objects.get(user=request.user)
         currency = pick_currency(user_instance)
         if user_instance.role == 'RA' or user_instance.role == 'ST':user_village = user_instance.village
         elif user_instance.role == 'ALL':user_country = user_instance.country
         elif user_instance.role == 'RS':researcher = user_instance.country
         #context = {'nurseryirrigationform':nurseryirrigationform}
         return render(request,'iwmiproject/nurseryirrigation.html',locals())
   else:
      user_instance = SystemUser.objects.get(user=request.user)
      currency = pick_currency(user_instance)
      if user_instance.role == 'RA' or user_instance.role == 'ST':user_village = user_instance.village
      elif user_instance.role == 'ALL':user_country = user_instance.country
      elif user_instance.role == 'RS':researcher = user_instance.country
      nurseryirrigationform = NurseryIrrigationForm()
      return render(request,'iwmiproject/nurseryirrigation.html',locals())


def plantingmethod(request):
   if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('signup:login'))
   
   if request.method == 'POST': 
      plantingmethodform = PlantingMethodForm(request.POST)
      if plantingmethodform.is_valid():
         farmer = plantingmethodform.cleaned_data['farmer']
         plotID = plantingmethodform.cleaned_data['plotID']
         transplanting_date_one = plantingmethodform.cleaned_data['transplanting_date_one']
         transplanting_date_two = plantingmethodform.cleaned_data['transplanting_date_two']
         nurseryID_one = plantingmethodform.cleaned_data['nurseryID_one']
         nurseryID_two = plantingmethodform.cleaned_data['nurseryID_two']   
         seeding_date = plantingmethodform.cleaned_data['seeding_date']
         seed_quantity = plantingmethodform.cleaned_data['seed_quantity']
         seeding_date2 = plantingmethodform.cleaned_data['seeding_date2']
         seed_quantity2 = plantingmethodform.cleaned_data['seed_quantity2']       
         number_of_plants_per_row = plantingmethodform.cleaned_data['number_of_plants_per_row']
         spacing_within_a_row = plantingmethodform.cleaned_data['spacing_within_a_row']
         spacing_btn_a_row = plantingmethodform.cleaned_data['spacing_btn_a_row']         
         number_of_plants_per_row_two = plantingmethodform.cleaned_data['number_of_plants_per_row_two']
         spacing_within_a_row_two = plantingmethodform.cleaned_data['spacing_within_a_row_two']
         #planting_method = plantingmethodform.cleaned_data['planting_method']       
         total_plants = plantingmethodform.cleaned_data['total_plants']
         total_seed_quantity = plantingmethodform.cleaned_data['total_seed_quantity']
         labour = plantingmethodform.cleaned_data['labour']
         hired_female_number = plantingmethodform.cleaned_data['hired_female_number']
         hired_male_number = plantingmethodform.cleaned_data['hired_male_number']
         family_female_number = plantingmethodform.cleaned_data['family_female_number']
         family_male_number = plantingmethodform.cleaned_data['family_male_number']
         wage = plantingmethodform.cleaned_data['wage']
         #currency = plantingmethodform.cleaned_data['currency']
         family_female_time = plantingmethodform.cleaned_data['family_female_time']
         family_male_time = plantingmethodform.cleaned_data['family_male_time']
         hired_female_time = plantingmethodform.cleaned_data['hired_female_time']
         hired_male_time = plantingmethodform.cleaned_data['hired_male_time']
         CroppingSystem = plantingmethodform.cleaned_data['CroppingSystem']
         
         crop1_plantingMethod = plantingmethodform.cleaned_data['crop1_plantingMethod']
         crop2_plantingMethod = plantingmethodform.cleaned_data['crop2_plantingMethod']
         
         user_instance = SystemUser.objects.get(user=request.user)
         currency = pick_currency(user_instance)
         
         try:
            PlantingMethod.objects.get(farm=Farm.objects.get(farmID=farmer),plotID=Plot.objects.get(plotID=plotID,farm=Farm.objects.get(farmID=farmer)))
         except PlantingMethod.DoesNotExist:
            pass
         else:
            message = 'Plot "{}" is registered already..'.format(plotID)
            if user_instance.role == 'RA' or user_instance.role == 'ST':user_village = user_instance.village
            elif user_instance.role == 'ALL':user_country = user_instance.country
            elif user_instance.role == 'RS':researcher = user_instance.country
            return render(request,'iwmiproject/plantingmethod.html',locals())
            
         try:
            BedPlot.objects.get(farm=Farm.objects.get(farmID=farmer),plotID=Plot.objects.get(plotID=plotID,farm=Farm.objects.get(farmID=farmer)))
         except BedPlot.DoesNotExist:
            message = 'Plot "{}" is not yet registered...Please register it or cross check with admin'.format(plotID)
            if user_instance.role == 'RA' or user_instance.role == 'ST':user_village = user_instance.village
            elif user_instance.role == 'ALL':user_country = user_instance.country
            elif user_instance.role == 'RS':researcher = user_instance.country
            return render(request,'iwmiproject/plantingmethod.html',locals())
         else:
            bednumber = BedPlot.objects.get(farm=Farm.objects.get(farmID=farmer),plotID=Plot.objects.get(plotID=plotID,farm=Farm.objects.get(farmID=farmer))).numbers
         
         if CroppingSystem =='Monocropping':
            if crop1_plantingMethod == 'direct seeding':
               if total_plants == 'NONE':total_plants=None
               else: total_plants = int(total_plants)
               plantingmethod_instance = PlantingMethod(CroppingSystem=CroppingSystem,farm=Farm.objects.get(farmID=farmer),total_plants=total_plants,date_one=seeding_date,plotID=plotID,spacing_within_a_row=spacing_within_a_row,spacing_btn_a_row=spacing_btn_a_row,seed_quantity=seed_quantity,total_seed_quantity=total_seed_quantity,enteredpersonel=SystemUser.objects.get(user=request.user))
            elif crop1_plantingMethod == 'transplanting':
               plantingmethod_instance = PlantingMethod(CroppingSystem=CroppingSystem,farm=Farm.objects.get(farmID=farmer),date_one=transplanting_date_one,plotID=plotID,nurseryID_one=nurseryID_one,spacing_within_a_row=spacing_within_a_row,spacing_btn_a_row=spacing_btn_a_row,plantsnumber_per_row_one=number_of_plants_per_row,total_plants=total_plants,enteredpersonel=SystemUser.objects.get(user=request.user))
         
         elif CroppingSystem =='Intercropping':
            if crop1_plantingMethod == 'direct seeding' and crop2_plantingMethod == 'direct seeding':
               if total_plants == 'NONE':total_plants=None
               else: total_plants = int(total_plants)
               plantingmethod_instance = PlantingMethod(CroppingSystem=CroppingSystem,farm=Farm.objects.get(farmID=farmer),date_one=seeding_date,date_two=seeding_date2,plotID=plotID,spacing_within_a_row=spacing_within_a_row,spacing_within_a_row_two=spacing_within_a_row_two,spacing_btn_a_row=spacing_btn_a_row,seed_quantity=seed_quantity,seed_quantity2=seed_quantity2,total_seed_quantity=total_seed_quantity,total_plants=total_plants,enteredpersonel=SystemUser.objects.get(user=request.user))
            elif crop1_plantingMethod == 'direct seeding' and crop2_plantingMethod == 'transplanting':
               total_plants = int(total_plants)
               plantingmethod_instance = PlantingMethod(farm=Farm.objects.get(farmID=farmer),plotID=plotID,CroppingSystem=CroppingSystem,date_one=seeding_date,date_two=transplanting_date_two,spacing_within_a_row=spacing_within_a_row,spacing_within_a_row_two=spacing_within_a_row_two,nurseryID_two=nurseryID_two,plantsnumber_per_row_two=number_of_plants_per_row_two,total_plants=total_plants,seed_quantity=seed_quantity,total_seed_quantity=total_seed_quantity,spacing_btn_a_row=spacing_btn_a_row,enteredpersonel=SystemUser.objects.get(user=request.user))
            elif crop1_plantingMethod == 'transplanting' and crop2_plantingMethod == 'direct seeding':
               total_plants = int(total_plants)
               plantingmethod_instance = PlantingMethod(farm=Farm.objects.get(farmID=farmer),plotID=plotID,CroppingSystem=CroppingSystem,date_one=transplanting_date_one,date_two=seeding_date2,nurseryID_one=nurseryID_one,seed_quantity2=seed_quantity2,total_seed_quantity=total_seed_quantity,total_plants=total_plants,spacing_btn_a_row=spacing_btn_a_row,plantsnumber_per_row_one=number_of_plants_per_row,spacing_within_a_row=spacing_within_a_row,spacing_within_a_row_two=spacing_within_a_row_two,enteredpersonel=SystemUser.objects.get(user=request.user))
            elif crop1_plantingMethod == 'transplanting' and crop2_plantingMethod == 'transplanting':
               total_plants = int(total_plants)
               plantingmethod_instance = PlantingMethod(CroppingSystem=CroppingSystem,farm=Farm.objects.get(farmID=farmer),date_one=transplanting_date_one,date_two=transplanting_date_two,plotID=plotID,nurseryID_one=nurseryID_one,nurseryID_two=nurseryID_two,spacing_within_a_row=spacing_within_a_row,spacing_within_a_row_two=spacing_within_a_row_two,spacing_btn_a_row=spacing_btn_a_row,plantsnumber_per_row_one=number_of_plants_per_row,plantsnumber_per_row_two=number_of_plants_per_row_two,total_plants=total_plants,enteredpersonel=SystemUser.objects.get(user=request.user))
         plantingmethod_instance.save()
         
         '''
         plantingmethod_instance.save()
         if CroppingSystem =='Monocropping' and planting_method == 'direct seeding':
            #plantsnumber=number_of_plants_per_row * bednumber
            plantingmethod_instance = PlantingMethod(CroppingSystem=CroppingSystem,farm=Farm.objects.get(farmID=farmer),date_one=seeding_date,planting_method=planting_method,plotID=plotID,spacing_within_a_row=spacing_within_a_row,spacing_btn_a_row=spacing_btn_a_row,seed_quantity=seed_quantity,total_seed_quantity=total_seed_quantity,enteredpersonel=SystemUser.objects.get(user=request.user))
         elif CroppingSystem =='Monocropping' and planting_method == 'transplanting':
            #plantsnumber=number_of_plants_per_row * bednumber
            plantingmethod_instance = PlantingMethod(CroppingSystem=CroppingSystem,farm=Farm.objects.get(farmID=farmer),date_one=transplanting_date_one,planting_method=planting_method,plotID=plotID,nurseryID_one=nurseryID_one,spacing_within_a_row=spacing_within_a_row,spacing_btn_a_row=spacing_btn_a_row,plantsnumber_per_row_one=number_of_plants_per_row,total_plants=total_plants,enteredpersonel=SystemUser.objects.get(user=request.user))
         elif CroppingSystem =='Intercropping' and planting_method == 'direct seeding':
            plantingmethod_instance = PlantingMethod(CroppingSystem=CroppingSystem,farm=Farm.objects.get(farmID=farmer),date_one=seeding_date,date_two=seeding_date2,planting_method=planting_method,plotID=plotID,spacing_within_a_row=spacing_within_a_row,spacing_within_a_row_two=spacing_within_a_row_two,spacing_btn_a_row=spacing_btn_a_row,seed_quantity=seed_quantity,seed_quantity2=seed_quantity2,total_seed_quantity=total_seed_quantity,enteredpersonel=SystemUser.objects.get(user=request.user))
         elif CroppingSystem =='Intercropping' and planting_method == 'transplanting':
            plantingmethod_instance = PlantingMethod(CroppingSystem=CroppingSystem,farm=Farm.objects.get(farmID=farmer),date_one=transplanting_date_one,date_two=transplanting_date_two,planting_method=planting_method,plotID=plotID,nurseryID_one=nurseryID_one,nurseryID_two=nurseryID_two,spacing_within_a_row=spacing_within_a_row,spacing_within_a_row_two=spacing_within_a_row_two,spacing_btn_a_row=spacing_btn_a_row,plantsnumber_per_row_one=number_of_plants_per_row,plantsnumber_per_row_two=number_of_plants_per_row_two,total_plants=total_plants,enteredpersonel=SystemUser.objects.get(user=request.user))
         plantingmethod_instance.save()
         '''
         
         if labour == 'Family':
            LabourManagament_instance = LabourManagament(family_female_time=family_female_time,family_male_time=family_male_time,farm=Farm.objects.get(farmID=farmer),areaID=plotID,areadescription='Plot',labour=labour,family_female_number=family_female_number,family_male_number=family_male_number,activity='Field Planting',wage=wage,price_unit=currency,enteredpersonel=SystemUser.objects.get(user=request.user))
         elif labour == 'Hired':
            LabourManagament_instance = LabourManagament(hired_female_time=hired_female_time,hired_male_time=hired_male_time,farm=Farm.objects.get(farmID=farmer),areaID=plotID,areadescription='Plot',labour=labour,hired_female_number=hired_female_number,hired_male_number=hired_male_number,activity='Field Planting',wage=wage,price_unit=currency,enteredpersonel=SystemUser.objects.get(user=request.user))
         elif labour == 'FamilyHired':
            LabourManagament_instance = LabourManagament(family_female_time=family_female_time,family_male_time=family_male_time,hired_female_time=hired_female_time,hired_male_time=hired_male_time,farm=Farm.objects.get(farmID=farmer),areaID=plotID,areadescription='Plot',labour=labour,hired_female_number=hired_female_number,hired_male_number=hired_male_number,family_female_number=family_female_number,family_male_number=family_male_number,activity='Field Planting',wage=wage,price_unit=currency,enteredpersonel=SystemUser.objects.get(user=request.user))
         LabourManagament_instance.save()
         '''
         if labour == 'Family':
            if planting_method == 'direct seeding':
               LabourManagament_instance = LabourManagament(family_female_time=family_female_time,family_male_time=family_male_time,date=seeding_date,farm=Farm.objects.get(farmID=farmer),areaID=plotID,areadescription='Plot',labour=labour,family_female_number=family_female_number,family_male_number=family_male_number,activity='Seeding',wage=wage,price_unit=currency,enteredpersonel=SystemUser.objects.get(user=request.user))
            elif planting_method == 'transplanting':
               LabourManagament_instance = LabourManagament(family_female_time=family_female_time,family_male_time=family_male_time,date=transplanting_date_one,farm=Farm.objects.get(farmID=farmer),areaID=plotID,areadescription='Plot',labour=labour,family_female_number=family_female_number,family_male_number=family_male_number,activity='Transplanting',wage=wage,price_unit=currency,enteredpersonel=SystemUser.objects.get(user=request.user))
         elif labour == 'Hired':
            if planting_method == 'direct seeding':
               LabourManagament_instance = LabourManagament(hired_female_time=hired_female_time,hired_male_time=hired_male_time,date=seeding_date,farm=Farm.objects.get(farmID=farmer),areaID=plotID,areadescription='Plot',labour=labour,hired_female_number=hired_female_number,hired_male_number=hired_male_number,activity='Seeding',wage=wage,price_unit=currency,enteredpersonel=SystemUser.objects.get(user=request.user))
            elif planting_method == 'transplanting':
               LabourManagament_instance = LabourManagament(hired_female_time=hired_female_time,hired_male_time=hired_male_time,date=transplanting_date_one,farm=Farm.objects.get(farmID=farmer),areaID=plotID,areadescription='Plot',labour=labour,hired_female_number=hired_female_number,hired_male_number=hired_male_number,activity='Transplanting',wage=wage,price_unit=currency,enteredpersonel=SystemUser.objects.get(user=request.user))
         elif labour == 'FamilyHired':
            if planting_method == 'direct seeding':
               LabourManagament_instance = LabourManagament(time_taken=labour_time_taken,date=seeding_date,farm=Farm.objects.get(farmID=farmer),areaID=plotID,areadescription='Plot',labour=labour,hired_female_number=hired_female_number,hired_male_number=hired_male_number,family_female_number=family_female_number,family_male_number=family_male_number,activity='Seeding',wage=wage,price_unit=currency,enteredpersonel=SystemUser.objects.get(user=request.user))
            elif planting_method == 'transplanting':
               LabourManagament_instance = LabourManagament(family_female_time=family_female_time,family_male_time=family_male_time,hired_female_time=hired_female_time,hired_male_time=hired_male_time,date=transplanting_date_one,farm=Farm.objects.get(farmID=farmer),areaID=plotID,areadescription='Plot',labour=labour,hired_female_number=hired_female_number,hired_male_number=hired_male_number,family_female_number=family_female_number,family_male_number=family_male_number,activity='Transplanting',wage=wage,price_unit=currency,enteredpersonel=SystemUser.objects.get(user=request.user))
         LabourManagament_instance.save()
         '''
         
         #seeding_date,transplanting_date
         message='saved'
         return render(request,'iwmiproject/saved.html',locals())
      else:
         user_instance = SystemUser.objects.get(user=request.user)
         currency = pick_currency(user_instance)
         if user_instance.role == 'RA' or user_instance.role == 'ST':
            user_village = user_instance.village
            context = {'plantingmethodform':plantingmethodform,'user_village':user_village}
         elif user_instance.role == 'ALL':
            user_country = user_instance.country
            context = {'plantingmethodform':plantingmethodform,'user_country':user_country}
         return render_to_response('iwmiproject/plantingmethod.html',context,context_instance=RequestContext(request))
   else:
      user_instance = SystemUser.objects.get(user=request.user)
      currency = pick_currency(user_instance)
      if user_instance.role == 'RA' or user_instance.role == 'ST':user_village = user_instance.village
      elif user_instance.role == 'ALL':user_country = user_instance.country
      elif user_instance.role == 'RS':researcher = user_instance.country
      plantingmethodform = PlantingMethodForm()
      return render(request,'iwmiproject/plantingmethod.html',locals())

def farminfo(request):
   if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('signup:login'))
    
   if request.method == 'POST': 
      farminfoform = FarmInfoForm(request.POST)
      if farminfoform.is_valid():

         farmer = farminfoform.cleaned_data['farmer']
         plotID = farminfoform.cleaned_data['plotID']
         
         farm_ownership_status = farminfoform.cleaned_data['farm_ownership_status']
         landownership = farminfoform.cleaned_data['landownership']
         
         fieldtype = farminfoform.cleaned_data['fieldtype']
         
         field_latitude_degree = farminfoform.cleaned_data['field_latitude_degree']
         field_latitude_minute = farminfoform.cleaned_data['field_latitude_minute']
         field_latitude_second = farminfoform.cleaned_data['field_latitude_second']
         field_latitude_direction = farminfoform.cleaned_data['field_latitude_direction']
         
         field_longitude_degree = farminfoform.cleaned_data['field_longitude_degree']
         field_longitude_minute = farminfoform.cleaned_data['field_longitude_minute']
         field_longitude_second = farminfoform.cleaned_data['field_longitude_second']
         field_longitude_direction = farminfoform.cleaned_data['field_longitude_direction']
         
         cropping_system = farminfoform.cleaned_data['cropping_system']

         crop1 = farminfoform.cleaned_data['crop1']
         crop_variety1 = farminfoform.cleaned_data['crop_variety1']
         variety_type1 = farminfoform.cleaned_data['variety_type1']
         crop1_planting_method = farminfoform.cleaned_data['crop1_planting_method']
         crop1_rootdepth = farminfoform.cleaned_data['crop1_rootdepth']
         crop1_management_practice = farminfoform.cleaned_data['crop1_management_practice']
         crop1_mulching_type = farminfoform.cleaned_data['crop1_mulching_type']
         crop1_mulching_quantity = farminfoform.cleaned_data['crop1_mulching_quantity']
         
         crop2 = farminfoform.cleaned_data['crop2']
         crop_variety2 = farminfoform.cleaned_data['crop_variety2']
         variety_type2 = farminfoform.cleaned_data['variety_type2']
         crop2_planting_method = farminfoform.cleaned_data['crop2_planting_method']
         crop2_rootdepth = farminfoform.cleaned_data['crop2_rootdepth']
         crop2_management_practice = farminfoform.cleaned_data['crop2_management_practice']
         crop2_mulching_type = farminfoform.cleaned_data['crop2_mulching_type']
         crop2_mulching_quantity = farminfoform.cleaned_data['crop2_mulching_quantity']
         
         fieldsize = farminfoform.cleaned_data['fieldsize']
         water_application = farminfoform.cleaned_data['water_application']
         water_management_method = farminfoform.cleaned_data['water_management_method']

         bed_length = farminfoform.cleaned_data['bed_length']
         bed_width = farminfoform.cleaned_data['bed_width']
         bednumber = farminfoform.cleaned_data['bednumber']
         furrow_length = farminfoform.cleaned_data['furrow_length']
         furrow_width = farminfoform.cleaned_data['furrow_width']
         nfurrow = farminfoform.cleaned_data['nfurrow']
         WFD_yellow_depth = farminfoform.cleaned_data['WFD_yellow_depth']
         WFD_red_depth = farminfoform.cleaned_data['WFD_red_depth']
         TDR_length = farminfoform.cleaned_data['TDR_length']
         elevation = farminfoform.cleaned_data['elevation']
         seasonstart = farminfoform.cleaned_data['seasonstart']
         
         lease_duration = farminfoform.cleaned_data['lease_duration']
         payment_option = farminfoform.cleaned_data['payment_option']
         payment_monetary = farminfoform.cleaned_data['payment_monetary']
         payement_other = farminfoform.cleaned_data['payement_other']
         #growinglength = (seasonend - seasonstart).days
         
         field_longitude=DegreeConverter(field_latitude_degree,field_latitude_minute,field_latitude_second,field_latitude_direction)
         field_latitude=DegreeConverter(field_longitude_degree,field_longitude_minute,field_longitude_second,field_longitude_direction)
         

         if fieldtype == 'Pocket garden':
            bed_length = -999
            bed_width = -999
            bednumber = -999
            furrow_length = -999
            furrow_width = -999
            nfurrow = -999
            
         user_instance = SystemUser.objects.get(user=request.user)
         currency = pick_currency(user_instance)
         try:
            Plot.objects.get(plotID=plotID,farm=Farm.objects.get(farmID=farmer))
         except Plot.DoesNotExist:
            if farm_ownership_status =='All owned':
               landownership = 'Owned'
               plot_instance = Plot(fieldtype=fieldtype,landownership=landownership,farm=Farm.objects.get(farmID=farmer),plotID=plotID,latitude=field_latitude,longitude=field_longitude,enteredpersonel= SystemUser.objects.get(user=request.user))
            elif farm_ownership_status =='Partly owned':
               #landownership = 'Owned'
               if landownership == 'Owned':
                  plot_instance = Plot(fieldtype=fieldtype,landownership=landownership,farm=Farm.objects.get(farmID=farmer),plotID=plotID,latitude=field_latitude,longitude=field_longitude,enteredpersonel= SystemUser.objects.get(user=request.user))
               elif landownership == 'Rented':
                  if payment_option == 'Monetary':
                     plot_instance = Plot(fieldtype=fieldtype,landownership=landownership,farm=Farm.objects.get(farmID=farmer),plotID=plotID,latitude=field_latitude,longitude=field_longitude,\
                                          lease_duration=lease_duration,payment_option=payment_option,payment_monetary=payment_monetary,currency=currency,\
                                          enteredpersonel= SystemUser.objects.get(user=request.user))
                  elif payment_option == 'Other':
                     plot_instance = Plot(fieldtype=fieldtype,landownership=landownership,farm=Farm.objects.get(farmID=farmer),plotID=plotID,latitude=field_latitude,longitude=field_longitude,\
                                       lease_duration=lease_duration,payment_option=payment_option,payement_other=payement_other,\
                                       enteredpersonel= SystemUser.objects.get(user=request.user))
               #plot_instance = Plot(landownership=landownership,farm=Farm.objects.get(farmID=farmer),plotID=plotID,latitude=field_latitude,longitude=field_longitude,enteredpersonel= SystemUser.objects.get(user=request.user))
            elif farm_ownership_status =='All rented':
               landownership = 'Rented'
               if payment_option == 'Monetary':
                  plot_instance = Plot(fieldtype=fieldtype,landownership=landownership,farm=Farm.objects.get(farmID=farmer),plotID=plotID,latitude=field_latitude,longitude=field_longitude,\
                                       lease_duration=lease_duration,payment_option=payment_option,payment_monetary=payment_monetary,currency=currency,\
                                       enteredpersonel= SystemUser.objects.get(user=request.user))
               elif payment_option == 'Other':
                  plot_instance = Plot(fieldtype=fieldtype,landownership=landownership,farm=Farm.objects.get(farmID=farmer),plotID=plotID,latitude=field_latitude,longitude=field_longitude, \
                                       lease_duration=lease_duration,payment_option=payment_option,payement_other=payement_other,\
                                       enteredpersonel= SystemUser.objects.get(user=request.user))
               #plot_instance = Plot(landownership=landownership,farm=Farm.objects.get(farmID=farmer),plotID=plotID,latitude=field_latitude,longitude=field_longitude,enteredpersonel= SystemUser.objects.get(user=request.user))
            plot_instance.save()
         else:
            firstname = People.objects.get(personID=farmer).firstname
            lastname = People.objects.get(personID=farmer).lastname
            message = 'The plot with id of {} for farmer {} {} is registered'.format(plotID,firstname,lastname)
            
            if user_instance.role == 'RA' or user_instance.role == 'ST':user_village = user_instance.village
            elif user_instance.role == 'ALL':user_country = user_instance.country
            elif user_instance.role == 'RS':researcher = user_instance.country
            return render(request,'iwmiproject/farmerinfo.html',locals())
         
         #cropvariety_instance = CropVarieties(farm=Farm.objects.get(farmID=farmer),plotID=Plot.objects.get(plotID=plotID,farm=Farm.objects.get(farmID=farmer)),cropname=crop,variety=crop_variety,varietytype=variety_type)
         #cropvariety_instance.save()
         
         if cropping_system == 'Monocropping':
            try:Crop.objects.get(name=crop1)
            except Crop.DoesNotExist:
               crop_instance = Crop(name=crop1)
               crop_instance.save()
            finally:crop1=Crop.objects.get(name=crop1)
            '''
            if management_practice =="Mulching":
               plotmanagement_instance = PlotManagement(cropping_system=cropping_system,management_practice=management_practice,mulching_type=mulching_type,mulching_quantity=mulching_quantity,date=seasonstart,farm=Farm.objects.get(farmID=farmer),plotID=Plot.objects.get(plotID=plotID,farm=Farm.objects.get(farmID=farmer)),elevation=elevation,plot_size=fieldsize,seasonstart=seasonstart,rootdepth=rootzone_depth,water_application=water_application,enteredpersonel= SystemUser.objects.get(user=request.user))
            elif management_practice =="No mulching":
               plotmanagement_instance = PlotManagement(cropping_system=cropping_system,management_practice=management_practice,date=seasonstart,farm=Farm.objects.get(farmID=farmer),plotID=Plot.objects.get(plotID=plotID,farm=Farm.objects.get(farmID=farmer)),elevation=elevation,plot_size=fieldsize,seasonstart=seasonstart,rootdepth=rootzone_depth,water_application=water_application,enteredpersonel= SystemUser.objects.get(user=request.user))
            plotmanagement_instance.save()
            plotmanagement_instance.crop.add(crop1)
            '''
            
            plotmanagement_instance = PlotManagement(cropping_system=cropping_system,date=seasonstart,farm=Farm.objects.get(farmID=farmer),plotID=Plot.objects.get(plotID=plotID,farm=Farm.objects.get(farmID=farmer)),elevation=elevation,plot_size=fieldsize,seasonstart=seasonstart,water_application=water_application,enteredpersonel= SystemUser.objects.get(user=request.user))
            plotmanagement_instance.save()
            plotmanagement_instance.crop.add(crop1)
            
            if crop1_management_practice =="Mulching":
               plotcrop_instance = PlotCrop(farm=Farm.objects.get(farmID=farmer),plotID=Plot.objects.get(plotID=plotID,farm=Farm.objects.get(farmID=farmer)),crop1=crop1,crop1_variety=crop_variety1,crop1_varietytype=variety_type1,crop1_planting_method=crop1_planting_method,\
                                         crop1_rootdepth=crop1_rootdepth,crop1_management_practice=crop1_management_practice,crop1_mulching_type=crop1_mulching_type,crop1_mulching_quantity=crop1_mulching_quantity, \
                                         cropping_system=cropping_system,enteredpersonel= SystemUser.objects.get(user=request.user))
            
            elif crop1_management_practice =="No mulching":
               plotcrop_instance = PlotCrop(farm=Farm.objects.get(farmID=farmer),plotID=Plot.objects.get(plotID=plotID,farm=Farm.objects.get(farmID=farmer)),crop1=crop1,crop1_variety=crop_variety1,crop1_varietytype=variety_type1,crop1_planting_method=crop1_planting_method,\
                                         crop1_rootdepth=crop1_rootdepth,crop1_management_practice=crop1_management_practice, \
                                         cropping_system=cropping_system,enteredpersonel= SystemUser.objects.get(user=request.user))
            plotcrop_instance.save()
            '''
            plotcrop_instance = PlotCrop(cropping_system=cropping_system,farm=Farm.objects.get(farmID=farmer),plotID=Plot.objects.get(plotID=plotID,farm=Farm.objects.get(farmID=farmer)),crop1=crop1,crop1_variety=crop_variety1,crop1_varietytype=variety_type1,crop1_planting_method=crop1_planting_method)
            plotcrop_instance.save()
            '''
            
         elif cropping_system == 'Intercropping':
            try:Crop.objects.get(name=crop1)
            except Crop.DoesNotExist:
               crop_instance = Crop(name=crop1)
               crop_instance.save()
            finally:crop1=Crop.objects.get(name=crop1)
            try:Crop.objects.get(name=crop2)
            except Crop.DoesNotExist:
               crop_instance = Crop(name=crop2)
               crop_instance.save()
            finally:crop2=Crop.objects.get(name=crop2)

            '''
            if management_practice =="Mulching":
               plotmanagement_instance = PlotManagement(cropping_system=cropping_system,management_practice=management_practice,mulching_type=mulching_type,mulching_quantity=mulching_quantity,date=seasonstart,farm=Farm.objects.get(farmID=farmer),plotID=Plot.objects.get(plotID=plotID,farm=Farm.objects.get(farmID=farmer)),elevation=elevation,plot_size=fieldsize,seasonstart=seasonstart,rootdepth=rootzone_depth,water_application=water_application,enteredpersonel= SystemUser.objects.get(user=request.user))
            elif management_practice =="No mulching":
               plotmanagement_instance = PlotManagement(cropping_system=cropping_system,management_practice=management_practice,date=seasonstart,farm=Farm.objects.get(farmID=farmer),plotID=Plot.objects.get(plotID=plotID,farm=Farm.objects.get(farmID=farmer)),elevation=elevation,plot_size=fieldsize,seasonstart=seasonstart,rootdepth=rootzone_depth,water_application=water_application,enteredpersonel= SystemUser.objects.get(user=request.user))         
            plotmanagement_instance.save()
            plotmanagement_instance.crop.add(crop1,crop2)
            '''
            
            plotmanagement_instance = PlotManagement(cropping_system=cropping_system,date=seasonstart,farm=Farm.objects.get(farmID=farmer),plotID=Plot.objects.get(plotID=plotID,farm=Farm.objects.get(farmID=farmer)),elevation=elevation,plot_size=fieldsize,seasonstart=seasonstart,water_application=water_application,enteredpersonel= SystemUser.objects.get(user=request.user))
            plotmanagement_instance.save()
            plotmanagement_instance.crop.add(crop1,crop2)
            
            '''
            plotcrop_instance = PlotCrop(cropping_system=cropping_system,farm=Farm.objects.get(farmID=farmer),plotID=Plot.objects.get(plotID=plotID,farm=Farm.objects.get(farmID=farmer)),crop1=crop1,crop1_variety=crop_variety1,crop1_varietytype=variety_type1,crop1_planting_method=crop1_planting_method,crop2=crop2,crop2_variety=crop_variety2,crop2_varietytype=variety_type2,crop2_planting_method=crop2_planting_method)
            plotcrop_instance.save()
            '''
            
            if crop1_management_practice =="Mulching" and crop2_management_practice =="Mulching":
               plotcrop_instance = PlotCrop(farm=Farm.objects.get(farmID=farmer),plotID=Plot.objects.get(plotID=plotID,farm=Farm.objects.get(farmID=farmer)),\
                                            crop1=crop1,crop1_variety=crop_variety1,crop1_varietytype=variety_type1,crop1_planting_method=crop1_planting_method,crop1_rootdepth=crop1_rootdepth,crop1_management_practice=crop1_management_practice,crop1_mulching_type=crop1_mulching_type,crop1_mulching_quantity=crop1_mulching_quantity, \
                                            crop2=crop2,crop2_variety=crop_variety2,crop2_varietytype=variety_type2,crop2_planting_method=crop2_planting_method,crop2_rootdepth=crop2_rootdepth,crop2_management_practice=crop2_management_practice,crop2_mulching_type=crop2_mulching_type,crop2_mulching_quantity=crop2_mulching_quantity, \
                                            cropping_system=cropping_system,enteredpersonel= SystemUser.objects.get(user=request.user))
            
            elif crop1_management_practice =="No mulching" and crop2_management_practice =="Mulching":
               plotcrop_instance = PlotCrop(farm=Farm.objects.get(farmID=farmer),plotID=Plot.objects.get(plotID=plotID,farm=Farm.objects.get(farmID=farmer)),\
                                            crop1=crop1,crop1_variety=crop_variety1,crop1_varietytype=variety_type1,crop1_planting_method=crop1_planting_method,crop1_rootdepth=crop1_rootdepth,crop1_management_practice=crop1_management_practice, \
                                            crop2=crop2,crop2_variety=crop_variety2,crop2_varietytype=variety_type2,crop2_planting_method=crop2_planting_method,crop2_rootdepth=crop2_rootdepth,crop2_management_practice=crop2_management_practice,crop2_mulching_type=crop2_mulching_type,crop2_mulching_quantity=crop2_mulching_quantity, \
                                            cropping_system=cropping_system,enteredpersonel= SystemUser.objects.get(user=request.user))
               
            elif crop1_management_practice =="Mulching" and crop2_management_practice =="No mulching":
               plotcrop_instance = PlotCrop(farm=Farm.objects.get(farmID=farmer),plotID=Plot.objects.get(plotID=plotID,farm=Farm.objects.get(farmID=farmer)),\
                                            crop1=crop1,crop1_variety=crop_variety1,crop1_varietytype=variety_type1,crop1_planting_method=crop1_planting_method,crop1_rootdepth=crop1_rootdepth,crop1_management_practice=crop1_management_practice,crop1_mulching_type=crop1_mulching_type,crop1_mulching_quantity=crop1_mulching_quantity, \
                                            crop2=crop2,crop2_variety=crop_variety2,crop2_varietytype=variety_type2,crop2_planting_method=crop2_planting_method,crop2_rootdepth=crop2_rootdepth,crop2_management_practice=crop2_management_practice, \
                                            cropping_system=cropping_system,enteredpersonel= SystemUser.objects.get(user=request.user))
               
            elif crop1_management_practice =="No mulching" and crop2_management_practice =="No mulching":
               plotcrop_instance = PlotCrop(farm=Farm.objects.get(farmID=farmer),plotID=Plot.objects.get(plotID=plotID,farm=Farm.objects.get(farmID=farmer)),\
                                            crop1=crop1,crop1_variety=crop_variety1,crop1_varietytype=variety_type1,crop1_planting_method=crop1_planting_method,crop1_rootdepth=crop1_rootdepth,crop1_management_practice=crop1_management_practice, \
                                            crop2=crop2,crop2_variety=crop_variety2,crop2_varietytype=variety_type2,crop2_planting_method=crop2_planting_method,crop2_rootdepth=crop2_rootdepth,crop2_management_practice=crop2_management_practice, \
                                            cropping_system=cropping_system,enteredpersonel= SystemUser.objects.get(user=request.user))
            plotcrop_instance.save()
            
         if water_management_method =='WFD WUA' or water_management_method=='WFD':
            watermanagement_instance = WaterManagement(farm=Farm.objects.get(farmID=farmer),plotID=Plot.objects.get(plotID=plotID,farm=Farm.objects.get(farmID=farmer)),water_management_method=water_management_method,yellow_depth_detector=WFD_yellow_depth,red_depth_detector=WFD_red_depth)#,rods_length)
         elif water_management_method =='TDR(soil moisture)':
            watermanagement_instance = WaterManagement(farm=Farm.objects.get(farmID=farmer),plotID=Plot.objects.get(plotID=plotID,farm=Farm.objects.get(farmID=farmer)),water_management_method=water_management_method,rods_length=TDR_length)
         else:
            watermanagement_instance = WaterManagement(farm=Farm.objects.get(farmID=farmer),plotID=Plot.objects.get(plotID=plotID,farm=Farm.objects.get(farmID=farmer)),water_management_method=water_management_method)

         bedplot_instance = BedPlot(farm=Farm.objects.get(farmID=farmer),plotID=Plot.objects.get(plotID=plotID,farm=Farm.objects.get(farmID=farmer)),length=bed_length,width=bed_width,numbers=bednumber)
         furrow_instance = Furrow(farm=Farm.objects.get(farmID=farmer),plotID=Plot.objects.get(plotID=plotID,farm=Farm.objects.get(farmID=farmer)),length=furrow_length,width=furrow_width,numbers=nfurrow)
         
         watermanagement_instance.save()
         bedplot_instance.save()
         furrow_instance.save()
         
         message='saved'
         return render(request,'iwmiproject/saved.html',locals())
      else:
         user_instance = SystemUser.objects.get(user=request.user)
         if user_instance.role == 'RA' or user_instance.role == 'ST':user_village = user_instance.village
         elif user_instance.role == 'ALL':user_country = user_instance.country
         elif user_instance.role == 'RS':researcher = user_instance.country
         
         currency = pick_currency(user_instance)
         return render(request,'iwmiproject/farmerinfo.html',locals())
   else:
      user_instance = SystemUser.objects.get(user=request.user)
      if user_instance.role == 'RA' or user_instance.role == 'ST':user_village = user_instance.village
      elif user_instance.role == 'ALL':user_country = user_instance.country
      elif user_instance.role == 'RS':researcher = user_instance.country
      
      currency = pick_currency(user_instance)
      farminfoform = FarmInfoForm()
      return render(request,'iwmiproject/farmerinfo.html',locals())
      


def fertilizerapplication(request):
   if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('signup:login'))
      
   if request.method == 'POST': 
      fertilizerapplicationform = FertilizerApplicationForm(request.POST)
      
      if fertilizerapplicationform.is_valid():
         plot = fertilizerapplicationform.cleaned_data['plot']
         farm = fertilizerapplicationform.cleaned_data['farm']
         #nursery = fertilizerapplicationform.cleaned_data['nursery']
         #choice = fertilizerapplicationform.cleaned_data['choice']
         date = fertilizerapplicationform.cleaned_data['date']
         fertilizer = fertilizerapplicationform.cleaned_data['fertilizer']
         compost_kind = fertilizerapplicationform.cleaned_data['compost_kind']
         fertilizer_management = fertilizerapplicationform.cleaned_data['fertilizer_management'] 
         quantity_kg = fertilizerapplicationform.cleaned_data['quantity_kg']
         crop_stage = fertilizerapplicationform.cleaned_data['crop_stage']
         #nitrogen = fertilizerapplicationform.cleaned_data['nitrogen']
         #phosphorus = fertilizerapplicationform.cleaned_data['phosphorus']
         #potassium = fertilizerapplicationform.cleaned_data['potassium']
         #sulphur = fertilizerapplicationform.cleaned_data['sulphur']
         #organic_matter = fertilizerapplicationform.cleaned_data['organic_matter']
         cost = fertilizerapplicationform.cleaned_data['cost']
         labour = fertilizerapplicationform.cleaned_data['labour']
         hired_female_number = fertilizerapplicationform.cleaned_data['hired_female_number']
         hired_male_number = fertilizerapplicationform.cleaned_data['hired_male_number']
         family_female_number = fertilizerapplicationform.cleaned_data['family_female_number']
         family_male_number = fertilizerapplicationform.cleaned_data['family_male_number']
         wage = fertilizerapplicationform.cleaned_data['wage']
         #currency = fertilizerapplicationform.cleaned_data['currency']
         #labour_time_taken = fertilizerapplicationform.cleaned_data['labour_time_taken']
         
         family_female_time = fertilizerapplicationform.cleaned_data['family_female_time']
         family_male_time = fertilizerapplicationform.cleaned_data['family_male_time']
         hired_female_time = fertilizerapplicationform.cleaned_data['hired_female_time']
         hired_male_time = fertilizerapplicationform.cleaned_data['hired_male_time']
         
         user_instance = SystemUser.objects.get(user=request.user)
         currency = pick_currency(user_instance)
         #family_female_time=family_female_time,family_male_time=family_male_time
         #hired_female_time=hired_female_time,hired_male_time=hired_male_time
         #family_female_time=family_female_time,family_male_time=family_male_time,hired_female_time=hired_female_time,hired_male_time=hired_male_time
         
         '''
         if choice =='Nursery':
            #nursery_instance = Nursery.objects.get(farm=farm)
            try:
               FertilizerManagement.objects.get(date=date,farm=farm,nurseryID=nursery,fertilizer=fertilizer)
            except FertilizerManagement.DoesNotExist:
               try:
                  Fertilizer.objects.get(name=fertilizer)
               except Fertilizer.DoesNotExist:
                  fertilizer_instance = Fertilizer(name=fertilizer)
                  fertilizer_instance.save()
               FertilizerManagement_instance = FertilizerManagement(date=date,farm=farm,nurseryID=nursery,crop_stage=crop_stage,fertilizer=Fertilizer.objects.get(name=fertilizer),quantity_in_kg=quantity_kg,fertilizer_management=fertilizer_management,nitrogen=nitrogen,phosphorus=phosphorus,potassium=potassium,sulphur=sulphur,organic_matter=organic_matter,price=cost,price_unit=currency,enteredpersonel=SystemUser.objects.get(user=request.user))
               FertilizerManagement_instance.save()
            else:
               message = 'Looks like information already exist'
               user_instance = SystemUser.objects.get(user=request.user)
               if user_instance.role == 'RA' or user_instance.role == 'ST':user_village = user_instance.village
               elif user_instance.role == 'ALL':user_country = user_instance.country
               elif user_instance.role == 'RS':researcher = user_instance.country
               return render (request,'iwmiproject/fertilizerapplication.html',locals())
               
         #elif choice == 'Field':
         '''
         try:
            FertilizerManagement.objects.get(date=date,farm=farm,plotID=Plot.objects.get(plotID=plot,farm=farm))#,fertilizer=fertilizer)
         except FertilizerManagement.DoesNotExist:
            try:
               Fertilizer.objects.get(name=fertilizer)
            except Fertilizer.DoesNotExist:
               fertilizer_instance = Fertilizer(name=fertilizer)
               fertilizer_instance.save()
            if fertilizer =='Compost':
               FertilizerManagement_instance = FertilizerManagement(date=date,farm=farm,plotID=Plot.objects.get(plotID=plot,farm=farm),crop_stage=crop_stage,fertilizer=Fertilizer.objects.get(name=fertilizer),compost_kind=compost_kind,quantity_in_kg=quantity_kg,fertilizer_management=fertilizer_management,price=cost,price_unit=currency,enteredpersonel=SystemUser.objects.get(user=request.user))
            else:
               FertilizerManagement_instance = FertilizerManagement(date=date,farm=farm,plotID=Plot.objects.get(plotID=plot,farm=farm),crop_stage=crop_stage,fertilizer=Fertilizer.objects.get(name=fertilizer),quantity_in_kg=quantity_kg,fertilizer_management=fertilizer_management,price=cost,price_unit=currency,enteredpersonel=SystemUser.objects.get(user=request.user))
            FertilizerManagement_instance.save()
         else:
            message = 'Looks like information already exist'
            user_instance = SystemUser.objects.get(user=request.user)
            currency = pick_currency(user_instance)
            if user_instance.role == 'RA' or user_instance.role == 'ST':user_village = user_instance.village
            elif user_instance.role == 'ALL':user_country = user_instance.country
            elif user_instance.role == 'RS':researcher = user_instance.country
            return render (request,'iwmiproject/fertilizerapplication.html',locals())
        
         if labour == 'Family':
            LabourManagament_instance = LabourManagament(date=date,family_female_time=family_female_time,family_male_time=family_male_time,farm=farm,areaID=plot,areadescription='Plot',labour=labour,family_female_number=family_female_number,family_male_number=family_male_number,activity='Fertilizer Application',wage=wage,price_unit=currency,enteredpersonel=SystemUser.objects.get(user=request.user))
         
         elif labour == 'Hired':
            LabourManagament_instance = LabourManagament(date=date,hired_female_time=hired_female_time,hired_male_time=hired_male_time,farm=farm,areaID=plot,areadescription='Plot',labour=labour,hired_female_number=hired_female_number,hired_male_number=hired_male_number,activity='Fertilizer Application',wage=wage,price_unit=currency,enteredpersonel=SystemUser.objects.get(user=request.user))
         
         elif labour == 'FamilyHired':
            LabourManagament_instance = LabourManagament(date=date,family_female_time=family_female_time,family_male_time=family_male_time,hired_female_time=hired_female_time,hired_male_time=hired_male_time,farm=farm,areaID=plot,areadescription='Plot',labour=labour,hired_female_number=hired_female_number,hired_male_number=hired_male_number,family_female_number=family_female_number,family_male_number=family_male_number,activity='Fertilizer Application',wage=wage,price_unit=currency,enteredpersonel=SystemUser.objects.get(user=request.user))

         LabourManagament_instance.save()
         message='saved'
         
         #user_instance = SystemUser.objects.get(user=request.user)
         #if user_instance.role == 'RA' or user_instance.role == 'ST':user_village = user_instance.village
         #elif user_instance.role == 'ALL':user_country = user_instance.country
         #return render (request,'iwmiproject/fertilizerapplication.html',locals())
         message='saved'
         return render(request,'iwmiproject/saved.html',locals())
        
      else:
         user_instance = SystemUser.objects.get(user=request.user)
         currency = pick_currency(user_instance)
         if user_instance.role == 'RA' or user_instance.role == 'ST':user_village = user_instance.village
         elif user_instance.role == 'ALL':user_country = user_instance.country
         elif user_instance.role == 'RS':researcher = user_instance.country
         context = {'fertilizerapplicationform':fertilizerapplicationform}
         return render (request,'iwmiproject/fertilizerapplication.html',locals())
      
   else:
      user_instance = SystemUser.objects.get(user=request.user)
      currency = pick_currency(user_instance)
      if user_instance.role == 'RA' or user_instance.role == 'ST':user_village = user_instance.village
      elif user_instance.role == 'ALL':user_country = user_instance.country
      elif user_instance.role == 'RS':researcher = user_instance.country
      fertilizerapplicationform = FertilizerApplicationForm()#initial={'hired_female_number':0,'hired_male_number':0,'family_female_number':0,'family_male_number':0},)
      return render (request,'iwmiproject/fertilizerapplication.html',locals())
   
   
   
def pesticideapplication(request):
   if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('signup:login'))
   print('**')
   if request.method == 'POST': 
      pesticideapplicationform = PesticideApplicationForm(request.POST)
        
      if pesticideapplicationform.is_valid():
         farm = pesticideapplicationform.cleaned_data['farm']
         plot = pesticideapplicationform.cleaned_data['plot']
         date = pesticideapplicationform.cleaned_data['date']
         pesticide = pesticideapplicationform.cleaned_data['pesticide']
         form = pesticideapplicationform.cleaned_data['form']
         water_volume = pesticideapplicationform.cleaned_data['water_volume']
         quantity_lt = pesticideapplicationform.cleaned_data['quantity_lt']
         quantity_kg = pesticideapplicationform.cleaned_data['quantity_kg']
         crop_stage = pesticideapplicationform.cleaned_data['crop_stage']
         cost = pesticideapplicationform.cleaned_data['cost']
         labour = pesticideapplicationform.cleaned_data['labour']
         hired_female_number = pesticideapplicationform.cleaned_data['hired_female_number']
         hired_male_number = pesticideapplicationform.cleaned_data['hired_male_number']
         family_female_number = pesticideapplicationform.cleaned_data['family_female_number']
         family_male_number = pesticideapplicationform.cleaned_data['family_male_number']
         wage = pesticideapplicationform.cleaned_data['wage']
         #currency = pesticideapplicationform.cleaned_data['currency']
         #labour_time_taken = pesticideapplicationform.cleaned_data['labour_time_taken']
         
         family_female_time = pesticideapplicationform.cleaned_data['family_female_time']
         family_male_time = pesticideapplicationform.cleaned_data['family_male_time']
         hired_female_time = pesticideapplicationform.cleaned_data['hired_female_time']
         hired_male_time = pesticideapplicationform.cleaned_data['hired_male_time']
         
         #family_female_time=family_female_time,family_male_time=family_male_time
         #hired_female_time=hired_female_time,hired_male_time=hired_male_time
         #family_female_time=family_female_time,family_male_time=family_male_time,hired_female_time=hired_female_time,hired_male_time=hired_male_time
         user_instance = SystemUser.objects.get(user=request.user)
         currency = pick_currency(user_instance)
         
         
         try:
            Pesticide.objects.get(name=pesticide)
         except Pesticide.DoesNotExist:
            Pesticide_isntance = Pesticide(name=pesticide)
            Pesticide_isntance.save()
         finally:
            pesticide = Pesticide.objects.get(name=pesticide)
         try:
            PesticideManagement.objects.get(date=date,farm=farm,plotID=Plot.objects.get(plotID=plot,farm=farm),form=form,name=Pesticide.objects.get(name=pesticide))
         except PesticideManagement.DoesNotExist:
            if form=='Liquid':
               pesticidemanagement_instance = PesticideManagement(date=date,farm=farm,plotID=Plot.objects.get(plotID=plot,farm=farm),name=pesticide,crop_stage=crop_stage,form=form,water_volume=water_volume,quantity_in_litre=quantity_lt,price=cost,price_unit=currency,enteredpersonel=SystemUser.objects.get(user=request.user))
            elif form=='Solid':
               pesticidemanagement_instance = PesticideManagement(date=date,farm=farm,plotID=Plot.objects.get(plotID=plot,farm=farm),name=pesticide,crop_stage=crop_stage,form=form,quantity_in_kg=quantity_kg,price=cost,price_unit=currency,enteredpersonel=SystemUser.objects.get(user=request.user))
            pesticidemanagement_instance.save()
         else:
            message = 'Looks like information already exist'
            user_instance = SystemUser.objects.get(user=request.user)
            currency = pick_currency(user_instance)
            if user_instance.role == 'RA' or user_instance.role == 'ST':user_village = user_instance.village
            elif user_instance.role == 'ALL':user_country = user_instance.country
            elif user_instance.role == 'RS':researcher = user_instance.country
            return render (request,'iwmiproject/pesticideapplication.html',locals())
         if labour == 'Family':
            LabourManagament_instance = LabourManagament(date=date,family_female_time=family_female_time,family_male_time=family_male_time,farm=farm,areaID=plot,areadescription='Plot',labour=labour,family_female_number=family_female_number,family_male_number=family_male_number,activity='Pesticide Application',wage=wage,price_unit=currency,enteredpersonel=SystemUser.objects.get(user=request.user))
         
         elif labour == 'Hired':
            LabourManagament_instance = LabourManagament(date=date,hired_female_time=hired_female_time,hired_male_time=hired_male_time,farm=farm,areaID=plot,areadescription='Plot',labour=labour,hired_female_number=hired_female_number,hired_male_number=hired_male_number,activity='Pesticide Application',wage=wage,price_unit=currency,enteredpersonel=SystemUser.objects.get(user=request.user))
         
         elif labour == 'FamilyHired':
            LabourManagament_instance = LabourManagament(date=date,family_female_time=family_female_time,family_male_time=family_male_time,hired_female_time=hired_female_time,hired_male_time=hired_male_time,farm=farm,areaID=plot,areadescription='Plot',labour=labour,hired_female_number=hired_female_number,hired_male_number=hired_male_number,family_female_number=family_female_number,family_male_number=family_male_number,activity='Pesticide Application',wage=wage,price_unit=currency,enteredpersonel=SystemUser.objects.get(user=request.user))
         
         LabourManagament_instance.save()
         #user_instance = SystemUser.objects.get(user=request.user)
         #if user_instance.role == 'RA' or user_instance.role == 'ST':user_village = user_instance.village
         #elif user_instance.role == 'ALL':user_country = user_instance.country
         #return render(request,'iwmiproject/pesticideapplication.html',locals())
         message='saved'
         return render(request,'iwmiproject/saved.html',locals())
        
      else:
         user_instance = SystemUser.objects.get(user=request.user)
         currency = pick_currency(user_instance)
         if user_instance.role == 'RA' or user_instance.role == 'ST':user_village = user_instance.village
         elif user_instance.role == 'ALL':user_country = user_instance.country
         elif user_instance.role == 'RS':researcher = user_instance.country
         return render(request,'iwmiproject/pesticideapplication.html',locals())
      
   else:
      user_instance = SystemUser.objects.get(user=request.user)
      currency = pick_currency(user_instance)
      if user_instance.role == 'RA' or user_instance.role == 'ST':user_village = user_instance.village
      elif user_instance.role == 'ALL':user_country = user_instance.country
      elif user_instance.role == 'RS':researcher = user_instance.country
      pesticideapplicationform = PesticideApplicationForm()
      return render(request,'iwmiproject/pesticideapplication.html',locals())
   
   
def waterliftingcalibration(request):
   if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('signup:login'))
      
   if request.method == 'POST': 
      waterliftingcalibrationform = WaterLiftingCalibrationForm(request.POST)
      
      if waterliftingcalibrationform.is_valid():
         farm = waterliftingcalibrationform.cleaned_data['farm']
         #plot = waterliftingcalibrationform.cleaned_data['plot']
         date = waterliftingcalibrationform.cleaned_data['date']
         waterlevel = waterliftingcalibrationform.cleaned_data['waterlevel']
         technology = waterliftingcalibrationform.cleaned_data['technology']
         bucketvolume = waterliftingcalibrationform.cleaned_data['bucketvolume']
         start_time= waterliftingcalibrationform.cleaned_data['start_time']
         end_time = waterliftingcalibrationform.cleaned_data['end_time']
         total_time = waterliftingcalibrationform.cleaned_data['total_time']
         discharge = waterliftingcalibrationform.cleaned_data['discharge']
         gender = waterliftingcalibrationform.cleaned_data['gender']
         age_group = waterliftingcalibrationform.cleaned_data['age_group']
         #total_time = timedifference(datetime.combine(date.today(), end_time) - datetime.combine(date.today(), start_time))
    
         try:
            WaterliftingCalibrations.objects.get(farm=farm,date=date,start_time=start_time,end_time=end_time)
         except WaterliftingCalibrations.DoesNotExist:
            events =[i.event for i in WaterliftingCalibrations.objects.all().filter(farm=farm)]
            if not events:current_event = 1
            else:current_event = max(events) + 1
            waterliftingcalibration_instance = WaterliftingCalibrations(farm=farm,date=date,technology=Technology.objects.get(name=technology),waterlevel=waterlevel,gender=gender,age_group=age_group,event=current_event,start_time=start_time,end_time=end_time,total_time=total_time,bucket_volume=bucketvolume,discharge=discharge,enteredpersonel=SystemUser.objects.get(user=request.user))
            waterliftingcalibration_instance.save()
         else:
            message = "Looks like the event already exist"
            user_instance = SystemUser.objects.get(user=request.user)
            if user_instance.role == 'RA' or user_instance.role == 'ST':user_village = user_instance.village
            elif user_instance.role == 'ALL':user_country = user_instance.country
            elif user_instance.role == 'RS':researcher = user_instance.country
            return render(request,'iwmiproject/waterliftingcalibration.html',locals())
         #message='saved'
         #user_instance = SystemUser.objects.get(user=request.user)
         #if user_instance.role == 'RA' or user_instance.role == 'ST':user_village = user_instance.village
         #elif user_instance.role == 'ALL':user_country = user_instance.country
         #return render(request,'iwmiproject/waterliftingcalibration.html',locals())
         message='saved'
         return render(request,'iwmiproject/saved.html',locals())
        
      else:
         user_instance = SystemUser.objects.get(user=request.user)
         if user_instance.role == 'RA' or user_instance.role == 'ST':user_village = user_instance.village
         elif user_instance.role == 'ALL':user_country = user_instance.country
         elif user_instance.role == 'RS':researcher = user_instance.country
         context = {'waterliftingcalibrationform':waterliftingcalibrationform}
         return render_to_response('iwmiproject/waterliftingcalibration.html',context,context_instance=RequestContext(request))
      
   else:
      user_instance = SystemUser.objects.get(user=request.user)
      if user_instance.role == 'RA' or user_instance.role == 'ST':user_village = user_instance.village
      elif user_instance.role == 'ALL':user_country = user_instance.country
      elif user_instance.role == 'RS':researcher = user_instance.country
      waterliftingcalibrationform = WaterLiftingCalibrationForm()
      return render(request,'iwmiproject/waterliftingcalibration.html',locals())
   

def applicationcalibration(request):
   
   if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('signup:login'))
   if request.method == 'POST': 
      applicationcalibrationform = ApplicationCalibrationForm(request.POST)
      print('before')
      if applicationcalibrationform.is_valid():
         farm = applicationcalibrationform.cleaned_data['farm']
         date = applicationcalibrationform.cleaned_data['date']
         plot = applicationcalibrationform.cleaned_data['plot']
         water_application = applicationcalibrationform.cleaned_data['water_application']
         bucketdiameter = applicationcalibrationform.cleaned_data['bucketdiameter']
         bucketvolume = applicationcalibrationform.cleaned_data['bucketvolume']
         start_time= applicationcalibrationform.cleaned_data['start_time']
         end_time = applicationcalibrationform.cleaned_data['end_time']
         total_time = applicationcalibrationform.cleaned_data['total_time']
         discharge = applicationcalibrationform.cleaned_data['discharge']
         bucketnumbers = applicationcalibrationform.cleaned_data['bucketnumbers']
         waterheight = applicationcalibrationform.cleaned_data['waterheight']
         topfurrowwidth = applicationcalibrationform.cleaned_data['topfurrowwidth']
         buttonfurrowwidth = applicationcalibrationform.cleaned_data['buttonfurrowwidth']
         wetteddiameteraroundplant = applicationcalibrationform.cleaned_data['wetteddiameteraroundplant']
         irrigate_whole_or_per_plant = applicationcalibrationform.cleaned_data['irrigate_whole_or_per_plant']
         field_efficiency = applicationcalibrationform.cleaned_data['field_efficiency']
         conveyance_efficiency = applicationcalibrationform.cleaned_data['conveyance_efficiency']
         dripline_numbers = applicationcalibrationform.cleaned_data['dripline_numbers']
         dripline_length = applicationcalibrationform.cleaned_data['dripline_length']
         dripline_spacing = applicationcalibrationform.cleaned_data['dripline_spacing']
         emitter_spacing = applicationcalibrationform.cleaned_data['emitter_spacing']
         driptank_volume = applicationcalibrationform.cleaned_data['driptank_volume']
         calibrationcup_volume = applicationcalibrationform.cleaned_data['calibrationcup_volume']
         emitter_wetted_diameter = applicationcalibrationform.cleaned_data['emitter_wetted_diameter']
         calibration_method = applicationcalibrationform.cleaned_data['calibration_method']
         calibration_cup_time = applicationcalibrationform.cleaned_data['calibration_cup_time']
         tankvolume = applicationcalibrationform.cleaned_data['tankvolume']
         #tanknumber = applicationcalibrationform.cleaned_data['tanknumber']
         #tankdiameter = applicationcalibrationform.cleaned_data['tankdiameter']
         print('after')
         fieldsize = PlotManagement.objects.get(plotID=Plot.objects.get(plotID=plot,farm=farm)).plot_size
         if water_application == 'NONE':
            message ="Please click the link ' http://127.0.0.1:8000/iwmiproject/farminfo' to add info for plot {} that's belong to {}".format(request.user)
            return render(request,'iwmiproject/applicationcalibration.html',locals())
         #totalnumberofplanttransplanted=2
         elif water_application =="Drip":
            if calibration_method =='Calibration cup':
               try:
                  ApplicationCalibration.objects.get(farm=farm,date=date,plot=(Plot.objects.get(plotID=plot,farm=farm)))
               except ApplicationCalibration.DoesNotExist:
                  applicationcalibration_instance = ApplicationCalibration(farm=farm,date=date,plot=Plot.objects.get(plotID=plot,farm=farm),water_application=water_application,start_time=start_time,end_time=end_time,total_time=total_time,irrigate_whole_or_per_plant=irrigate_whole_or_per_plant,dripline_length=dripline_length,dripline_spacing=dripline_spacing,calibration_method=calibration_method,calibration_cup_time=calibration_cup_time,dripline_numbers=dripline_numbers,emitter_spacing=emitter_spacing,emitter_wetted_diameter=emitter_wetted_diameter,driptank_volume=driptank_volume,calibrationcup_volume=calibrationcup_volume,application_rate=discharge,enteredpersonel=SystemUser.objects.get(user=request.user))
                  applicationcalibration_instance.save()
               else:
                  message = "Looks like the event already exist"
                  user_instance = SystemUser.objects.get(user=request.user)
                  if user_instance.role == 'RA' or user_instance.role == 'ST':user_village = user_instance.village
                  #elif user_instance.role == 'RS':researcher = user_instance.country
                  elif user_instance.role == 'ALL':user_country = user_instance.country
                  elif user_instance.role == 'RS':researcher = user_instance.country
                  return render(request,'iwmiproject/applicationcalibration.html',locals())
            else:
               try:
                  ApplicationCalibration.objects.get(farm=farm,date=date,plot=(Plot.objects.get(plotID=plot,farm=farm)))
               except ApplicationCalibration.DoesNotExist:
                  applicationcalibration_instance = ApplicationCalibration(farm=farm,date=date,plot=Plot.objects.get(plotID=plot,farm=farm),water_application=water_application,start_time=start_time,end_time=end_time,total_time=total_time,irrigate_whole_or_per_plant=irrigate_whole_or_per_plant,dripline_length=dripline_length,dripline_spacing=dripline_spacing,calibration_method=calibration_method,dripline_numbers=dripline_numbers,emitter_spacing=emitter_spacing,emitter_wetted_diameter=emitter_wetted_diameter,driptank_volume=driptank_volume,calibrationcup_volume=calibrationcup_volume,application_rate=discharge,enteredpersonel=SystemUser.objects.get(user=request.user))
                  applicationcalibration_instance.save()
               else:
                  message = "Looks like the event already exist"
                  user_instance = SystemUser.objects.get(user=request.user)
                  if user_instance.role == 'RA' or user_instance.role == 'ST':user_village = user_instance.village
                  #elif user_instance.role == 'RS':researcher = user_instance.country
                  elif user_instance.role == 'ALL':user_country = user_instance.country
                  elif user_instance.role == 'RS':researcher = user_instance.country
                  return render(request,'iwmiproject/applicationcalibration.html',locals())
                  
         
         elif water_application =="Tank and hose":
            try:
               ApplicationCalibration.objects.get(farm=farm,date=date,plot=(Plot.objects.get(plotID=plot,farm=farm)))
            except ApplicationCalibration.DoesNotExist:
               applicationcalibration_instance = ApplicationCalibration(farm=farm,date=date,plot=Plot.objects.get(plotID=plot,farm=farm),water_application=water_application,start_time=start_time,end_time=end_time,total_time=total_time,bucketvolume=tankvolume,wetteddiameteraroundplant=wetteddiameteraroundplant,application_rate=discharge,enteredpersonel=SystemUser.objects.get(user=request.user))
               applicationcalibration_instance.save()
            else:
               message = "Looks like the event already exist"
               user_instance = SystemUser.objects.get(user=request.user)
               if user_instance.role == 'RA' or user_instance.role == 'ST':user_village = user_instance.village
               #elif user_instance.role == 'RS':researcher = user_instance.country
               elif user_instance.role == 'ALL':user_country = user_instance.country
               elif user_instance.role == 'RS':researcher = user_instance.country
               return render(request,'iwmiproject/applicationcalibration.html',locals())
            
         elif water_application =="Sprinkler":
            try:
               ApplicationCalibration.objects.get(farm=farm,date=date,plot=(Plot.objects.get(plotID=plot,farm=farm)))
            except ApplicationCalibration.DoesNotExist:
               applicationcalibration_instance = ApplicationCalibration(farm=farm,date=date,plot=Plot.objects.get(plotID=plot,farm=farm),water_application=water_application,start_time=start_time,end_time=end_time,total_time=total_time,bucketvolume=bucketvolume,bucketnumbers=bucketnumbers,bucketdiameter=bucketdiameter,application_rate=discharge,enteredpersonel=SystemUser.objects.get(user=request.user))
               applicationcalibration_instance.save()
            else:
               message = "Looks like the event already exist"
               user_instance = SystemUser.objects.get(user=request.user)
               if user_instance.role == 'RA' or user_instance.role == 'ST':user_village = user_instance.village
               #elif user_instance.role == 'RS':researcher = user_instance.country
               elif user_instance.role == 'ALL':user_country = user_instance.country
               elif user_instance.role == 'RS':researcher = user_instance.country
               return render(request,'iwmiproject/applicationcalibration.html',locals())
            
         elif water_application =="Furrow/bed":
            try:
               ApplicationCalibration.objects.get(farm=farm,date=date,plot=(Plot.objects.get(plotID=plot,farm=farm)))
            except ApplicationCalibration.DoesNotExist:
               applicationcalibration_instance = ApplicationCalibration(farm=farm,date=date,plot=Plot.objects.get(plotID=plot,farm=farm),water_application=water_application,buttonfurrowwidth=buttonfurrowwidth,topfurrowwidth=topfurrowwidth,waterheight=waterheight,application_rate=discharge,field_efficiency=field_efficiency,conveyance_efficiency=conveyance_efficiency,enteredpersonel=SystemUser.objects.get(user=request.user))
               applicationcalibration_instance.save()
            else:
               message = "Looks like the event already exist"
               user_instance = SystemUser.objects.get(user=request.user)
               if user_instance.role == 'RA' or user_instance.role == 'ST':user_village = user_instance.village
               #elif user_instance.role == 'RS':researcher = user_instance.country
               elif user_instance.role == 'ALL':user_country = user_instance.country
               elif user_instance.role == 'RS':researcher = user_instance.country
               return render(request,'iwmiproject/applicationcalibration.html',locals())

         message='saved'
         return render(request,'iwmiproject/saved.html',locals())
        
      else:
         user_instance = SystemUser.objects.get(user=request.user)
         if user_instance.role == 'RA' or user_instance.role == 'ST':user_village = user_instance.village
         elif user_instance.role == 'ALL':user_country = user_instance.country
         elif user_instance.role == 'RS':researcher = user_instance.country
         return render(request,'iwmiproject/applicationcalibration.html',locals())
   else:
      user_instance = SystemUser.objects.get(user=request.user)
      if user_instance.role == 'RA' or user_instance.role == 'ST':user_village = user_instance.village
      elif user_instance.role == 'ALL':user_country = user_instance.country
      elif user_instance.role == 'RS':researcher = user_instance.country
      applicationcalibrationform = ApplicationCalibrationForm()
      return render(request,'iwmiproject/applicationcalibration.html',locals())
   
   
def farmirrigation(request):
   if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('signup:login'))
      
   if request.method == 'POST': 
      farmirrigationform = FarmIrrigationForm(request.POST)
      print('**********')
      if farmirrigationform.is_valid():
         
         date = farmirrigationform.cleaned_data['date']
         farm = farmirrigationform.cleaned_data['farm']
         plot = farmirrigationform.cleaned_data['plot']
         start_time = farmirrigationform.cleaned_data['start_time']
         end_time  = farmirrigationform.cleaned_data['end_time']         
         total_time = farmirrigationform.cleaned_data['total_time']
         service_provider = farmirrigationform.cleaned_data['service_provider']
         '''
         quantification_method = farmirrigationform.cleaned_data['quantification_method']
         flume_location  = farmirrigationform.cleaned_data['flume_location']
         waterlevel1 = farmirrigationform.cleaned_data['waterlevel1']
         waterlevel2 = farmirrigationform.cleaned_data['waterlevel2']
         '''
         furrow_irr_time = farmirrigationform.cleaned_data['furrow_irr_time']
         nfurrorws_irrigated_once = farmirrigationform.cleaned_data['nfurrorws_irrigated_once']
         discharge = farmirrigationform.cleaned_data['discharge']
         '''
         standardvolume  = farmirrigationform.cleaned_data['standardvolume']
         quantity_of_units  = farmirrigationform.cleaned_data['quantity_of_units']
         '''
         yellow_WFD_before_irrigation = farmirrigationform.cleaned_data['yellow_WFD_before_irrigation']
         red_WFD_before_irrigation = farmirrigationform.cleaned_data['red_WFD_before_irrigation']
         yellow_WFD_time_after_irrigation  = farmirrigationform.cleaned_data['yellow_WFD_time_after_irrigation']
         red_WFD_time_after_irrigation = farmirrigationform.cleaned_data['red_WFD_time_after_irrigation']
         
         climate = farmirrigationform.cleaned_data['climate']
         
         fuel = farmirrigationform.cleaned_data['fuel']
         fuelcost = farmirrigationform.cleaned_data['fuelcost']
         #currency = farmirrigationform.cleaned_data['currency']
         amount_used = farmirrigationform.cleaned_data['amount_used']
         refilled_amount = farmirrigationform.cleaned_data['refilled_amount']
        
         water_application = farmirrigationform.cleaned_data['water_application']
         #total_time = timedifference(datetime.combine(date.today(), end_time) - datetime.combine(date.today(), start_time))
         '''
         wetteddiameteraroundplant = farmirrigationform.cleaned_data['wetteddiameteraroundplant']
         '''
         irrigate_whole_or_per_plant = farmirrigationform.cleaned_data['irrigate_whole_or_per_plant']
      
         buttonfurrowwidth = farmirrigationform.cleaned_data['buttonfurrowwidth']
         topfurrowwidth = farmirrigationform.cleaned_data['topfurrowwidth']
         waterheight = farmirrigationform.cleaned_data['waterheight']
         
         #bucketdiameter = farmirrigationform.cleaned_data['bucketdiameter']
         bucketvolume = farmirrigationform.cleaned_data['bucketvolume']
         bucketnumbers = farmirrigationform.cleaned_data['bucketnumbers']
         wetteddiameteraroundplant = farmirrigationform.cleaned_data['wetteddiameteraroundplant']
         
         field_efficiency = farmirrigationform.cleaned_data['field_efficiency']
         conveyance_efficiency = farmirrigationform.cleaned_data['conveyance_efficiency']
         
         #dripline_length = farmirrigationform.cleaned_data['dripline_length']
         #dripline_spacing = farmirrigationform.cleaned_data['dripline_spacing']
         #emitter_spacing = farmirrigationform.cleaned_data['emitter_spacing']
         driptank_volume = farmirrigationform.cleaned_data['driptank_volume']
         #calibrationcup_volume = farmirrigationform.cleaned_data['calibrationcup_volume']
         #emitter_wetted_diameter = farmirrigationform.cleaned_data['emitter_wetted_diameter']
         
         irrigation_depth = farmirrigationform.cleaned_data['irrigation_depth']
         water_management = farmirrigationform.cleaned_data['water_management']
         tanknumber = farmirrigationform.cleaned_data['tanknumber']
         
         gender = farmirrigationform.cleaned_data['gender']
         distance_from_water_source = farmirrigationform.cleaned_data['distance_from_water_source']
         time_to_fetch_water = farmirrigationform.cleaned_data['time_to_fetch_water']
         
         water_level_bf_filling = farmirrigationform.cleaned_data['water_level_bf_filling']
         water_level_aftr_filling = farmirrigationform.cleaned_data['water_level_aftr_filling']
         time_to_fill_water_tank = farmirrigationform.cleaned_data['time_to_fill_water_tank']
         
         technology = farmirrigationform.cleaned_data['technology']
        
         labour = farmirrigationform.cleaned_data['labour']
         hired_female_number = farmirrigationform.cleaned_data['hired_female_number']
         hired_male_number = farmirrigationform.cleaned_data['hired_male_number']
         family_female_number = farmirrigationform.cleaned_data['family_female_number']
         family_male_number = farmirrigationform.cleaned_data['family_male_number']
         wage = farmirrigationform.cleaned_data['wage']
         family_female_time = farmirrigationform.cleaned_data['family_female_time']
         family_male_time = farmirrigationform.cleaned_data['family_male_time']
         hired_female_time = farmirrigationform.cleaned_data['hired_female_time']
         hired_male_time = farmirrigationform.cleaned_data['hired_male_time']
         
         #total_irrigation = dicharge (or bucket or) * total_time
         user_instance = SystemUser.objects.get(user=request.user)
         currency = pick_currency(user_instance)
         
         if water_application == 'Bucket' or water_application == 'Watering Can':

            if water_management =='WFD':
               print('WFD')
               try:
                  PlotIrrigationEvent.objects.get(farm=farm,date=date,plotID=(Plot.objects.get(plotID=plot,farm=farm)))
               except PlotIrrigationEvent.DoesNotExist:
                  events =[i.irrigation_event for i in PlotIrrigationEvent.objects.all().filter(farm=farm,plotID=(Plot.objects.get(plotID=plot,farm=farm)))]
                  if not events:current_event = 1
                  else:current_event = max(events) + 1
                  if technology =='Petrol motorized pump':
                     if irrigate_whole_or_per_plant =='Perplant':
                        plotirrigationevent_instance = PlotIrrigationEvent(service_provider=service_provider,farm=farm,date=date,plotID=Plot.objects.get(plotID=plot,farm=farm),irrigated_depth=irrigation_depth,irrigate_whole_or_per_plant=irrigate_whole_or_per_plant,climate=climate,bucketvolume=bucketvolume,bucketnumbers=bucketnumbers,wetteddiameteraroundplant=wetteddiameteraroundplant,water_application=water_application,application_rate=discharge,irrigation_event=current_event,yellow_WFD_before_irrigation=yellow_WFD_before_irrigation,red_WFD_before_irrigation=red_WFD_before_irrigation,yellow_WFD_time_after_irrigation=yellow_WFD_time_after_irrigation,red_WFD_time_after_irrigation=red_WFD_time_after_irrigation,technology=Technology.objects.get(name=technology),fuel=fuel,fuelcost=fuelcost,currency=currency,amount_used=amount_used,refilled_amount=refilled_amount,enteredpersonel=SystemUser.objects.get(user=request.user))
                     elif irrigate_whole_or_per_plant =='Wholefield':
                        plotirrigationevent_instance = PlotIrrigationEvent(service_provider=service_provider,farm=farm,date=date,plotID=Plot.objects.get(plotID=plot,farm=farm),irrigated_depth=irrigation_depth,irrigate_whole_or_per_plant=irrigate_whole_or_per_plant,climate=climate,bucketvolume=bucketvolume,bucketnumbers=bucketnumbers,water_application=water_application,application_rate=discharge,irrigation_event=current_event,yellow_WFD_before_irrigation=yellow_WFD_before_irrigation,red_WFD_before_irrigation=red_WFD_before_irrigation,yellow_WFD_time_after_irrigation=yellow_WFD_time_after_irrigation,red_WFD_time_after_irrigation=red_WFD_time_after_irrigation,technology=Technology.objects.get(name=technology),fuel=fuel,fuelcost=fuelcost,currency=currency,amount_used=amount_used,refilled_amount=refilled_amount,enteredpersonel=SystemUser.objects.get(user=request.user))
                  elif technology =='Tractor mounted pump':
                     if irrigate_whole_or_per_plant =='Perplant':
                        plotirrigationevent_instance = PlotIrrigationEvent(service_provider=service_provider,farm=farm,date=date,plotID=Plot.objects.get(plotID=plot,farm=farm),irrigated_depth=irrigation_depth,irrigate_whole_or_per_plant=irrigate_whole_or_per_plant,climate=climate,bucketvolume=bucketvolume,bucketnumbers=bucketnumbers,wetteddiameteraroundplant=wetteddiameteraroundplant,water_application=water_application,application_rate=discharge,irrigation_event=current_event,yellow_WFD_before_irrigation=yellow_WFD_before_irrigation,red_WFD_before_irrigation=red_WFD_before_irrigation,yellow_WFD_time_after_irrigation=yellow_WFD_time_after_irrigation,red_WFD_time_after_irrigation=red_WFD_time_after_irrigation,technology=Technology.objects.get(name=technology),gender=gender,distance_from_water_source=distance_from_water_source,time_to_fetch_water=time_to_fetch_water,enteredpersonel=SystemUser.objects.get(user=request.user))
                     elif irrigate_whole_or_per_plant =='Wholefield':
                        plotirrigationevent_instance = PlotIrrigationEvent(service_provider=service_provider,farm=farm,date=date,plotID=Plot.objects.get(plotID=plot,farm=farm),irrigated_depth=irrigation_depth,irrigate_whole_or_per_plant=irrigate_whole_or_per_plant,climate=climate,bucketvolume=bucketvolume,bucketnumbers=bucketnumbers,water_application=water_application,application_rate=discharge,irrigation_event=current_event,yellow_WFD_before_irrigation=yellow_WFD_before_irrigation,red_WFD_before_irrigation=red_WFD_before_irrigation,yellow_WFD_time_after_irrigation=yellow_WFD_time_after_irrigation,red_WFD_time_after_irrigation=red_WFD_time_after_irrigation,technology=Technology.objects.get(name=technology),gender=gender,distance_from_water_source=distance_from_water_source,time_to_fetch_water=time_to_fetch_water,enteredpersonel=SystemUser.objects.get(user=request.user))
                  else:
                     if irrigate_whole_or_per_plant =='Perplant':
                        plotirrigationevent_instance = PlotIrrigationEvent(service_provider=service_provider,farm=farm,date=date,plotID=Plot.objects.get(plotID=plot,farm=farm),irrigated_depth=irrigation_depth,irrigate_whole_or_per_plant=irrigate_whole_or_per_plant,climate=climate,bucketvolume=bucketvolume,bucketnumbers=bucketnumbers,wetteddiameteraroundplant=wetteddiameteraroundplant,water_application=water_application,application_rate=discharge,irrigation_event=current_event,yellow_WFD_before_irrigation=yellow_WFD_before_irrigation,red_WFD_before_irrigation=red_WFD_before_irrigation,yellow_WFD_time_after_irrigation=yellow_WFD_time_after_irrigation,red_WFD_time_after_irrigation=red_WFD_time_after_irrigation,technology=Technology.objects.get(name=technology),enteredpersonel=SystemUser.objects.get(user=request.user))
                     elif irrigate_whole_or_per_plant =='Wholefield':
                        plotirrigationevent_instance = PlotIrrigationEvent(service_provider=service_provider,farm=farm,date=date,plotID=Plot.objects.get(plotID=plot,farm=farm),irrigated_depth=irrigation_depth,irrigate_whole_or_per_plant=irrigate_whole_or_per_plant,climate=climate,bucketvolume=bucketvolume,bucketnumbers=bucketnumbers,water_application=water_application,application_rate=discharge,irrigation_event=current_event,yellow_WFD_before_irrigation=yellow_WFD_before_irrigation,red_WFD_before_irrigation=red_WFD_before_irrigation,yellow_WFD_time_after_irrigation=yellow_WFD_time_after_irrigation,red_WFD_time_after_irrigation=red_WFD_time_after_irrigation,technology=Technology.objects.get(name=technology),enteredpersonel=SystemUser.objects.get(user=request.user))
                  plotirrigationevent_instance.save()
               else:
                  message = "Looks like the event already exist"
                  user_instance = SystemUser.objects.get(user=request.user)
                  if user_instance.role == 'RA' or user_instance.role == 'ST':user_village = user_instance.village
                  #elif user_instance.role == 'RS':researcher = user_instance.country
                  elif user_instance.role == 'ALL':user_country = user_instance.country
                  elif user_instance.role == 'RS':researcher = user_instance.country
                  return render(request,'iwmiproject/farmirrigation.html',locals())
            else:
               try:
                  #technology=Technology.objects.get(name=technology),fuel=fuel,fuelcost=fuelcost,currency=currency,amount_used=amount_used,refilled_amount=refilled_amount,
                  #technology=Technology.objects.get(name=technology),gender=gender,distance_from_water_source=distance_from_water_source,time_to_fetch_water=time_to_fetch_water,
                  #technology=Technology.objects.get(name=technology),
                  PlotIrrigationEvent.objects.get(farm=farm,date=date,plotID=(Plot.objects.get(plotID=plot,farm=farm)))
                  #PlotIrrigationEvent.objects.get(date=date,plotID=plot)
               except PlotIrrigationEvent.DoesNotExist:
                  events =[i.irrigation_event for i in PlotIrrigationEvent.objects.all().filter(farm=farm,plotID=(Plot.objects.get(plotID=plot,farm=farm)))]
                  if not events:current_event = 1
                  else:current_event = max(events) + 1
                  if technology =='Petrol motorized pump':
                     if irrigate_whole_or_per_plant =='Perplant':
                        plotirrigationevent_instance = PlotIrrigationEvent(service_provider=service_provider,farm=farm,date=date,plotID=Plot.objects.get(plotID=plot,farm=farm),irrigated_depth=irrigation_depth,irrigate_whole_or_per_plant=irrigate_whole_or_per_plant,climate=climate,bucketvolume=bucketvolume,bucketnumbers=bucketnumbers,wetteddiameteraroundplant=wetteddiameteraroundplant,water_application=water_application,application_rate=discharge,irrigation_event=current_event,technology=Technology.objects.get(name=technology),fuel=fuel,fuelcost=fuelcost,currency=currency,amount_used=amount_used,refilled_amount=refilled_amount,enteredpersonel=SystemUser.objects.get(user=request.user))
                     elif irrigate_whole_or_per_plant =='Wholefield':
                        plotirrigationevent_instance = PlotIrrigationEvent(service_provider=service_provider,farm=farm,date=date,plotID=Plot.objects.get(plotID=plot,farm=farm),irrigated_depth=irrigation_depth,irrigate_whole_or_per_plant=irrigate_whole_or_per_plant,climate=climate,bucketvolume=bucketvolume,bucketnumbers=bucketnumbers,water_application=water_application,application_rate=discharge,irrigation_event=current_event,technology=Technology.objects.get(name=technology),fuel=fuel,fuelcost=fuelcost,currency=currency,amount_used=amount_used,refilled_amount=refilled_amount,enteredpersonel=SystemUser.objects.get(user=request.user))
                  elif technology =='Tractor mounted pump':
                     if irrigate_whole_or_per_plant =='Perplant':
                        plotirrigationevent_instance = PlotIrrigationEvent(service_provider=service_provider,farm=farm,date=date,plotID=Plot.objects.get(plotID=plot,farm=farm),irrigated_depth=irrigation_depth,irrigate_whole_or_per_plant=irrigate_whole_or_per_plant,climate=climate,bucketvolume=bucketvolume,bucketnumbers=bucketnumbers,wetteddiameteraroundplant=wetteddiameteraroundplant,water_application=water_application,application_rate=discharge,irrigation_event=current_event,technology=Technology.objects.get(name=technology),gender=gender,distance_from_water_source=distance_from_water_source,time_to_fetch_water=time_to_fetch_water,enteredpersonel=SystemUser.objects.get(user=request.user))
                     elif irrigate_whole_or_per_plant =='Wholefield':
                        plotirrigationevent_instance = PlotIrrigationEvent(service_provider=service_provider,farm=farm,date=date,plotID=Plot.objects.get(plotID=plot,farm=farm),irrigated_depth=irrigation_depth,irrigate_whole_or_per_plant=irrigate_whole_or_per_plant,climate=climate,bucketvolume=bucketvolume,bucketnumbers=bucketnumbers,water_application=water_application,application_rate=discharge,irrigation_event=current_event,technology=Technology.objects.get(name=technology),gender=gender,distance_from_water_source=distance_from_water_source,time_to_fetch_water=time_to_fetch_water,enteredpersonel=SystemUser.objects.get(user=request.user))
                  else:
                     if irrigate_whole_or_per_plant =='Perplant':
                        plotirrigationevent_instance = PlotIrrigationEvent(service_provider=service_provider,farm=farm,date=date,plotID=Plot.objects.get(plotID=plot,farm=farm),irrigated_depth=irrigation_depth,irrigate_whole_or_per_plant=irrigate_whole_or_per_plant,climate=climate,bucketvolume=bucketvolume,bucketnumbers=bucketnumbers,wetteddiameteraroundplant=wetteddiameteraroundplant,water_application=water_application,application_rate=discharge,irrigation_event=current_event,technology=Technology.objects.get(name=technology),enteredpersonel=SystemUser.objects.get(user=request.user))
                     elif irrigate_whole_or_per_plant =='Wholefield':
                        plotirrigationevent_instance = PlotIrrigationEvent(service_provider=service_provider,farm=farm,date=date,plotID=Plot.objects.get(plotID=plot,farm=farm),irrigated_depth=irrigation_depth,irrigate_whole_or_per_plant=irrigate_whole_or_per_plant,climate=climate,bucketvolume=bucketvolume,bucketnumbers=bucketnumbers,water_application=water_application,application_rate=discharge,irrigation_event=current_event,technology=Technology.objects.get(name=technology),enteredpersonel=SystemUser.objects.get(user=request.user))
                  plotirrigationevent_instance.save()
               else:
                  message = "Looks like the event already exist"
                  user_instance = SystemUser.objects.get(user=request.user)
                  if user_instance.role == 'RA' or user_instance.role == 'ST':user_village = user_instance.village
                  elif user_instance.role == 'ALL':user_country = user_instance.country
                  elif user_instance.role == 'RS':researcher = user_instance.country
                  return render(request,'iwmiproject/farmirrigation.html',locals())

         elif water_application == 'Furrow/bed':
            if water_management == 'WFD':
               try:
                  PlotIrrigationEvent.objects.get(farm=farm,date=date,plotID=(Plot.objects.get(plotID=plot,farm=farm)))
                  #PlotIrrigationEvent.objects.get(date=date,plotID=plot)
               except PlotIrrigationEvent.DoesNotExist:
                  events =[i.irrigation_event for i in PlotIrrigationEvent.objects.all().filter(farm=farm,plotID=(Plot.objects.get(plotID=plot,farm=farm)))]
                  if not events:current_event = 1
                  else:current_event = max(events) + 1
                  if technology =='Petrol motorized pump':
                     plotirrigationevent_instance = PlotIrrigationEvent(service_provider=service_provider,farm=farm,date=date,plotID=Plot.objects.get(plotID=plot,farm=farm),climate=climate,furrow_irr_time=furrow_irr_time,water_application=water_application,irrigated_depth=irrigation_depth,buttonfurrowwidth=buttonfurrowwidth,topfurrowwidth=topfurrowwidth,waterheight=waterheight,application_rate=discharge,irrigation_event=current_event,field_efficiency=field_efficiency,conveyance_efficiency=conveyance_efficiency,yellow_WFD_before_irrigation=yellow_WFD_before_irrigation,red_WFD_before_irrigation=red_WFD_before_irrigation,yellow_WFD_time_after_irrigation=yellow_WFD_time_after_irrigation,red_WFD_time_after_irrigation=red_WFD_time_after_irrigation,technology=Technology.objects.get(name=technology),fuel=fuel,fuelcost=fuelcost,currency=currency,amount_used=amount_used,refilled_amount=refilled_amount,enteredpersonel=SystemUser.objects.get(user=request.user))
                  elif technology =='Tractor mounted pump':
                     plotirrigationevent_instance = PlotIrrigationEvent(service_provider=service_provider,farm=farm,date=date,plotID=Plot.objects.get(plotID=plot,farm=farm),climate=climate,furrow_irr_time=furrow_irr_time,water_application=water_application,irrigated_depth=irrigation_depth,buttonfurrowwidth=buttonfurrowwidth,topfurrowwidth=topfurrowwidth,waterheight=waterheight,application_rate=discharge,irrigation_event=current_event,field_efficiency=field_efficiency,conveyance_efficiency=conveyance_efficiency,yellow_WFD_before_irrigation=yellow_WFD_before_irrigation,red_WFD_before_irrigation=red_WFD_before_irrigation,yellow_WFD_time_after_irrigation=yellow_WFD_time_after_irrigation,red_WFD_time_after_irrigation=red_WFD_time_after_irrigation,technology=Technology.objects.get(name=technology),gender=gender,distance_from_water_source=distance_from_water_source,time_to_fetch_water=time_to_fetch_water,enteredpersonel=SystemUser.objects.get(user=request.user))
                  else:
                     plotirrigationevent_instance = PlotIrrigationEvent(service_provider=service_provider,farm=farm,date=date,plotID=Plot.objects.get(plotID=plot,farm=farm),climate=climate,furrow_irr_time=furrow_irr_time,water_application=water_application,irrigated_depth=irrigation_depth,buttonfurrowwidth=buttonfurrowwidth,topfurrowwidth=topfurrowwidth,waterheight=waterheight,application_rate=discharge,irrigation_event=current_event,field_efficiency=field_efficiency,conveyance_efficiency=conveyance_efficiency,yellow_WFD_before_irrigation=yellow_WFD_before_irrigation,red_WFD_before_irrigation=red_WFD_before_irrigation,yellow_WFD_time_after_irrigation=yellow_WFD_time_after_irrigation,red_WFD_time_after_irrigation=red_WFD_time_after_irrigation,technology=Technology.objects.get(name=technology),enteredpersonel=SystemUser.objects.get(user=request.user))
                  plotirrigationevent_instance.save()
               else:
                  message = "Looks like the event already exist"
                  user_instance = SystemUser.objects.get(user=request.user)
                  if user_instance.role == 'RA' or user_instance.role == 'ST':user_village = user_instance.village
                  elif user_instance.role == 'ALL':user_country = user_instance.country
                  elif user_instance.role == 'RS':researcher = user_instance.country
                  return render(request,'iwmiproject/farmirrigation.html',locals())
            else:
               try:
                                   
                  PlotIrrigationEvent.objects.get(farm=farm,date=date,plotID=(Plot.objects.get(plotID=plot,farm=farm)))
                  #PlotIrrigationEvent.objects.get(date=date,plotID=plot)
               except PlotIrrigationEvent.DoesNotExist:
                  events =[i.irrigation_event for i in PlotIrrigationEvent.objects.all().filter(farm=farm,plotID=(Plot.objects.get(plotID=plot,farm=farm)))]
                  if not events:current_event = 1
                  else:current_event = max(events) + 1
                  if technology =='Petrol motorized pump':
                     plotirrigationevent_instance = PlotIrrigationEvent(service_provider=service_provider,farm=farm,date=date,plotID=Plot.objects.get(plotID=plot,farm=farm),climate=climate,furrow_irr_time=furrow_irr_time,water_application=water_application,irrigated_depth=irrigation_depth,buttonfurrowwidth=buttonfurrowwidth,topfurrowwidth=topfurrowwidth,waterheight=waterheight,application_rate=discharge,irrigation_event=current_event,field_efficiency=field_efficiency,conveyance_efficiency=conveyance_efficiency,technology=Technology.objects.get(name=technology),fuel=fuel,fuelcost=fuelcost,currency=currency,amount_used=amount_used,refilled_amount=refilled_amount,enteredpersonel=SystemUser.objects.get(user=request.user))
                  elif technology =='Tractor mounted pump':
                     plotirrigationevent_instance = PlotIrrigationEvent(service_provider=service_provider,farm=farm,date=date,plotID=Plot.objects.get(plotID=plot,farm=farm),climate=climate,furrow_irr_time=furrow_irr_time,water_application=water_application,irrigated_depth=irrigation_depth,buttonfurrowwidth=buttonfurrowwidth,topfurrowwidth=topfurrowwidth,waterheight=waterheight,application_rate=discharge,irrigation_event=current_event,field_efficiency=field_efficiency,conveyance_efficiency=conveyance_efficiency,technology=Technology.objects.get(name=technology),gender=gender,distance_from_water_source=distance_from_water_source,time_to_fetch_water=time_to_fetch_water,enteredpersonel=SystemUser.objects.get(user=request.user))
                  else:
                     plotirrigationevent_instance = PlotIrrigationEvent(service_provider=service_provider,farm=farm,date=date,plotID=Plot.objects.get(plotID=plot,farm=farm),climate=climate,furrow_irr_time=furrow_irr_time,water_application=water_application,irrigated_depth=irrigation_depth,buttonfurrowwidth=buttonfurrowwidth,topfurrowwidth=topfurrowwidth,waterheight=waterheight,application_rate=discharge,irrigation_event=current_event,field_efficiency=field_efficiency,conveyance_efficiency=conveyance_efficiency,technology=Technology.objects.get(name=technology),enteredpersonel=SystemUser.objects.get(user=request.user))
                  plotirrigationevent_instance.save()
               else:
                  message = "Looks like the event already exist"
                  user_instance = SystemUser.objects.get(user=request.user)
                  if user_instance.role == 'RA' or user_instance.role == 'ST':user_village = user_instance.village
                  elif user_instance.role == 'ALL':user_country = user_instance.country
                  elif user_instance.role == 'RS':researcher = user_instance.country
                  return render(request,'iwmiproject/farmirrigation.html',locals())
          
         elif water_application == 'Tank and hose':
            print('Irrigation')
            if water_management == 'WFD':
               try:
                  PlotIrrigationEvent.objects.get(farm=farm,date=date,plotID=(Plot.objects.get(plotID=plot,farm=farm)))
                  #PlotIrrigationEvent.objects.get(date=date,plotID=plot)
               except PlotIrrigationEvent.DoesNotExist:
                  events =[i.irrigation_event for i in PlotIrrigationEvent.objects.all().filter(farm=farm,plotID=(Plot.objects.get(plotID=plot,farm=farm)))]
                  if not events:current_event = 1
                  else:current_event = max(events) + 1
                  if technology =='Petrol motorized pump':
                     plotirrigationevent_instance = PlotIrrigationEvent(service_provider=service_provider,farm=farm,date=date,plotID=Plot.objects.get(plotID=plot,farm=farm),start_time=start_time,end_time=end_time,total_time=total_time,climate=climate,water_application=water_application,irrigated_depth=irrigation_depth,irrigation_event=current_event,yellow_WFD_before_irrigation=yellow_WFD_before_irrigation,red_WFD_before_irrigation=red_WFD_before_irrigation,yellow_WFD_time_after_irrigation=yellow_WFD_time_after_irrigation,red_WFD_time_after_irrigation=red_WFD_time_after_irrigation,tanknumber=tanknumber,technology=Technology.objects.get(name=technology),fuel=fuel,fuelcost=fuelcost,currency=currency,amount_used=amount_used,refilled_amount=refilled_amount,enteredpersonel=SystemUser.objects.get(user=request.user))
                  elif technology =='Tractor mounted pump':
                     plotirrigationevent_instance = PlotIrrigationEvent(service_provider=service_provider,farm=farm,date=date,plotID=Plot.objects.get(plotID=plot,farm=farm),start_time=start_time,end_time=end_time,total_time=total_time,climate=climate,water_application=water_application,irrigated_depth=irrigation_depth,irrigation_event=current_event,yellow_WFD_before_irrigation=yellow_WFD_before_irrigation,red_WFD_before_irrigation=red_WFD_before_irrigation,yellow_WFD_time_after_irrigation=yellow_WFD_time_after_irrigation,red_WFD_time_after_irrigation=red_WFD_time_after_irrigation,tanknumber=tanknumber,technology=Technology.objects.get(name=technology),gender=gender,distance_from_water_source=distance_from_water_source,time_to_fetch_water=time_to_fetch_water,enteredpersonel=SystemUser.objects.get(user=request.user))
                  else:
                     plotirrigationevent_instance = PlotIrrigationEvent(service_provider=service_provider,farm=farm,date=date,plotID=Plot.objects.get(plotID=plot,farm=farm),start_time=start_time,end_time=end_time,total_time=total_time,climate=climate,water_application=water_application,irrigated_depth=irrigation_depth,irrigation_event=current_event,yellow_WFD_before_irrigation=yellow_WFD_before_irrigation,red_WFD_before_irrigation=red_WFD_before_irrigation,yellow_WFD_time_after_irrigation=yellow_WFD_time_after_irrigation,red_WFD_time_after_irrigation=red_WFD_time_after_irrigation,tanknumber=tanknumber,technology=Technology.objects.get(name=technology),enteredpersonel=SystemUser.objects.get(user=request.user))
                  plotirrigationevent_instance.save()
                  
               else:
                  message = "Looks like the event already exist"
                  user_instance = SystemUser.objects.get(user=request.user)
                  if user_instance.role == 'RA' or user_instance.role == 'ST':user_village = user_instance.village
                  elif user_instance.role == 'ALL':user_country = user_instance.country
                  elif user_instance.role == 'RS':researcher = user_instance.country
                  return render(request,'iwmiproject/farmirrigation.html',locals())
            else:
               try:
                  PlotIrrigationEvent.objects.get(farm=farm,date=date,plotID=(Plot.objects.get(plotID=plot,farm=farm)))
                  #PlotIrrigationEvent.objects.get(date=date,plotID=plot)
               except PlotIrrigationEvent.DoesNotExist:
                  events =[i.irrigation_event for i in PlotIrrigationEvent.objects.all().filter(farm=farm,plotID=(Plot.objects.get(plotID=plot,farm=farm)))]
                  if not events:current_event = 1
                  else:current_event = max(events) + 1
                  if technology =='Petrol motorized pump':
                     plotirrigationevent_instance = PlotIrrigationEvent(service_provider=service_provider,farm=farm,date=date,plotID=Plot.objects.get(plotID=plot,farm=farm),start_time=start_time,end_time=end_time,total_time=total_time,climate=climate,water_application=water_application,irrigated_depth=irrigation_depth,irrigation_event=current_event,tanknumber=tanknumber,technology=Technology.objects.get(name=technology),fuel=fuel,fuelcost=fuelcost,currency=currency,amount_used=amount_used,refilled_amount=refilled_amount,enteredpersonel=SystemUser.objects.get(user=request.user))
                  elif technology =='Tractor mounted pump':
                     plotirrigationevent_instance = PlotIrrigationEvent(service_provider=service_provider,farm=farm,date=date,plotID=Plot.objects.get(plotID=plot,farm=farm),start_time=start_time,end_time=end_time,total_time=total_time,climate=climate,water_application=water_application,irrigated_depth=irrigation_depth,irrigation_event=current_event,tanknumber=tanknumber,technology=Technology.objects.get(name=technology),gender=gender,distance_from_water_source=distance_from_water_source,time_to_fetch_water=time_to_fetch_water,enteredpersonel=SystemUser.objects.get(user=request.user))
                  else:
                     plotirrigationevent_instance = PlotIrrigationEvent(service_provider=service_provider,farm=farm,date=date,plotID=Plot.objects.get(plotID=plot,farm=farm),start_time=start_time,end_time=end_time,total_time=total_time,climate=climate,water_application=water_application,irrigated_depth=irrigation_depth,irrigation_event=current_event,tanknumber=tanknumber,technology=Technology.objects.get(name=technology),enteredpersonel=SystemUser.objects.get(user=request.user))
                  plotirrigationevent_instance.save()
                  
               else:
                  message = "Looks like the event already exist"
                  user_instance = SystemUser.objects.get(user=request.user)
                  if user_instance.role == 'RA' or user_instance.role == 'ST':user_village = user_instance.village
                  elif user_instance.role == 'ALL':user_country = user_instance.country
                  elif user_instance.role == 'RS':researcher = user_instance.country
                  return render(request,'iwmiproject/farmirrigation.html',locals())
               
            pass
         
         elif water_application == 'Drip':
            if water_management == 'WFD':
               try:
                  PlotIrrigationEvent.objects.get(farm=farm,date=date,plotID=(Plot.objects.get(plotID=plot,farm=farm)))
                  #PlotIrrigationEvent.objects.get(date=date,plotID=plot)
               except PlotIrrigationEvent.DoesNotExist:
                  events =[i.irrigation_event for i in PlotIrrigationEvent.objects.all().filter(farm=farm,plotID=(Plot.objects.get(plotID=plot,farm=farm)))]
                  if not events:current_event = 1
                  else:current_event = max(events) + 1
                  #if technology =='Petrol motorized pump':
                     #plotirrigationevent_instance = PlotIrrigationEvent(service_provider=service_provider,farm=farm,date=date,plotID=Plot.objects.get(plotID=plot,farm=farm),climate=climate,start_time=start_time,end_time=end_time,total_time=total_time,emitter_spacing=emitter_spacing,driptank_volume=driptank_volume,calibrationcup_volume=calibrationcup_volume,emitter_wetted_diameter=emitter_wetted_diameter,water_application=water_application,application_rate=discharge,irrigation_event=current_event,yellow_WFD_before_irrigation=yellow_WFD_before_irrigation,red_WFD_before_irrigation=red_WFD_before_irrigation,yellow_WFD_time_after_irrigation=yellow_WFD_time_after_irrigation,red_WFD_time_after_irrigation=red_WFD_time_after_irrigation,technology=Technology.objects.get(name=technology),fuel=fuel,fuelcost=fuelcost,currency=currency,amount_used=amount_used,refilled_amount=refilled_amount,irrigated_depth=irrigation_depth,enteredpersonel=SystemUser.objects.get(user=request.user))
                  if technology =='Tractor mounted pump' or technology =='Petrol motorized pump':
                     plotirrigationevent_instance = PlotIrrigationEvent(tanknumber=tanknumber,service_provider=service_provider,farm=farm,date=date,plotID=Plot.objects.get(plotID=plot,farm=farm),climate=climate,start_time=start_time,end_time=end_time,total_time=total_time,driptank_volume=driptank_volume,water_application=water_application,application_rate=discharge,irrigation_event=current_event,yellow_WFD_before_irrigation=yellow_WFD_before_irrigation,red_WFD_before_irrigation=red_WFD_before_irrigation,yellow_WFD_time_after_irrigation=yellow_WFD_time_after_irrigation,red_WFD_time_after_irrigation=red_WFD_time_after_irrigation,technology=Technology.objects.get(name=technology),irrigated_depth=irrigation_depth,fuel=fuel,fuelcost=fuelcost,currency=currency,amount_used=amount_used,refilled_amount=refilled_amount,gender=gender,distance_from_water_source=distance_from_water_source,time_to_fetch_water=time_to_fetch_water,water_level_bf_filling=water_level_bf_filling,water_level_aftr_filling=water_level_aftr_filling,time_to_fill_water_tank=time_to_fill_water_tank,enteredpersonel=SystemUser.objects.get(user=request.user))
                  elif technology == 'Solar pump':
                     plotirrigationevent_instance = PlotIrrigationEvent(tanknumber=tanknumber,service_provider=service_provider,farm=farm,date=date,plotID=Plot.objects.get(plotID=plot,farm=farm),climate=climate,start_time=start_time,end_time=end_time,total_time=total_time,driptank_volume=driptank_volume,water_application=water_application,application_rate=discharge,irrigation_event=current_event,yellow_WFD_before_irrigation=yellow_WFD_before_irrigation,red_WFD_before_irrigation=red_WFD_before_irrigation,yellow_WFD_time_after_irrigation=yellow_WFD_time_after_irrigation,red_WFD_time_after_irrigation=red_WFD_time_after_irrigation,technology=Technology.objects.get(name=technology),irrigated_depth=irrigation_depth,gender=gender,time_to_fetch_water=time_to_fetch_water,enteredpersonel=SystemUser.objects.get(user=request.user))
                  else:
                     plotirrigationevent_instance = PlotIrrigationEvent(tanknumber=tanknumber,service_provider=service_provider,farm=farm,date=date,plotID=Plot.objects.get(plotID=plot,farm=farm),climate=climate,start_time=start_time,end_time=end_time,total_time=total_time,driptank_volume=driptank_volume,water_application=water_application,application_rate=discharge,irrigation_event=current_event,yellow_WFD_before_irrigation=yellow_WFD_before_irrigation,red_WFD_before_irrigation=red_WFD_before_irrigation,yellow_WFD_time_after_irrigation=yellow_WFD_time_after_irrigation,red_WFD_time_after_irrigation=red_WFD_time_after_irrigation,technology=Technology.objects.get(name=technology),irrigated_depth=irrigation_depth,enteredpersonel=SystemUser.objects.get(user=request.user))
                  plotirrigationevent_instance.save()
               else:
                  message = "Looks like the event already exist"
                  user_instance = SystemUser.objects.get(user=request.user)
                  if user_instance.role == 'RA' or user_instance.role == 'ST':user_village = user_instance.village
                  elif user_instance.role == 'ALL':user_country = user_instance.country
                  elif user_instance.role == 'RS':researcher = user_instance.country
                  return render(request,'iwmiproject/farmirrigation.html',locals())
            else:
               try:
                  PlotIrrigationEvent.objects.get(farm=farm,date=date,plotID=(Plot.objects.get(plotID=plot,farm=farm)))
                  #PlotIrrigationEvent.objects.get(date=date,plotID=plot)
               except PlotIrrigationEvent.DoesNotExist:
                  events =[i.irrigation_event for i in PlotIrrigationEvent.objects.all().filter(farm=farm,plotID=(Plot.objects.get(plotID=plot,farm=farm)))]
                  if not events:current_event = 1
                  else:current_event = max(events) + 1
                  #if technology =='Petrol motorized pump':
                     #plotirrigationevent_instance = PlotIrrigationEvent(service_provider=service_provider,farm=farm,date=date,plotID=Plot.objects.get(plotID=plot,farm=farm),climate=climate,start_time=start_time,end_time=end_time,total_time=total_time,emitter_spacing=emitter_spacing,driptank_volume=driptank_volume,calibrationcup_volume=calibrationcup_volume,emitter_wetted_diameter=emitter_wetted_diameter,water_application=water_application,application_rate=discharge,irrigation_event=current_event,technology=Technology.objects.get(name=technology),fuel=fuel,fuelcost=fuelcost,currency=currency,amount_used=amount_used,refilled_amount=refilled_amount,irrigated_depth=irrigation_depth,enteredpersonel=SystemUser.objects.get(user=request.user))
                  if technology =='Tractor mounted pump' or technology =='Petrol motorized pump':
                     plotirrigationevent_instance = PlotIrrigationEvent(tanknumber=tanknumber,service_provider=service_provider,farm=farm,date=date,plotID=Plot.objects.get(plotID=plot,farm=farm),climate=climate,start_time=start_time,end_time=end_time,total_time=total_time,driptank_volume=driptank_volume,water_application=water_application,application_rate=discharge,irrigation_event=current_event,technology=Technology.objects.get(name=technology),irrigated_depth=irrigation_depth,fuel=fuel,fuelcost=fuelcost,currency=currency,amount_used=amount_used,refilled_amount=refilled_amount,gender=gender,distance_from_water_source=distance_from_water_source,time_to_fetch_water=time_to_fetch_water,water_level_bf_filling=water_level_bf_filling,water_level_aftr_filling=water_level_aftr_filling,time_to_fill_water_tank=time_to_fill_water_tank,enteredpersonel=SystemUser.objects.get(user=request.user))
                  elif technology =='Solar pump':
                     plotirrigationevent_instance = PlotIrrigationEvent(tanknumber=tanknumber,service_provider=service_provider,farm=farm,date=date,plotID=Plot.objects.get(plotID=plot,farm=farm),climate=climate,start_time=start_time,end_time=end_time,total_time=total_time,driptank_volume=driptank_volume,water_application=water_application,application_rate=discharge,irrigation_event=current_event,technology=Technology.objects.get(name=technology),irrigated_depth=irrigation_depth,gender=gender,time_to_fetch_water=time_to_fetch_water,enteredpersonel=SystemUser.objects.get(user=request.user))
                  else:
                     plotirrigationevent_instance = PlotIrrigationEvent(tanknumber=tanknumber,service_provider=service_provider,farm=farm,date=date,plotID=Plot.objects.get(plotID=plot,farm=farm),climate=climate,start_time=start_time,end_time=end_time,total_time=total_time,driptank_volume=driptank_volume,water_application=water_application,application_rate=discharge,irrigation_event=current_event,technology=Technology.objects.get(name=technology),irrigated_depth=irrigation_depth,enteredpersonel=SystemUser.objects.get(user=request.user))
                  plotirrigationevent_instance.save()
               else:
                  message = "Looks like the event already exist"
                  user_instance = SystemUser.objects.get(user=request.user)
                  if user_instance.role == 'RA' or user_instance.role == 'ST':user_village = user_instance.village
                  elif user_instance.role == 'ALL':user_country = user_instance.country
                  elif user_instance.role == 'RS':researcher = user_instance.country
                  return render(request,'iwmiproject/farmirrigation.html',locals())

         elif water_application == 'Sprinkler':
            if water_management == 'WFD':
               pass
            else:
               pass
            pass
         
         if labour == 'Family':
            LabourManagament_instance = LabourManagament(date=date,family_female_time=family_female_time,family_male_time=family_male_time,farm=farm,areaID=plot,areadescription='Plot',labour=labour,family_female_number=family_female_number,family_male_number=family_male_number,activity='Plot Irrigation',wage=wage,price_unit=currency,enteredpersonel=SystemUser.objects.get(user=request.user))
         
         elif labour == 'Hired':
            LabourManagament_instance = LabourManagament(date=date,hired_female_time=hired_female_time,hired_male_time=hired_male_time,farm=farm,areaID=plot,areadescription='Plot',labour=labour,hired_female_number=hired_female_number,hired_male_number=hired_male_number,activity='Plot Irrigation',wage=wage,price_unit=currency,enteredpersonel=SystemUser.objects.get(user=request.user))
         
         elif labour == 'FamilyHired':
            LabourManagament_instance = LabourManagament(date=date,family_female_time=family_female_time,family_male_time=family_male_time,hired_female_time=hired_female_time,hired_male_time=hired_male_time,farm=farm,areaID=plot,areadescription='Plot',labour=labour,hired_female_number=hired_female_number,hired_male_number=hired_male_number,family_female_number=family_female_number,family_male_number=family_male_number,activity='Plot Irrigation',wage=wage,price_unit=currency,enteredpersonel=SystemUser.objects.get(user=request.user))
         
         LabourManagament_instance.save()
         
         print('total_time:{}'.format(total_time))
         
         #user_instance = SystemUser.objects.get(user=request.user)
         #if user_instance.role == 'RA' or user_instance.role == 'ST':user_village = user_instance.village
         #elif user_instance.role == 'ALL':user_country = user_instance.country
         #return render(request,'iwmiproject/farmirrigation.html',locals())
         message='saved'
         return render(request,'iwmiproject/saved.html',locals())
        
      else:
         user_instance = SystemUser.objects.get(user=request.user)
         currency = pick_currency(user_instance)
         if user_instance.role == 'RA' or user_instance.role == 'ST':user_village = user_instance.village
         elif user_instance.role == 'ALL':user_country = user_instance.country
         elif user_instance.role == 'RS':researcher = user_instance.country
         #context = {'farmirrigationform':farmirrigationform,'user_village':user_village}
         #return render_to_response('iwmiproject/farmirrigation.html',context,context_instance=RequestContext(request))
         return render(request,'iwmiproject/farmirrigation.html',locals())
      
   else:
      user_instance = SystemUser.objects.get(user=request.user)
      currency = pick_currency(user_instance)
      if user_instance.role == 'RA' or user_instance.role == 'ST':user_village = user_instance.village
      elif user_instance.role == 'ALL':user_country = user_instance.country
      elif user_instance.role == 'RS':researcher = user_instance.country
      farmirrigationform = FarmIrrigationForm()
      return render(request,'iwmiproject/farmirrigation.html',locals())
   
   
def soil(request):
   if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('signup:login'))
      
   if request.method == 'POST': 
      soilform = SoilForm(request.POST)
        
      if soilform.is_valid():
         date = soilform.cleaned_data['date']
         farm = soilform.cleaned_data['farm']
         plot = soilform.cleaned_data['plot']
         soilclass = soilform.cleaned_data['soilclass']
         soil_depth = soilform.cleaned_data['soil_depth']
         pH = soilform.cleaned_data['pH']
         ec = soilform.cleaned_data['ec']
         sand = soilform.cleaned_data['sand']
         clay = soilform.cleaned_data['clay']
         silt = soilform.cleaned_data['silt']
         cec = soilform.cleaned_data['cec']
         om = soilform.cleaned_data['om']
         tn = soilform.cleaned_data['tn']
         av_p= soilform.cleaned_data['av_p']
         fe = soilform.cleaned_data['fe']
         fc = soilform.cleaned_data['fc']
         pwp = soilform.cleaned_data['pwp']
         k = soilform.cleaned_data['k']
         bulkdensity = soilform.cleaned_data['bulkdensity']
         zn = soilform.cleaned_data['zn']
         se = soilform.cleaned_data['se']
         ca = soilform.cleaned_data['ca']
         s = soilform.cleaned_data['s']
         mg = soilform.cleaned_data['mg']
         na = soilform.cleaned_data['na']
         
         try:
            SoilProperty.objects.get(farm=farm,date=date,plotID=Plot.objects.get(plotID=plot,farm=farm))
         except SoilProperty.DoesNotExist:
            soilproperty_instance = SoilProperty(farm=farm,date=date,plotID=Plot.objects.get(plotID=plot,farm=farm),soil_depth=soil_depth,soilclass=Soil.objects.get(name=soilclass),pH=pH,ec=ec,sand=sand,clay=clay,silt=silt,cec=cec,om=om,tn=tn,av_p=av_p,fe=fe,fc=fc,pwp=pwp,k=k,bulkdensity=bulkdensity,zn=zn,se=se,ca=ca,s=s,mg=mg,na=na,enteredpersonel=SystemUser.objects.get(user=request.user))
            soilproperty_instance.save()
         else:
            message = "Looks like the service on that date is already recorded"
            user_instance = SystemUser.objects.get(user=request.user)
            if user_instance.role == 'RA' or user_instance.role == 'ST':user_village = user_instance.village
            elif user_instance.role == 'ALL':user_country = user_instance.country
            elif user_instance.role == 'RS':researcher = user_instance.country
            return render(request,'iwmiproject/soils.html',locals())
         message='saved'
         return render(request,'iwmiproject/saved.html',locals())
        
      else:
         user_instance = SystemUser.objects.get(user=request.user)
         if user_instance.role == 'RA' or user_instance.role == 'ST':user_village = user_instance.village
         elif user_instance.role == 'ALL':user_country = user_instance.country
         elif user_instance.role == 'RS':researcher = user_instance.country
         applicationcalibrationform = ApplicationCalibrationForm()
         context = {'soilform':soilform}
         return render(request,'iwmiproject/soil.html',locals())
      
   else:
      user_instance = SystemUser.objects.get(user=request.user)
      if user_instance.role == 'RA' or user_instance.role == 'ST':user_village = user_instance.village
      elif user_instance.role == 'ALL':user_country = user_instance.country
      elif user_instance.role == 'RS':researcher = user_instance.country
      applicationcalibrationform = ApplicationCalibrationForm()
      soilform = SoilForm()
      return render(request,'iwmiproject/soil.html',locals())
   

def soilmoisture(request):
   if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('signup:login'))
      
   if request.method == 'POST': 
      soilmoisturemeasurementform = SoilMoistureMeasurementForm(request.POST)
     
      if soilmoisturemeasurementform.is_valid():
         measurement_option = soilmoisturemeasurementform.cleaned_data['measurement_option']
         date = soilmoisturemeasurementform.cleaned_data['date']
         farm = soilmoisturemeasurementform.cleaned_data['farm']
         plot = soilmoisturemeasurementform.cleaned_data['plot']
         #event = soilmoisturemeasurementform.cleaned_data['event']
         measurement_one = soilmoisturemeasurementform.cleaned_data['measurement_one']
         measurement_two = soilmoisturemeasurementform.cleaned_data['measurement_two']
         measurement_three = soilmoisturemeasurementform.cleaned_data['measurement_three']
         measurement_four = soilmoisturemeasurementform.cleaned_data['measurement_four']
         measurement_five = soilmoisturemeasurementform.cleaned_data['measurement_five']
         measurement_six = soilmoisturemeasurementform.cleaned_data['measurement_six']
         measurement_seven = soilmoisturemeasurementform.cleaned_data['measurement_seven']
         measurement_eigth = soilmoisturemeasurementform.cleaned_data['measurement_eigth']
         measurement_nine = soilmoisturemeasurementform.cleaned_data['measurement_nine']
         measurement_ten = soilmoisturemeasurementform.cleaned_data['measurement_ten']
         measurement_depth = soilmoisturemeasurementform.cleaned_data['measurement_depth']
         time = soilmoisturemeasurementform.cleaned_data['time']
         depth_sample = soilmoisturemeasurementform.cleaned_data['depth_sample']
         volume_core_used = soilmoisturemeasurementform.cleaned_data['volume_core_used']
         weight_core_used = soilmoisturemeasurementform.cleaned_data['weight_core_used']
         wet_weight = soilmoisturemeasurementform.cleaned_data['wet_weight']
         dry_weight = soilmoisturemeasurementform.cleaned_data['dry_weight']
         bulk_density = soilmoisturemeasurementform.cleaned_data['bulk_density']
         gravimetric_moisture_content = soilmoisturemeasurementform.cleaned_data['gravimetric_moisture_content']
         volumetric_moisture_content = soilmoisturemeasurementform.cleaned_data['volumetric_moisture_content']
         depth_10 = soilmoisturemeasurementform.cleaned_data['depth_10']
         depth_20 = soilmoisturemeasurementform.cleaned_data['depth_20']
         depth_30 = soilmoisturemeasurementform.cleaned_data['depth_30']
         depth_40 = soilmoisturemeasurementform.cleaned_data['depth_40']
         depth_60 = soilmoisturemeasurementform.cleaned_data['depth_60']
         depth_100 = soilmoisturemeasurementform.cleaned_data['depth_100']
         
         if measurement_option == 'gravimetric':
            events =[i.event for i in GravimetricSoilMoisture.objects.all().filter(farm=farm,plotID=Plot.objects.get(plotID=plot,farm=farm))]
            if not events:current_event = 1
            else:current_event = max(events) + 1
            
            try:
               GravimetricSoilMoisture.objects.get(farm=farm,date=date,plotID=Plot.objects.get(plotID=plot,farm=farm))
            except GravimetricSoilMoisture.DoesNotExist:
               gravimetricsoilmoisture_instance = GravimetricSoilMoisture(farm=farm,date=date,plotID=Plot.objects.get(plotID=plot,farm=farm),event=current_event,time_taken=time,depth=depth_sample,volume_core_used=volume_core_used,weight_core_used=weight_core_used,wet_weight=wet_weight,dry_weight=dry_weight,bulk_density=bulk_density,gravimetric_moisture_content=gravimetric_moisture_content,volumetric_moisture_content=volumetric_moisture_content,enteredpersonel=SystemUser.objects.get(user=request.user))
               gravimetricsoilmoisture_instance.save()
            else:
               message = "Looks like the event on that date is already recorded"
               user_instance = SystemUser.objects.get(user=request.user)
               currency = pick_currency(user_instance)
               if user_instance.role == 'RA' or user_instance.role == 'ST':user_village = user_instance.village
               elif user_instance.role == 'ALL':user_country = user_instance.country
               elif user_instance.role == 'RS':researcher = user_instance.country
               return render(request,'iwmiproject/soilmoisture.html',locals())
            
         elif measurement_option == 'TDR':
            events =[i.event for i in TDRMeasurement.objects.all().filter(farm=farm,plotID=Plot.objects.get(plotID=plot,farm=farm))]
            if not events:current_event = 1
            else:current_event = max(events) + 1
            
            try:
               TDRMeasurement.objects.get(date=date,farm=farm,plotID=Plot.objects.get(plotID=plot,farm=farm))
            except TDRMeasurement.DoesNotExist:
               tdrmeasurement_instance = TDRMeasurement(farm=farm,date=date,plotID=Plot.objects.get(plotID=plot,farm=farm),event=current_event,\
                                                   measurement_one=measurement_one,measurement_two=measurement_two,measurement_three=measurement_three,\
                                                   measurement_four=measurement_four,measurement_five=measurement_five,measurement_six=measurement_six,\
                                                   measurement_seven=measurement_seven,measurement_eigth=measurement_eigth, measurement_nine=measurement_nine,\
                                                   measurement_ten=measurement_ten,measurement_depth=measurement_depth,enteredpersonel=SystemUser.objects.get(user=request.user))
               tdrmeasurement_instance.save()
            else:
               message = "Looks like the event on that date is already recorded"
               user_instance = SystemUser.objects.get(user=request.user)
               currency = pick_currency(user_instance)
               if user_instance.role == 'RA' or user_instance.role == 'ST':user_village = user_instance.village
               elif user_instance.role == 'ALL':user_country = user_instance.country
               elif user_instance.role == 'RS':researcher = user_instance.country
               return render(request,'iwmiproject/soilmoisture.html',locals())
            
            
         elif measurement_option == 'SoilMoistureProfiler':
            events =[i.event for i in SoilMoistureProfiler.objects.all().filter(farm=farm,plotID=Plot.objects.get(plotID=plot,farm=farm))]
            if not events:current_event = 1
            else:current_event = max(events) + 1
            
            try:
               SoilMoistureProfiler.objects.get(date=date,farm=farm,plotID=Plot.objects.get(plotID=plot,farm=farm))
            except SoilMoistureProfiler.DoesNotExist:
               soilmoistureprofiler_instance = SoilMoistureProfiler(farm=farm,date=date,plotID=Plot.objects.get(plotID=plot,farm=farm),event=current_event,depth_10=depth_10,depth_20=depth_20,depth_30=depth_30,depth_40=depth_40,depth_60=depth_60,depth_100=depth_100,enteredpersonel=SystemUser.objects.get(user=request.user))
               soilmoistureprofiler_instance.save()
            else:
               message = "Looks like the event on that date is already recorded"
               user_instance = SystemUser.objects.get(user=request.user)
               currency = pick_currency(user_instance)
               if user_instance.role == 'RA' or user_instance.role == 'ST':user_village = user_instance.village
               elif user_instance.role == 'ALL':user_country = user_instance.country
               elif user_instance.role == 'RS':researcher = user_instance.country
               return render(request,'iwmiproject/soilmoisture.html',locals())
            

         #user_instance = SystemUser.objects.get(user=request.user)
         #if user_instance.role == 'RA' or user_instance.role == 'ST':user_village = user_instance.village
         #elif user_instance.role == 'ALL':user_country = user_instance.country
         #applicationcalibrationform = ApplicationCalibrationForm()
         #return render(request,'iwmiproject/soilmoisture.html',locals())
         message='saved'
         return render(request,'iwmiproject/saved.html',locals())
        
      else:
         user_instance = SystemUser.objects.get(user=request.user)
         if user_instance.role == 'RA' or user_instance.role == 'ST':user_village = user_instance.village
         elif user_instance.role == 'ALL':user_country = user_instance.country
         elif user_instance.role == 'RS':researcher = user_instance.country
         applicationcalibrationform = ApplicationCalibrationForm()
         #context = {'soilmoisturemeasurementform':soilmoisturemeasurementform}
         return render(request,'iwmiproject/soilmoisture.html',locals())
   else:
      user_instance = SystemUser.objects.get(user=request.user)
      if user_instance.role == 'RA' or user_instance.role == 'ST':user_village = user_instance.village
      elif user_instance.role == 'ALL':user_country = user_instance.country
      elif user_instance.role == 'RS':researcher = user_instance.country
      applicationcalibrationform = ApplicationCalibrationForm()
      soilmoisturemeasurementform = SoilMoistureMeasurementForm()
      return render(request,'iwmiproject/soilmoisture.html',locals())
   
   
   
def fuelconsumption(request):
   if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('signup:login'))
      
   return render(request,'iwmiproject/fuelconsumption.html',locals())

def service_repaire(request):
   if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('signup:login'))
      
   if request.method == 'POST': 
      servicerepaireform = ServiceRepaireForm(request.POST)
        
      if servicerepaireform.is_valid():
         date = servicerepaireform.cleaned_data['date']
         farm = servicerepaireform.cleaned_data['farm']
         repaire_type = servicerepaireform.cleaned_data['repaire_type']
         spaire = servicerepaireform.cleaned_data['spaire']
         price = servicerepaireform.cleaned_data['price']
         #currency = servicerepaireform.cleaned_data['currency']
         maintenance_place = servicerepaireform.cleaned_data['maintenance_place']
         technology_broken = servicerepaireform.cleaned_data['technology_broken']
         distance_to_shop = servicerepaireform.cleaned_data['distance_to_shop']
         travel_cost = servicerepaireform.cleaned_data['travel_cost']
         repair_personel = servicerepaireform.cleaned_data['repair_personel']
         time_taken = servicerepaireform.cleaned_data['time_taken']
         
         user_instance = SystemUser.objects.get(user=request.user)
         currency = pick_currency(user_instance)
         
         try:
            Service.objects.get(date=date,farm=farm)
         except Service.DoesNotExist:
            if maintenance_place =='Repair shop':
               service_instance = Service(date=date,farm=farm,repaire_type=repaire_type,total_cost=price,currency=currency,maintenance_place=maintenance_place,technology_broken=technology_broken,distance_to_shop=distance_to_shop,travel_cost=travel_cost,time_taken=time_taken,enteredpersonel=SystemUser.objects.get(user=request.user))
            else:
               service_instance = Service(date=date,farm=farm,repaire_type=repaire_type,total_cost=price,currency=currency,maintenance_place=maintenance_place,technology_broken=technology_broken,time_taken=time_taken,enteredpersonel=SystemUser.objects.get(user=request.user))
            service_instance.save()
            service = Service.objects.get(date=date,farm=farm)
            service.spaire.add(Spaire.objects.get(name=spaire))
         else:
            message = "Looks like the service on that date is already recorded"
            user_instance = SystemUser.objects.get(user=request.user)
            currency = pick_currency(user_instance)
            if user_instance.role == 'RA' or user_instance.role == 'ST':user_village = user_instance.village
            elif user_instance.role == 'ALL':user_country = user_instance.country
            elif user_instance.role == 'RS':researcher = user_instance.country
            return render(request,'iwmiproject/service_repaire.html',locals())

         message='saved'
         return render(request,'iwmiproject/saved.html',locals())
        
      else:
         user_instance = SystemUser.objects.get(user=request.user)
         currency = pick_currency(user_instance)
         if user_instance.role == 'RA' or user_instance.role == 'ST':user_village = user_instance.village
         elif user_instance.role == 'ALL':user_country = user_instance.country
         elif user_instance.role == 'RS':researcher = user_instance.country
         context = {'servicerepaireform':servicerepaireform}
         return render(request,'iwmiproject/service_repaire.html',locals())
      
   else:
      user_instance = SystemUser.objects.get(user=request.user)
      currency = pick_currency(user_instance)
      print('currency: {}'.format(currency))
      if user_instance.role == 'RA' or user_instance.role == 'ST':user_village = user_instance.village
      elif user_instance.role == 'ALL':user_country = user_instance.country
      elif user_instance.role == 'RS':researcher = user_instance.country
      servicerepaireform = ServiceRepaireForm()
      return render(request,'iwmiproject/service_repaire.html',locals())
   

def sale_harvest_crop(request):
   if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('signup:login'))
      
   if request.method == 'POST': 
      harvestedcropsaleform = HarvestedCropSaleForm(request.POST)
        
      if harvestedcropsaleform.is_valid():
         date = harvestedcropsaleform.cleaned_data['date']
         farm = harvestedcropsaleform.cleaned_data['farm']
         plot = harvestedcropsaleform.cleaned_data['plot']
         quantity = harvestedcropsaleform.cleaned_data['quantity']
         marketprice = harvestedcropsaleform.cleaned_data['marketprice']
         totalvalue = harvestedcropsaleform.cleaned_data['totalvalue']
         #expenditure = harvestedcropsaleform.cleaned_data['expenditure']
         #currency = harvestedcropsaleform.cleaned_data['currency']
         distance_to_the_market = harvestedcropsaleform.cleaned_data['distance_to_the_market']
         labour = harvestedcropsaleform.cleaned_data['labour']
         hired_female_number = harvestedcropsaleform.cleaned_data['hired_female_number']
         hired_male_number = harvestedcropsaleform.cleaned_data['hired_male_number']
         family_female_number = harvestedcropsaleform.cleaned_data['family_female_number']
         family_male_number = harvestedcropsaleform.cleaned_data['family_male_number']
         wage = harvestedcropsaleform.cleaned_data['wage']
         #currency = harvestedcropsaleform.cleaned_data['currency']
         mode_of_transport = harvestedcropsaleform.cleaned_data['mode_of_transport']
         fare = harvestedcropsaleform.cleaned_data['fare']
         fuel_type = harvestedcropsaleform.cleaned_data['fuel_type']
         fuel_cost = harvestedcropsaleform.cleaned_data['fuel_cost']
         family_female_time = harvestedcropsaleform.cleaned_data['family_female_time']
         family_male_time = harvestedcropsaleform.cleaned_data['family_male_time']
         hired_female_time = harvestedcropsaleform.cleaned_data['hired_female_time']
         hired_male_time = harvestedcropsaleform.cleaned_data['hired_male_time']
         
         user_instance = SystemUser.objects.get(user=request.user)
         currency = pick_currency(user_instance)
         try:
            SaleHarvestedCrop.objects.get(farm=farm,date=date,plotID=Plot.objects.get(plotID=plot,farm=farm))
         except SaleHarvestedCrop.DoesNotExist:
            #net_income = totalvalue - expenditure
            if mode_of_transport=='Public transport':
               saleharvestedcrop_instance = SaleHarvestedCrop(marketprice=marketprice,farm=farm,date=date,distance_to_the_market=distance_to_the_market,currency=currency,amount=quantity,income=totalvalue,mode_of_transport=mode_of_transport,fare=fare,plotID=Plot.objects.get(plotID=plot,farm=farm),enteredpersonel=SystemUser.objects.get(user=request.user))
            elif mode_of_transport=='Own transportation':
               saleharvestedcrop_instance = SaleHarvestedCrop(marketprice=marketprice,farm=farm,date=date,distance_to_the_market=distance_to_the_market,currency=currency,amount=quantity,income=totalvalue,plotID=Plot.objects.get(plotID=plot,farm=farm),mode_of_transport=mode_of_transport,fuel_type=fuel_type,fuel_cost=fuel_cost,enteredpersonel=SystemUser.objects.get(user=request.user))
            else:
               saleharvestedcrop_instance = SaleHarvestedCrop(marketprice=marketprice,farm=farm,date=date,distance_to_the_market=distance_to_the_market,currency=currency,amount=quantity,income=totalvalue,plotID=Plot.objects.get(plotID=plot,farm=farm),mode_of_transport=mode_of_transport,enteredpersonel=SystemUser.objects.get(user=request.user))
            saleharvestedcrop_instance.save()
         else:
            message = "Looks like the event already exist"
            user_instance = SystemUser.objects.get(user=request.user)
            if user_instance.role == 'RA' or user_instance.role == 'ST':user_village = user_instance.village
            elif user_instance.role == 'ALL':user_country = user_instance.country
            elif user_instance.role == 'RS':researcher = user_instance.country
            return render(request,'iwmiproject/sale_harvest_crop.html',locals())
         
         if labour == 'Family':
            if not wage:
               LabourManagament_instance = LabourManagament(date=date,family_female_time=family_female_time,family_male_time=family_male_time,farm=farm,areaID=Plot.objects.get(plotID=plot,farm=farm),areadescription='Plot',labour=labour,family_female_number=family_female_number,family_male_number=family_male_number,activity='Plot harvest sale',wage=0,price_unit='',enteredpersonel=SystemUser.objects.get(user=request.user))
            else:
               LabourManagament_instance = LabourManagament(date=date,family_female_time=family_female_time,family_male_time=family_male_time,farm=farm,areaID=Plot.objects.get(plotID=plot,farm=farm),areadescription='Plot',labour=labour,family_female_number=family_female_number,family_male_number=family_male_number,activity='Plot harvest sale',wage=wage,price_unit=currency,enteredpersonel=SystemUser.objects.get(user=request.user))
         
         elif labour == 'Hired':
            LabourManagament_instance = LabourManagament(date=date,hired_female_time=hired_female_time,hired_male_time=hired_male_time,farm=farm,areaID=Plot.objects.get(plotID=plot,farm=farm),areadescription='Plot',labour=labour,hired_female_number=hired_female_number,hired_male_number=hired_male_number,activity='Plot harvest sale',wage=wage,price_unit=currency,enteredpersonel=SystemUser.objects.get(user=request.user))
         
         elif labour == 'FamilyHired':
            LabourManagament_instance = LabourManagament(date=date,family_female_time=family_female_time,family_male_time=family_male_time,hired_female_time=hired_female_time,hired_male_time=hired_male_time,farm=farm,areaID=Plot.objects.get(plotID=plot,farm=farm),areadescription='Plot',labour=labour,hired_female_number=hired_female_number,hired_male_number=hired_male_number,family_female_number=family_female_number,family_male_number=family_male_number,activity='Plot harvest sale',wage=wage,price_unit=currency,enteredpersonel=SystemUser.objects.get(user=request.user))
         
         LabourManagament_instance.save()

         message='saved'
         return render(request,'iwmiproject/saved.html',locals())
        
      else:
         user_instance = SystemUser.objects.get(user=request.user)
         currency = pick_currency(user_instance)
         if user_instance.role == 'RA' or user_instance.role == 'ST':user_village = user_instance.village
         elif user_instance.role == 'ALL':user_country = user_instance.country
         elif user_instance.role == 'RS':researcher = user_instance.country
         #context = {'consumedcropbyhouseholdform':consumedcropbyhouseholdform}
         return render(request,'iwmiproject/sale_harvest_crop.html',locals())
   else:
      user_instance = SystemUser.objects.get(user=request.user)
      currency = pick_currency(user_instance)
      if user_instance.role == 'RA' or user_instance.role == 'ST':user_village = user_instance.village
      elif user_instance.role == 'ALL':user_country = user_instance.country
      elif user_instance.role == 'RS':researcher = user_instance.country
      harvestedcropsaleform = HarvestedCropSaleForm()
      return render(request,'iwmiproject/sale_harvest_crop.html',locals())
      
   

def consumed_crop_by_household(request):
   if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('signup:login'))
      
   if request.method == 'POST': 
      consumedcropbyhouseholdform = ConsumedCropbyHouseholdForm(request.POST)
        
      if consumedcropbyhouseholdform.is_valid():
         date = consumedcropbyhouseholdform.cleaned_data['date']
         farm = consumedcropbyhouseholdform.cleaned_data['farm']
         plot = consumedcropbyhouseholdform.cleaned_data['plot']
         quantity = consumedcropbyhouseholdform.cleaned_data['quantity']
         marketprice = consumedcropbyhouseholdform.cleaned_data['marketprice']
         totalvalue = consumedcropbyhouseholdform.cleaned_data['totalvalue']
         #currency = consumedcropbyhouseholdform.cleaned_data['currency']
         where_consumed = consumedcropbyhouseholdform.cleaned_data['where_consumed']
         how_consumed = consumedcropbyhouseholdform.cleaned_data['how_consumed']
         
         user_instance = SystemUser.objects.get(user=request.user)
         currency = pick_currency(user_instance)
         
         try:
            ConsumedCrops.objects.get(farm=farm,date=date,plotID=Plot.objects.get(plotID=plot,farm=farm))
         except ConsumedCrops.DoesNotExist:
            consumedcrop_instance = ConsumedCrops(farm=farm,date=date,plotID=Plot.objects.get(plotID=plot,farm=farm),where_consumed=where_consumed,how_consumed=how_consumed,quantity=quantity,marketprice=marketprice,totalvalue=totalvalue,currency=currency,enteredpersonel=SystemUser.objects.get(user=request.user))
            consumedcrop_instance.save()
         else:
            message = "Looks like the event already exist"
            user_instance = SystemUser.objects.get(user=request.user)
            if user_instance.role == 'RA' or user_instance.role == 'ST':user_village = user_instance.village
            elif user_instance.role == 'ALL':user_country = user_instance.country
            elif user_instance.role == 'RS':researcher = user_instance.country
            return render(request,'iwmiproject/consumed_crop_by_household.html',locals())
         
         
         #user_instance = SystemUser.objects.get(user=request.user)
         #if user_instance.role == 'RA' or user_instance.role == 'ST':user_village = user_instance.village
         #elif user_instance.role == 'ALL':user_country = user_instance.country
         #return render(request,'iwmiproject/consumed_crop_by_household.html',locals())
         message='saved'
         return render(request,'iwmiproject/saved.html',locals())
        
      else:
         user_instance = SystemUser.objects.get(user=request.user)
         currency = pick_currency(user_instance)
         if user_instance.role == 'RA' or user_instance.role == 'ST':user_village = user_instance.village
         elif user_instance.role == 'ALL':user_country = user_instance.country
         elif user_instance.role == 'RS':researcher = user_instance.country
         #context = {'consumedcropbyhouseholdform':consumedcropbyhouseholdform}
         return render(request,'iwmiproject/consumed_crop_by_household.html',locals())
   else:
      user_instance = SystemUser.objects.get(user=request.user)
      currency = pick_currency(user_instance)
      if user_instance.role == 'RA' or user_instance.role == 'ST':user_village = user_instance.village
      elif user_instance.role == 'ALL':user_country = user_instance.country
      elif user_instance.role == 'RS':researcher = user_instance.country
      consumedcropbyhouseholdform = ConsumedCropbyHouseholdForm()
      return render(request,'iwmiproject/consumed_crop_by_household.html',locals())

def farmer_detail(request):
   if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('signup:login'))
      
   countries = Country.objects.all().order_by('name')
   return render(request,'iwmiproject/farmer_detail.html',locals())

def plant_level_yield(request):
   if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('signup:login'))
         
   if request.method == 'POST': 
      plantlevelyieldform = PlantLevelYieldForm(request.POST)
      
      if plantlevelyieldform.is_valid():
         date = plantlevelyieldform.cleaned_data['date']
         farm =  plantlevelyieldform.cleaned_data['farm']
         plot = plantlevelyieldform.cleaned_data['plot']
         Crop = plantlevelyieldform.cleaned_data['Crop']
         dry_fresh =  plantlevelyieldform.cleaned_data['dry_fresh']
         harvesting_method  = plantlevelyieldform.cleaned_data['harvesting_method']
         row_number  = plantlevelyieldform.cleaned_data['row_number']
         plant_number = plantlevelyieldform.cleaned_data['plant_number']
         marketable_produced = plantlevelyieldform.cleaned_data['marketable_produced']
         unmarketable_produced = plantlevelyieldform.cleaned_data['unmarketable_produced']
         marketable_produced_weight = plantlevelyieldform.cleaned_data['marketable_produced_weight']
         unmarketable_produced_weight = plantlevelyieldform.cleaned_data['unmarketable_produced_weight']
         diameter_width_produced = plantlevelyieldform.cleaned_data['diameter_width_produced']
         length= plantlevelyieldform.cleaned_data['length']
         residual_biomass = plantlevelyieldform.cleaned_data['residual_biomass']
              
         try:
            YieldPlantLevel.objects.get(date=date,farm=farm,plotID=Plot.objects.get(plotID=plot,farm=farm),Crop=Crop,row_number=row_number,plant_number=plant_number)
         except YieldPlantLevel.DoesNotExist:
            yieldplantlevel_instance = YieldPlantLevel(date=date,Crop=Crop,farm=farm,plotID=Plot.objects.get(plotID=plot,farm=farm),row_number=row_number,harvest_method=harvesting_method,fresh_dry=dry_fresh,plant_number=plant_number,marketable_produced=marketable_produced,unmarketable_produced=unmarketable_produced,marketable_produced_weight=marketable_produced_weight,unmarketable_produced_weight=unmarketable_produced_weight,diameter_width_produced=diameter_width_produced,length=length,residual_biomass=residual_biomass,enteredpersonel=SystemUser.objects.get(user=request.user))
            yieldplantlevel_instance.save()
         else:
            message = "Looks like the event already exist"
            user_instance = SystemUser.objects.get(user=request.user)
            if user_instance.role == 'RA' or user_instance.role == 'ST':user_village = user_instance.village
            elif user_instance.role == 'ALL':user_country = user_instance.country
            elif user_instance.role == 'RS':researcher = user_instance.country
            return render(request,'iwmiproject/plant_level_yield.html',locals())
         
         #print('*****aaaaaa******')
         #user_instance = SystemUser.objects.get(user=request.user)
         #if user_instance.role == 'RA' or user_instance.role == 'ST':user_village = user_instance.village
         #elif user_instance.role == 'ALL':user_country = user_instance.country
         #return render(request,'iwmiproject/plant_level_yield.html',locals())
         message='saved'
         return render(request,'iwmiproject/saved.html',locals())
        
      else:
         user_instance = SystemUser.objects.get(user=request.user)
         if user_instance.role == 'RA' or user_instance.role == 'ST':user_village = user_instance.village
         elif user_instance.role == 'ALL':user_country = user_instance.country
         elif user_instance.role == 'RS':researcher = user_instance.country
         #context = {'plantlevelyieldform':plantlevelyieldform}
         return render(request,'iwmiproject/plant_level_yield.html',locals())
   else:
      user_instance = SystemUser.objects.get(user=request.user)
      if user_instance.role == 'RA' or user_instance.role == 'ST':user_village = user_instance.village
      elif user_instance.role == 'ALL':user_country = user_instance.country
      elif user_instance.role == 'RS':researcher = user_instance.country
      plantlevelyieldform= PlantLevelYieldForm()
      return render(request,'iwmiproject/plant_level_yield.html',locals())
   

def bed_level_yield(request):
   
   if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('signup:login'))
      
   if request.method == 'POST': 
      bedyieldlevelform = BedYieldLevelForm(request.POST)
      print('***********')
      if bedyieldlevelform.is_valid():
         date = bedyieldlevelform.cleaned_data['date']
         farm = bedyieldlevelform.cleaned_data['farm']
         plot = bedyieldlevelform.cleaned_data['plot']
         Crop = bedyieldlevelform.cleaned_data['Crop'] 
         data_row_number = bedyieldlevelform.cleaned_data['data_row_number']
         harvesting_method = bedyieldlevelform.cleaned_data['harvesting_method']
         dry_fresh = bedyieldlevelform.cleaned_data['dry_fresh']
         marketable_produce = bedyieldlevelform.cleaned_data['marketable_produce']
         unmarketable_produce = bedyieldlevelform.cleaned_data['unmarketable_produce']
         marketable_produce_weight = bedyieldlevelform.cleaned_data['marketable_produce_weight']
         unmarketable_produce_weight = bedyieldlevelform.cleaned_data['unmarketable_produce_weight']
         
         try:
            YieldRowBedLevel.objects.get(date=date,farm=farm,plotID=Plot.objects.get(plotID=plot,farm=farm),Crop=Crop)
         except YieldRowBedLevel.DoesNotExist:
            yieldrowbedlevel_instance = YieldRowBedLevel(date=date,Crop=Crop,farm=farm,plotID=Plot.objects.get(plotID=plot,farm=farm),harvesting_method=harvesting_method,fresh_dry=dry_fresh,marketable_produced=marketable_produce,ummarketable_produced=unmarketable_produce,row_number=data_row_number,marketable_produced_weight=marketable_produce_weight,unmarketable_produced_weight=unmarketable_produce_weight,enteredpersonel=SystemUser.objects.get(user=request.user))
            yieldrowbedlevel_instance.save()
         else:
            message = "Looks like the event already exist"
            user_instance = SystemUser.objects.get(user=request.user)
            if user_instance.role == 'RA' or user_instance.role == 'ST':user_village = user_instance.village
            elif user_instance.role == 'ALL':user_country = user_instance.country
            elif user_instance.role == 'RS':researcher = user_instance.country
            return render(request,'iwmiproject/consumed_crop_by_household.html',locals())
         print('*****aaaaaa******')
         #user_instance = SystemUser.objects.get(user=request.user)
         #if user_instance.role == 'RA' or user_instance.role == 'ST':user_village = user_instance.village
         #elif user_instance.role == 'ALL':user_country = user_instance.country
         #return render(request,'iwmiproject/bedyieldlevel.html',locals())
         message='saved'
         return render(request,'iwmiproject/saved.html',locals())
        
      else:
         user_instance = SystemUser.objects.get(user=request.user)
         if user_instance.role == 'RA' or user_instance.role == 'ST':user_village = user_instance.village
         elif user_instance.role == 'ALL':user_country = user_instance.country
         elif user_instance.role == 'RS':researcher = user_instance.country
         #context = {'bedyieldlevelform':bedyieldlevelform}
         return render(request,'iwmiproject/bedyieldlevel.html',locals())
   else:
      user_instance = SystemUser.objects.get(user=request.user)
      if user_instance.role == 'RA' or user_instance.role == 'ST':user_village = user_instance.village
      elif user_instance.role == 'ALL':user_country = user_instance.country
      elif user_instance.role == 'RS':researcher = user_instance.country
      bedyieldlevelform= BedYieldLevelForm()
      return render(request,'iwmiproject/bedyieldlevel.html',locals())
   

def farmyieldlevel(request):
   if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('signup:login'))
      
   if request.method == 'POST': 
      farmyieldlevelform = FarmYieldLevelForm(request.POST)
      
      if farmyieldlevelform.is_valid():
         date = farmyieldlevelform.cleaned_data['date']
         farm = farmyieldlevelform.cleaned_data['farm']
         plot = farmyieldlevelform.cleaned_data['plot']
         Crop = farmyieldlevelform.cleaned_data['Crop']
         
         marketable_yield = farmyieldlevelform.cleaned_data['marketable_yield']
         unmarketable_yield = farmyieldlevelform.cleaned_data['unmarketable_yield']
         biomas = farmyieldlevelform.cleaned_data['biomas']
         dry_fresh = farmyieldlevelform.cleaned_data['dry_fresh']
         quantity_harvested = farmyieldlevelform.cleaned_data['quantity_harvested']
         payement = farmyieldlevelform.cleaned_data['payement']
         labour = farmyieldlevelform.cleaned_data['labour']
         hired_female_number = farmyieldlevelform.cleaned_data['hired_female_number']
         hired_male_number = farmyieldlevelform.cleaned_data['hired_male_number']
         family_female_number = farmyieldlevelform.cleaned_data['family_female_number']
         family_male_number = farmyieldlevelform.cleaned_data['family_male_number']
         #currency = farmyieldlevelform.cleaned_data['currency']
         #labour_time_taken = farmyieldlevelform.cleaned_data['labour_time_taken']
         
         family_female_time = farmyieldlevelform.cleaned_data['family_female_time']
         family_male_time = farmyieldlevelform.cleaned_data['family_male_time']
         hired_female_time = farmyieldlevelform.cleaned_data['hired_female_time']
         hired_male_time = farmyieldlevelform.cleaned_data['hired_male_time']
         
         user_instance = SystemUser.objects.get(user=request.user)
         currency = pick_currency(user_instance)
         
         try:
            YieldFarmLevel.objects.get(date=date,farm=farm,plotID=Plot.objects.get(plotID=plot,farm=farm),Crop=Crop)
         except YieldFarmLevel.DoesNotExist:
            yieldfarmlevel_instance = YieldFarmLevel(quantity_harvested=quantity_harvested,date=date,Crop=Crop,farm=farm,plotID=Plot.objects.get(plotID=plot,farm=farm),fresh_dry=dry_fresh,marketable_yield=marketable_yield,unmarketable_yield=unmarketable_yield,biomas=biomas,enteredpersonel=SystemUser.objects.get(user=request.user))
            yieldfarmlevel_instance.save()
         else:
            message = "Looks like the info already exist"
            user_instance = SystemUser.objects.get(user=request.user)
            if user_instance.role == 'RA' or user_instance.role == 'ST':user_village = user_instance.village
            elif user_instance.role == 'ALL':user_country = user_instance.country
            elif user_instance.role == 'RS':researcher = user_instance.country
            return render(request,'iwmiproject/farmyieldlevel.html',locals())
         
         if labour == 'Family':
            LabourManagament_instance = LabourManagament(date=date,farm=farm,family_female_time=family_female_time,family_male_time=family_male_time,areaID=plot,areadescription='Plot',labour=labour,family_female_number=family_female_number,family_male_number=family_male_number,activity='Field harvesting',wage=payement,price_unit=currency,enteredpersonel=SystemUser.objects.get(user=request.user))
         
         elif labour == 'Hired':
            LabourManagament_instance = LabourManagament(date=date,farm=farm,hired_female_time=hired_female_time,hired_male_time=hired_male_time,areaID=plot,areadescription='Plot',labour=labour,hired_female_number=hired_female_number,hired_male_number=hired_male_number,activity='Field harvesting',wage=payement,price_unit=currency,enteredpersonel=SystemUser.objects.get(user=request.user))
         
         elif labour == 'FamilyHired':
            LabourManagament_instance = LabourManagament(date=date,farm=farm,family_female_time=family_female_time,family_male_time=family_male_time,hired_female_time=hired_female_time,hired_male_time=hired_male_time,areaID=plot,areadescription='Plot',labour=labour,hired_female_number=hired_female_number,hired_male_number=hired_male_number,family_female_number=family_female_number,family_male_number=family_male_number,activity='Field harvesting',wage=payement,price_unit=currency,enteredpersonel=SystemUser.objects.get(user=request.user))
        
         LabourManagament_instance.save()
         #user_instance = SystemUser.objects.get(user=request.user)
         #if user_instance.role == 'RA' or user_instance.role == 'ST':user_village = user_instance.village
         #elif user_instance.role == 'ALL':user_country = user_instance.country
         #return render(request,'iwmiproject/farmyieldlevel.html',locals())
         message='saved'
         return render(request,'iwmiproject/saved.html',locals())
         
      else:
         user_instance = SystemUser.objects.get(user=request.user)
         currency = pick_currency(user_instance)
         if user_instance.role == 'RA' or user_instance.role == 'ST':user_village = user_instance.village
         elif user_instance.role == 'ALL':user_country = user_instance.country
         elif user_instance.role == 'RS':researcher = user_instance.country
         #context = {'farmyieldlevelform':farmyieldlevelform}
         return render(request,'iwmiproject/farmyieldlevel.html',locals())
   else:
      user_instance = SystemUser.objects.get(user=request.user)
      currency = pick_currency(user_instance)
      if user_instance.role == 'RA' or user_instance.role == 'ST':user_village = user_instance.village
      elif user_instance.role == 'ALL':user_country = user_instance.country
      elif user_instance.role == 'RS':researcher = user_instance.country
      farmyieldlevelform = FarmYieldLevelForm()
      return render(request,'iwmiproject/farmyieldlevel.html',locals())
   

def technology_failure(request):
   
   if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('signup:login'))
      
   if request.method == 'POST': 
      technologyfailureform = TechnologyFailureForm(request.POST)
      print('***********')
      if technologyfailureform.is_valid():
         date = technologyfailureform.cleaned_data['date']
         farm = technologyfailureform.cleaned_data['farm']
         technology = technologyfailureform.cleaned_data['technology']
         reason = technologyfailureform.cleaned_data['reason']
         
         try:
            technologyfailure_instance = TechnologyFailure.objects.get(farm=farm,date=date)
         except TechnologyFailure.DoesNotExist:
            technologyfailure_instance = TechnologyFailure(date=date,farm=farm,technology=Technology.objects.get(name=technology),reason=reason,enteredpersonel=SystemUser.objects.get(user=request.user))
            technologyfailure_instance.save()
         else:
            message = 'Looks like information already exist'
            user_instance = SystemUser.objects.get(user=request.user)
            if user_instance.role == 'RA' or user_instance.role == 'ST':user_village = user_instance.village
            elif user_instance.role == 'ALL':user_country = user_instance.country
            elif user_instance.role == 'RS':researcher = user_instance.country
            return render(request,'iwmiproject/technology_failure.html',locals())
         
         message='saved'
         return render(request,'iwmiproject/saved.html',locals())
        
      else:
         user_instance = SystemUser.objects.get(user=request.user)
         if user_instance.role == 'RA' or user_instance.role == 'ST':user_village = user_instance.village
         elif user_instance.role == 'ALL':user_country = user_instance.country
         elif user_instance.role == 'RS':researcher = user_instance.country
         return render(request,'iwmiproject/technology_failure.html',locals())
   else:
      user_instance = SystemUser.objects.get(user=request.user)
      if user_instance.role == 'RA' or user_instance.role == 'ST':user_village = user_instance.village
      elif user_instance.role == 'ALL':user_country = user_instance.country
      elif user_instance.role == 'RS':researcher = user_instance.country
      technologyfailureform = TechnologyFailureForm()
      return render(request,'iwmiproject/technology_failure.html',locals())
   

def tissuenutrientanalysis(request):
   
   if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('signup:login'))
      
   if request.method == 'POST': 
      tissuenutrientanalysisform = TissueNutrientAnalysisForm(request.POST)
   
      if tissuenutrientanalysisform.is_valid():
         date = tissuenutrientanalysisform.cleaned_data['date']
         farm = tissuenutrientanalysisform.cleaned_data['farm']
         plot = tissuenutrientanalysisform.cleaned_data['plot']
         Crop = tissuenutrientanalysisform.cleaned_data['Crop']
         plant_tissue_part = tissuenutrientanalysisform.cleaned_data['plant_tissue_part']
         plant_number = tissuenutrientanalysisform.cleaned_data['plant_number']
         bed_number = tissuenutrientanalysisform.cleaned_data['bed_number']
         fresh_weight = tissuenutrientanalysisform.cleaned_data['fresh_weight']
         dry_weight = tissuenutrientanalysisform.cleaned_data['dry_weight']
         n = tissuenutrientanalysisform.cleaned_data['n']
         p = tissuenutrientanalysisform.cleaned_data['p']
         k = tissuenutrientanalysisform.cleaned_data['k']
         s = tissuenutrientanalysisform.cleaned_data['s']
         mg = tissuenutrientanalysisform.cleaned_data['mg']
         ca = tissuenutrientanalysisform.cleaned_data['ca']
         fe = tissuenutrientanalysisform.cleaned_data['fe']
         zn = tissuenutrientanalysisform.cleaned_data['zn']
         
         try:
            TissueNutrientAnalysis.objects.get(farm=farm,date=date,plotID=Plot.objects.get(plotID=plot,farm=farm),plantnumber=plant_number,Crop=Crop,bed_number=bed_number)
         except TissueNutrientAnalysis.DoesNotExist:
            tissuenutrientanalysis_instance = TissueNutrientAnalysis(Crop=Crop,farm=farm,date=date,plotID=Plot.objects.get(plotID=plot,farm=farm),plant_tissue_part=plant_tissue_part,plantnumber=plant_number,bed_number=bed_number,freshweight=fresh_weight,dryweight=dry_weight,n=n,p=p,k=k,s=s,mg=mg,ca=ca,fe=fe,zn=zn,enteredpersonel=SystemUser.objects.get(user=request.user))
            tissuenutrientanalysis_instance.save()
         else:
            message = 'Looks like information already exist'
            user_instance = SystemUser.objects.get(user=request.user)
            if user_instance.role == 'RA' or user_instance.role == 'ST':user_village = user_instance.village
            elif user_instance.role == 'ALL':user_country = user_instance.country
            elif user_instance.role == 'RS':researcher = user_instance.country
            return render(request,'iwmiproject/tissuenutrientanalysis.html',locals())
         
        
         #user_instance = SystemUser.objects.get(user=request.user)
         #if user_instance.role == 'RA' or user_instance.role == 'ST':user_village = user_instance.village
         #elif user_instance.role == 'ALL':user_country = user_instance.country
         #return render(request,'iwmiproject/tissuenutrientanalysis.html',locals())
         message='saved'
         return render(request,'iwmiproject/saved.html',locals())
        
      else:
         user_instance = SystemUser.objects.get(user=request.user)
         if user_instance.role == 'RA' or user_instance.role == 'ST':user_village = user_instance.village
         elif user_instance.role == 'ALL':user_country = user_instance.country
         elif user_instance.role == 'RS':researcher = user_instance.country
         context = {'tissuenutrientanalysisform':tissuenutrientanalysisform}
         return render(request,'iwmiproject/tissuenutrientanalysis.html',locals())
   else:
      user_instance = SystemUser.objects.get(user=request.user)
      if user_instance.role == 'RA' or user_instance.role == 'ST':user_village = user_instance.village
      elif user_instance.role == 'ALL':user_country = user_instance.country
      elif user_instance.role == 'RS':researcher = user_instance.country
      tissuenutrientanalysisform = TissueNutrientAnalysisForm()
      return render(request,'iwmiproject/tissuenutrientanalysis.html',locals())
   
def cropmonitoring(request):
   if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('signup:login'))
      
   if request.method == 'POST': 
      cropmonitoringplantheightform = CropMonitoringPlantHeightForm(request.POST)
   
      if cropmonitoringplantheightform.is_valid():
         date = cropmonitoringplantheightform.cleaned_data['date']
         farm = cropmonitoringplantheightform.cleaned_data['farm']
         Crop = cropmonitoringplantheightform.cleaned_data['Crop']
         crop_stage = cropmonitoringplantheightform.cleaned_data['crop_stage']
         plot = cropmonitoringplantheightform.cleaned_data['plot']

         row_number  = cropmonitoringplantheightform.cleaned_data['row_number']
         number_of_good_plants = cropmonitoringplantheightform.cleaned_data['number_of_good_plants']
         number_of_bad_plants = cropmonitoringplantheightform.cleaned_data['number_of_bad_plants']
         
         LAI_one = cropmonitoringplantheightform.cleaned_data['LAI_one']
         plant_height_one = cropmonitoringplantheightform.cleaned_data['plant_height_one']
         plant_canopy_width_one = cropmonitoringplantheightform.cleaned_data['plant_canopy_width_one']
         lenght_of_crop_stage_one = cropmonitoringplantheightform.cleaned_data['lenght_of_crop_stage_one']
         plant_leave_number_one = cropmonitoringplantheightform.cleaned_data['plant_leave_number_one']
         plant_leave_length_one = cropmonitoringplantheightform.cleaned_data['plant_leave_length_one']
         plant_leave_width_one = cropmonitoringplantheightform.cleaned_data['plant_leave_width_one']
         
         LAI_two = cropmonitoringplantheightform.cleaned_data['LAI_two']
         plant_height_two = cropmonitoringplantheightform.cleaned_data['plant_height_two']
         plant_canopy_width_two = cropmonitoringplantheightform.cleaned_data['plant_canopy_width_two']
         lenght_of_crop_stage_two = cropmonitoringplantheightform.cleaned_data['lenght_of_crop_stage_two']
         plant_leave_number_two = cropmonitoringplantheightform.cleaned_data['plant_leave_number_two']
         plant_leave_length_two = cropmonitoringplantheightform.cleaned_data['plant_leave_length_two']
         plant_leave_width_two = cropmonitoringplantheightform.cleaned_data['plant_leave_width_two']
         
         LAI_three = cropmonitoringplantheightform.cleaned_data['LAI_three']
         plant_height_three = cropmonitoringplantheightform.cleaned_data['plant_height_three']
         plant_canopy_width_three = cropmonitoringplantheightform.cleaned_data['plant_canopy_width_three']
         lenght_of_crop_stage_three = cropmonitoringplantheightform.cleaned_data['lenght_of_crop_stage_three']
         plant_leave_number_three = cropmonitoringplantheightform.cleaned_data['plant_leave_number_three']
         plant_leave_length_three = cropmonitoringplantheightform.cleaned_data['plant_leave_length_three']
         plant_leave_width_three = cropmonitoringplantheightform.cleaned_data['plant_leave_width_three']
         
         totalPlant = cropmonitoringplantheightform.cleaned_data['totalPlant'] 
         sub_plot_size = cropmonitoringplantheightform.cleaned_data['sub_plot_size']
         sub_plot_plant_number = cropmonitoringplantheightform.cleaned_data['sub_plot_plant_number']
         total_plant_number = cropmonitoringplantheightform.cleaned_data['total_plant_number']
         
         plant_density_per_bed = cropmonitoringplantheightform.cleaned_data['plant_density_per_bed']
         plant_density_per_sqm = cropmonitoringplantheightform.cleaned_data['plant_density_per_sqm']
         
         #bed_width=BedPlot.objects.get(plotID=Plot.objects.get(plotID=plot,farm=farm)).length
         #bed_length=BedPlot.objects.get(plotID=Plot.objects.get(plotID=plot,farm=farm)).width
         #plant_density_per_sqm = round(((number_of_good_plants + number_of_bad_plants)/ (bed_width * bed_length)),2)
         #plant_density_per_bed = (number_of_good_plants + number_of_bad_plants)
         
         
         try:
            CropMonitoringPlantHeight.objects.get(date=date,farm=farm,plotID=Plot.objects.get(plotID=plot,farm=farm),crop_stage=crop_stage,row_number=row_number,Crop=Crop)
         except CropMonitoringPlantHeight.DoesNotExist:
            if totalPlant == -999: #in case it's monocropping/intercropping and total plants obtained from planting method tab is None
               cropmonitoringplantheight_instance=CropMonitoringPlantHeight(date=date,Crop=Crop,farm=farm,plotID=Plot.objects.get(plotID=plot,farm=farm),crop_stage=crop_stage,row_number=row_number,number_of_good_plants=number_of_good_plants,number_of_bad_plants=number_of_bad_plants,plant_density_per_sqm=plant_density_per_sqm,plant_density_per_bed=plant_density_per_bed, \
                                                                         plant_number=1,LAI=LAI_one,plant_height=plant_height_one,plant_canopy_width=plant_canopy_width_one,length_of_crop_stage=lenght_of_crop_stage_one,plant_leave_number=plant_leave_number_one,plant_leave_length=plant_leave_length_one,plant_leave_width=plant_leave_width_one, \
                                                                         plant_number_two=2,LAI_two=LAI_two,plant_height_two=plant_height_two,plant_canopy_width_two=plant_canopy_width_two,length_of_crop_stage_two=lenght_of_crop_stage_two,plant_leave_number_two=plant_leave_number_two,plant_leave_length_two=plant_leave_length_two,plant_leave_width_two=plant_leave_width_two, \
                                                                         plant_number_three=3,LAI_three=LAI_three,plant_height_three=plant_height_three,plant_canopy_width_three=plant_canopy_width_three,length_of_crop_stage_three=lenght_of_crop_stage_three,plant_leave_number_three=plant_leave_number_three,plant_leave_length_three=plant_leave_length_three,plant_leave_width_three=plant_leave_width_three, \
                                                                         sub_plot_size=sub_plot_size,sub_plot_plant_number=sub_plot_plant_number,total_plant_number=total_plant_number,enteredpersonel=SystemUser.objects.get(user=request.user))
            else:
               cropmonitoringplantheight_instance=CropMonitoringPlantHeight(date=date,Crop=Crop,farm=farm,plotID=Plot.objects.get(plotID=plot,farm=farm),crop_stage=crop_stage,row_number=row_number,number_of_good_plants=number_of_good_plants,number_of_bad_plants=number_of_bad_plants,plant_density_per_sqm=plant_density_per_sqm,plant_density_per_bed=plant_density_per_bed, \
                                                                         plant_number=1,LAI=LAI_one,plant_height=plant_height_one,plant_canopy_width=plant_canopy_width_one,length_of_crop_stage=lenght_of_crop_stage_one,plant_leave_number=plant_leave_number_one,plant_leave_length=plant_leave_length_one,plant_leave_width=plant_leave_width_one, \
                                                                         plant_number_two=2,LAI_two=LAI_two,plant_height_two=plant_height_two,plant_canopy_width_two=plant_canopy_width_two,length_of_crop_stage_two=lenght_of_crop_stage_two,plant_leave_number_two=plant_leave_number_two,plant_leave_length_two=plant_leave_length_two,plant_leave_width_two=plant_leave_width_two, \
                                                                         plant_number_three=3,LAI_three=LAI_three,plant_height_three=plant_height_three,plant_canopy_width_three=plant_canopy_width_three,length_of_crop_stage_three=lenght_of_crop_stage_three,plant_leave_number_three=plant_leave_number_three,plant_leave_length_three=plant_leave_length_three,plant_leave_width_three=plant_leave_width_three, \
                                                                         enteredpersonel=SystemUser.objects.get(user=request.user))
            cropmonitoringplantheight_instance.save()
         else:
            user_instance = SystemUser.objects.get(user=request.user)
            message = 'Looks like information already exist'
            if user_instance.role == 'RA' or user_instance.role == 'ST':user_village = user_instance.village
            elif user_instance.role == 'ALL':user_country = user_instance.country
            elif user_instance.role == 'RS':researcher = user_instance.country
            return render(request,'iwmiproject/cropmonitoring.html',locals())
       
         #user_instance = SystemUser.objects.get(user=request.user)
         #if user_instance.role == 'RA' or user_instance.role == 'ST':user_village = user_instance.village
         #elif user_instance.role == 'ALL':user_country = user_instance.country
         #return render(request,'iwmiproject/cropmonitoring.html',locals())
         message='saved'
         return render(request,'iwmiproject/saved.html',locals())
        
      else:
         user_instance = SystemUser.objects.get(user=request.user)
         if user_instance.role == 'RA' or user_instance.role == 'ST':user_village = user_instance.village
         elif user_instance.role == 'ALL':user_country = user_instance.country
         elif user_instance.role == 'RS':researcher = user_instance.country
         context = {'cropmonitoringplantheightform':cropmonitoringplantheightform}
         return render(request,'iwmiproject/cropmonitoring.html',locals())
   else:
      user_instance = SystemUser.objects.get(user=request.user)
      if user_instance.role == 'RA' or user_instance.role == 'ST':user_village = user_instance.village
      elif user_instance.role == 'ALL':user_country = user_instance.country
      elif user_instance.role == 'RS':researcher = user_instance.country
      cropmonitoringplantheightform = CropMonitoringPlantHeightForm()
      return render(request,'iwmiproject/cropmonitoring.html',locals())
   
def  landpreparation(request):
   if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('signup:login'))
      
   if request.method == 'POST': 
      landpreparationform = LandPreparationForm(request.POST)
   
      if landpreparationform.is_valid():
         date = landpreparationform.cleaned_data['date']
         farm = landpreparationform.cleaned_data['farm']
         landpreparationtool = landpreparationform.cleaned_data['landpreparationtool']
         other = landpreparationform.cleaned_data['other']
         plot = landpreparationform.cleaned_data['plot']
         labour = landpreparationform.cleaned_data['labour']
         hired_female_number = landpreparationform.cleaned_data['hired_female_number']
         hired_male_number = landpreparationform.cleaned_data['hired_male_number']
         family_female_number = landpreparationform.cleaned_data['family_female_number']
         family_male_number = landpreparationform.cleaned_data['family_male_number']
         #labour_time_taken = landpreparationform.cleaned_data['labour_time_taken']
         wage = landpreparationform.cleaned_data['wage']
         #currency = landpreparationform.cleaned_data['currency']
         
         family_female_time = landpreparationform.cleaned_data['family_female_time']
         family_male_time = landpreparationform.cleaned_data['family_male_time']
         hired_female_time = landpreparationform.cleaned_data['hired_female_time']
         hired_male_time = landpreparationform.cleaned_data['hired_male_time']
         
         user_instance = SystemUser.objects.get(user=request.user)
         currency = pick_currency(user_instance)
         
         if other =='99999999':
            landpreparationtool = landpreparationtool
         else:
            landpreparationtool = other
            
         try:
            landpreparation_instance = LandPreparation.objects.get(farm=farm,date=date,plotID=Plot.objects.get(plotID=plot,farm=farm),landpreparationtool=landpreparationtool,enteredpersonel=SystemUser.objects.get(user=request.user))
         except LandPreparation.DoesNotExist:
            landpreparation_instance = LandPreparation(farm=farm,date=date,plotID=Plot.objects.get(plotID=plot,farm=farm),landpreparationtool=landpreparationtool,enteredpersonel=SystemUser.objects.get(user=request.user))
         else:
            message = 'Looks like information already exist'
            if user_instance.role == 'RA' or user_instance.role == 'ST':user_village = user_instance.village
            elif user_instance.role == 'ALL':user_country = user_instance.country
            elif user_instance.role == 'RS':researcher = user_instance.country
            return render(request,'iwmiproject/landpreparation.html',locals())
         if labour == 'Family':
            LabourManagament_instance = LabourManagament(date=date,family_female_time=family_female_time,family_male_time=family_male_time,farm=farm,areaID=plot,areadescription='Plot',labour=labour,family_female_number=family_female_number,family_male_number=family_male_number,activity='land preparation',wage=wage,price_unit=currency,enteredpersonel=SystemUser.objects.get(user=request.user))
         
         elif labour == 'Hired':
            LabourManagament_instance = LabourManagament(date=date,hired_female_time=hired_female_time,hired_male_time=hired_male_time,farm=farm,areaID=plot,areadescription='Plot',labour=labour,hired_female_number=hired_female_number,hired_male_number=hired_male_number,activity='land preparation',wage=wage,price_unit=currency,enteredpersonel=SystemUser.objects.get(user=request.user))
         
         elif labour == 'FamilyHired':
            LabourManagament_instance = LabourManagament(date=date,family_female_time=family_female_time,family_male_time=family_male_time,hired_female_time=hired_female_time,hired_male_time=hired_male_time,farm=farm,areaID=plot,areadescription='Plot',labour=labour,hired_female_number=hired_female_number,hired_male_number=hired_male_number,family_female_number=family_female_number,family_male_number=family_male_number,activity='land preparation',wage=wage,price_unit=currency,enteredpersonel=SystemUser.objects.get(user=request.user))
         landpreparation_instance.save()
         LabourManagament_instance.save()
         #if user_instance.role == 'RA' or user_instance.role == 'ST':user_village = user_instance.village
         #elif user_instance.role == 'ALL':user_country = user_instance.country  
         #return render(request,'iwmiproject/landpreparation.html',locals())
         message='saved'
         return render(request,'iwmiproject/saved.html',locals())
        
      else:
         user_instance = SystemUser.objects.get(user=request.user)
         currency = pick_currency(user_instance)
         if user_instance.role == 'RA' or user_instance.role == 'ST':user_village = user_instance.village
         elif user_instance.role == 'ALL':user_country = user_instance.country
         elif user_instance.role == 'RS':researcher = user_instance.country
         return render(request,'iwmiproject/landpreparation.html',locals())
   else:
      user_instance = SystemUser.objects.get(user=request.user)
      currency = pick_currency(user_instance)
      if user_instance.role == 'RA' or user_instance.role == 'ST':user_village = user_instance.village
      elif user_instance.role == 'ALL':user_country = user_instance.country
      elif user_instance.role == 'RS':researcher = user_instance.country
      landpreparationform = LandPreparationForm()
      return render(request,'iwmiproject/landpreparation.html',locals())

def landclearance(request):
   if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('signup:login'))
      
   if request.method == 'POST': 
      landcleareanceform = LandCleareanceForm(request.POST)
   
      if landcleareanceform.is_valid():
         date = landcleareanceform.cleaned_data['date']
         farm = landcleareanceform.cleaned_data['farm']
         landpreparationtool = landcleareanceform.cleaned_data['landpreparationtool']
         plot = landcleareanceform.cleaned_data['plot']
         
         labour = landcleareanceform.cleaned_data['labour']
         hired_female_number = landcleareanceform.cleaned_data['hired_female_number']
         hired_male_number = landcleareanceform.cleaned_data['hired_male_number']
         family_female_number = landcleareanceform.cleaned_data['family_female_number']
         family_male_number = landcleareanceform.cleaned_data['family_male_number']
         wage = landcleareanceform.cleaned_data['wage']
         #currency = landcleareanceform.cleaned_data['currency']
         
         family_female_time = landcleareanceform.cleaned_data['family_female_time']
         family_male_time = landcleareanceform.cleaned_data['family_male_time']
         hired_female_time = landcleareanceform.cleaned_data['hired_female_time']
         hired_male_time = landcleareanceform.cleaned_data['hired_male_time']
         
         user_instance = SystemUser.objects.get(user=request.user)
         currency = pick_currency(user_instance)
         
         try:
            landclearance_instance = LandClearance.objects.get(farm=farm,date=date,plotID=Plot.objects.get(plotID=plot,farm=farm),landclearanceoption=landpreparationtool,enteredpersonel=SystemUser.objects.get(user=request.user))
         
         except LandClearance.DoesNotExist:
            landclearance_instance = LandClearance(farm=farm,date=date,plotID=Plot.objects.get(plotID=plot,farm=farm),landclearanceoption=landpreparationtool,enteredpersonel=SystemUser.objects.get(user=request.user))
         else:
            message = 'Looks like information already exist'
            if user_instance.role == 'RA' or user_instance.role == 'ST':user_village = user_instance.village
            elif user_instance.role == 'ALL':user_country = user_instance.country
            elif user_instance.role == 'RS':researcher = user_instance.country
            return render(request,'iwmiproject/landcleareance.html',locals())
         
         if labour == 'Family':
            LabourManagament_instance = LabourManagament(date=date,family_female_time=family_female_time,family_male_time=family_male_time,farm=farm,areaID=plot,areadescription='Plot',labour=labour,family_female_number=family_female_number,family_male_number=family_male_number,activity='land clearance',wage=wage,price_unit=currency,enteredpersonel=SystemUser.objects.get(user=request.user))
         
         elif labour == 'Hired':#
            LabourManagament_instance = LabourManagament(date=date,hired_female_time=hired_female_time,hired_male_time=hired_male_time,farm=farm,areaID=plot,areadescription='Plot',labour=labour,hired_female_number=hired_female_number,hired_male_number=hired_male_number,activity='land clearance',wage=wage,price_unit=currency,enteredpersonel=SystemUser.objects.get(user=request.user))
         
         elif labour == 'FamilyHired':
            LabourManagament_instance = LabourManagament(date=date,family_female_time=family_female_time,family_male_time=family_male_time,hired_female_time=hired_female_time,hired_male_time=hired_male_time,farm=farm,areaID=plot,areadescription='Plot',labour=labour,hired_female_number=hired_female_number,hired_male_number=hired_male_number,family_female_number=family_female_number,family_male_number=family_male_number,activity='land clearance',wage=wage,price_unit=currency,enteredpersonel=SystemUser.objects.get(user=request.user))
            
         landclearance_instance.save()
         LabourManagament_instance.save()
         #if user_instance.role == 'RA' or user_instance.role == 'ST':user_village = user_instance.village
         #elif user_instance.role == 'ALL':user_country = user_instance.country
         #return render(request,'iwmiproject/landcleareance.html',locals())
         message='saved'
         return render(request,'iwmiproject/saved.html',locals())
        
      else:
         currency = pick_currency(user_instance)
         if user_instance.role == 'RA' or user_instance.role == 'ST':user_village = user_instance.village
         elif user_instance.role == 'ALL':user_country = user_instance.country
         elif user_instance.role == 'RS':researcher = user_instance.country
         return render(request,'iwmiproject/landcleareance.html',locals())
   else:
      user_instance = SystemUser.objects.get(user=request.user)
      if user_instance.role == 'RA' or user_instance.role == 'ST':user_village = user_instance.village
      elif user_instance.role == 'ALL':user_country = user_instance.country
      elif user_instance.role == 'RS':researcher = user_instance.country
      landcleareanceform = LandCleareanceForm()
      currency = pick_currency(user_instance)
      return render(request,'iwmiproject/landcleareance.html',locals())
   
def residue_handling(request):
   if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('signup:login'))
   
   if request.method == 'POST': 
      residuehandlingform= ResidueHandlingForm(request.POST)

      if residuehandlingform.is_valid():
         date = residuehandlingform.cleaned_data['date']
         farm = residuehandlingform.cleaned_data['farm']
         residual_activities = residuehandlingform.cleaned_data['residual_activities']
         plot = residuehandlingform.cleaned_data['plot']
         time = residuehandlingform.cleaned_data['time']
         other = residuehandlingform.cleaned_data['other']
         labour = residuehandlingform.cleaned_data['labour']
         hired_female_number = residuehandlingform.cleaned_data['hired_female_number']
         hired_male_number = residuehandlingform.cleaned_data['hired_male_number']
         family_female_number = residuehandlingform.cleaned_data['family_female_number']
         family_male_number = residuehandlingform.cleaned_data['family_male_number']
         #labour_time_taken = residuehandlingform.cleaned_data['labour_time_taken']
         wage = residuehandlingform.cleaned_data['wage']
         #currency = residuehandlingform.cleaned_data['currency']
         
         family_female_time = residuehandlingform.cleaned_data['family_female_time']
         family_male_time = residuehandlingform.cleaned_data['family_male_time']
         hired_female_time = residuehandlingform.cleaned_data['hired_female_time']
         hired_male_time = residuehandlingform.cleaned_data['hired_male_time']
         
         user_instance = SystemUser.objects.get(user=request.user)
         currency = pick_currency(user_instance)
         
         try:
            ResidualHandling.objects.get(farm=farm,date=date,plotID=Plot.objects.get(plotID=plot),residual_activities=residual_activities,time=time)
         except ResidualHandling.DoesNotExist:
            if other=='N///A':
               residuehandling_instance = ResidualHandling(farm=farm,date=date,plotID=Plot.objects.get(plotID=plot,farm=farm),residual_activities=residual_activities,time=time,enteredpersonel= SystemUser.objects.get(user=request.user))
            else:
               residuehandling_instance = ResidualHandling(farm=farm,date=date,plotID=Plot.objects.get(plotID=plot,farm=farm),residual_activities=other,time=time,enteredpersonel= SystemUser.objects.get(user=request.user))
            residuehandling_instance.save()
         else:
            message = 'Looks like information already exist'
            user_instance = SystemUser.objects.get(user=request.user)
            if user_instance.role == 'RA' or user_instance.role == 'ST':user_village = user_instance.village
            elif user_instance.role == 'ALL':user_country = user_instance.country
            elif user_instance.role == 'RS':researcher = user_instance.country
            return render (request,'iwmiproject/residue_handling.html',locals())
            
         if labour == 'Family':
            if not wage:
               LabourManagament_instance = LabourManagament(date=date,family_female_time=family_female_time,family_male_time=family_male_time,farm=farm,areaID=plot,areadescription='Plot',labour=labour,family_female_number=family_female_number,family_male_number=family_male_number,activity='Residue handling',wage=0,price_unit='',enteredpersonel=SystemUser.objects.get(user=request.user))
            
            else:
               LabourManagament_instance = LabourManagament(date=date,family_female_time=family_female_time,family_male_time=family_male_time,farm=farm,areaID=plot,areadescription='Plot',labour=labour,family_female_number=family_female_number,family_male_number=family_male_number,activity='Residue handling',wage=wage,price_unit=currency,enteredpersonel=SystemUser.objects.get(user=request.user))
         
         elif labour == 'Hired':
            LabourManagament_instance = LabourManagament(date=date,hired_female_time=hired_female_time,hired_male_time=hired_male_time,farm=farm,areaID=plot,areadescription='Plot',labour=labour,hired_female_number=hired_female_number,hired_male_number=hired_male_number,activity='Residue handling',wage=wage,price_unit=currency,enteredpersonel=SystemUser.objects.get(user=request.user))
         
         elif labour == 'FamilyHired':
            LabourManagament_instance = LabourManagament(date=date,family_female_time=family_female_time,family_male_time=family_male_time,hired_female_time=hired_female_time,hired_male_time=hired_male_time,farm=farm,areaID=plot,areadescription='Plot',labour=labour,hired_female_number=hired_female_number,hired_male_number=hired_male_number,family_female_number=family_female_number,family_male_number=family_male_number,activity='Residue handling',wage=wage,price_unit=currency,enteredpersonel=SystemUser.objects.get(user=request.user))
         
         
         LabourManagament_instance.save()
         
         message='saved'
         return render(request,'iwmiproject/saved.html',locals())
        
      else:
         user_instance = SystemUser.objects.get(user=request.user)
         currency = pick_currency(user_instance)
         if user_instance.role == 'RA' or user_instance.role == 'ST':user_village = user_instance.village
         elif user_instance.role == 'ALL':user_country = user_instance.country
         elif user_instance.role == 'RS':researcher = user_instance.country
         return render(request,'iwmiproject/residue_handling.html',locals())
   else:
      user_instance = SystemUser.objects.get(user=request.user)
      currency = pick_currency(user_instance)
      if user_instance.role == 'RA' or user_instance.role == 'ST':user_village = user_instance.village
      elif user_instance.role == 'ALL':user_country = user_instance.country
      elif user_instance.role == 'RS':researcher = user_instance.country
      residuehandlingform= ResidueHandlingForm()
      return render(request,'iwmiproject/residue_handling.html',locals())

def otherwaterusage(request):
   if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('signup:login'))
   
   if request.method == 'POST': 
      otherwaterusageform= OtherWaterUsageForm(request.POST)

      if otherwaterusageform.is_valid():
         date = otherwaterusageform.cleaned_data['date']
         farm = otherwaterusageform.cleaned_data['farm']
         #plot = otherwaterusageform.cleaned_data['plot']
         bucketnumber = otherwaterusageform.cleaned_data['bucketnumber']
         bucketvolume = otherwaterusageform.cleaned_data['bucketvolume']
         technology = otherwaterusageform.cleaned_data['technology']
         usagepurpose = otherwaterusageform.cleaned_data['usagepurpose']
         start_time = otherwaterusageform.cleaned_data['start_time']
         end_time = otherwaterusageform.cleaned_data['end_time']
         total_time = otherwaterusageform.cleaned_data['total_time']
         totalvolume = otherwaterusageform.cleaned_data['totalvolume']
         lifting_technology_yes_no = otherwaterusageform.cleaned_data['lifting_technology_yes_no']
         
         #otherwaterusage_instance = OtherWaterUsage(date,farm,plot,bucketnumber,bucketvolume,technology,usagepurpose,start_time,end_time,total_time,totalvolume,lifting_technology_yes_no)
         if lifting_technology_yes_no == 'Yes':
            otherwaterusage_instance = OtherWaterUsage(date=date,farm=farm,bucketnumber=bucketnumber,bucketvolume=bucketvolume,technology=Technology.objects.get(name=technology),usagepurpose=usagepurpose,start_time=start_time,end_time=end_time,total_time=total_time,totalvolume=totalvolume,lifting_technology_yes_no=lifting_technology_yes_no)
         elif lifting_technology_yes_no == 'No':
            otherwaterusage_instance = OtherWaterUsage(date=date,farm=farm,bucketnumber=bucketnumber,bucketvolume=bucketvolume,technology=Technology.objects.get(name=technology),usagepurpose=usagepurpose,totalvolume=totalvolume,lifting_technology_yes_no=lifting_technology_yes_no)
         
         otherwaterusage_instance.save()
         message='saved'
         return render(request,'iwmiproject/saved.html',locals())
        
      else:
         user_instance = SystemUser.objects.get(user=request.user)
         if user_instance.role == 'RA' or user_instance.role == 'ST':user_village = user_instance.village
         elif user_instance.role == 'ALL':user_country = user_instance.country
         elif user_instance.role == 'RS':researcher = user_instance.country
         return render(request,'iwmiproject/otherwaterusage.html',locals())
   else:
      user_instance = SystemUser.objects.get(user=request.user)
      if user_instance.role == 'RA' or user_instance.role == 'ST':user_village = user_instance.village
      elif user_instance.role == 'ALL':user_country = user_instance.country
      elif user_instance.role == 'RS':researcher = user_instance.country
      otherwaterusageform= OtherWaterUsageForm()
      return render(request,'iwmiproject/otherwaterusage.html',locals())


def remarks(request):
   if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('signup:login'))
   
   if request.method == 'POST': 
      remarkform= RemarkForm(request.POST)
      #Remark
      if remarkform.is_valid():
         start_date = remarkform.cleaned_data['start_date']
         end_date = remarkform.cleaned_data['end_date']
         farm = remarkform.cleaned_data['farm']
         plot = remarkform.cleaned_data['plot']
         stress = remarkform.cleaned_data['stress']
         severness = remarkform.cleaned_data['severness']
         other = remarkform.cleaned_data['other']
         
         if other =='99999999':stress=stress
         else:stress=other
         
         try:
            Remark.objects.get(start_date=start_date,end_date=end_date,plot=Plot.objects.get(plotID=plot,farm=farm),farm=farm,stress=stress)
         except Remark.DoesNotExist:
            if other =='99999999':
               remark_instance = Remark(start_date=start_date,end_date=end_date,farm=farm,plot=plot,stress=stress,severness=severness,enteredpersonel=SystemUser.objects.get(user=request.user))
            else:
               remark_instance = Remark(start_date=start_date,end_date=end_date,farm=farm,plot=plot,stress=other,severness=severness,enteredpersonel=SystemUser.objects.get(user=request.user))
            remark_instance.save()
         else:
            message = 'Looks like information already exist'
            user_instance = SystemUser.objects.get(user=request.user)
            if user_instance.role == 'RA' or user_instance.role == 'ST':user_village = user_instance.village
            elif user_instance.role == 'ALL':user_country = user_instance.country
            elif user_instance.role == 'RS':researcher = user_instance.country
            return render (request,'iwmiproject/remarks.html',locals())
            
         message='saved'
         return render(request,'iwmiproject/saved.html',locals())
        
      else:
         user_instance = SystemUser.objects.get(user=request.user)
         if user_instance.role == 'RA' or user_instance.role == 'ST':user_village = user_instance.village
         elif user_instance.role == 'ALL':user_country = user_instance.country
         elif user_instance.role == 'RS':researcher = user_instance.country
         return render(request,'iwmiproject/remarks.html',locals())
   else:
      user_instance = SystemUser.objects.get(user=request.user)
      if user_instance.role == 'RA' or user_instance.role == 'ST':user_village = user_instance.village
      elif user_instance.role == 'ALL':user_country = user_instance.country
      elif user_instance.role == 'RS':researcher = user_instance.country
      remarkform= RemarkForm()
      return render(request,'iwmiproject/remarks.html',locals())
   

def fertilizerspecification(request):
   if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('signup:login'))
   
   user_instance = SystemUser.objects.get(user=request.user)
   currency = pick_currency(user_instance)
   if user_instance.role == 'RA' or user_instance.role == 'ST':user_village = user_instance.village
   elif user_instance.role == 'ALL':user_country = user_instance.country
   elif user_instance.role == 'RS':researcher = user_instance.country
   
   if request.method == 'POST': 
      fertilizerspecificationform = FertilizerSpecificationForm(request.POST)
      
      if fertilizerspecificationform.is_valid():
         plotID = fertilizerspecificationform.cleaned_data['plotID']
         farm = fertilizerspecificationform.cleaned_data['farm']
         fertilizer = fertilizerspecificationform.cleaned_data['fertilizer']
         nitrogen = fertilizerspecificationform.cleaned_data['nitrogen']
         phosphorus = fertilizerspecificationform.cleaned_data['phosphorus']
         potassium = fertilizerspecificationform.cleaned_data['potassium']
         sulphur = fertilizerspecificationform.cleaned_data['sulphur']
         organic_matter = fertilizerspecificationform.cleaned_data['organic_matter']

         if nitrogen == -999:nitrogen = None
         if phosphorus == -999:phosphorus = None
         if phosphorus == -999:phosphorus = None
         if potassium == -999:potassium = None
         if sulphur == -999:sulphur = None
         if organic_matter == -999:organic_matter = None
            
         try:
            FertilizerSpecification.objects.get(farm=farm,plotID=Plot.objects.get(plotID=plotID,farm=farm),fertilizer=fertilizer)
         except FertilizerSpecification.DoesNotExist:
            try:
               Fertilizer.objects.get(name=fertilizer)
            except Fertilizer.DoesNotExist:
               fertilizer_instance = Fertilizer(name=fertilizer)
               fertilizer_instance.save()
            fertilizerspecification_instance = FertilizerSpecification(farm=farm,plotID=Plot.objects.get(plotID=plotID,farm=farm),fertilizer=Fertilizer.objects.get(name=fertilizer),nitrogen=nitrogen,phosphorus=phosphorus,potassium=potassium,sulphur=sulphur,organic_matter=organic_matter,enteredpersonel=SystemUser.objects.get(user=request.user))
            fertilizerspecification_instance.save()
         else:
            message = 'Looks like information already exist'
            return render (request,'iwmiproject/fertilizerspecification.html',locals())

         message='saved'
         return render(request,'iwmiproject/saved.html',locals())
        
      else:
         context = {'fertilizerspecificationform':FertilizerSpecificationForm}
         return render (request,'iwmiproject/fertilizerspecification.html',locals())
      
   else:
      fertilizerspecificationform = FertilizerSpecificationForm()#initial={'hired_female_number':0,'hired_male_number':0,'family_female_number':0,'family_male_number':0},)
      return render (request,'iwmiproject/fertilizerspecification.html',locals())



def download_csv(request):
   if not request.user.is_authenticated():
      return HttpResponseRedirect(reverse('signup:login'))
   
   if request.method == 'POST':
      mytestmodel_instance = MyTestModel.objects.all()
      
      opts = mytestmodel_instance.model._meta
      model = mytestmodel_instance.model
    
      response = HttpResponse(content_type='text/csv')
      
      # force download.
      response['Content-Disposition'] = 'attachment;filename=export.csv'
      # the csv writer
      writer = csv.writer(response)
      field_names = [field.name for field in opts.fields if field.name !='id']
      # Write a first row with header information
      writer.writerow(field_names)
      # Write data rows
      for obj in mytestmodel_instance:
         writer.writerow([getattr(obj, field) for field in field_names if field=='name'])
      return HttpResponse (response, content_type='text/csv')
   else:
      return render (request,'iwmiproject/downloadform.html',locals())

def upload_excel(request):
   if not request.user.is_authenticated():
      return HttpResponseRedirect(reverse('signup:login'))
      
   if request.method == 'POST':
      form = UploadFileForm(request.POST, request.FILES)
      if form.is_valid():
         filehandle = TextIOWrapper(request.FILES['csv_file'].file, encoding=request.encoding)

         reader = csv.reader(filehandle)#,dialect='excel')
         
         for row in reader:
            mytestmodel = MyTestModel()
            if row[0] == 'name':continue
            else:mytestmodel.name = row[0]
            if row[1] == 'age':continue
            else:mytestmodel.age = int(row[1])
            if row[2] == 'length':continue
            else:mytestmodel.length = float(row[2])
            mytestmodel.save()

         message='saved'
         return render(request,'iwmiproject/saved.html',locals())
         #data = [row for row in csv.reader(file.read().splitlines())]
      else:
         return render (request,'iwmiproject/upload_form.html',locals())
   else:
      form = UploadFileForm()
      return render (request,'iwmiproject/upload_form.html',locals())
   
'''
from iwmiproject.models import MyTestModel, MyTestModelCSVImporter
from data_importer.importers import CSVImporter

def addvalues(myfile):
   myfile = '/Users/peterngimbwa/Desktop/NCMC_training/my_csv_file_name.csv'
   mycsvlist = MyTestModelCSVImporter(source=myfile)
   filelength = len(mycsvlist.cleaned_data)
   mytestmodel = MyTestModel()
   for i in range(filelength):
      row, line_data = mycsvlist.cleaned_data[i]
      mytestmodel.name = line_data['name']
      mytestmodel.age = line_data['age']
      mytestmodel.length = line_data['length']
      mytestmodel.save()
      print('Saved')
'''

   
'''
def point_of_interest(request):
   if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('signup:login'))
   
   if request.method == 'POST': 
      pointofinterestform = PointOfInterestForm(request.POST)
      
      if pointofinterestform.is_valid():
         name = pointofinterestform.cleaned_data['name']
         position = pointofinterestform.cleaned_data['position']
         
         pointofinterest_instance = PointOfInterest(name=name,position=position)
         pointofinterest_instance.save()
         message='saved'
         return render(request,'iwmiproject/saved.html',locals())
   else:
      #pointofinterest_instance = PointOfInterest.objects.get(id=1)
      pointofinterestform = PointOfInterestForm()

      user_instance = SystemUser.objects.get(user=request.user)
      if user_instance.role == 'RA' or user_instance.role == 'ST':user_village = user_instance.village
      elif user_instance.role == 'ALL':user_country = user_instance.country
      elif user_instance.role == 'RS':researcher = user_instance.country
   return render(request,'iwmiproject/pointofinterest.html',locals())

'''
 