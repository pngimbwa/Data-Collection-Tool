from django.shortcuts import render, render_to_response, get_object_or_404,redirect,RequestContext, HttpResponseRedirect
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.core.context_processors import csrf
from datetime import datetime, date
#from iwmi.models import Country, Crop,CropCategory
from .models import Country, Crop,TDRMeasurement,GravimetricSoilMoisture
from iwmi.forms import TransplantingForm,NurseryIrrigationForm,ApplicationCalibrationForm,CropMonitoringPlantHeightForm,ServiceRepaireForm,WeedingForm,FarmInfoForm,NurseryForm,FertilizerApplicationForm,PesticideApplicationForm,WaterLiftingCalibrationForm,FarmIrrigationForm,SoilForm,SoilMoistureMeasurementForm,TissueNutrientAnalysisForm,TechnologyFailureForm,FarmYieldLevelForm,BedYieldLevelForm,PlantLevelYieldForm,LandPreparationForm,LandCleareanceForm
#from dal import autocomplete
from .generic import timedifference
import math
   
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

def farmirrigation(request):
   
   return render(request,'iwmi/farmirrigation.html',locals())


def farmer(request):
   return render(request,'iwmi/farmer.html',locals())

def weeding(request):
   
   if request.method == 'POST': 
      weedingform= WeedingForm(request.POST)
   
      if weedingform.is_valid():
         date = weedingform.cleaned_data['date']
         farm = weedingform.cleaned_data['farm']
         weed_activities = weedingform.cleaned_data['weed_activities']
         crop = weedingform.cleaned_data['crop']
         time = weedingform.cleaned_data['time']
         payment = weedingform.cleaned_data['payment']
         labour = weedingform.cleaned_data['labour']
         hired_female_number = weedingform.cleaned_data['hired_female_number']
         hired_male_number = weedingform.cleaned_data['hired_male_number']
         family_female_number = weedingform.cleaned_data['family_female_number']
         family_male_number = weedingform.cleaned_data['family_male_number']
         wage = weedingform.cleaned_data['wage']
         currency = weedingform.cleaned_data['currency']
         
         
         return render(request,'iwmi/weeding.html',locals())
        
      else:
         context = {'weedingform':weedingform}
         return render_to_response('iwmi/weeding.html',context,context_instance=RequestContext(request))
   else:
      weedingform= WeedingForm()
      return render(request,'iwmi/weeding.html',locals())
   
   

def nursery(request):
   if request.method == 'POST': 
      nurseryform = NurseryForm(request.POST)
        
      if nurseryform.is_valid():
         nurseryID = nurseryform.cleaned_data['nurseryID']
         area = nurseryform.cleaned_data['area']
         plot = nurseryform.cleaned_data['farm']
         crop = nurseryform.cleaned_data['crop']
         date_bed_preparation = nurseryform.cleaned_data['date_bed_preparation']
         date_trasplanting = nurseryform.cleaned_data['date_trasplanting']
         bed_length = nurseryform.cleaned_data['bed_length']
         bed_width = nurseryform.cleaned_data['bed_width']
         bednumber = nurseryform.cleaned_data['bednumber']
         seed_per_bed = nurseryform.cleaned_data['seed_per_bed']
         seedtype = nurseryform.cleaned_data['seedtype']
         seeding_date = nurseryform.cleaned_data['seeding_date']
         labour = nurseryform.cleaned_data['labour']
         hired_female_number = nurseryform.cleaned_data['hired_female_number']
         hired_male_number = nurseryform.cleaned_data['hired_male_number']
         family_female_number = nurseryform.cleaned_data['family_female_number']
         family_male_number = nurseryform.cleaned_data['family_male_number']
         wage = nurseryform.cleaned_data['wage']
         currency = nurseryform.cleaned_data['currency']
         
         return render(request,'iwmi/nursery.html',locals())
        
      else:
         context = {'nurseryform':nurseryform}
         return render_to_response('iwmi/nursery.html',context,context_instance=RequestContext(request))
      
   else:
      nurseryform = NurseryForm()
      return render(request,'iwmi/nursery.html',locals())
   
def nurseryirrigation(request):
   if request.method == 'POST': 
      nurseryirrigationform = NurseryIrrigationForm(request.POST)
        
      if nurseryirrigationform.is_valid():
         date = nurseryirrigationform.cleaned_data['date']
         climate = nurseryirrigationform.cleaned_data['climate']
         nurseryID = nurseryirrigationform.cleaned_data['nurseryID']
         time_started = nurseryirrigationform.cleaned_data['time_started']
         time_ended = nurseryirrigationform.cleaned_data['time_ended']
         total_time = nurseryirrigationform.cleaned_data['total_time']
         event = nurseryirrigationform.cleaned_data['event']
         bucket_volume = nurseryirrigationform.cleaned_data['bucket_volume']
         bucket_numbers = nurseryirrigationform.cleaned_data['bucket_numbers']
         total_volume = nurseryirrigationform.cleaned_data['total_volume']
         labour = nurseryirrigationform.cleaned_data['labour']
         hired_female_number = nurseryirrigationform.cleaned_data['hired_female_number']
         hired_male_number = nurseryirrigationform.cleaned_data['hired_male_number']
         family_female_number = nurseryirrigationform.cleaned_data['family_female_number']
         family_male_number = nurseryirrigationform.cleaned_data['family_male_number']
         currency = nurseryirrigationform.cleaned_data['currency']
         wage  = nurseryirrigationform.cleaned_data['wage']
         
         '''
         total volume can be calculated by this formula.
         total_volume = (bucket_numbers * bucket_volume)/1000
         '''
         
         return render(request,'iwmi/nurseryirrigation.html',locals())
      else:
         context = {'nurseryirrigationform':nurseryirrigationform}
         return render_to_response('iwmi/nurseryirrigation.html',context,context_instance=RequestContext(request))
      
   else:
      nurseryirrigationform = NurseryIrrigationForm()
      return render(request,'iwmi/nurseryirrigation.html',locals())
   
   
def farminfo(request):
    
   if request.method == 'POST': 
      farminfoform = FarmInfoForm(request.POST)
      print('**********')
      if farminfoform.is_valid():
         #farmer = farminfoform.cleaned_data['farmer']
         
         fieldID = farminfoform.cleaned_data['fieldID']
         field_latitude = farminfoform.cleaned_data['field_latitude']
         field_longitude = farminfoform.cleaned_data['field_longitude']
         crop = farminfoform.cleaned_data['crop']
         planting_method = farminfoform.cleaned_data['planting_method']
         planting_date = farminfoform.cleaned_data['planting_date']
         fieldsize = farminfoform.cleaned_data['fieldsize']
         #field_type = farminfoform.cleaned_data['field_type']
         water_application = farminfoform.cleaned_data['water_application']
         water_management_method = farminfoform.cleaned_data['water_management_method']
         seed_rate = farminfoform.cleaned_data['seed_rate']
         seed_date = farminfoform.cleaned_data['seed_date']
         bed_length = farminfoform.cleaned_data['bed_length']
         bed_width = farminfoform.cleaned_data['bed_width']
         bednumber = farminfoform.cleaned_data['bednumber']
         furrow_length = farminfoform.cleaned_data['furrow_length']
         furrow_width = farminfoform.cleaned_data['furrow_width']
         nfurrow = farminfoform.cleaned_data['nfurrow']
         WFD_yellow_depth = farminfoform.cleaned_data['WFD_yellow_depth']
         WFD_red_depth = farminfoform.cleaned_data['WFD_red_depth']
         TDR_length = farminfoform.cleaned_data['TDR_length']
         rootzone_depth = farminfoform.cleaned_data['rootzone_depth']
         #number_of_plots = farminfoform.cleaned_data['number_of_rows']
         
         print('**aaaaaa**')
         print('Seed date:'.format(seed_date))
         print('planting date:'.format(planting_date))
            #instance = People(personID=personID,firstname=firstname,middlename=middlename,lastname=lastname,gender=gender,role=role)
       
            #try:
               #People.objects.get(personID=personID)
               #message ='UserID already exist'
               #return render(request,'signup/register.html',locals())
            #except People.DoesNotExist:
               #village_instance = Village.objects.get(village=village)
               #instance.village = village_instance
               #instance.save()
         return render(request,'iwmi/farmerinfo.html',locals())
        
      else:
         context = {'farminfoform':farminfoform}
         return render_to_response('iwmi/farmerinfo.html',context,context_instance=RequestContext(request))
      
   else:
      farminfoform = FarmInfoForm()
      return render(request,'iwmi/farmerinfo.html',locals())
      
   
def fertilizerapplication(request):
   
   if request.method == 'POST': 
      fertilizerapplicationform = FertilizerApplicationForm(request.POST)
   
      if fertilizerapplicationform.is_valid():
         
         farm = fertilizerapplicationform.cleaned_data['farm']
         date = fertilizerapplicationform.cleaned_data['date']
         fertilizer = fertilizerapplicationform.cleaned_data['fertilizer']
         fertilizer_management = fertilizerapplicationform.cleaned_data['fertilizer_management'] 
         quantity_kg = fertilizerapplicationform.cleaned_data['quantity_kg']
         crop_stage = fertilizerapplicationform.cleaned_data['crop_stage']
         nitrogen = fertilizerapplicationform.cleaned_data['nitrogen']
         phosphorus = fertilizerapplicationform.cleaned_data['phosphorus']
         potassium = fertilizerapplicationform.cleaned_data['potassium']
         sulphur = fertilizerapplicationform.cleaned_data['sulphur']
         organic_matter = fertilizerapplicationform.cleaned_data['organic_matter']
         cost = fertilizerapplicationform.cleaned_data['cost']
         labour = fertilizerapplicationform.cleaned_data['labour']
         hired_female_number = fertilizerapplicationform.cleaned_data['hired_female_number']
         hired_male_number = fertilizerapplicationform.cleaned_data['hired_male_number']
         family_female_number = fertilizerapplicationform.cleaned_data['family_female_number']
         family_male_number = fertilizerapplicationform.cleaned_data['family_male_number']
         wage = fertilizerapplicationform.cleaned_data['wage']
         currency = fertilizerapplicationform.cleaned_data['currency']
         
         activity_performed='Fertilizer Application'

         return render (request,'iwmi/fertilizerapplication.html',locals())
        
      else:
         context = {'fertilizerapplicationform':fertilizerapplicationform}
         return render_to_response('iwmi/fertilizerapplication.html',context,context_instance=RequestContext(request))
      
   else:
      fertilizerapplicationform = FertilizerApplicationForm()#initial={'hired_female_number':0,'hired_male_number':0,'family_female_number':0,'family_male_number':0},)
      return render (request,'iwmi/fertilizerapplication.html',locals())
   
   
   
def pesticideapplication(request):
   
   if request.method == 'POST': 
      pesticideapplicationform = PesticideApplicationForm(request.POST)
        
      if pesticideapplicationform.is_valid():
         farm = pesticideapplicationform.cleaned_data['farm']
         date = pesticideapplicationform.cleaned_data['date']
         pesticide = pesticideapplicationform.cleaned_data['pesticide']
         form = pesticideapplicationform.cleaned_data['form']
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
         currency = pesticideapplicationform.cleaned_data['currency']
         
         activity_performed='Pesticide Application'
         
         return render(request,'iwmi/pesticideapplication.html',locals())
        
      else:
         context = {'pesticideapplicationform':pesticideapplicationform}
         return render_to_response('iwmi/pesticideapplication.html',context,context_instance=RequestContext(request))
      
   else:
      pesticideapplicationform = PesticideApplicationForm()
      return render(request,'iwmi/pesticideapplication.html',locals())
   
   
def waterliftingcalibration(request):
   
   if request.method == 'POST': 
      waterliftingcalibrationform = WaterLiftingCalibrationForm(request.POST)
        
      if waterliftingcalibrationform.is_valid():
         farm = waterliftingcalibrationform.cleaned_data['farm']
         date = waterliftingcalibrationform.cleaned_data['date']
         technology = waterliftingcalibrationform.cleaned_data['technology']
         #repetition = waterliftingcalibrationform.cleaned_data['repetition']
         bucketvolume = waterliftingcalibrationform.cleaned_data['bucketvolume']
         start_time= waterliftingcalibrationform.cleaned_data['start_time']
         end_time = waterliftingcalibrationform.cleaned_data['end_time']
         total_time = waterliftingcalibrationform.cleaned_data['total_time']
         discharge = waterliftingcalibrationform.cleaned_data['discharge']
         
         total_time = timedifference(datetime.combine(date.today(), end_time) - datetime.combine(date.today(), start_time))
         #last_event =max(TechnologyCalibration.objects.all().filter(farm=farm).event)
         #current_event = last_event + 1 
         return render(request,'iwmi/waterliftingcalibration.html',locals())
        
      else:
         context = {'waterliftingcalibrationform':waterliftingcalibrationform}
         return render_to_response('iwmi/waterliftingcalibration.html',context,context_instance=RequestContext(request))
      
   else:
      waterliftingcalibrationform = WaterLiftingCalibrationForm()
      return render(request,'iwmi/waterliftingcalibration.html',locals())
   

def applicationcalibration(request):
   
   if request.method == 'POST': 
      applicationcalibrationform = ApplicationCalibrationForm(request.POST)
        
      if applicationcalibrationform.is_valid():
         farm = applicationcalibrationform.cleaned_data['farm']
         date = applicationcalibrationform.cleaned_data['date']
         water_application = applicationcalibrationform.cleaned_data['water_application']
         #repetition = applicationcalibrationform.cleaned_data['repetition']
         bucketvolume = applicationcalibrationform.cleaned_data['bucketvolume']
         start_time= applicationcalibrationform.cleaned_data['start_time']
         end_time = applicationcalibrationform.cleaned_data['end_time']
         total_time = applicationcalibrationform.cleaned_data['total_time']
         discharge = applicationcalibrationform.cleaned_data['discharge']
         bucketnumbers = applicationcalibrationform.cleaned_data['bucketnumbers']
         furrowefficiency = applicationcalibrationform.cleaned_data['furrowefficiency']
         waterheight = applicationcalibrationform.cleaned_data['waterheight']
         topfurrowwidth = applicationcalibrationform.cleaned_data['topfurrowwidth']
         buttonfurrowwidth = applicationcalibrationform.cleaned_data['buttonfurrowwidth']
         #wetteddiameteraroundplant = applicationcalibrationform.cleaned_data['wetteddiameteraroundplant']
         irrigate_whole_or_per_plant = applicationcalibrationform.cleaned_data['irrigate_whole_or_per_plant']
         
         #plot is same as field
         if irrigate_whole_or_per_plant=='Perplant':
            area = plotsize *w
         elif irrigate_whole_or_per_plant=='Perplant':
            dd
         if water_application =='Watering Can' or 'Bucket':
            wsss
         elif water_application == 'Furrow/bed':
            area = (waterheight /2) * (topfurrowwidth + buttonfurrowwidth )
            applicationrate = ((furrowefficiency * 60)/100 * dischargefromwaterlifitingtechnology)/area
            #60 is the field efficiency 
            #application rate should be in mm/hr
         
         if irrigate_whole_or_per_plant == 'Perplant':
            irrigated_depth = (bucketnumbers * bucketvolume)/((totalnumberofplanttransplanted)*(math.pi *pow(wetteddiameteraroundplant,2)/4))
            #totalnumberofplanttransplanted--> for that particular farm use the number of plants entered in the transplanting sheet
            #irrigated_depth--> has to be in mm
            
         elif irrigate_whole_or_per_plant == 'wholefield':
            irrigated_depth =  (bucketnumbers * bucketvolume)/(fieldsize)
            #fieldsize--->is the field size value of that particular field that is entered in farmdetail sheet
            #irrigated_depth--> has to be in mm
            
            
         total_time = timedifference(datetime.combine(date.today(), end_time) - datetime.combine(date.today(), start_time))
         #last_event =max(TechnologyCalibration.objects.all().filter(farm=farm).event)
         #current_event = last_event + 1 
         return render(request,'iwmi/applicationcalibration.html',locals())
        
      else:
         context = {'applicationcalibrationform':applicationcalibrationform}
         return render_to_response('iwmi/applicationcalibration.html',context,context_instance=RequestContext(request))
      
   else:
      applicationcalibrationform = ApplicationCalibrationForm()
      return render(request,'iwmi/applicationcalibration.html',locals())
   
   
def farmirrigation(request):
   
   if request.method == 'POST': 
      farmirrigationform = FarmIrrigationForm(request.POST)
        
      if farmirrigationform.is_valid():
         
         date = farmirrigationform.cleaned_data['date']
         farm = farmirrigationform.cleaned_data['farm']
         #irrigation_event = farmirrigationform.cleaned_data['irrigation_event']
         #technology = farmirrigationform.cleaned_data['technology']
         start_time = farmirrigationform.cleaned_data['start_time']
         end_time  = farmirrigationform.cleaned_data['end_time']         
         #total_time = farmirrigationform.cleaned_data['total_time']
         quantification_method = farmirrigationform.cleaned_data['quantification_method']
         flume_location  = farmirrigationform.cleaned_data['flume_location']
         waterlevel1 = farmirrigationform.cleaned_data['waterlevel1']
         waterlevel2 = farmirrigationform.cleaned_data['waterlevel2']
         furrow_irr_time = farmirrigationform.cleaned_data['furrow_irr_time']
         nfurrorws_irrigated_once = farmirrigationform.cleaned_data['nfurrorws_irrigated_once']
         discharge = farmirrigationform.cleaned_data['discharge']
         standardvolume  = farmirrigationform.cleaned_data['standardvolume']
         quantity_of_units  = farmirrigationform.cleaned_data['quantity_of_units']
         yellow_WFD_before_irrigation = farmirrigationform.cleaned_data['yellow_WFD_before_irrigation']
         red_WFD_before_irrigation = farmirrigationform.cleaned_data['red_WFD_before_irrigation']
         yellow_WFD_time_after_irrigation  = farmirrigationform.cleaned_data['yellow_WFD_time_after_irrigation']
         red_WFD_time_after_irrigation = farmirrigationform.cleaned_data['red_WFD_time_after_irrigation']
         climate = farmirrigationform.cleaned_data['climate']
         fuel = farmirrigationform.cleaned_data['fuel']
         fuelcost = farmirrigationform.cleaned_data['fuelcost']
         currency = farmirrigationform.cleaned_data['currency']
         amount_used = farmirrigationform.cleaned_data['amount_used']
         refilled_amount = farmirrigationform.cleaned_data['refilled_amount']
         water_application = farmirrigationform.cleaned_data['water_application']
         total_time = timedifference(datetime.combine(date.today(), end_time) - datetime.combine(date.today(), start_time))
         wetteddiameteraroundplant = farmirrigationform.cleaned_data['wetteddiameteraroundplant']
         irrigate_whole_or_per_plant = farmirrigationform.cleaned_data['irrigate_whole_or_per_plant']
         #total_irrigation = dicharge (or bucket or) * total_time
         
         #last_event =max(FarmIrrigationEvent.objects.all().filter(farm=farm).event)
         #current_event = last_event + 1
         
         if irrigate_whole_or_per_plant == 'Perplant':
            irrigated_depth = (bucketnumbers * bucketvolume)/((totalnumberofplanttransplanted)*(math.pi *pow(wetteddiameteraroundplant,2)/4))
            #totalnumberofplanttransplanted--> for that particular farm use the number of plants entered in the transplanting sheet
            #irrigated_depth--> has to be in mm
            
         elif irrigate_whole_or_per_plant == 'wholefield':
            irrigated_depth =  (bucketnumbers * bucketvolume)/(fieldsize)
            #fieldsize--->is the field size value of that particular field that is entered in farmdetail sheet
            #irrigated_depth--> has to be in mm
            
         
         print('total_time:{}'.format(total_time))
         
         return render(request,'iwmi/farmirrigation.html',locals())
        
      else:
         context = {'farmirrigationform':farmirrigationform}
         return render_to_response('iwmi/farmirrigation.html',context,context_instance=RequestContext(request))
      
   else:
      farmirrigationform = FarmIrrigationForm()
      return render(request,'iwmi/farmirrigation.html',locals())
   
   
def soil(request):
   if request.method == 'POST': 
      soilform = SoilForm(request.POST)
        
      if soilform.is_valid():
         date = soilform.cleaned_data['date']
         farm = soilform.cleaned_data['farm']
         soilclass = soilform.cleaned_data['soilclass']
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
         
         return render(request,'iwmi/soil.html',locals())
        
      else:
         context = {'soilform':soilform}
         return render_to_response('iwmi/soil.html',context,context_instance=RequestContext(request))
      
   else:
      soilform = SoilForm()
      return render(request,'iwmi/soil.html',locals())
   

def soilmoisture(request):
   if request.method == 'POST': 
      soilmoisturemeasurementform = SoilMoistureMeasurementForm(request.POST)
      print('********')
      if soilmoisturemeasurementform.is_valid():
         measurement_option = soilmoisturemeasurementform.cleaned_data['measurement_option']
         date = soilmoisturemeasurementform.cleaned_data['date']
         farm = soilmoisturemeasurementform.cleaned_data['farm']
         #event = soilmoisturemeasurementform.cleaned_data['event']
         measurement = soilmoisturemeasurementform.cleaned_data['measurement']
         time = soilmoisturemeasurementform.cleaned_data['time']
         depth_sample = soilmoisturemeasurementform.cleaned_data['depth_sample']
         volume_core_used = soilmoisturemeasurementform.cleaned_data['volume_core_used']
         weight_core_used = soilmoisturemeasurementform.cleaned_data['weight_core_used']
         wet_weight = soilmoisturemeasurementform.cleaned_data['wet_weight']
         dry_weight = soilmoisturemeasurementform.cleaned_data['dry_weight']
         bulk_density = soilmoisturemeasurementform.cleaned_data['bulk_density']
         gravimetric_moisture_content = soilmoisturemeasurementform.cleaned_data['gravimetric_moisture_content']
         volumetric_moisture_content = soilmoisturemeasurementform.cleaned_data['volumetric_moisture_content']
         
         
         #last_event =max(GravimetricSoilMoisture.objects.all().filter(farm=farm).event)
         #current_event = last_event + 1
         print('****aaaaa****')
         print('gravimetric_moisture_content:{}'.format(gravimetric_moisture_content))
         print('measurement:{}'.format(measurement))
         #if measurement_option =='gravimetric':
            #instance = GravimetricSoilMoisture(date=date,farm=farm,time=time,depth=depth_sample,volume_core_used=volume_core_used,weight_core_used=weight_core_used,wet_weight=wet_weight,dry_weight=dry_weight,bulk_density=bulk_density,gravimetric_moisture_content=gravimetric_moisture_content,volumetric_moisture_content=volumetric_moisture_content)
         
            #instance.save()
            
         #elif measurement_option =='TDR':
            #instance = TDRMeasurement(date=date,farm=farm,measurement=measurement,event=event)
            #instance.save()
            
         return render(request,'iwmi/soilmoisture.html',locals())
        
      else:
         context = {'soilmoisturemeasurementform':soilmoisturemeasurementform}
         return render_to_response('iwmi/soilmoisture.html',context,context_instance=RequestContext(request))
   else:
      soilmoisturemeasurementform = SoilMoistureMeasurementForm()
      return render(request,'iwmi/soilmoisture.html',locals())
   
   
   
def fuelconsumption(request):
   return render(request,'iwmi/fuelconsumption.html',locals())

def service_repaire(request):
   
   if request.method == 'POST': 
      servicerepaireform = ServiceRepaireForm(request.POST)
        
      if servicerepaireform.is_valid():
         date = servicerepaireform.cleaned_data['date']
         #group = servicerepaireform.cleaned_data['group']
         repaire_type = servicerepaireform.cleaned_data['repaire_type']
         spaire = servicerepaireform.cleaned_data['spaire']
         pump = servicerepaireform.cleaned_data['pump']
         price = servicerepaireform.cleaned_data['price']
         currency = servicerepaireform.cleaned_data['currency']
         
         print('currency:{}'.format(currency))
         
         return render(request,'iwmi/service_repaire.html',locals())
        
      else:
         context = {'servicerepaireform':servicerepaireform}
         return render_to_response('iwmi/service_repaire.html',context,context_instance=RequestContext(request))
      
   else:
      servicerepaireform = ServiceRepaireForm()
      return render(request,'iwmi/service_repaire.html',locals())
   

def sale_harvest_crop(request):
   return render(request,'iwmi/sale_harvest_crop.html',locals())

def consumed_crop_by_household(request):
   return render(request,'iwmi/consumed_crop_by_household.html',locals())

def farmer_detail(request):
   countries = Country.objects.all().order_by('name')
   return render(request,'iwmi/farmer_detail.html',locals())

def plant_level_yield(request):
   
   if request.method == 'POST': 
      plantlevelyieldform = PlantLevelYieldForm(request.POST)
      
      if plantlevelyieldform.is_valid():
         date = plantlevelyieldform.cleaned_data['date']
         farm =  plantlevelyieldform.cleaned_data['farm']
         plot = plantlevelyieldform.cleaned_data['plot']    
         dry_fresh =  plantlevelyieldform.cleaned_data['dry_fresh']
         harvesting_method  = plantlevelyieldform.cleaned_data['harvesting_method']
         plant_number = plantlevelyieldform.cleaned_data['plant_number']
         marketable_produced = plantlevelyieldform.cleaned_data['marketable_produced']
         unmarketable_produced = plantlevelyieldform.cleaned_data['unmarketable_produced']
         marketable_produced_weight = plantlevelyieldform.cleaned_data['marketable_produced_weight']
         unmarketable_produced_weight = plantlevelyieldform.cleaned_data['unmarketable_produced_weight']
         diameter_width_produced = plantlevelyieldform.cleaned_data['diameter_width_produced']
         length= plantlevelyieldform.cleaned_data['length']
         residual_biomass = plantlevelyieldform.cleaned_data['residual_biomass']
              
         print('dry/fresh:{}'.format(dry_fresh))
         if dry_fresh == 'dry':
            flesh =False
            dry = True
         elif dry_fresh == 'fresh':
            flesh =True
            dry = False
         
         return render(request,'iwmi/plant_level_yield.html',locals())
        
      else:
         context = {'plantlevelyieldform':plantlevelyieldform}
         return render_to_response('iwmi/plant_level_yield.html',context,context_instance=RequestContext(request))
   else:
      plantlevelyieldform= PlantLevelYieldForm()
      return render(request,'iwmi/plant_level_yield.html',locals())
   

def bed_level_yield(request):
   
   if request.method == 'POST': 
      bedyieldlevelform = BedYieldLevelForm(request.POST)
      
      if bedyieldlevelform.is_valid():
         date = bedyieldlevelform.cleaned_data['date']
         farm = bedyieldlevelform.cleaned_data['farm']
         harvesting_method = bedyieldlevelform.cleaned_data['harvesting_method']
         dry_fresh = bedyieldlevelform.cleaned_data['dry_fresh']
         area = bedyieldlevelform.cleaned_data['sub_plot_area']
         plot = bedyieldlevelform.cleaned_data['plot']
         marketable_produce = bedyieldlevelform.cleaned_data['marketable_produce']
         unmarketable_produce = bedyieldlevelform.cleaned_data['unmarketable_produce']
         marketable_produce_weight = bedyieldlevelform.cleaned_data['marketable_produce_weight']
         unmarketable_produce_weight = bedyieldlevelform.cleaned_data['unmarketable_produce_weight']
         
         print('dry/fresh:{}'.format(dry_fresh))
         if dry_fresh == 'dry':
            flesh =False
            dry = True
         elif dry_fresh == 'fresh':
            flesh =True
            dry = False
         
         return render(request,'iwmi/bedyieldlevel.html',locals())
        
      else:
         context = {'bedyieldlevelform':bedyieldlevelform}
         return render_to_response('iwmi/bedyieldlevel.html',context,context_instance=RequestContext(request))
   else:
      bedyieldlevelform= BedYieldLevelForm()
      return render(request,'iwmi/bedyieldlevel.html',locals())
   

def farmyieldlevel(request):
   
   if request.method == 'POST': 
      farmyieldlevelform = FarmYieldLevelForm(request.POST)
      
      if farmyieldlevelform.is_valid():
         date = farmyieldlevelform.cleaned_data['date']
         farm = farmyieldlevelform.cleaned_data['farm']
         area = farmyieldlevelform.cleaned_data['area']
         #fresh = farmyieldlevelform.cleaned_data['fresh']
         #dry = farmyieldlevelform.cleaned_data['dry']
         marketable_yield = farmyieldlevelform.cleaned_data['marketable_yield']
         unmarketable_yield = farmyieldlevelform.cleaned_data['unmarketable_yield']
         biomas = farmyieldlevelform.cleaned_data['biomas']
         dry_fresh = farmyieldlevelform.cleaned_data['dry_fresh']
         quantity_harvested = farmyieldlevelform.cleaned_data['quantity_harvested']
         payement = pesticideapplicationform.cleaned_data['payement']
         labour = pesticideapplicationform.cleaned_data['labour']
         hired_female_number = pesticideapplicationform.cleaned_data['hired_female_number']
         hired_male_number = pesticideapplicationform.cleaned_data['hired_male_number']
         family_female_number = pesticideapplicationform.cleaned_data['family_female_number']
         family_male_number = pesticideapplicationform.cleaned_data['family_male_number']
         
         print('dry/fresh:{}'.format(dry_fresh))
         if dry_fresh == 'dry':
            flesh =False
            dry = True
         elif dry_fresh == 'fresh':
            flesh =True
            dry = False
         
         return render(request,'iwmi/farmyieldlevel.html',locals())
        
      else:
         context = {'farmyieldlevelform':farmyieldlevelform}
         return render_to_response('iwmi/farmyieldlevel.html',context,context_instance=RequestContext(request))
   else:
      farmyieldlevelform = FarmYieldLevelForm()
      return render(request,'iwmi/farmyieldlevel.html',locals())
   

def technology_failure(request):
   
   if request.method == 'POST': 
      technologyfailureform = TechnologyFailureForm(request.POST)
   
      if technologyfailureform.is_valid():
         date = technologyfailureform.cleaned_data['date']
         farm = technologyfailureform.cleaned_data['farm']
         technology = technologyfailureform.cleaned_data['technology']
         reason = technologyfailureform.cleaned_data['reason']
         
            
         return render(request,'iwmi/technology_failure.html',locals())
        
      else:
         context = {'technologyfailureform':technologyfailureform}
         return render_to_response('iwmi/technology_failure.html',context,context_instance=RequestContext(request))
   else:
      technologyfailureform = TechnologyFailureForm()
      return render(request,'iwmi/technology_failure.html',locals())
   

def tissuenutrientanalysis(request):
   
   if request.method == 'POST': 
      tissuenutrientanalysisform = TissueNutrientAnalysisForm(request.POST)
   
      if tissuenutrientanalysisform.is_valid():
         date = tissuenutrientanalysisform.cleaned_data['date']
         farm = tissuenutrientanalysisform.cleaned_data['farm']
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
            
         return render(request,'iwmi/tissuenutrientanalysis.html',locals())
        
      else:
         context = {'tissuenutrientanalysisform':tissuenutrientanalysisform}
         return render_to_response('iwmi/tissuenutrientanalysis.html',context,context_instance=RequestContext(request))
   else:
      tissuenutrientanalysisform = TissueNutrientAnalysisForm()
      return render(request,'iwmi/tissuenutrientanalysis.html',locals())
   
def cropmonitoring(request):
   
   if request.method == 'POST': 
      cropmonitoringplantheightform = CropMonitoringPlantHeightForm(request.POST)
   
      if cropmonitoringplantheightform.is_valid():
         date = cropmonitoringplantheightform.cleaned_data['date']
         farm = cropmonitoringplantheightform.cleaned_data['farm']
         crop_stage = cropmonitoringplantheightform.cleaned_data['crop_stage']
         plot = cropmonitoringplantheightform.cleaned_data['plot']
         plant_density_per_bed = cropmonitoringplantheightform.cleaned_data['plant_density_per_bed']
         plant_density_per_sqm = cropmonitoringplantheightform.cleaned_data['plant_density_per_sqm']
         number_of_good_plants = cropmonitoringplantheightform.cleaned_data['number_of_good_plants']
         number_of_bad_plants = cropmonitoringplantheightform.cleaned_data['number_of_bad_plants']
         plant_number = cropmonitoringplantheightform.cleaned_data['plant_number']
         plant_height = cropmonitoringplantheightform.cleaned_data['plant_height']
         plant_canopy_width = cropmonitoringplantheightform.cleaned_data['plant_canopy_width']
         lenght_of_crop_stage = cropmonitoringplantheightform.cleaned_data['lenght_of_crop_stage']
         plant_leave_number = cropmonitoringplantheightform.cleaned_data['plant_leave_number']
         plant_leave_length = cropmonitoringplantheightform.cleaned_data['plant_leave_length']
         plant_leave_width = cropmonitoringplantheightform.cleaned_data['plant_leave_width']
            
         return render(request,'iwmi/cropmonitoring.html',locals())
        
      else:
         context = {'cropmonitoringplantheightform':cropmonitoringplantheightform}
         return render_to_response('iwmi/cropmonitoring.html',context,context_instance=RequestContext(request))
   else:
      cropmonitoringplantheightform = CropMonitoringPlantHeightForm()
      return render(request,'iwmi/cropmonitoring.html',locals())
   
def  landpreparation(request):
   
   if request.method == 'POST': 
      landpreparationform = LandPreparationForm(request.POST)
   
      if landpreparationform.is_valid():
         date = landpreparationform.cleaned_data['date']
         farm = landpreparationform.cleaned_data['farm']
         landpreparationtool = landpreparationform.cleaned_data['landpreparationtool']
         plot = landpreparationform.cleaned_data['plot']
         labour = landpreparationform.cleaned_data['labour']
         hired_female_number = landpreparationform.cleaned_data['hired_female_number']
         hired_male_number = landpreparationform.cleaned_data['hired_male_number']
         family_female_number = landpreparationform.cleaned_data['family_female_number']
         family_male_number = landpreparationform.cleaned_data['family_male_number']
         wage = landpreparationform.cleaned_data['wage']
         currency = landpreparationform.cleaned_data['currency']

            
         return render(request,'iwmi/landpreparation.html',locals())
        
      else:
         context = {'landpreparationform':landpreparationform}
         return render_to_response('iwmi/landpreparation.html',context,context_instance=RequestContext(request))
   else:
      landpreparationform = LandPreparationForm()
      return render(request,'iwmi/landpreparation.html',locals())

def landclearance(request):
   
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
         currency = landcleareanceform.cleaned_data['currency']

            
         return render(request,'iwmi/landcleareance.html',locals())
        
      else:
         context = {'landcleareanceform':landcleareanceform}
         return render_to_response('iwmi/landcleareance.html',context,context_instance=RequestContext(request))
   else:
      landcleareanceform = LandCleareanceForm()
      return render(request,'iwmi/landcleareance.html',locals())
   
   
def transplanting(request):
   
   if request.method == 'POST': 
      transplantingform = TransplantingForm(request.POST)
        
      if transplantingform.is_valid():
         plot = transplantingform.cleaned_data['farm']
         seedprice = transplantingform.cleaned_data['seedprice']
         plants_transplanted = transplantingform.cleaned_data['plants_transplanted']
         number_of_plants_per_row = transplantingform.cleaned_data['number_of_plants_per_row']
         trasplanting_date = transplantingform.cleaned_data['trasplanting_date']
         labour = transplantingform.cleaned_data['labour']
         hired_female_number = transplantingform.cleaned_data['hired_female_number']
         hired_male_number = transplantingform.cleaned_data['hired_male_number']
         family_female_number = transplantingform.cleaned_data['family_female_number']
         family_male_number = transplantingform.cleaned_data['family_male_number']
         wage = transplantingform.cleaned_data['wage']
         currency = transplantingform.cleaned_data['currency']
         plant_spacing_btn_rows = transplantingform.cleaned_data['plant_spacing_btn_rows']
         plant_spacing_btn_plants_within_rows = transplantingform.cleaned_data['plant_spacing_btn_plants_within_rows']
         number_of_plants_per_row = transplantingform.cleaned_data['number_of_plants_per_row']
         
         return render(request,'iwmi/transplanting.html',locals())
      else:
         context = {'transplantingform':transplantingform}
         return render_to_response('iwmi/transplanting.html',context,context_instance=RequestContext(request))
      
   else:
      transplantingform = TransplantingForm()
      return render(request,'iwmi/transplanting.html',locals())
   

   