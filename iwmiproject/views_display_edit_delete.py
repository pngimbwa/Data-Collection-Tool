from django.shortcuts import render, render_to_response,get_object_or_404,redirect,RequestContext, HttpResponseRedirect
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.core.context_processors import csrf
from datetime import datetime, date
from .models import FertilizerSpecification,Farm,TechnologyFailure,ConsumedCrops,SeedManagement,BedNursery,Nursery,CropMonitoringPlantHeight,GravimetricSoilMoisture,SoilMoistureMeasurementManagement,SoilMoistureProfiler,SaleHarvestedCrop,TissueNutrientAnalysis,OtherWaterUsage,SoilProperty,YieldRowBedLevel,YieldPlantLevel,ResidualHandling,LandClearance,LandPreparation,LabourManagament,SystemUser,PlotCrop,Region,District,Village,Remark,SaleHarvestedCrop,OtherWaterUsage,ResidualHandling,Service,Spaire,CropVarieties,BedPlot,SoilProperty,PlotIrrigationEvent,ApplicationCalibration,YieldFarmLevel,YieldRowBedLevel,YieldPlantLevel,ConsumedCrops,TissueNutrientAnalysis,CropMonitoringPlantHeight,GravimetricSoilMoisture,TDRMeasurement,SoilMoistureProfiler,Country,Soil,Weed,WaterliftingCalibrations,TechnologyFailure,Technology,TechnologyManagement,FertilizerManagement,PesticideManagement,Pesticide,Fertilizer,SystemUser,Farm,LandPreparation,NurseryIrrigationEvent,Nursery,BedNursery,Crop,SeedManagement,LandClearance,LabourManagament,WaterManagement,TDRMeasurement,GravimetricSoilMoisture,Plot,PlotManagement,People,Furrow,BedPlot,PlantingMethod
from iwmiproject.forms import FertilizerSpecificationForm,TechnologyFailure_Form,ConsumedCrops_Form,SeedManagement_Form,BedNursery_Form,Nursery_Form,CropMonitoringPlantHeight_Form,GravimetricSoilMoisture_Form,SoilMoistureMeasurementManagement_Form,SoilMoistureProfiler_Form,SaleHarvestedCrop_Form,TissueNutrientAnalysis_Form,OtherWaterUsage_Form,SoilProperty_Form,YieldPlantLevel_Form,YieldRowBedLevel_Form,ResidualHandling_Form,ResidualHandling_Form,YieldFarmLevel_Form,Weeding_Form,PesticideManagement_Form,FertilizerManagement_Form,LandClearance_Form,LandPreparation_Form,LabourManagement_Form,Remark_Form,PlotManagementForm,PlotForm,CropVarietiesForm,BedPlotForm,FurrowForm,WaterManagementForm,PlotCropForm
from .generic import timedifference
import math

from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger
from django.shortcuts import render
from .functions import pick_currency, labourmanagement

def edit_farmer_detail(request,plotID,personID):
   if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('signup:login'))

   if request.method == 'POST':
      watermanagementform = WaterManagementForm(request.POST)
      plotmanagementform = PlotManagementForm(request.POST or None)
      plotcropform = PlotCropForm(request.POST)
      plotform =PlotForm(request.POST)
      cropvarietiesform=CropVarietiesForm(request.POST)
      bedplotform = BedPlotForm(request.POST)
      furrowform = FurrowForm(request.POST)
      print('**QQQQ***')

      if watermanagementform.is_valid() and plotform.is_valid() and bedplotform.is_valid() and furrowform.is_valid() and plotmanagementform.is_valid() and plotcropform.is_valid():
         #plotmanagementform
         farm = plotmanagementform.cleaned_data['farm']
         plotID = plotmanagementform.cleaned_data['plotID']
        
         #crop = plotmanagementform.cleaned_data['crop']
         elevation = plotmanagementform.cleaned_data['elevation']
         plot_size = plotmanagementform.cleaned_data['plot_size']
         seasonstart = plotmanagementform.cleaned_data['seasonstart']
         water_application = plotmanagementform.cleaned_data['water_application']
         rootdepth = plotmanagementform.cleaned_data['rootdepth']
         cropping_system = plotmanagementform.cleaned_data['cropping_system']
         #plotcropform
         crop1 = plotcropform.cleaned_data['crop1']
         crop1_variety = plotcropform.cleaned_data['crop1_variety']
         crop1_varietytype = plotcropform.cleaned_data['crop1_varietytype']
         crop2 = plotcropform.cleaned_data['crop2']
         crop2_variety = plotcropform.cleaned_data['crop2_variety']
         crop2_varietytype = plotcropform.cleaned_data['crop2_varietytype']
         #watermanagementform
         water_management_method = watermanagementform.cleaned_data['water_management_method']
         rods_length = watermanagementform.cleaned_data['rods_length']
         yellow_depth_detector = watermanagementform.cleaned_data['yellow_depth_detector']
         red_depth_detector = watermanagementform.cleaned_data['red_depth_detector']
         #plotform
         fieldtype = plotform.cleaned_data['fieldtype']
         latitude = plotform.cleaned_data['latitude']
         longitude = plotform.cleaned_data['longitude']
         #bedplotform
         #bed_length,bed_width,bednumber
         bed_length = bedplotform.cleaned_data['length']
         bed_width = bedplotform.cleaned_data['width']
         bednumber = bedplotform.cleaned_data['numbers']
         #furrowform
         length = furrowform.cleaned_data['length']
         width = furrowform.cleaned_data['width']
         numbers = furrowform.cleaned_data['numbers']
         
         if str(fieldtype) == 'Pocket garden':
            bed_length = -999
            bed_width = -999
            bednumber = -999
            furrow_length = -999
            furrow_width = -999
            nfurrow = -999
            
         try:
            plotmanagement_instance = PlotManagement.objects.get(farm=farm,plotID=plotID)
         except PlotManagement.DoesNotExist:
            pass
         else:
            #PlotManagementForm
            plotmanagement_instance = PlotManagement.objects.get(farm=farm,plotID=plotID)
            plotmanagement_instance.elevation = elevation
            plotmanagement_instance.plot_size = plot_size
            plotmanagement_instance.cropping_system = cropping_system
            plotmanagement_instance.water_application = water_application
            plotmanagement_instance.rootdepth = rootdepth
            plotmanagement_instance.seasonstart = seasonstart
            plotmanagement_instance.save()
            #WaterManagementForm
            watermanagement_instance = WaterManagement.objects.get(farm=farm,plotID=plotID)
            watermanagement_instance.water_management_method = water_management_method
            watermanagement_instance.yellow_depth_detector = yellow_depth_detector
            watermanagement_instance.red_depth_detector = red_depth_detector
            watermanagement_instance.rods_length = rods_length
            watermanagement_instance.save()
            #FurrowForm
            furrow_instance = Furrow.objects.get(farm=farm,plotID=plotID)
            furrow_instance.length = length
            furrow_instance.width = width
            furrow_instance.numbers = numbers
            furrow_instance.save()
            #BedPlotForm
            bedplot_instance = BedPlot.objects.get(farm=farm,plotID=plotID)
            #bed_length,bed_width,bednumber
            bedplot_instance.length = bed_length
            bedplot_instance.width = bed_width
            bedplot_instance.numbers = bednumber
            bedplot_instance.save()
            #PlotForm
            plot_instance = Plot.objects.get(farm=farm,plotID=plotID)
            plot_instance.latitude = latitude
            plot_instance.longitude = longitude
            plot_instance.fieldtype =  fieldtype
            plot_instance.save()
            #PlotCropForm
            plotcrop_instance = PlotCrop.objects.get(farm=farm,plotID=plotID)
            if cropping_system =='Monocropping':
               plotcrop_instance.crop1 =crop1
               plotcrop_instance.crop1_variety = crop1_variety
               plotcrop_instance.crop1_varietytype = crop1_varietytype
               plotcrop_instance.crop2 = None
               plotcrop_instance.crop2_variety= None
               plotcrop_instance.crop2_varietytype = None
               plotmanagement_instance.crop.add(crop1)
            elif cropping_system =='Intercropping':
               plotcrop_instance.crop1 =crop1
               plotcrop_instance.crop1_variety = crop1_variety
               plotcrop_instance.crop1_varietytype = crop1_varietytype
               plotcrop_instance.crop2 = crop2
               plotcrop_instance.crop2_variety= crop1_variety
               plotcrop_instance.crop2_varietytype = crop2_varietytype
               plotmanagement_instance.crop.add(crop1,crop2)
            plotcrop_instance.save()
         message='saved'
         return render(request,'iwmiproject/saved.html',locals())
         #return redirect('https://www.google.com')
   else:
      plotmanagement_instance = PlotManagement.objects.get(farm=personID,plotID=Plot.objects.get(plotID=plotID,farm=personID))
      plot_instance = Plot.objects.get(plotID=plotID,farm=personID)
      bedplot_instance = BedPlot.objects.get(farm=personID,plotID=Plot.objects.get(plotID=plotID,farm=personID))
      furrow_instance = Furrow.objects.get(farm=personID,plotID=Plot.objects.get(plotID=plotID,farm=personID))
      watermanagement_instance = WaterManagement.objects.get(farm=personID,plotID=Plot.objects.get(plotID=plotID,farm=personID))
      plotcrop_instance = PlotCrop.objects.get(farm=personID,plotID=Plot.objects.get(plotID=plotID,farm=personID))

      watermanagementform = WaterManagementForm(instance = watermanagement_instance)
      plotmanagementform = PlotManagementForm(instance = plotmanagement_instance)
      plotform = PlotForm(instance = plot_instance)
      bedplotform = BedPlotForm(instance = bedplot_instance)
      plotcropform = PlotCropForm(instance = plotcrop_instance)


      user_instance = SystemUser.objects.get(user=request.user)
      if user_instance.role == 'RA' or user_instance.role == 'ST':user_village = user_instance.village
      elif user_instance.role == 'ALL':user_country = user_instance.country
      elif user_instance.role == 'RS':researcher = user_instance.country

      furrowform = FurrowForm(instance = furrow_instance)
   return render(request,'iwmiproject/iwmiproject_edit/farmer_detail.html',locals())
   #Plot,Crop,CropVarieties,PlotManagement,WaterManagement,BedPlot,Furrow

def list_farmers(request):
   if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('signup:login'))

   user_instance = SystemUser.objects.get(user=request.user)
   if user_instance.role == 'RA' or user_instance.role == 'ST':
      user_village = user_instance.village
      plot_queryset_list = PlotManagement.objects.filter(enteredpersonel=user_instance).select_related()
      #x = [i.plotID for i in plot_queryset_list if str(i.plotID)=='BUCKET']
      #print('plot_queryset_list: {}'.format(x))
   elif user_instance.role == 'ALL':
      user_country = user_instance.country
      plot_queryset_list = PlotManagement.objects.all().select_related()
   elif user_instance.role == 'RS':
      researcher_country = user_instance.country
      plot_queryset_list = PlotManagement.objects.filter(farm__farmID__village__district__region__country=researcher_country).select_related()

   paginator = Paginator(plot_queryset_list, 20)

   page = request.GET.get('page')
   try:
      plot_queryset = paginator.page(page)
   except PageNotAnInteger:
      plot_queryset = paginator.page(1)
   except EmptyPage:
      plot_queryset = paginator.page(paginator.num_pages)

   context ={
         'object_list':plot_queryset,
         'title':"List",
         'user_instance':user_instance
   }
   #Plot,PlotManagement,BedPlot,Furrow,WaterManagement,People,Farm
   return render(request,'iwmiproject/iwmiproject_display/farmer_detail.html',context)


def list_crop_production(request):
   if not request.user.is_authenticated():
      return HttpResponseRedirect(reverse('signup:login'))

   user_instance = SystemUser.objects.get(user=request.user)
   if user_instance.role == 'RA' or user_instance.role == 'ST':
      user_village = user_instance.village
      plot_queryset_list = PlotManagement.objects.filter(enteredpersonel=user_instance).select_related()
   elif user_instance.role == 'ALL':
      user_country = user_instance.country
      plot_queryset_list = PlotManagement.objects.all().select_related()
   elif user_instance.role == 'RS':
      researcher_country = user_instance.country
      plot_queryset_list = PlotManagement.objects.filter(farm__farmID__village__district__region__country=researcher_country).select_related()

   paginator = Paginator(plot_queryset_list, 20)

   page = request.GET.get('page')
   try:
      plot_queryset = paginator.page(page)
   except PageNotAnInteger:
      plot_queryset = paginator.page(1)
   except EmptyPage:
      plot_queryset = paginator.page(paginator.num_pages)

   context ={
         'object_list':plot_queryset,
         'title':"List",
         'user_instance':user_instance
   }
   #Plot,PlotManagement,BedPlot,Furrow,WaterManagement,People,Farm
   return render(request,'iwmiproject/iwmiproject_display/remark_detail.html',context)

def delete_remark_specific_detail(request,plotID,personID,start_date,end_date):
   if not request.user.is_authenticated():
      return HttpResponseRedirect(reverse('signup:login'))
   plot_remark_instance = Remark.objects.get(farm=personID,plot=Plot.objects.get(plotID=plotID,farm=personID),start_date=start_date,end_date=end_date)

   plot_remark_instance.delete()

   message='deleted'
   return render(request,'iwmiproject/delete.html',locals())

def delete_remark_detail(request,plotID,personID):
   if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('signup:login'))
   user_instance = SystemUser.objects.get(user=request.user)

   if user_instance.role == 'RA' or user_instance.role == 'ST':
      user_village = user_instance.village
      plot_remark_queryset_list = Remark.objects.filter(enteredpersonel=user_instance,farm=personID,plot=Plot.objects.get(plotID=plotID,farm=personID)).select_related()
      #print('plot_remark_queryset_list_RA_ST: {}'.format(plot_remark_queryset_list))
   elif user_instance.role == 'ALL':
      user_country = user_instance.country
      plot_remark_queryset_list = Remark.objects.filter(farm=personID,plot=Plot.objects.get(plotID=plotID,farm=personID)).select_related()
   elif user_instance.role == 'RS':
      researcher_country = user_instance.country
      plot_remark_queryset_list = Remark.objects.filter(farm__farmID__village__district__region__country=researcher_country).select_related()
      #print('plot_remark_queryset_list_RS: {}'.format(plot_remark_queryset_list))
   paginator = Paginator(plot_remark_queryset_list, 20)

   page = request.GET.get('page')
   try:
      plot_remark_queryset = paginator.page(page)
   except PageNotAnInteger:
      plot_remark_queryset = paginator.page(1)
   except EmptyPage:
      plot_remark_queryset = paginator.page(paginator.num_pages)

   context ={
         'object_list':plot_remark_queryset,
         'title':"List",
         'user_instance':user_instance
      }
   return render(request,'iwmiproject/iwmiproject_delete/delete_remark_detail_display.html',context)


def edit_remark_specific_detail(request,plotID,personID,start_date,end_date):
   if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('signup:login'))
   user_instance = SystemUser.objects.get(user=request.user)
   if request.method == 'POST':
      remarkform = Remark_Form(request.POST)

      if remarkform.is_valid():
         farm = remarkform.cleaned_data['farm']
         plot = remarkform.cleaned_data['plot']
         start_date = remarkform.cleaned_data['start_date']
         end_date = remarkform.cleaned_data['end_date']
         stress = remarkform.cleaned_data['stress']
         severness = remarkform.cleaned_data['severness']
         other = remarkform.cleaned_data['other']

         try:
            plot_remark_instance = Remark.objects.get(farm=personID,plot=Plot.objects.get(plotID=plotID,farm=personID),start_date=start_date,end_date=end_date)
         except Remark.DoesNotExist:
            plot_remark_instance =Remark(start_date=start_date,end_date=end_date,stress = stress,severness = severness,farm=Farm.objects.get(farmID=personID),plot=Plot.objects.get(plotID=plotID,farm=Farm.objects.get(farmID=personID)),enteredpersonel= SystemUser.objects.get(user=request.user))
            plot_remark_instance.save()
         else:
            plot_remark_instance.severness = severness
            if other =='99999999':
               plot_remark_instance.stress = stress
            else:
               plot_remark_instance.stress = other
            plot_remark_instance.save()

         message='saved'
         return render(request,'iwmiproject/saved.html',locals())
      else:
         user_instance = SystemUser.objects.get(user=request.user)
         if user_instance.role == 'RA' or user_instance.role == 'ST':user_village = user_instance.village
         elif user_instance.role == 'ALL':user_country = user_instance.country
         elif user_instance.role == 'RS':researcher = user_instance.country
         return render(request,'iwmiproject/iwmiproject_edit/edit_remark_detail.html',locals())
   else:
      remark_instance = Remark.objects.get(start_date=start_date,end_date=end_date,farm=personID,plot=Plot.objects.get(plotID=plotID,farm=personID))
      print('remark_instance: {}'.format(remark_instance))
      remarkform = Remark_Form(instance = remark_instance)

      if user_instance.role == 'RA' or user_instance.role == 'ST':user_village = user_instance.village
      elif user_instance.role == 'ALL':user_country = user_instance.country
      elif user_instance.role == 'RS':researcher = user_instance.country
      return render(request,'iwmiproject/iwmiproject_edit/edit_remark_detail.html',locals())


def edit_remark_detail(request,plotID,personID):
   if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('signup:login'))
   user_instance = SystemUser.objects.get(user=request.user)
   if user_instance.role == 'RA' or user_instance.role == 'ST':user_village = user_instance.village
   elif user_instance.role == 'ALL':user_country = user_instance.country
   elif user_instance.role == 'RS':researcher = user_instance.country
            
   remark_instance = Remark.objects.filter(farm=personID,plot=Plot.objects.get(plotID=plotID,farm=personID))

   if not remark_instance:
         return render(request,'iwmiproject/iwmiproject_display/none.html',locals())

   elif len(remark_instance) == 1:

      if request.method == 'POST':
         remarkform = Remark_Form(request.POST)

         if remarkform.is_valid():
            farm = remarkform.cleaned_data['farm']
            plot = remarkform.cleaned_data['plot']
            start_date = remarkform.cleaned_data['start_date']
            end_date = remarkform.cleaned_data['end_date']
            stress = remarkform.cleaned_data['stress']
            severness = remarkform.cleaned_data['severness']
            other = remarkform.cleaned_data['other']

            plot_remark_instance = Remark.objects.get(farm=personID,plot=Plot.objects.get(plotID=plotID,farm=personID))
            plot_remark_instance.start_date = start_date
            plot_remark_instance.end_date = end_date
            plot_remark_instance.severness = severness
            if other =='99999999':
               plot_remark_instance.stress = stress
            else:
               plot_remark_instance.stress = other
            plot_remark_instance.save()

            message='saved'
            return render(request,'iwmiproject/saved.html',locals())
         else:
            return render(request,'iwmiproject/iwmiproject_edit/edit_remark_detail.html',locals())
      else:
         remark_instance = Remark.objects.get(farm=personID,plot=Plot.objects.get(plotID=plotID,farm=personID))
         remarkform = Remark_Form(instance = remark_instance)

         return render(request,'iwmiproject/iwmiproject_edit/edit_remark_detail.html',locals())

   else:
      if user_instance.role == 'RA' or user_instance.role == 'ST':
         user_village = user_instance.village
         plot_remark_queryset_list = Remark.objects.filter(enteredpersonel=user_instance,farm=personID,plot=Plot.objects.get(plotID=plotID,farm=personID)).select_related()
         print('plot_remark_queryset_list_RA_ST: {}'.format(plot_remark_queryset_list))
      elif user_instance.role == 'ALL':
         user_country = user_instance.country
         plot_remark_queryset_list = Remark.objects.filter(farm=personID,plot=Plot.objects.get(plotID=plotID,farm=personID)).select_related()
      elif user_instance.role == 'RS':
         researcher_country = user_instance.country
         plot_remark_queryset_list = Remark.objects.filter(farm__farmID__village__district__region__country=researcher_country).select_related()
         print('plot_remark_queryset_list_RS: {}'.format(plot_remark_queryset_list))
      paginator = Paginator(plot_remark_queryset_list, 20)

      page = request.GET.get('page')
      try:
         plot_remark_queryset = paginator.page(page)
      except PageNotAnInteger:
         plot_remark_queryset = paginator.page(1)
      except EmptyPage:
         plot_remark_queryset = paginator.page(paginator.num_pages)

      context ={
            'object_list':plot_remark_queryset,
            'title':"List",
            'user_instance':user_instance
      }
      return render(request,'iwmiproject/iwmiproject_display/remark_detail_display.html',context)

def edit_detail(request,plotID,personID):
   if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('signup:login'))
   #print('my request: {}'.format(request))
   return render(request,'iwmiproject/iwmiproject_display/edit_option.html',locals())

def delete_detail(request,plotID,personID):
   if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('signup:login'))
   #print('my request: {}'.format(request))
   return render(request,'iwmiproject/iwmiproject_delete/delete_option.html',locals())

def edit_landclearance_detail(request,plotID,personID,date):
   if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('signup:login'))
   user_instance = SystemUser.objects.get(user=request.user)

   if request.method == 'POST':
      landclearance_form = LandClearance_Form(request.POST)
      labourmanagement_form = LabourManagement_Form(request.POST)

      if landclearance_form.is_valid() and labourmanagement_form.is_valid():
         farm = landclearance_form.cleaned_data['farm']
         plotID = landclearance_form.cleaned_data['plotID']
         date = landclearance_form.cleaned_data['date']
         landclearanceoption = landclearance_form.cleaned_data['landclearanceoption']

         labour = labourmanagement_form.cleaned_data['labour']
         hired_female_number = labourmanagement_form.cleaned_data['hired_female_number']
         hired_female_time = labourmanagement_form.cleaned_data['hired_female_time']
         hired_male_number = labourmanagement_form.cleaned_data['hired_male_number']
         hired_male_time = labourmanagement_form.cleaned_data['hired_male_time']

         family_female_number = labourmanagement_form.cleaned_data['family_female_number']
         family_female_time = labourmanagement_form.cleaned_data['family_female_time']
         family_male_number = labourmanagement_form.cleaned_data['family_male_number']
         family_male_time = labourmanagement_form.cleaned_data['family_male_time']
         #activity = labourmanagement_form.cleaned_data['activity']
         wage = labourmanagement_form.cleaned_data['wage']
         price_unit = labourmanagement_form.cleaned_data['price_unit']

         currency = pick_currency(user_instance)

         try:
            plot_landclearance_instance = LandClearance.objects.get(date=date,farm=personID,plotID=Plot.objects.get(plotID=plotID,farm=personID))
         except LandClearance.DoesNotExist:
            plot_landclearance_instance =LandClearance(date = date,farm=Farm.objects.get(farmID=personID),plotID=Plot.objects.get(plotID=plotID,farm=Farm.objects.get(farmID=personID)),landclearanceoption=landclearanceoption,enteredpersonel= SystemUser.objects.get(user=request.user))
            plot_landclearance_instance.save()
         else:
            plot_landclearance_instance.landclearanceoption = landclearanceoption
            plot_landclearance_instance.save()

         try:
            plot_labourmanagament_instance = LabourManagament.objects.get(farm=personID,areaID=plotID,date=date)
            print('****1111****')
         except LabourManagament.DoesNotExist:
            print('****2222****')
            if labour == 'Family':
               plot_labourmanagament_instance = LabourManagament(date=date,family_female_time=family_female_time,family_male_time=family_male_time,farm=farm,areaID=plotID,areadescription='Plot',labour=labour,family_female_number=family_female_number,family_male_number=family_male_number,activity='land clearance',wage=wage,price_unit=currency,enteredpersonel=SystemUser.objects.get(user=request.user))
            elif labour == 'Hired':
               plot_labourmanagament_instance = LabourManagament(date=date,hired_female_time=hired_female_time,hired_male_time=hired_male_time,farm=farm,areaID=plotID,areadescription='Plot',labour=labour,hired_female_number=hired_female_number,hired_male_number=hired_male_number,activity='land clearance',wage=wage,price_unit=currency,enteredpersonel=SystemUser.objects.get(user=request.user))
            elif labour == 'FamilyHired':
               plot_labourmanagament_instance = LabourManagament(date=date,family_female_time=family_female_time,family_male_time=family_male_time,hired_female_time=hired_female_time,hired_male_time=hired_male_time,farm=farm,areaID=plotID,areadescription='Plot',labour=labour,hired_female_number=hired_female_number,hired_male_number=hired_male_number,family_female_number=family_female_number,family_male_number=family_male_number,activity='land clearance',wage=wage,price_unit=currency,enteredpersonel=SystemUser.objects.get(user=request.user))
            plot_labourmanagament_instance.save()
         else:
            print('****3333****')
            if labour == 'Family':
               plot_labourmanagament_instance.date = date
               plot_labourmanagament_instance.family_female_time = family_female_time
               plot_labourmanagament_instance.family_male_time = family_male_time
               plot_labourmanagament_instance.areadescription = 'Plot'
               plot_labourmanagament_instance.labour = labour
               plot_labourmanagament_instance.family_female_number = family_female_number
               plot_labourmanagament_instance.family_male_number = family_male_number
               plot_labourmanagament_instance.activity = 'land clearance'
               plot_labourmanagament_instance.wage = wage
               plot_labourmanagament_instance.enteredpersonel = SystemUser.objects.get(user=request.user)
            elif labour == 'Hired':
               plot_labourmanagament_instance.date = date
               plot_labourmanagament_instance.hired_female_time = hired_female_time
               plot_labourmanagament_instance.hired_male_time = hired_male_time
               plot_labourmanagament_instance.areadescription = 'Plot'
               plot_labourmanagament_instance.labour = labour
               plot_labourmanagament_instance.hired_female_number = hired_female_number
               plot_labourmanagament_instance.hired_male_number = hired_male_number
               plot_labourmanagament_instance.activity = 'land clearance'
               plot_labourmanagament_instance.wage = wage
               plot_labourmanagament_instance.enteredpersonel = SystemUser.objects.get(user=request.user)
            elif labour == 'FamilyHired':
               plot_labourmanagament_instance.date = date
               plot_labourmanagament_instance.family_female_time = family_female_time
               plot_labourmanagament_instance.family_male_time = family_male_time
               plot_labourmanagament_instance.areadescription = 'Plot'
               plot_labourmanagament_instance.labour = labour
               plot_labourmanagament_instance.family_female_number = family_female_number
               plot_labourmanagament_instance.family_male_number = family_male_number
               plot_labourmanagament_instance.hired_female_time = hired_female_time
               plot_labourmanagament_instance.hired_male_time = hired_male_time
               plot_labourmanagament_instance.hired_female_number = hired_female_number
               plot_labourmanagament_instance.hired_male_number = hired_male_number
               plot_labourmanagament_instance.activity = 'land clearance'
               plot_labourmanagament_instance.wage = wage
               plot_labourmanagament_instance.enteredpersonel = SystemUser.objects.get(user=request.user)
            plot_labourmanagament_instance.save()

         message='saved'
         return render(request,'iwmiproject/saved.html',locals())
      else:
         user_instance = SystemUser.objects.get(user=request.user)
         if user_instance.role == 'RA' or user_instance.role == 'ST':user_village = user_instance.village
         elif user_instance.role == 'ALL':user_country = user_instance.country
         elif user_instance.role == 'RS':researcher = user_instance.country
         currency = pick_currency(user_instance)
         return render(request,'iwmiproject/iwmiproject_edit/edit_landclearance_detail.html',locals())
   else:
      landclearance_instance = LandClearance.objects.get(farm=personID,plotID=Plot.objects.get(plotID=plotID,farm=personID),date=date)
      plot_labourmanagament_instance = LabourManagament.objects.get(farm=personID,areaID=plotID,date=date,activity = 'land clearance')

      landclearance_form = LandClearance_Form(instance = landclearance_instance)
      labourmanagement_form = LabourManagement_Form(instance = plot_labourmanagament_instance)

      if user_instance.role == 'RA' or user_instance.role == 'ST':user_village = user_instance.village
      elif user_instance.role == 'ALL':user_country = user_instance.country
      elif user_instance.role == 'RS':researcher = user_instance.country
      currency = pick_currency(user_instance)
      return render(request,'iwmiproject/iwmiproject_edit/edit_landclearance_detail.html',locals())


def land_clearance_detail(request,plotID,personID):
   if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('signup:login'))
   user_instance = SystemUser.objects.get(user=request.user)
   landclearance_instance = LandClearance.objects.filter(farm=personID,plotID=Plot.objects.get(plotID=plotID,farm=personID))

   if not landclearance_instance:
         return render(request,'iwmiproject/iwmiproject_display/none.html',locals())

   elif len(landclearance_instance) == 1:

      if request.method == 'POST':
         landclearance_form = LandClearance_Form(request.POST)
         labourmanagement_form = LabourManagement_Form(request.POST)

         if landclearance_form.is_valid() and labourmanagement_form.is_valid():
            farm = landclearance_form.cleaned_data['farm']
            plotID = landclearance_form.cleaned_data['plotID']
            date = landclearance_form.cleaned_data['date']
            landclearanceoption = landclearance_form.cleaned_data['landclearanceoption']

            labour = labourmanagement_form.cleaned_data['labour']
            hired_female_number = labourmanagement_form.cleaned_data['hired_female_number']
            hired_female_time = labourmanagement_form.cleaned_data['hired_female_time']
            hired_male_number = labourmanagement_form.cleaned_data['hired_male_number']
            hired_male_time = labourmanagement_form.cleaned_data['hired_male_time']

            family_female_number = labourmanagement_form.cleaned_data['family_female_number']
            family_female_time = labourmanagement_form.cleaned_data['family_female_time']
            family_male_number = labourmanagement_form.cleaned_data['family_male_number']
            family_male_time = labourmanagement_form.cleaned_data['family_male_time']
            #activity = labourmanagement_form.cleaned_data['activity']
            wage = labourmanagement_form.cleaned_data['wage']
            price_unit = labourmanagement_form.cleaned_data['price_unit']

            
            plot_landclearance_instance = LandClearance.objects.get(farm=personID,plotID=Plot.objects.get(plotID=plotID,farm=personID))
            plot_labourmanagament_instance = LabourManagament.objects.get(farm=personID,areaID=plotID,date=plot_landclearance_instance.date,activity = 'land clearance')
            
            plot_landclearance_instance.date = date
            plot_landclearance_instance.landclearanceoption = landclearanceoption

            if labour == 'Family':
               plot_labourmanagament_instance.date = date
               plot_labourmanagament_instance.family_female_time = family_female_time
               plot_labourmanagament_instance.family_male_time = family_male_time
               plot_labourmanagament_instance.areadescription = 'Plot'
               plot_labourmanagament_instance.labour = labour
               plot_labourmanagament_instance.family_female_number = family_female_number
               plot_labourmanagament_instance.family_male_number = family_male_number
               plot_labourmanagament_instance.activity = 'land clearance'
               plot_labourmanagament_instance.wage = wage
               plot_labourmanagament_instance.enteredpersonel = SystemUser.objects.get(user=request.user)
            elif labour == 'Hired':
               plot_labourmanagament_instance.date = date
               plot_labourmanagament_instance.hired_female_time = hired_female_time
               plot_labourmanagament_instance.hired_male_time = hired_male_time
               plot_labourmanagament_instance.areadescription = 'Plot'
               plot_labourmanagament_instance.labour = labour
               plot_labourmanagament_instance.hired_female_number = hired_female_number
               plot_labourmanagament_instance.hired_male_number = hired_male_number
               plot_labourmanagament_instance.activity = 'land clearance'
               plot_labourmanagament_instance.wage = wage
               plot_labourmanagament_instance.enteredpersonel = SystemUser.objects.get(user=request.user)
            elif labour == 'FamilyHired':
               plot_labourmanagament_instance.date = date
               plot_labourmanagament_instance.family_female_time = family_female_time
               plot_labourmanagament_instance.family_male_time = family_male_time
               plot_labourmanagament_instance.areadescription = 'Plot'
               plot_labourmanagament_instance.labour = labour
               plot_labourmanagament_instance.family_female_number = family_female_number
               plot_labourmanagament_instance.family_male_number = family_male_number
               plot_labourmanagament_instance.hired_female_time = hired_female_time
               plot_labourmanagament_instance.hired_male_time = hired_male_time
               plot_labourmanagament_instance.hired_female_number = hired_female_number
               plot_labourmanagament_instance.hired_male_number = hired_male_number
               plot_labourmanagament_instance.activity = 'land clearance'
               plot_labourmanagament_instance.wage = wage
               plot_labourmanagament_instance.enteredpersonel = SystemUser.objects.get(user=request.user)
            plot_labourmanagament_instance.save()
            plot_landclearance_instance.save()

            message='saved'
            return render(request,'iwmiproject/saved.html',locals())
         else:
            user_instance = SystemUser.objects.get(user=request.user)
            if user_instance.role == 'RA' or user_instance.role == 'ST':user_village = user_instance.village
            elif user_instance.role == 'ALL':user_country = user_instance.country
            elif user_instance.role == 'RS':researcher = user_instance.country
            currency = pick_currency(user_instance)
            return render(request,'iwmiproject/iwmiproject_edit/edit_landclearance_detail.html',locals())
      else:
         landclearance_instance = LandClearance.objects.get(farm=personID,plotID=Plot.objects.get(plotID=plotID,farm=personID))
         plot_labourmanagament_instance = LabourManagament.objects.get(farm=personID,areaID=plotID,date=landclearance_instance.date,activity = 'land clearance')

         landclearance_form = LandClearance_Form(instance = landclearance_instance)
         labourmanagement_form = LabourManagement_Form(instance = plot_labourmanagament_instance)

         if user_instance.role == 'RA' or user_instance.role == 'ST':user_village = user_instance.village
         elif user_instance.role == 'ALL':user_country = user_instance.country
         elif user_instance.role == 'RS':researcher = user_instance.country
         currency = pick_currency(user_instance)
         return render(request,'iwmiproject/iwmiproject_edit/edit_landclearance_detail.html',locals())

   else:
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
      return render(request,'iwmiproject/iwmiproject_display/landclearance_detail_display.html',context)


def edit_land_preparation(request,plotID,personID):
   if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('signup:login'))

   user_instance = SystemUser.objects.get(user=request.user)
   if user_instance.role == 'RA' or user_instance.role == 'ST':user_village = user_instance.village
   elif user_instance.role == 'ALL':user_country = user_instance.country
   elif user_instance.role == 'RS':researcher = user_instance.country
   currency = pick_currency(user_instance)

   landpreparation_instance = LandPreparation.objects.filter(farm=personID,plotID=Plot.objects.get(plotID=plotID,farm=personID))

   if not landpreparation_instance:
         return render(request,'iwmiproject/iwmiproject_display/none.html',locals())

   elif len(landpreparation_instance) == 1:

      if request.method == 'POST':
         landpreparation_form = LandPreparation_Form(request.POST)
         labourmanagement_form = LabourManagement_Form(request.POST)

         if landpreparation_form.is_valid() and labourmanagement_form.is_valid():
            farm = landpreparation_form.cleaned_data['farm']
            plotID = landpreparation_form.cleaned_data['plotID']
            date = landpreparation_form.cleaned_data['date']
            landpreparationtool = landpreparation_form.cleaned_data['landpreparationtool']
            other = landpreparation_form.cleaned_data['other']
            
            labour = labourmanagement_form.cleaned_data['labour']
            hired_female_number = labourmanagement_form.cleaned_data['hired_female_number']
            hired_female_time = labourmanagement_form.cleaned_data['hired_female_time']
            hired_male_number = labourmanagement_form.cleaned_data['hired_male_number']
            hired_male_time = labourmanagement_form.cleaned_data['hired_male_time']
            family_female_number = labourmanagement_form.cleaned_data['family_female_number']
            family_female_time = labourmanagement_form.cleaned_data['family_female_time']
            family_male_number = labourmanagement_form.cleaned_data['family_male_number']
            family_male_time = labourmanagement_form.cleaned_data['family_male_time']
            wage = labourmanagement_form.cleaned_data['wage']
            price_unit = labourmanagement_form.cleaned_data['price_unit']

            
            plot_landpreparation_instance = LandPreparation.objects.get(farm=personID,plotID=Plot.objects.get(plotID=plotID,farm=personID))
            plot_labourmanagament_instance = LabourManagament.objects.get(farm=personID,areaID=plotID,date=plot_landpreparation_instance.date,activity = 'land preparation')

            plot_landpreparation_instance.date = date
            if other =='99999999':
               plot_landpreparation_instance.landpreparationtool = landpreparationtool
            else:
               plot_landpreparation_instance.landpreparationtool = other
            plot_landpreparation_instance.save()

            if labour == 'Family':
               plot_labourmanagament_instance.date = date
               plot_labourmanagament_instance.family_female_time = family_female_time
               plot_labourmanagament_instance.family_male_time = family_male_time
               plot_labourmanagament_instance.areadescription = 'Plot'
               plot_labourmanagament_instance.labour = labour
               plot_labourmanagament_instance.family_female_number = family_female_number
               plot_labourmanagament_instance.family_male_number = family_male_number
               plot_labourmanagament_instance.activity = 'land preparation'
               plot_labourmanagament_instance.wage = wage
               plot_labourmanagament_instance.enteredpersonel = SystemUser.objects.get(user=request.user)
            elif labour == 'Hired':
               plot_labourmanagament_instance.date = date
               plot_labourmanagament_instance.hired_female_time = hired_female_time
               plot_labourmanagament_instance.hired_male_time = hired_male_time
               plot_labourmanagament_instance.areadescription = 'Plot'
               plot_labourmanagament_instance.labour = labour
               plot_labourmanagament_instance.hired_female_number = hired_female_number
               plot_labourmanagament_instance.hired_male_number = hired_male_number
               plot_labourmanagament_instance.activity = 'land preparation'
               plot_labourmanagament_instance.wage = wage
               plot_labourmanagament_instance.enteredpersonel = SystemUser.objects.get(user=request.user)
            elif labour == 'FamilyHired':
               plot_labourmanagament_instance.date = date
               plot_labourmanagament_instance.family_female_time = family_female_time
               plot_labourmanagament_instance.family_male_time = family_male_time
               plot_labourmanagament_instance.areadescription = 'Plot'
               plot_labourmanagament_instance.labour = labour
               plot_labourmanagament_instance.family_female_number = family_female_number
               plot_labourmanagament_instance.family_male_number = family_male_number
               plot_labourmanagament_instance.hired_female_time = hired_female_time
               plot_labourmanagament_instance.hired_male_time = hired_male_time
               plot_labourmanagament_instance.hired_female_number = hired_female_number
               plot_labourmanagament_instance.hired_male_number = hired_male_number
               plot_labourmanagament_instance.activity = 'land preparation'
               plot_labourmanagament_instance.wage = wage
               plot_labourmanagament_instance.enteredpersonel = SystemUser.objects.get(user=request.user)

            plot_labourmanagament_instance.save()
            

            message='saved'
            return render(request,'iwmiproject/saved.html',locals())
         else:
            return render(request,'iwmiproject/iwmiproject_edit/edit_landpreparation_specific_detail.html',locals())
      else:
         landpreparation_instance = LandPreparation.objects.get(farm=personID,plotID=Plot.objects.get(plotID=plotID,farm=personID))
         plot_labourmanagament_instance = LabourManagament.objects.get(farm=personID,areaID=plotID,date=landpreparation_instance.date,activity = 'land preparation')
         landpreparation_form = LandPreparation_Form(instance = landpreparation_instance)
         labourmanagement_form = LabourManagement_Form(instance = plot_labourmanagament_instance)
         return render(request,'iwmiproject/iwmiproject_edit/edit_landpreparation_specific_detail.html',locals())
   else:
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
      return render(request,'iwmiproject/iwmiproject_display/landpreparation_detail_display.html',context)

def edit_landpreparation_specific_detail(request,plotID,personID,date):
   if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('signup:login'))

   user_instance = SystemUser.objects.get(user=request.user)
   if user_instance.role == 'RA' or user_instance.role == 'ST':user_village = user_instance.village
   elif user_instance.role == 'ALL':user_country = user_instance.country
   elif user_instance.role == 'RS':researcher = user_instance.country
   currency = pick_currency(user_instance)

   landpreparation_instance = LandPreparation.objects.filter(farm=personID,plotID=Plot.objects.get(plotID=plotID,farm=personID))

   if not landpreparation_instance:
      return render(request,'iwmiproject/iwmiproject_display/none.html',locals())

   if request.method == 'POST':
      landpreparation_form = LandPreparation_Form(request.POST)
      labourmanagement_form = LabourManagement_Form(request.POST)

      if landpreparation_form.is_valid() and labourmanagement_form.is_valid():
         farm = landpreparation_form.cleaned_data['farm']
         plotID = landpreparation_form.cleaned_data['plotID']
         date = landpreparation_form.cleaned_data['date']
         landpreparationtool = landpreparation_form.cleaned_data['landpreparationtool']
         other = landpreparation_form.cleaned_data['other']
         
         labour = labourmanagement_form.cleaned_data['labour']
         hired_female_number = labourmanagement_form.cleaned_data['hired_female_number']
         hired_female_time = labourmanagement_form.cleaned_data['hired_female_time']
         hired_male_number = labourmanagement_form.cleaned_data['hired_male_number']
         hired_male_time = labourmanagement_form.cleaned_data['hired_male_time']
         family_female_number = labourmanagement_form.cleaned_data['family_female_number']
         family_female_time = labourmanagement_form.cleaned_data['family_female_time']
         family_male_number = labourmanagement_form.cleaned_data['family_male_number']
         family_male_time = labourmanagement_form.cleaned_data['family_male_time']
         wage = labourmanagement_form.cleaned_data['wage']
         price_unit = labourmanagement_form.cleaned_data['price_unit']
         
         
               
         try:
            plot_landpreparation_instance = LandPreparation.objects.get(date=date,farm=personID,plotID=Plot.objects.get(plotID=plotID,farm=personID))
         except LandPreparation.DoesNotExist:
            if other =='99999999':
               plot_landpreparation_instance =LandPreparation(date = date,farm=Farm.objects.get(farmID=personID),plotID=Plot.objects.get(plotID=plotID,farm=Farm.objects.get(farmID=personID)),landpreparationtool=landpreparationtool,enteredpersonel= SystemUser.objects.get(user=request.user))
            else:
               plot_landpreparation_instance =LandPreparation(date = date,farm=Farm.objects.get(farmID=personID),plotID=Plot.objects.get(plotID=plotID,farm=Farm.objects.get(farmID=personID)),landpreparationtool=other,enteredpersonel= SystemUser.objects.get(user=request.user))
            plot_landpreparation_instance.save()
         else:
            if other =='99999999':
               plot_landpreparation_instance.landpreparationtool = landpreparationtool
            else:
               plot_landpreparation_instance.landpreparationtool = other
            #plot_landpreparation_instance.landpreparationtool = landpreparationtool
            plot_landpreparation_instance.save()

         try:
            plot_labourmanagament_instance = LabourManagament.objects.get(farm=personID,areaID=plotID,date=date,activity='land preparation')
         except LabourManagament.DoesNotExist:
            if labour == 'Family':
               plot_labourmanagament_instance = LabourManagament(date=date,family_female_time=family_female_time,family_male_time=family_male_time,farm=farm,areaID=plotID,areadescription='Plot',labour=labour,family_female_number=family_female_number,family_male_number=family_male_number,activity='land preparation',wage=wage,price_unit=currency,enteredpersonel=SystemUser.objects.get(user=request.user))
            elif labour == 'Hired':
               plot_labourmanagament_instance = LabourManagament(date=date,hired_female_time=hired_female_time,hired_male_time=hired_male_time,farm=farm,areaID=plotID,areadescription='Plot',labour=labour,hired_female_number=hired_female_number,hired_male_number=hired_male_number,activity='land preparation',wage=wage,price_unit=currency,enteredpersonel=SystemUser.objects.get(user=request.user))
            elif labour == 'FamilyHired':
               plot_labourmanagament_instance = LabourManagament(date=date,family_female_time=family_female_time,family_male_time=family_male_time,hired_female_time=hired_female_time,hired_male_time=hired_male_time,farm=farm,areaID=plotID,areadescription='Plot',labour=labour,hired_female_number=hired_female_number,hired_male_number=hired_male_number,family_female_number=family_female_number,family_male_number=family_male_number,activity='land preparation',wage=wage,price_unit=currency,enteredpersonel=SystemUser.objects.get(user=request.user))
            plot_labourmanagament_instance.save()
         else:
            if labour == 'Family':
               plot_labourmanagament_instance.date = date
               plot_labourmanagament_instance.family_female_time = family_female_time
               plot_labourmanagament_instance.family_male_time = family_male_time
               plot_labourmanagament_instance.areadescription = 'Plot'
               plot_labourmanagament_instance.labour = labour
               plot_labourmanagament_instance.family_female_number = family_female_number
               plot_labourmanagament_instance.family_male_number = family_male_number
               plot_labourmanagament_instance.activity = 'land preparation'
               plot_labourmanagament_instance.wage = wage
               plot_labourmanagament_instance.enteredpersonel = SystemUser.objects.get(user=request.user)
            elif labour == 'Hired':
               plot_labourmanagament_instance.date = date
               plot_labourmanagament_instance.hired_female_time = hired_female_time
               plot_labourmanagament_instance.hired_male_time = hired_male_time
               plot_labourmanagament_instance.areadescription = 'Plot'
               plot_labourmanagament_instance.labour = labour
               plot_labourmanagament_instance.hired_female_number = hired_female_number
               plot_labourmanagament_instance.hired_male_number = hired_male_number
               plot_labourmanagament_instance.activity = 'land preparation'
               plot_labourmanagament_instance.wage = wage
               plot_labourmanagament_instance.enteredpersonel = SystemUser.objects.get(user=request.user)
            elif labour == 'FamilyHired':
               plot_labourmanagament_instance.date = date
               plot_labourmanagament_instance.family_female_time = family_female_time
               plot_labourmanagament_instance.family_male_time = family_male_time
               plot_labourmanagament_instance.areadescription = 'Plot'
               plot_labourmanagament_instance.labour = labour
               plot_labourmanagament_instance.family_female_number = family_female_number
               plot_labourmanagament_instance.family_male_number = family_male_number
               plot_labourmanagament_instance.hired_female_time = hired_female_time
               plot_labourmanagament_instance.hired_male_time = hired_male_time
               plot_labourmanagament_instance.hired_female_number = hired_female_number
               plot_labourmanagament_instance.hired_male_number = hired_male_number
               plot_labourmanagament_instance.activity = 'land preparation'
               plot_labourmanagament_instance.wage = wage
               plot_labourmanagament_instance.enteredpersonel = SystemUser.objects.get(user=request.user)
            plot_labourmanagament_instance.save()

         message='saved'
         return render(request,'iwmiproject/saved.html',locals())
      else:
         return render(request,'iwmiproject/iwmiproject_edit/edit_landpreparation_specific_detail.html',locals())
   else:
      landpreparation_instance = LandPreparation.objects.get(farm=personID,plotID=Plot.objects.get(plotID=plotID,farm=personID),date=date)
      plot_labourmanagament_instance = LabourManagament.objects.get(farm=personID,areaID=plotID,date=date,activity = 'land preparation')

      landpreparation_form = LandPreparation_Form(instance = landpreparation_instance)
      labourmanagement_form = LabourManagement_Form(instance = plot_labourmanagament_instance)

      return render(request,'iwmiproject/iwmiproject_edit/edit_landpreparation_specific_detail.html',locals())


def edit_plot_fertilizermanagement(request,plotID,personID):
   if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('signup:login'))

   user_instance = SystemUser.objects.get(user=request.user)
   if user_instance.role == 'RA' or user_instance.role == 'ST':user_village = user_instance.village
   elif user_instance.role == 'ALL':user_country = user_instance.country
   elif user_instance.role == 'RS':researcher = user_instance.country
   currency = pick_currency(user_instance)

   fertilizermanagement_instance = FertilizerManagement.objects.filter(farm=personID,plotID=Plot.objects.get(plotID=plotID,farm=personID))

   if not fertilizermanagement_instance:
         return render(request,'iwmiproject/iwmiproject_display/none.html',locals())

   elif len(fertilizermanagement_instance) == 1:

      if request.method == 'POST':
         try:
            fertilizer_instance = Fertilizer.objects.get(name=request.POST['fertilizer'])
         except Fertilizer.DoesNotExist:
            fertilizer_instance = Fertilizer(name=request.POST['fertilizer'])
            fertilizer_instance.save()
         myfertilizer  = Fertilizer.objects.get(name=request.POST['fertilizer'])
            
         fertilizermanagement_form = FertilizerManagement_Form(request.POST,instance = myfertilizer)
         labourmanagement_form = LabourManagement_Form(request.POST)

         if fertilizermanagement_form.is_valid() and labourmanagement_form.is_valid():
            date = fertilizermanagement_form.cleaned_data['date']
            farm = fertilizermanagement_form.cleaned_data['farm']
            plotID = fertilizermanagement_form.cleaned_data['plotID']
            nurseryID = fertilizermanagement_form.cleaned_data['nurseryID']
            crop_stage = fertilizermanagement_form.cleaned_data['crop_stage']
            fertilizer = fertilizermanagement_form.cleaned_data['fertilizer']
            compost_kind = fertilizermanagement_form.cleaned_data['compost_kind']
            quantity_in_kg = fertilizermanagement_form.cleaned_data['quantity_in_kg']
            fertilizer_management = fertilizermanagement_form.cleaned_data['fertilizer_management']
            price = fertilizermanagement_form.cleaned_data['price']

            labour = labourmanagement_form.cleaned_data['labour']
            hired_female_number = labourmanagement_form.cleaned_data['hired_female_number']
            hired_female_time = labourmanagement_form.cleaned_data['hired_female_time']
            hired_male_number = labourmanagement_form.cleaned_data['hired_male_number']
            hired_male_time = labourmanagement_form.cleaned_data['hired_male_time']
            family_female_number = labourmanagement_form.cleaned_data['family_female_number']
            family_female_time = labourmanagement_form.cleaned_data['family_female_time']
            family_male_number = labourmanagement_form.cleaned_data['family_male_number']
            family_male_time = labourmanagement_form.cleaned_data['family_male_time']
            wage = labourmanagement_form.cleaned_data['wage']
            price_unit = labourmanagement_form.cleaned_data['price_unit']
            
            try:
               fertilizer_instance = Fertilizer.objects.get(name=fertilizer)
            except Fertilizer.DoesNotExist:
               fertilizer_instance = Fertilizer(name=fertilizer)
               fertilizer_instance.save()
            fertilizer = Fertilizer.objects.get(name=fertilizer)
         
            plot_fertilizermanagement_instance = FertilizerManagement.objects.get(farm=personID,plotID=Plot.objects.get(plotID=plotID,farm=personID))
            plot_labourmanagament_instance = LabourManagament.objects.get(farm=personID,areaID=plotID,date=plot_fertilizermanagement_instance.date)

            plot_fertilizermanagement_instance.date = date
            plot_fertilizermanagement_instance.nurseryID = nurseryID
            plot_fertilizermanagement_instance.crop_stage = crop_stage
            plot_fertilizermanagement_instance.fertilizer = fertilizer
            if str(fertilizer) == 'Compost':plot_fertilizermanagement_instance.compost_kind = compost_kind
            plot_fertilizermanagement_instance.quantity_in_kg = quantity_in_kg
            plot_fertilizermanagement_instance.fertilizer_management = fertilizer_management
            plot_fertilizermanagement_instance.price = price
            plot_fertilizermanagement_instance.price_unit = currency

            if labour == 'Family':
               plot_labourmanagament_instance.date = date
               plot_labourmanagament_instance.family_female_time = family_female_time
               plot_labourmanagament_instance.family_male_time = family_male_time
               plot_labourmanagament_instance.areadescription = 'Plot'
               plot_labourmanagament_instance.labour = labour
               plot_labourmanagament_instance.family_female_number = family_female_number
               plot_labourmanagament_instance.family_male_number = family_male_number
               plot_labourmanagament_instance.activity = 'Fertilizer Application'
               plot_labourmanagament_instance.wage = wage
               plot_labourmanagament_instance.enteredpersonel = SystemUser.objects.get(user=request.user)
            elif labour == 'Hired':
               plot_labourmanagament_instance.date = date
               plot_labourmanagament_instance.hired_female_time = hired_female_time
               plot_labourmanagament_instance.hired_male_time = hired_male_time
               plot_labourmanagament_instance.areadescription = 'Plot'
               plot_labourmanagament_instance.labour = labour
               plot_labourmanagament_instance.hired_female_number = hired_female_number
               plot_labourmanagament_instance.hired_male_number = hired_male_number
               plot_labourmanagament_instance.activity = 'Fertilizer Application'
               plot_labourmanagament_instance.wage = wage
               plot_labourmanagament_instance.enteredpersonel = SystemUser.objects.get(user=request.user)
            elif labour == 'FamilyHired':
               plot_labourmanagament_instance.date = date
               plot_labourmanagament_instance.family_female_time = family_female_time
               plot_labourmanagament_instance.family_male_time = family_male_time
               plot_labourmanagament_instance.areadescription = 'Plot'
               plot_labourmanagament_instance.labour = labour
               plot_labourmanagament_instance.family_female_number = family_female_number
               plot_labourmanagament_instance.family_male_number = family_male_number
               plot_labourmanagament_instance.hired_female_time = hired_female_time
               plot_labourmanagament_instance.hired_male_time = hired_male_time
               plot_labourmanagament_instance.hired_female_number = hired_female_number
               plot_labourmanagament_instance.hired_male_number = hired_male_number
               plot_labourmanagament_instance.activity = 'Fertilizer Application'
               plot_labourmanagament_instance.wage = wage
               plot_labourmanagament_instance.enteredpersonel = SystemUser.objects.get(user=request.user)

            plot_labourmanagament_instance.save()
            plot_fertilizermanagement_instance.save()

            message='saved'
            return render(request,'iwmiproject/saved.html',locals())
         else:
            return render(request,'iwmiproject/iwmiproject_edit/edit_plot_fertilizermanagement_specific_detail.html',locals())
      else:
         fertilizermanagement_instance = FertilizerManagement.objects.get(farm=personID,plotID=Plot.objects.get(plotID=plotID,farm=personID))
         plot_labourmanagament_instance = LabourManagament.objects.get(farm=personID,areaID=plotID,date=fertilizermanagement_instance.date)

         fertilizermanagement_form = FertilizerManagement_Form(instance = fertilizermanagement_instance)
         labourmanagement_form = LabourManagement_Form(instance = plot_labourmanagament_instance)
         return render(request,'iwmiproject/iwmiproject_edit/edit_plot_fertilizermanagement_specific_detail.html',locals())
   else:
      if user_instance.role == 'RA' or user_instance.role == 'ST':
         user_village = user_instance.village
         plot_fertilizermanagement_queryset_list = LandPreFertilizerManagementparation.objects.filter(enteredpersonel=user_instance,farm=personID,plotID=Plot.objects.get(plotID=plotID,farm=personID)).select_related()
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
      return render(request,'iwmiproject/iwmiproject_display/plot_fertilizermanagement_detail_display.html',context)


def edit_fertilizermanagement_specific_detail(request,plotID,personID,date,fertilizer):
   if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('signup:login'))

   user_instance = SystemUser.objects.get(user=request.user)
   if user_instance.role == 'RA' or user_instance.role == 'ST':user_village = user_instance.village
   elif user_instance.role == 'ALL':user_country = user_instance.country
   elif user_instance.role == 'RS':researcher = user_instance.country
   currency = pick_currency(user_instance)

   fertilizermanagement_instance = FertilizerManagement.objects.filter(farm=personID,plotID=Plot.objects.get(plotID=plotID,farm=personID))

   if request.method == 'POST':      
      try:
         fertilizer_instance = Fertilizer.objects.get(name=request.POST['fertilizer'])
      except Fertilizer.DoesNotExist:
         fertilizer_instance = Fertilizer(name=request.POST['fertilizer'])
         fertilizer_instance.save()
      myfertilizer  = Fertilizer.objects.get(name=request.POST['fertilizer'])
      fertilizermanagement_form = FertilizerManagement_Form(request.POST,instance = myfertilizer)
      labourmanagement_form = LabourManagement_Form(request.POST)
      
      if fertilizermanagement_form.is_valid() and labourmanagement_form.is_valid():
         date = fertilizermanagement_form.cleaned_data['date']
         farm = fertilizermanagement_form.cleaned_data['farm']
         plotID = fertilizermanagement_form.cleaned_data['plotID']
         nurseryID = fertilizermanagement_form.cleaned_data['nurseryID']
         crop_stage = fertilizermanagement_form.cleaned_data['crop_stage']
         fertilizer = fertilizermanagement_form.cleaned_data['fertilizer']
         compost_kind = fertilizermanagement_form.cleaned_data['compost_kind']
         quantity_in_kg = fertilizermanagement_form.cleaned_data['quantity_in_kg']
         fertilizer_management = fertilizermanagement_form.cleaned_data['fertilizer_management']
         price = fertilizermanagement_form.cleaned_data['price']

         labour = labourmanagement_form.cleaned_data['labour']
         hired_female_number = labourmanagement_form.cleaned_data['hired_female_number']
         hired_female_time = labourmanagement_form.cleaned_data['hired_female_time']
         hired_male_number = labourmanagement_form.cleaned_data['hired_male_number']
         hired_male_time = labourmanagement_form.cleaned_data['hired_male_time']
         family_female_number = labourmanagement_form.cleaned_data['family_female_number']
         family_female_time = labourmanagement_form.cleaned_data['family_female_time']
         family_male_number = labourmanagement_form.cleaned_data['family_male_number']
         family_male_time = labourmanagement_form.cleaned_data['family_male_time']
         wage = labourmanagement_form.cleaned_data['wage']
         price_unit = labourmanagement_form.cleaned_data['price_unit']

         try:
            fertilizer_instance = Fertilizer.objects.get(name=fertilizer)
         except Fertilizer.DoesNotExist:
            fertilizer_instance = Fertilizer(name=fertilizer)
            fertilizer_instance.save()
         fertilizer = Fertilizer.objects.get(name=fertilizer)
         try:
            plot_fertilizermanagement_instance = FertilizerManagement.objects.get(date=date,farm=personID,plotID=Plot.objects.get(plotID=plotID,farm=personID))
         except FertilizerManagement.DoesNotExist:
            plot_fertilizermanagement_instance = FertilizerManagement(date=date,farm=farm,plotID=Plot.objects.get(plotID=plotID,farm=farm),crop_stage=crop_stage,fertilizer=Fertilizer.objects.get(name=fertilizer),compost_kind=compost_kind,quantity_in_kg=quantity_in_kg,fertilizer_management=fertilizer_management,price=price,price_unit=currency,enteredpersonel=SystemUser.objects.get(user=request.user))
            plot_fertilizermanagement_instance.save()
         else:
            plot_fertilizermanagement_instance.date = date
            plot_fertilizermanagement_instance.nurseryID = nurseryID
            plot_fertilizermanagement_instance.crop_stage = crop_stage
            plot_fertilizermanagement_instance.fertilizer = fertilizer
            if str(fertilizer) == 'Compost':plot_fertilizermanagement_instance.compost_kind = compost_kind
            plot_fertilizermanagement_instance.quantity_in_kg = quantity_in_kg
            plot_fertilizermanagement_instance.fertilizer_management = fertilizer_management
            plot_fertilizermanagement_instance.price = price
            plot_fertilizermanagement_instance.price_unit = currency
            plot_fertilizermanagement_instance.save()

         try:
            plot_labourmanagament_instance = LabourManagament.objects.get(farm=personID,areaID=plotID,date=date,activity='Fertilizer Application')
         except LabourManagament.DoesNotExist:
            if labour == 'Family':
               plot_labourmanagament_instance = LabourManagament(date=date,family_female_time=family_female_time,family_male_time=family_male_time,farm=farm,areaID=plotID,areadescription='Plot',labour=labour,family_female_number=family_female_number,family_male_number=family_male_number,activity='Fertilizer Application',wage=wage,price_unit=currency,enteredpersonel=SystemUser.objects.get(user=request.user))
            elif labour == 'Hired':
               plot_labourmanagament_instance = LabourManagament(date=date,hired_female_time=hired_female_time,hired_male_time=hired_male_time,farm=farm,areaID=plotID,areadescription='Plot',labour=labour,hired_female_number=hired_female_number,hired_male_number=hired_male_number,activity='Fertilizer Application',wage=wage,price_unit=currency,enteredpersonel=SystemUser.objects.get(user=request.user))
            elif labour == 'FamilyHired':
               plot_labourmanagament_instance = LabourManagament(date=date,family_female_time=family_female_time,family_male_time=family_male_time,hired_female_time=hired_female_time,hired_male_time=hired_male_time,farm=farm,areaID=plotID,areadescription='Plot',labour=labour,hired_female_number=hired_female_number,hired_male_number=hired_male_number,family_female_number=family_female_number,family_male_number=family_male_number,activity='Fertilizer Application',wage=wage,price_unit=currency,enteredpersonel=SystemUser.objects.get(user=request.user))
            plot_labourmanagament_instance.save()
         else:
            if labour == 'Family':
               plot_labourmanagament_instance.date = date
               plot_labourmanagament_instance.family_female_time = family_female_time
               plot_labourmanagament_instance.family_male_time = family_male_time
               plot_labourmanagament_instance.areadescription = 'Plot'
               plot_labourmanagament_instance.labour = labour
               plot_labourmanagament_instance.family_female_number = family_female_number
               plot_labourmanagament_instance.family_male_number = family_male_number
               plot_labourmanagament_instance.activity = 'Fertilizer Application'
               plot_labourmanagament_instance.wage = wage
               plot_labourmanagament_instance.enteredpersonel = SystemUser.objects.get(user=request.user)
            elif labour == 'Hired':
               plot_labourmanagament_instance.date = date
               plot_labourmanagament_instance.hired_female_time = hired_female_time
               plot_labourmanagament_instance.hired_male_time = hired_male_time
               plot_labourmanagament_instance.areadescription = 'Plot'
               plot_labourmanagament_instance.labour = labour
               plot_labourmanagament_instance.hired_female_number = hired_female_number
               plot_labourmanagament_instance.hired_male_number = hired_male_number
               plot_labourmanagament_instance.activity = 'Fertilizer Application'
               plot_labourmanagament_instance.wage = wage
               plot_labourmanagament_instance.enteredpersonel = SystemUser.objects.get(user=request.user)
            elif labour == 'FamilyHired':
               plot_labourmanagament_instance.date = date
               plot_labourmanagament_instance.family_female_time = family_female_time
               plot_labourmanagament_instance.family_male_time = family_male_time
               plot_labourmanagament_instance.areadescription = 'Plot'
               plot_labourmanagament_instance.labour = labour
               plot_labourmanagament_instance.family_female_number = family_female_number
               plot_labourmanagament_instance.family_male_number = family_male_number
               plot_labourmanagament_instance.hired_female_time = hired_female_time
               plot_labourmanagament_instance.hired_male_time = hired_male_time
               plot_labourmanagament_instance.hired_female_number = hired_female_number
               plot_labourmanagament_instance.hired_male_number = hired_male_number
               plot_labourmanagament_instance.activity = 'Fertilizer Application'
               plot_labourmanagament_instance.wage = wage
               plot_labourmanagament_instance.enteredpersonel = SystemUser.objects.get(user=request.user)
            plot_labourmanagament_instance.save()

         message='saved'
         return render(request,'iwmiproject/saved.html',locals())
      else:
         return render(request,'iwmiproject/iwmiproject_edit/edit_plot_fertilizermanagement_specific_detail.html',locals())
   else:
      fertilizermanagement_instance = FertilizerManagement.objects.get(farm=personID,plotID=Plot.objects.get(plotID=plotID,farm=personID),date=date,fertilizer=fertilizer)
      plot_labourmanagament_instance = LabourManagament.objects.get(farm=personID,areaID=plotID,date=date,activity = 'Fertilizer Application')

      fertilizermanagement_form = FertilizerManagement_Form(instance = fertilizermanagement_instance)
      labourmanagement_form = LabourManagement_Form(instance = plot_labourmanagament_instance)

      return render(request,'iwmiproject/iwmiproject_edit/edit_plot_fertilizermanagement_specific_detail.html',locals())



def edit_plot_pestcidemanagement(request,plotID,personID):
   if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('signup:login'))

   user_instance = SystemUser.objects.get(user=request.user)
   if user_instance.role == 'RA' or user_instance.role == 'ST':user_village = user_instance.village
   elif user_instance.role == 'ALL':user_country = user_instance.country
   elif user_instance.role == 'RS':researcher = user_instance.country
   currency = pick_currency(user_instance)
      
   pesticidemanagement_instance = PesticideManagement.objects.filter(farm=personID,plotID=Plot.objects.get(plotID=plotID,farm=personID))

   if not pesticidemanagement_instance:
         return render(request,'iwmiproject/iwmiproject_display/none.html',locals())

   elif len(pesticidemanagement_instance) == 1:

      if request.method == 'POST':
         
         try:
            pesticide_instance = Pesticide.objects.get(name=request.POST['name'])
         except Pesticide.DoesNotExist:
            pesticide_instance = Pesticide(name=request.POST['name'])
            pesticide_instance.save()
         pesticide  = Pesticide.objects.get(name=request.POST['name'])
         pesticidemanagement_form = PesticideManagement_Form(request.POST,instance = pesticide)
         
         labourmanagement_form = LabourManagement_Form(request.POST)

         if pesticidemanagement_form.is_valid() and labourmanagement_form.is_valid():
            date = pesticidemanagement_form.cleaned_data['date']
            farm = pesticidemanagement_form.cleaned_data['farm']
            plotID = pesticidemanagement_form.cleaned_data['plotID']
            name = pesticidemanagement_form.cleaned_data['name']
            crop_stage = pesticidemanagement_form.cleaned_data['crop_stage']
            form = pesticidemanagement_form.cleaned_data['form']
            water_volume = pesticidemanagement_form.cleaned_data['water_volume']
            quantity_in_litre = pesticidemanagement_form.cleaned_data['quantity_in_litre']
            quantity_in_kg = pesticidemanagement_form.cleaned_data['quantity_in_kg']
            price = pesticidemanagement_form.cleaned_data['price']

            labour = labourmanagement_form.cleaned_data['labour']
            hired_female_number = labourmanagement_form.cleaned_data['hired_female_number']
            hired_female_time = labourmanagement_form.cleaned_data['hired_female_time']
            hired_male_number = labourmanagement_form.cleaned_data['hired_male_number']
            hired_male_time = labourmanagement_form.cleaned_data['hired_male_time']
            family_female_number = labourmanagement_form.cleaned_data['family_female_number']
            family_female_time = labourmanagement_form.cleaned_data['family_female_time']
            family_male_number = labourmanagement_form.cleaned_data['family_male_number']
            family_male_time = labourmanagement_form.cleaned_data['family_male_time']
            wage = labourmanagement_form.cleaned_data['wage']
            price_unit = labourmanagement_form.cleaned_data['price_unit']

            plot_pesticidemanagement_instance = PesticideManagement.objects.get(farm=personID,plotID=Plot.objects.get(plotID=plotID,farm=personID))
            plot_labourmanagament_instance = LabourManagament.objects.get(farm=personID,areaID=plotID,date=plot_pesticidemanagement_instance.date,activity='Pesticide Application')
            
            try:
               Pesticide.objects.get(name=name)
            except Pesticide.DoesNotExist:
               Pesticide_instance = Pesticide(name=name)
               Pesticide_instance.save()
            name  = Pesticide.objects.get(name=name)
            
            plot_pesticidemanagement_instance.date = date
            plot_pesticidemanagement_instance.name = name
            plot_pesticidemanagement_instance.crop_stage = crop_stage
            plot_pesticidemanagement_instance.form = form
            plot_pesticidemanagement_instance.water_volume = water_volume
            plot_pesticidemanagement_instance.quantity_in_litre = quantity_in_litre
            plot_pesticidemanagement_instance.quantity_in_kg = quantity_in_kg
            plot_pesticidemanagement_instance.price = price

            
            if labour == 'Family':
               plot_labourmanagament_instance.date = date
               plot_labourmanagament_instance.family_female_time = family_female_time
               plot_labourmanagament_instance.family_male_time = family_male_time
               plot_labourmanagament_instance.areadescription = 'Plot'
               plot_labourmanagament_instance.labour = labour
               plot_labourmanagament_instance.family_female_number = family_female_number
               plot_labourmanagament_instance.family_male_number = family_male_number
               plot_labourmanagament_instance.activity = 'Pesticide Application'
               plot_labourmanagament_instance.wage = wage
               plot_labourmanagament_instance.enteredpersonel = SystemUser.objects.get(user=request.user)
            elif labour == 'Hired':
               plot_labourmanagament_instance.date = date
               plot_labourmanagament_instance.hired_female_time = hired_female_time
               plot_labourmanagament_instance.hired_male_time = hired_male_time
               plot_labourmanagament_instance.areadescription = 'Plot'
               plot_labourmanagament_instance.labour = labour
               plot_labourmanagament_instance.hired_female_number = hired_female_number
               plot_labourmanagament_instance.hired_male_number = hired_male_number
               plot_labourmanagament_instance.activity = 'Pesticide Application'
               plot_labourmanagament_instance.wage = wage
               plot_labourmanagament_instance.enteredpersonel = SystemUser.objects.get(user=request.user)
            elif labour == 'FamilyHired':
               plot_labourmanagament_instance.date = date
               plot_labourmanagament_instance.family_female_time = family_female_time
               plot_labourmanagament_instance.family_male_time = family_male_time
               plot_labourmanagament_instance.areadescription = 'Plot'
               plot_labourmanagament_instance.labour = labour
               plot_labourmanagament_instance.family_female_number = family_female_number
               plot_labourmanagament_instance.family_male_number = family_male_number
               plot_labourmanagament_instance.hired_female_time = hired_female_time
               plot_labourmanagament_instance.hired_male_time = hired_male_time
               plot_labourmanagament_instance.hired_female_number = hired_female_number
               plot_labourmanagament_instance.hired_male_number = hired_male_number
               plot_labourmanagament_instance.activity = 'Pesticide Application'
               plot_labourmanagament_instance.wage = wage
               plot_labourmanagament_instance.enteredpersonel = SystemUser.objects.get(user=request.user)

            plot_labourmanagament_instance.save()
            plot_pesticidemanagement_instance.save()

            message='saved'
            return render(request,'iwmiproject/saved.html',locals())
         else:
            return render(request,'iwmiproject/iwmiproject_edit/edit_plot_pesticidemanagement_specific_detail.html',locals())
      else:
         pesticidemanagement_instance = PesticideManagement.objects.get(farm=personID,plotID=Plot.objects.get(plotID=plotID,farm=personID))
         plot_labourmanagament_instance = LabourManagament.objects.get(farm=personID,areaID=plotID,date=pesticidemanagement_instance.date,activity = 'Pesticide Application')

         pesticidemanagement_form = PesticideManagement_Form(instance = pesticidemanagement_instance)
         labourmanagement_form = LabourManagement_Form(instance = plot_labourmanagament_instance)
         return render(request,'iwmiproject/iwmiproject_edit/edit_plot_pesticidemanagement_specific_detail.html',locals())
   else:
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
      return render(request,'iwmiproject/iwmiproject_display/plot_pesticidemanagement_detail_display.html',context)


def edit_pesticidemanagement_specific_detail(request,plotID,personID,date,pesticide):
   if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('signup:login'))

   user_instance = SystemUser.objects.get(user=request.user)
   if user_instance.role == 'RA' or user_instance.role == 'ST':user_village = user_instance.village
   elif user_instance.role == 'ALL':user_country = user_instance.country
   elif user_instance.role == 'RS':researcher = user_instance.country
   currency = pick_currency(user_instance)

   pesticidemanagement_instance = PesticideManagement.objects.filter(farm=personID,plotID=Plot.objects.get(plotID=plotID,farm=personID))

   if request.method == 'POST':
      try:
         pesticide_instance = Pesticide.objects.get(name=request.POST['name'])
      except Pesticide.DoesNotExist:
         pesticide_instance = Pesticide(name=request.POST['name'])
         pesticide_instance.save()
      pesticide  = Pesticide.objects.get(name=request.POST['name'])
      
      pesticidemanagement_form = PesticideManagement_Form(request.POST,instance = pesticide)
      labourmanagement_form = LabourManagement_Form(request.POST)

      if pesticidemanagement_form.is_valid() and labourmanagement_form.is_valid():
         date = pesticidemanagement_form.cleaned_data['date']
         farm = pesticidemanagement_form.cleaned_data['farm']
         plotID = pesticidemanagement_form.cleaned_data['plotID']
         name = pesticidemanagement_form.cleaned_data['name']
         crop_stage = pesticidemanagement_form.cleaned_data['crop_stage']
         form = pesticidemanagement_form.cleaned_data['form']
         water_volume = pesticidemanagement_form.cleaned_data['water_volume']
         quantity_in_litre = pesticidemanagement_form.cleaned_data['quantity_in_litre']
         quantity_in_kg = pesticidemanagement_form.cleaned_data['quantity_in_kg']
         price = pesticidemanagement_form.cleaned_data['price']

         labour = labourmanagement_form.cleaned_data['labour']
         hired_female_number = labourmanagement_form.cleaned_data['hired_female_number']
         hired_female_time = labourmanagement_form.cleaned_data['hired_female_time']
         hired_male_number = labourmanagement_form.cleaned_data['hired_male_number']
         hired_male_time = labourmanagement_form.cleaned_data['hired_male_time']
         family_female_number = labourmanagement_form.cleaned_data['family_female_number']
         family_female_time = labourmanagement_form.cleaned_data['family_female_time']
         family_male_number = labourmanagement_form.cleaned_data['family_male_number']
         family_male_time = labourmanagement_form.cleaned_data['family_male_time']
         wage = labourmanagement_form.cleaned_data['wage']
         price_unit = labourmanagement_form.cleaned_data['price_unit']
         
         try:
            Pesticide.objects.get(name=name)
         except Pesticide.DoesNotExist:
            Pesticide_instance = Pesticide(name=name)
            Pesticide_instance.save()
         name  = Pesticide.objects.get(name=name)
            
         try:
            plot_pesticidemanagement_instance = PesticideManagement.objects.get(date=date,farm=personID,plotID=Plot.objects.get(plotID=plotID,farm=personID))
         except PesticideManagement.DoesNotExist:
            if form=='Liquid':
               plot_pesticidemanagement_instance = PesticideManagement(date=date,farm=farm,plotID=Plot.objects.get(plotID=plot,farm=farm),name=name,crop_stage=crop_stage,form=form,water_volume=water_volume,quantity_in_litre=quantity_lt,price=price,price_unit=currency,enteredpersonel=SystemUser.objects.get(user=request.user))
            elif form=='Solid':
               plot_pesticidemanagement_instance = PesticideManagement(date=date,farm=farm,plotID=Plot.objects.get(plotID=plot,farm=farm),name=name,crop_stage=crop_stage,form=form,quantity_in_kg=quantity_kg,price=price,price_unit=currency,enteredpersonel=SystemUser.objects.get(user=request.user))
            plot_pesticidemanagement_instance.save()
         else:
            plot_pesticidemanagement_instance.date = date
            plot_pesticidemanagement_instance.name = name
            plot_pesticidemanagement_instance.crop_stage = crop_stage
            plot_pesticidemanagement_instance.form = form
            plot_pesticidemanagement_instance.water_volume = water_volume
            plot_pesticidemanagement_instance.quantity_in_litre = quantity_in_litre
            plot_pesticidemanagement_instance.quantity_in_kg = quantity_in_kg
            plot_pesticidemanagement_instance.price = price
            plot_pesticidemanagement_instance.save()
            
         areadescription='Plot'
         try:
            plot_labourmanagament_instance = LabourManagament.objects.get(farm=personID,areaID=plotID,date=date,activity='Pesticide Application')
         except LabourManagament.DoesNotExist:
            if labour == 'Family':
               plot_labourmanagament_instance = LabourManagament(date=date,family_female_time=family_female_time,family_male_time=family_male_time,farm=farm,areaID=plotID,areadescription='Plot',labour=labour,family_female_number=family_female_number,family_male_number=family_male_number,activity='Pesticide Application',wage=wage,price_unit=currency,enteredpersonel=SystemUser.objects.get(user=request.user))
            elif labour == 'Hired':
               plot_labourmanagament_instance = LabourManagament(date=date,hired_female_time=hired_female_time,hired_male_time=hired_male_time,farm=farm,areaID=plotID,areadescription='Plot',labour=labour,hired_female_number=hired_female_number,hired_male_number=hired_male_number,activity='Pesticide Application',wage=wage,price_unit=currency,enteredpersonel=SystemUser.objects.get(user=request.user))
            elif labour == 'FamilyHired':
               plot_labourmanagament_instance = LabourManagament(date=date,family_female_time=family_female_time,family_male_time=family_male_time,hired_female_time=hired_female_time,hired_male_time=hired_male_time,farm=farm,areaID=plotID,areadescription='Plot',labour=labour,hired_female_number=hired_female_number,hired_male_number=hired_male_number,family_female_number=family_female_number,family_male_number=family_male_number,activity='Pesticide Application',wage=wage,price_unit=currency,enteredpersonel=SystemUser.objects.get(user=request.user))
            plot_labourmanagament_instance.save()
         else:
            activity='Pesticide Application'
            if labour == 'Family':
               labourmanagement(activity,labour,plot_labourmanagament_instance,areadescription,request.user,date,wage,family_female_number=family_female_number,family_female_time=family_female_time,family_male_number=family_male_number,family_male_time=family_male_time)
            elif labour == 'Hired':
               labourmanagement(activity,labour,plot_labourmanagament_instance,areadescription,request.user,date,wage,hired_female_number=hired_female_number,hired_female_time=hired_female_time,hired_male_number=hired_male_number,hired_male_time=hired_male_time)
            elif labour == 'FamilyHired':
               labourmanagement(activity,labour,plot_labourmanagament_instance,areadescription,request.user,date,wage,hired_female_number=hired_female_number,hired_female_time=hired_female_time,hired_male_number=hired_male_number,hired_male_time=hired_male_time,family_female_number=family_female_number,family_female_time=family_female_time,family_male_number=family_male_number,family_male_time=family_male_time)

         message='saved'
         return render(request,'iwmiproject/saved.html',locals())
      else:
         return render(request,'iwmiproject/iwmiproject_edit/edit_plot_pesticidemanagement_specific_detail.html',locals())
   else:
      pesticidemanagement_instance = PesticideManagement.objects.get(farm=personID,plotID=Plot.objects.get(plotID=plotID,farm=personID),date=date,name=pesticide)
      plot_labourmanagament_instance = LabourManagament.objects.get(farm=personID,areaID=plotID,date=date,activity = 'Pesticide Application')

      pesticidemanagement_form = PesticideManagement_Form(instance = pesticidemanagement_instance)
      labourmanagement_form = LabourManagement_Form(instance = plot_labourmanagament_instance)

      return render(request,'iwmiproject/iwmiproject_edit/edit_plot_pesticidemanagement_specific_detail.html',locals())


def edit_plot_weeding(request,plotID,personID):
   if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('signup:login'))

   user_instance = SystemUser.objects.get(user=request.user)
   if user_instance.role == 'RA' or user_instance.role == 'ST':user_village = user_instance.village
   elif user_instance.role == 'ALL':user_country = user_instance.country
   elif user_instance.role == 'RS':researcher = user_instance.country
   currency = pick_currency(user_instance)

   weeding_instance = Weed.objects.filter(farm=personID,plotID=Plot.objects.get(plotID=plotID,farm=personID))

   if not weeding_instance:
         return render(request,'iwmiproject/iwmiproject_display/none.html',locals())

   elif len(weeding_instance) == 1:

      if request.method == 'POST':
         weeding_form = Weeding_Form(request.POST)
         labourmanagement_form = LabourManagement_Form(request.POST)

         if weeding_form.is_valid() and labourmanagement_form.is_valid():
            date = weeding_form.cleaned_data['date']
            farm = weeding_form.cleaned_data['farm']
            plotID = weeding_form.cleaned_data['plotID']
            weed_activities = weeding_form.cleaned_data['weed_activities']

            labour = labourmanagement_form.cleaned_data['labour']
            hired_female_number = labourmanagement_form.cleaned_data['hired_female_number']
            hired_female_time = labourmanagement_form.cleaned_data['hired_female_time']
            hired_male_number = labourmanagement_form.cleaned_data['hired_male_number']
            hired_male_time = labourmanagement_form.cleaned_data['hired_male_time']
            family_female_number = labourmanagement_form.cleaned_data['family_female_number']
            family_female_time = labourmanagement_form.cleaned_data['family_female_time']
            family_male_number = labourmanagement_form.cleaned_data['family_male_number']
            family_male_time = labourmanagement_form.cleaned_data['family_male_time']
            wage = labourmanagement_form.cleaned_data['wage']
            price_unit = labourmanagement_form.cleaned_data['price_unit']

            plot_weed_instance = Weed.objects.get(farm=personID,plotID=Plot.objects.get(plotID=plotID,farm=personID))
            plot_labourmanagament_instance = LabourManagament.objects.get(farm=personID,areaID=plotID,date=plot_weed_instance.date,activity='Weeding')

            plot_weed_instance.date = date
            plot_weed_instance.weed_activities = weed_activities
            
            activity='Weeding'
            areadescription='Plot'
            if labour == 'Family':
               labourmanagement(activity,labour,plot_labourmanagament_instance,areadescription,request.user,date,wage,family_female_number=family_female_number,family_female_time=family_female_time,family_male_number=family_male_number,family_male_time=family_male_time)
            elif labour == 'Hired':
               labourmanagement(activity,labour,plot_labourmanagament_instance,areadescription,request.user,date,wage,hired_female_number=hired_female_number,hired_female_time=hired_female_time,hired_male_number=hired_male_number,hired_male_time=hired_male_time)
            elif labour == 'FamilyHired':
               labourmanagement(activity,labour,plot_labourmanagament_instance,areadescription,request.user,date,wage,hired_female_number=hired_female_number,hired_female_time=hired_female_time,hired_male_number=hired_male_number,hired_male_time=hired_male_time,family_female_number=family_female_number,family_female_time=family_female_time,family_male_number=family_male_number,family_male_time=family_male_time)

            plot_weed_instance.save()

            message='saved'
            return render(request,'iwmiproject/saved.html',locals())
         else:
            return render(request,'iwmiproject/iwmiproject_edit/edit_plot_weeding_specific_detail.html',locals())
      else:
         weeding_instance = Weed.objects.get(farm=personID,plotID=Plot.objects.get(plotID=plotID,farm=personID))
         plot_labourmanagament_instance = LabourManagament.objects.get(farm=personID,areaID=plotID,date=weeding_instance.date,activity='Weeding')

         weeding_form = Weeding_Form(instance = weeding_instance)
         labourmanagement_form = LabourManagement_Form(instance = plot_labourmanagament_instance)
         return render(request,'iwmiproject/iwmiproject_edit/edit_plot_weeding_specific_detail.html',locals())
   else:
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
      return render(request,'iwmiproject/iwmiproject_display/plot_weeding_detail_display.html',context)


def edit_plot_weeding_specific_detail(request,plotID,personID,date):
   if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('signup:login'))

   user_instance = SystemUser.objects.get(user=request.user)
   if user_instance.role == 'RA' or user_instance.role == 'ST':user_village = user_instance.village
   elif user_instance.role == 'ALL':user_country = user_instance.country
   elif user_instance.role == 'RS':researcher = user_instance.country
   currency = pick_currency(user_instance)

   weeding_instance = Weed.objects.filter(farm=personID,plotID=Plot.objects.get(plotID=plotID,farm=personID))

   if request.method == 'POST':

      weeding_form = Weeding_Form(request.POST)
      labourmanagement_form = LabourManagement_Form(request.POST)

      if weeding_form.is_valid() and labourmanagement_form.is_valid():
         date = weeding_form.cleaned_data['date']
         farm = weeding_form.cleaned_data['farm']
         plotID = weeding_form.cleaned_data['plotID']
         weed_activities = weeding_form.cleaned_data['weed_activities']

         labour = labourmanagement_form.cleaned_data['labour']
         hired_female_number = labourmanagement_form.cleaned_data['hired_female_number']
         hired_female_time = labourmanagement_form.cleaned_data['hired_female_time']
         hired_male_number = labourmanagement_form.cleaned_data['hired_male_number']
         hired_male_time = labourmanagement_form.cleaned_data['hired_male_time']
         family_female_number = labourmanagement_form.cleaned_data['family_female_number']
         family_female_time = labourmanagement_form.cleaned_data['family_female_time']
         family_male_number = labourmanagement_form.cleaned_data['family_male_number']
         family_male_time = labourmanagement_form.cleaned_data['family_male_time']
         wage = labourmanagement_form.cleaned_data['wage']
         price_unit = labourmanagement_form.cleaned_data['price_unit']
         
         try:
            plot_weeding_instance = Weed.objects.get(date=date,farm=personID,plotID=Plot.objects.get(plotID=plotID,farm=personID))
         except Weed.DoesNotExist:
            plot_weeding_instance = Weed(farm=farm,date=date,plotID=Plot.objects.get(plotID=plotID),weed_activities=weed_activities,enteredpersonel= SystemUser.objects.get(user=request.user))
            plot_weeding_instance.save()
         else:
            plot_weeding_instance.date = date
            plot_weeding_instance.weed_activities = weed_activities
            plot_weeding_instance.save()
         
         areadescription='Plot'
         try:
            plot_labourmanagament_instance = LabourManagament.objects.get(farm=personID,areaID=plotID,date=date,activity='Weeding')
         except LabourManagament.DoesNotExist:
            if labour == 'Family':
               plot_labourmanagament_instance = LabourManagament(date=date,family_female_time=family_female_time,family_male_time=family_male_time,farm=farm,areaID=plotID,areadescription='Plot',labour=labour,family_female_number=family_female_number,family_male_number=family_male_number,activity='land preparation',wage=wage,price_unit=currency,enteredpersonel=SystemUser.objects.get(user=request.user))
            elif labour == 'Hired':
               plot_labourmanagament_instance = LabourManagament(date=date,hired_female_time=hired_female_time,hired_male_time=hired_male_time,farm=farm,areaID=plotID,areadescription='Plot',labour=labour,hired_female_number=hired_female_number,hired_male_number=hired_male_number,activity='land preparation',wage=wage,price_unit=currency,enteredpersonel=SystemUser.objects.get(user=request.user))
            elif labour == 'FamilyHired':
               plot_labourmanagament_instance = LabourManagament(date=date,family_female_time=family_female_time,family_male_time=family_male_time,hired_female_time=hired_female_time,hired_male_time=hired_male_time,farm=farm,areaID=plotID,areadescription='Plot',labour=labour,hired_female_number=hired_female_number,hired_male_number=hired_male_number,family_female_number=family_female_number,family_male_number=family_male_number,activity='land preparation',wage=wage,price_unit=currency,enteredpersonel=SystemUser.objects.get(user=request.user))
            plot_labourmanagament_instance.save()
         else:
            activity='Weeding'
            if labour == 'Family':
               labourmanagement(activity,labour,plot_labourmanagament_instance,areadescription,request.user,date,wage,family_female_number=family_female_number,family_female_time=family_female_time,family_male_number=family_male_number,family_male_time=family_male_time)
            elif labour == 'Hired':
               labourmanagement(activity,labour,plot_labourmanagament_instance,areadescription,request.user,date,wage,hired_female_number=hired_female_number,hired_female_time=hired_female_time,hired_male_number=hired_male_number,hired_male_time=hired_male_time)
            elif labour == 'FamilyHired':
               labourmanagement(activity,labour,plot_labourmanagament_instance,areadescription,request.user,date,wage,hired_female_number=hired_female_number,hired_female_time=hired_female_time,hired_male_number=hired_male_number,hired_male_time=hired_male_time,family_female_number=family_female_number,family_female_time=family_female_time,family_male_number=family_male_number,family_male_time=family_male_time)

         message='saved'
         return render(request,'iwmiproject/saved.html',locals())
      else:
         return render(request,'iwmiproject/iwmiproject_edit/edit_plot_weeding_specific_detail.html',locals())
   else:
      weeding_instance = Weed.objects.get(farm=personID,plotID=Plot.objects.get(plotID=plotID,farm=personID),date=date)
      plot_labourmanagament_instance = LabourManagament.objects.get(farm=personID,areaID=plotID,date=weeding_instance.date,activity='Weeding')

      weeding_form = Weeding_Form(instance = weeding_instance)
      labourmanagement_form = LabourManagement_Form(instance = plot_labourmanagament_instance)
      return render(request,'iwmiproject/iwmiproject_edit/edit_plot_weeding_specific_detail.html',locals())
            

def edit_yieldfarmlevel_specific_detail(request,plotID,personID,date):
   if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('signup:login'))

   user_instance = SystemUser.objects.get(user=request.user)
   if user_instance.role == 'RA' or user_instance.role == 'ST':user_village = user_instance.village
   elif user_instance.role == 'ALL':user_country = user_instance.country
   elif user_instance.role == 'RS':researcher = user_instance.country
   currency = pick_currency(user_instance)
   
   if request.method == 'POST':
      yieldfarmlevel_form = YieldFarmLevel_Form(request.POST)
      labourmanagement_form = LabourManagement_Form(request.POST)

      if yieldfarmlevel_form.is_valid() and labourmanagement_form.is_valid():
         date = yieldfarmlevel_form.cleaned_data['date']
         farm = yieldfarmlevel_form.cleaned_data['farm']
         plotID = yieldfarmlevel_form.cleaned_data['plotID']
         Crop = yieldfarmlevel_form.cleaned_data['Crop']
         fresh_dry = yieldfarmlevel_form.cleaned_data['fresh_dry']
         quantity_harvested = yieldfarmlevel_form.cleaned_data['quantity_harvested']
         marketable_yield = yieldfarmlevel_form.cleaned_data['marketable_yield']
         unmarketable_yield = yieldfarmlevel_form.cleaned_data['unmarketable_yield']
         biomas = yieldfarmlevel_form.cleaned_data['biomas']

         labour = labourmanagement_form.cleaned_data['labour']
         hired_female_number = labourmanagement_form.cleaned_data['hired_female_number']
         hired_female_time = labourmanagement_form.cleaned_data['hired_female_time']
         hired_male_number = labourmanagement_form.cleaned_data['hired_male_number']
         hired_male_time = labourmanagement_form.cleaned_data['hired_male_time']
         family_female_number = labourmanagement_form.cleaned_data['family_female_number']
         family_female_time = labourmanagement_form.cleaned_data['family_female_time']
         family_male_number = labourmanagement_form.cleaned_data['family_male_number']
         family_male_time = labourmanagement_form.cleaned_data['family_male_time']
         wage = labourmanagement_form.cleaned_data['wage']
         price_unit = labourmanagement_form.cleaned_data['price_unit']
         
         print('33')
         try:
            plot_yieldfarmlevel_instance = YieldFarmLevel.objects.get(date=date,farm=farm,plotID=Plot.objects.get(plotID=plotID,farm=farm),Crop=Crop)
         except YieldFarmLevel.DoesNotExist:
            plot_yieldfarmlevel_instance = YieldFarmLevel(quantity_harvested=quantity_harvested,date=date,Crop=Crop,farm=farm,plotID=Plot.objects.get(plotID=plotID,farm=farm),fresh_dry=fresh_dry,marketable_yield=marketable_yield,unmarketable_yield=unmarketable_yield,biomas=biomas,enteredpersonel=SystemUser.objects.get(user=request.user))
            plot_yieldfarmlevel_instance.save()
         else:

            plot_yieldfarmlevel_instance.date = date
            plot_yieldfarmlevel_instance.Crop = Crop 
            plot_yieldfarmlevel_instance.fresh_dry = fresh_dry
            plot_yieldfarmlevel_instance.quantity_harvested = quantity_harvested
            plot_yieldfarmlevel_instance.marketable_yield = marketable_yield
            plot_yieldfarmlevel_instance.unmarketable_yield = unmarketable_yield
            plot_yieldfarmlevel_instance.biomas = biomas
            plot_yieldfarmlevel_instance.save()
            
         areadescription='Plot'
         try:
            plot_labourmanagament_instance = LabourManagament.objects.get(farm=personID,areaID=plotID,date=date,activity='Field harvesting')
         except LabourManagament.DoesNotExist:
            print('eee')
            if labour == 'Family':
               plot_labourmanagament_instance = LabourManagament(date=date,family_female_time=family_female_time,family_male_time=family_male_time,farm=farm,areaID=plotID,areadescription='Plot',labour=labour,family_female_number=family_female_number,family_male_number=family_male_number,activity='Field harvesting',wage=wage,price_unit=currency,enteredpersonel=SystemUser.objects.get(user=request.user))
            elif labour == 'Hired':
               plot_labourmanagament_instance = LabourManagament(date=date,hired_female_time=hired_female_time,hired_male_time=hired_male_time,farm=farm,areaID=plotID,areadescription='Plot',labour=labour,hired_female_number=hired_female_number,hired_male_number=hired_male_number,activity='Field harvesting',wage=wage,price_unit=currency,enteredpersonel=SystemUser.objects.get(user=request.user))
            elif labour == 'FamilyHired':
               plot_labourmanagament_instance = LabourManagament(date=date,family_female_time=family_female_time,family_male_time=family_male_time,hired_female_time=hired_female_time,hired_male_time=hired_male_time,farm=farm,areaID=plotID,areadescription='Plot',labour=labour,hired_female_number=hired_female_number,hired_male_number=hired_male_number,family_female_number=family_female_number,family_male_number=family_male_number,activity='Field harvesting',wage=wage,price_unit=currency,enteredpersonel=SystemUser.objects.get(user=request.user))
            plot_labourmanagament_instance.save()
         else:
            print('rr')
            activity='Field harvesting'
            if labour == 'Family':
               labourmanagement(activity,labour,plot_labourmanagament_instance,areadescription,request.user,date,wage,family_female_number=family_female_number,family_female_time=family_female_time,family_male_number=family_male_number,family_male_time=family_male_time)
            elif labour == 'Hired':
               labourmanagement(activity,labour,plot_labourmanagament_instance,areadescription,request.user,date,wage,hired_female_number=hired_female_number,hired_female_time=hired_female_time,hired_male_number=hired_male_number,hired_male_time=hired_male_time)
            elif labour == 'FamilyHired':
               labourmanagement(activity,labour,plot_labourmanagament_instance,areadescription,request.user,date,wage,hired_female_number=hired_female_number,hired_female_time=hired_female_time,hired_male_number=hired_male_number,hired_male_time=hired_male_time,family_female_number=family_female_number,family_female_time=family_female_time,family_male_number=family_male_number,family_male_time=family_male_time)
                  
         message='saved'
         return render(request,'iwmiproject/saved.html',locals())
      else:
         return render(request,'iwmiproject/iwmiproject_edit/edit_plot_yieldfarmlevel_specific_detail.html',locals())
   else:
         yieldfarmlevel_instance = YieldFarmLevel.objects.get(farm=personID,plotID=Plot.objects.get(plotID=plotID,farm=personID),date=date)
         plot_labourmanagament_instance = LabourManagament.objects.get(farm=personID,areaID=plotID,date=yieldfarmlevel_instance.date,activity='Field harvesting')

         yieldfarmlevel_form = YieldFarmLevel_Form(instance = yieldfarmlevel_instance)
         labourmanagement_form = LabourManagement_Form(instance = plot_labourmanagament_instance)
         return render(request,'iwmiproject/iwmiproject_edit/edit_plot_yieldfarmlevel_specific_detail.html',locals())

def edit_yieldfarmlevel(request,plotID,personID):
   if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('signup:login'))

   user_instance = SystemUser.objects.get(user=request.user)
   if user_instance.role == 'RA' or user_instance.role == 'ST':user_village = user_instance.village
   elif user_instance.role == 'ALL':user_country = user_instance.country
   elif user_instance.role == 'RS':researcher = user_instance.country
   currency = pick_currency(user_instance)

   yieldfarmlevel_instance = YieldFarmLevel.objects.filter(farm=personID,plotID=Plot.objects.get(plotID=plotID,farm=personID))

   if not yieldfarmlevel_instance:
         return render(request,'iwmiproject/iwmiproject_display/none.html',locals())

   elif len(yieldfarmlevel_instance) == 1:
      if request.method == 'POST':
         yieldfarmlevel_form = YieldFarmLevel_Form(request.POST)
         labourmanagement_form = LabourManagement_Form(request.POST)

         if yieldfarmlevel_form.is_valid() and labourmanagement_form.is_valid():
            date = yieldfarmlevel_form.cleaned_data['date']
            farm = yieldfarmlevel_form.cleaned_data['farm']
            plotID = yieldfarmlevel_form.cleaned_data['plotID']
            Crop = yieldfarmlevel_form.cleaned_data['Crop']
            fresh_dry = yieldfarmlevel_form.cleaned_data['fresh_dry']
            quantity_harvested = yieldfarmlevel_form.cleaned_data['quantity_harvested']
            marketable_yield = yieldfarmlevel_form.cleaned_data['marketable_yield']
            unmarketable_yield = yieldfarmlevel_form.cleaned_data['unmarketable_yield']
            biomas = yieldfarmlevel_form.cleaned_data['biomas']

            labour = labourmanagement_form.cleaned_data['labour']
            hired_female_number = labourmanagement_form.cleaned_data['hired_female_number']
            hired_female_time = labourmanagement_form.cleaned_data['hired_female_time']
            hired_male_number = labourmanagement_form.cleaned_data['hired_male_number']
            hired_male_time = labourmanagement_form.cleaned_data['hired_male_time']
            family_female_number = labourmanagement_form.cleaned_data['family_female_number']
            family_female_time = labourmanagement_form.cleaned_data['family_female_time']
            family_male_number = labourmanagement_form.cleaned_data['family_male_number']
            family_male_time = labourmanagement_form.cleaned_data['family_male_time']
            wage = labourmanagement_form.cleaned_data['wage']
            price_unit = labourmanagement_form.cleaned_data['price_unit']
            

            plot_yieldfarmlevel_instance = YieldFarmLevel.objects.get(farm=personID,plotID=Plot.objects.get(plotID=plotID,farm=personID))
            plot_labourmanagament_instance = LabourManagament.objects.get(farm=personID,areaID=plotID,date=plot_yieldfarmlevel_instance.date,activity='Field harvesting')

            plot_yieldfarmlevel_instance.date = date
            plot_yieldfarmlevel_instance.Crop = Crop 
            plot_yieldfarmlevel_instance.fresh_dry = fresh_dry
            plot_yieldfarmlevel_instance.quantity_harvested = quantity_harvested
            plot_yieldfarmlevel_instance.marketable_yield = marketable_yield
            plot_yieldfarmlevel_instance.unmarketable_yield = unmarketable_yield
            plot_yieldfarmlevel_instance.biomas = biomas
            
            activity='Field harvesting'
            areadescription='Plot'
            if labour == 'Family':
               labourmanagement(activity,labour,plot_labourmanagament_instance,areadescription,request.user,date,wage,family_female_number=family_female_number,family_female_time=family_female_time,family_male_number=family_male_number,family_male_time=family_male_time)
            elif labour == 'Hired':
               labourmanagement(activity,labour,plot_labourmanagament_instance,areadescription,request.user,date,wage,hired_female_number=hired_female_number,hired_female_time=hired_female_time,hired_male_number=hired_male_number,hired_male_time=hired_male_time)
            elif labour == 'FamilyHired':
               labourmanagement(activity,labour,plot_labourmanagament_instance,areadescription,request.user,date,wage,hired_female_number=hired_female_number,hired_female_time=hired_female_time,hired_male_number=hired_male_number,hired_male_time=hired_male_time,family_female_number=family_female_number,family_female_time=family_female_time,family_male_number=family_male_number,family_male_time=family_male_time)

            plot_yieldfarmlevel_instance.save()

            message='saved'
            return render(request,'iwmiproject/saved.html',locals())
         else:
            return render(request,'iwmiproject/iwmiproject_edit/edit_plot_yieldfarmlevel_specific_detail.html',locals())
      else:
         yieldfarmlevel_instance = YieldFarmLevel.objects.get(farm=personID,plotID=Plot.objects.get(plotID=plotID,farm=personID))
         plot_labourmanagament_instance = LabourManagament.objects.get(farm=personID,areaID=plotID,date=yieldfarmlevel_instance.date,activity='Field harvesting')

         yieldfarmlevel_form = YieldFarmLevel_Form(instance = yieldfarmlevel_instance)
         labourmanagement_form = LabourManagement_Form(instance = plot_labourmanagament_instance)
         return render(request,'iwmiproject/iwmiproject_edit/edit_plot_yieldfarmlevel_specific_detail.html',locals())
   else:
      if user_instance.role == 'RA' or user_instance.role == 'ST':
         user_village = user_instance.village
         plot_yieldfarmlevel_queryset_list = YieldFarmLevel.objects.filter(enteredpersonel=user_instance,farm=personID,plotID=Plot.objects.get(plotID=plotID,farm=personID)).select_related()
      elif user_instance.role == 'ALL':
         user_country = user_instance.country
         plot_yieldfarmlevel_queryset_list = YieldFarmLevel.objects.filter(farm=personID,plotID=Plot.objects.get(plotID=plotID,farm=personID)).select_related()
      elif user_instance.role == 'RS':
         researcher_country = user_instance.country
         plot_yieldfarmlevel_queryset_list = YieldFarmLevel.objects.filter(farm__farmID__village__district__region__country=researcher_country).select_related()
      paginator = Paginator(plot_yieldfarmlevel_queryset_list, 20)

      page = request.GET.get('page')
      try:
         plot_yieldfarmlevel_queryset = paginator.page(page)
      except PageNotAnInteger:
         plot_yieldfarmlevel_queryset = paginator.page(1)
      except EmptyPage:
         plot_yieldfarmlevel_queryset = paginator.page(paginator.num_pages)

      context ={
            'object_list':plot_yieldfarmlevel_queryset,
            'title':"List",
            'user_instance':user_instance
      }
      return render(request,'iwmiproject/iwmiproject_display/plot_yieldfarmlevel_detail_display.html',context)

#ResidualHandling_Form
def edit_plot_residualhandling(request,plotID,personID):
   if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('signup:login'))

   user_instance = SystemUser.objects.get(user=request.user)
   if user_instance.role == 'RA' or user_instance.role == 'ST':user_village = user_instance.village
   elif user_instance.role == 'ALL':user_country = user_instance.country
   elif user_instance.role == 'RS':researcher = user_instance.country
   currency = pick_currency(user_instance)

   residualhandling_instance = ResidualHandling.objects.filter(farm=personID,plotID=Plot.objects.get(plotID=plotID,farm=personID))

   if not residualhandling_instance:
         return render(request,'iwmiproject/iwmiproject_display/none.html',locals())

   elif len(residualhandling_instance) == 1:

      if request.method == 'POST':
         residuehandlingform = ResidualHandling_Form(request.POST)
         labourmanagement_form = LabourManagement_Form(request.POST)

         if residuehandlingform.is_valid() and labourmanagement_form.is_valid():
            date = residuehandlingform.cleaned_data['date']
            farm = residuehandlingform.cleaned_data['farm']
            plotID = residuehandlingform.cleaned_data['plotID']
            residual_activities = residuehandlingform.cleaned_data['residual_activities']
            time = residuehandlingform.cleaned_data['time']
            other = residuehandlingform.cleaned_data['other']
            
            labour = labourmanagement_form.cleaned_data['labour']
            hired_female_number = labourmanagement_form.cleaned_data['hired_female_number']
            hired_female_time = labourmanagement_form.cleaned_data['hired_female_time']
            hired_male_number = labourmanagement_form.cleaned_data['hired_male_number']
            hired_male_time = labourmanagement_form.cleaned_data['hired_male_time']
            family_female_number = labourmanagement_form.cleaned_data['family_female_number']
            family_female_time = labourmanagement_form.cleaned_data['family_female_time']
            family_male_number = labourmanagement_form.cleaned_data['family_male_number']
            family_male_time = labourmanagement_form.cleaned_data['family_male_time']
            wage = labourmanagement_form.cleaned_data['wage']
            price_unit = labourmanagement_form.cleaned_data['price_unit']

            plot_residualhandling_instance = ResidualHandling.objects.get(farm=personID,plotID=Plot.objects.get(plotID=plotID,farm=personID))
            plot_labourmanagament_instance = LabourManagament.objects.get(farm=personID,areaID=plotID,date=plot_residualhandling_instance.date,activity='Residue handling')

            if other == 'N///A':
               plot_residualhandling_instance.residual_activities = residual_activities
            else:
               plot_residualhandling_instance.residual_activities = other
            plot_residualhandling_instance.date = date
            plot_residualhandling_instance.time = time
            plot_residualhandling_instance.save()
            activity='Residue handling'
            areadescription='Plot'
            if labour == 'Family':
               labourmanagement(activity,labour,plot_labourmanagament_instance,areadescription,request.user,date,wage,family_female_number=family_female_number,family_female_time=family_female_time,family_male_number=family_male_number,family_male_time=family_male_time)
            elif labour == 'Hired':
               labourmanagement(activity,labour,plot_labourmanagament_instance,areadescription,request.user,date,wage,hired_female_number=hired_female_number,hired_female_time=hired_female_time,hired_male_number=hired_male_number,hired_male_time=hired_male_time)
            elif labour == 'FamilyHired':
               labourmanagement(activity,labour,plot_labourmanagament_instance,areadescription,request.user,date,wage,hired_female_number=hired_female_number,hired_female_time=hired_female_time,hired_male_number=hired_male_number,hired_male_time=hired_male_time,family_female_number=family_female_number,family_female_time=family_female_time,family_male_number=family_male_number,family_male_time=family_male_time)

            message='saved'
            return render(request,'iwmiproject/saved.html',locals())
         else:
            return render(request,'iwmiproject/iwmiproject_edit/edit_plot_residualhandling_specific_detail.html',locals())
      else:
         residualhandling_instance = ResidualHandling.objects.get(farm=personID,plotID=Plot.objects.get(plotID=plotID,farm=personID))
         plot_labourmanagament_instance = LabourManagament.objects.get(farm=personID,areaID=plotID,date=residualhandling_instance.date,activity='Residue handling')

         residuehandlingform = ResidualHandling_Form(instance = residualhandling_instance)
         labourmanagement_form = LabourManagement_Form(instance = plot_labourmanagament_instance)
         return render(request,'iwmiproject/iwmiproject_edit/edit_plot_residualhandling_specific_detail.html',locals())
   else:
      if user_instance.role == 'RA' or user_instance.role == 'ST':
         user_village = user_instance.village
         plot_residualhandling_queryset_list = ResidualHandling.objects.filter(enteredpersonel=user_instance,farm=personID,plotID=Plot.objects.get(plotID=plotID,farm=personID)).select_related()
      elif user_instance.role == 'ALL':
         user_country = user_instance.country
         plot_residualhandling_queryset_list = ResidualHandling.objects.filter(farm=personID,plotID=Plot.objects.get(plotID=plotID,farm=personID)).select_related()
      elif user_instance.role == 'RS':
         researcher_country = user_instance.country
         plot_residualhandling_queryset_list = ResidualHandling.objects.filter(farm__farmID__village__district__region__country=researcher_country).select_related()
      paginator = Paginator(plot_residualhandling_queryset_list, 20)

      page = request.GET.get('page')
      try:
         plot_residualhandling_queryset = paginator.page(page)
      except PageNotAnInteger:
         plot_residualhandling_queryset = paginator.page(1)
      except EmptyPage:
         plot_residualhandling_queryset = paginator.page(paginator.num_pages)

      context ={
            'object_list':plot_residualhandling_queryset,
            'title':"List",
            'user_instance':user_instance
      }
      return render(request,'iwmiproject/iwmiproject_display/plot_residualhandling_detail_display.html',context)



def edit_plot_residualhandling_specific_detail(request,plotID,personID,date):
   if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('signup:login'))

   user_instance = SystemUser.objects.get(user=request.user)
   if user_instance.role == 'RA' or user_instance.role == 'ST':user_village = user_instance.village
   elif user_instance.role == 'ALL':user_country = user_instance.country
   elif user_instance.role == 'RS':researcher = user_instance.country
   currency = pick_currency(user_instance)

   residualhandling_instance = ResidualHandling.objects.filter(farm=personID,plotID=Plot.objects.get(plotID=plotID,farm=personID))

   if request.method == 'POST':

      residualhandling_form = ResidualHandling_Form(request.POST)
      labourmanagement_form = LabourManagement_Form(request.POST)

      if residualhandling_form.is_valid() and labourmanagement_form.is_valid():
         date = residualhandling_form.cleaned_data['date']
         farm = residualhandling_form.cleaned_data['farm']
         plotID = residualhandling_form.cleaned_data['plotID']
         residual_activities = residualhandling_form.cleaned_data['residual_activities']
         time = residualhandling_form.cleaned_data['time']
         other = residualhandling_form.cleaned_data['other']
         
         labour = labourmanagement_form.cleaned_data['labour']
         hired_female_number = labourmanagement_form.cleaned_data['hired_female_number']
         hired_female_time = labourmanagement_form.cleaned_data['hired_female_time']
         hired_male_number = labourmanagement_form.cleaned_data['hired_male_number']
         hired_male_time = labourmanagement_form.cleaned_data['hired_male_time']
         family_female_number = labourmanagement_form.cleaned_data['family_female_number']
         family_female_time = labourmanagement_form.cleaned_data['family_female_time']
         family_male_number = labourmanagement_form.cleaned_data['family_male_number']
         family_male_time = labourmanagement_form.cleaned_data['family_male_time']
         wage = labourmanagement_form.cleaned_data['wage']
         price_unit = labourmanagement_form.cleaned_data['price_unit']

         try:
            plot_residualhandling_instance = ResidualHandling.objects.get(date=date,farm=personID,plotID=Plot.objects.get(plotID=plotID,farm=personID))
         except ResidualHandling.DoesNotExist:
            if other == 'N///A':
               plot_residualhandling_instance = ResidualHandling(farm=farm,date=date,plotID=Plot.objects.get(plotID=plotID,farm=farm),residual_activities=residual_activities,time=time,enteredpersonel= SystemUser.objects.get(user=request.user))
            else:
               plot_residualhandling_instance = ResidualHandling(farm=farm,date=date,plotID=Plot.objects.get(plotID=plotID,farm=farm),residual_activities=other,time=time,enteredpersonel= SystemUser.objects.get(user=request.user))
            plot_residualhandling_instance.save()
         else:
            if other == 'N///A':
               plot_residualhandling_instance.residual_activities = residual_activities
            else:
               plot_residualhandling_instance.residual_activities = other
            plot_residualhandling_instance.date = date
            plot_residualhandling_instance.time = time
            plot_residualhandling_instance.save()
            
         areadescription='Plot'
         try:
            plot_labourmanagament_instance = LabourManagament.objects.get(farm=personID,areaID=plotID,date=date,activity='Residue handling')
         except LabourManagament.DoesNotExist:
            if labour == 'Family':
               plot_labourmanagament_instance = LabourManagament(date=date,family_female_time=family_female_time,family_male_time=family_male_time,farm=farm,areaID=plotID,areadescription='Plot',labour=labour,family_female_number=family_female_number,family_male_number=family_male_number,activity='Residue handling',wage=wage,price_unit=currency,enteredpersonel=SystemUser.objects.get(user=request.user))
            elif labour == 'Hired':
               plot_labourmanagament_instance = LabourManagament(date=date,hired_female_time=hired_female_time,hired_male_time=hired_male_time,farm=farm,areaID=plotID,areadescription='Plot',labour=labour,hired_female_number=hired_female_number,hired_male_number=hired_male_number,activity='Residue handling',wage=wage,price_unit=currency,enteredpersonel=SystemUser.objects.get(user=request.user))
            elif labour == 'FamilyHired':
               plot_labourmanagament_instance = LabourManagament(date=date,family_female_time=family_female_time,family_male_time=family_male_time,hired_female_time=hired_female_time,hired_male_time=hired_male_time,farm=farm,areaID=plotID,areadescription='Plot',labour=labour,hired_female_number=hired_female_number,hired_male_number=hired_male_number,family_female_number=family_female_number,family_male_number=family_male_number,activity='Residue handling',wage=wage,price_unit=currency,enteredpersonel=SystemUser.objects.get(user=request.user))
            plot_labourmanagament_instance.save()
         else:
            activity='Residue handling'
            if labour == 'Family':
               labourmanagement(activity,labour,plot_labourmanagament_instance,areadescription,request.user,date,wage,family_female_number=family_female_number,family_female_time=family_female_time,family_male_number=family_male_number,family_male_time=family_male_time)
            elif labour == 'Hired':
               labourmanagement(activity,labour,plot_labourmanagament_instance,areadescription,request.user,date,wage,hired_female_number=hired_female_number,hired_female_time=hired_female_time,hired_male_number=hired_male_number,hired_male_time=hired_male_time)
            elif labour == 'FamilyHired':
               labourmanagement(activity,labour,plot_labourmanagament_instance,areadescription,request.user,date,wage,hired_female_number=hired_female_number,hired_female_time=hired_female_time,hired_male_number=hired_male_number,hired_male_time=hired_male_time,family_female_number=family_female_number,family_female_time=family_female_time,family_male_number=family_male_number,family_male_time=family_male_time)

         message='saved'
         return render(request,'iwmiproject/saved.html',locals())
      else:
         return render(request,'iwmiproject/iwmiproject_edit/edit_plot_residualhandling_specific_detail.html',locals())
   else:
      residualhandling_instance = ResidualHandling.objects.get(farm=personID,plotID=Plot.objects.get(plotID=plotID,farm=personID),date=date)
      plot_labourmanagament_instance = LabourManagament.objects.get(farm=personID,areaID=plotID,date=residualhandling_instance.date,activity='Residue handling')

      residuehandlingform = ResidualHandling_Form(instance = residualhandling_instance)
      labourmanagement_form = LabourManagement_Form(instance = plot_labourmanagament_instance)
      return render(request,'iwmiproject/iwmiproject_edit/edit_plot_residualhandling_specific_detail.html',locals())
   

#YieldRowBedLevel_Form
def edit_plot_yieldrowbedlevel(request,plotID,personID):
   if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('signup:login'))

   user_instance = SystemUser.objects.get(user=request.user)
   if user_instance.role == 'RA' or user_instance.role == 'ST':user_village = user_instance.village
   elif user_instance.role == 'ALL':user_country = user_instance.country
   elif user_instance.role == 'RS':researcher = user_instance.country
   currency = pick_currency(user_instance)

   yieldrowbedlevel_instance = YieldRowBedLevel.objects.filter(farm=personID,plotID=Plot.objects.get(plotID=plotID,farm=personID))

   if not yieldrowbedlevel_instance:
         return render(request,'iwmiproject/iwmiproject_display/none.html',locals())

   elif len(yieldrowbedlevel_instance) == 1:

      if request.method == 'POST':
         yieldrowbedlevel_form = YieldRowBedLevel_Form(request.POST)

         if yieldrowbedlevel_form.is_valid():
            date = yieldrowbedlevel_form.cleaned_data['date']
            farm = yieldrowbedlevel_form.cleaned_data['farm']
            plotID = yieldrowbedlevel_form.cleaned_data['plotID']
            Crop = yieldrowbedlevel_form.cleaned_data['Crop']
            harvesting_method = yieldrowbedlevel_form.cleaned_data['harvesting_method']
            fresh_dry = yieldrowbedlevel_form.cleaned_data['fresh_dry']
            row_number = yieldrowbedlevel_form.cleaned_data['row_number']
            marketable_produced = yieldrowbedlevel_form.cleaned_data['marketable_produced']
            ummarketable_produced = yieldrowbedlevel_form.cleaned_data['ummarketable_produced']
            marketable_produced_weight = yieldrowbedlevel_form.cleaned_data['marketable_produced_weight']
            unmarketable_produced_weight = yieldrowbedlevel_form.cleaned_data['unmarketable_produced_weight']

            plot_yieldrowbedlevel_instance = YieldRowBedLevel.objects.get(farm=personID,plotID=Plot.objects.get(plotID=plotID,farm=personID))

            plot_yieldrowbedlevel_instance.date = date
            plot_yieldrowbedlevel_instance.Crop = Crop
            plot_yieldrowbedlevel_instance.harvesting_method = harvesting_method
            plot_yieldrowbedlevel_instance.fresh_dry = fresh_dry
            plot_yieldrowbedlevel_instance.row_number = row_number
            plot_yieldrowbedlevel_instance.marketable_produced = marketable_produced
            plot_yieldrowbedlevel_instance.ummarketable_produced = ummarketable_produced
            plot_yieldrowbedlevel_instance.marketable_produced_weight = marketable_produced_weight
            plot_yieldrowbedlevel_instance.unmarketable_produced_weight = unmarketable_produced_weight
            
            plot_yieldrowbedlevel_instance.save()

            message='saved'
            return render(request,'iwmiproject/saved.html',locals())
         else:
            return render(request,'iwmiproject/iwmiproject_edit/edit_plot_yieldrowbedlevel_specific_detail.html',locals())
      else:
         yieldrowbedlevel_instance = YieldRowBedLevel.objects.get(farm=personID,plotID=Plot.objects.get(plotID=plotID,farm=personID))
         yieldrowbedlevel_form = YieldRowBedLevel_Form(instance = yieldrowbedlevel_instance)

         return render(request,'iwmiproject/iwmiproject_edit/edit_plot_yieldrowbedlevel_specific_detail.html',locals())
   else:
      if user_instance.role == 'RA' or user_instance.role == 'ST':
         user_village = user_instance.village
         plot_yieldrowbedlevel_queryset_list = YieldRowBedLevel.objects.filter(enteredpersonel=user_instance,farm=personID,plotID=Plot.objects.get(plotID=plotID,farm=personID)).select_related()
      elif user_instance.role == 'ALL':
         user_country = user_instance.country
         plot_yieldrowbedlevel_queryset_list = YieldRowBedLevel.objects.filter(farm=personID,plotID=Plot.objects.get(plotID=plotID,farm=personID)).select_related()
      elif user_instance.role == 'RS':
         researcher_country = user_instance.country
         plot_yieldrowbedlevel_queryset_list = YieldRowBedLevel.objects.filter(farm__farmID__village__district__region__country=researcher_country).select_related()
      paginator = Paginator(plot_yieldrowbedlevel_queryset_list, 20)

      page = request.GET.get('page')
      try:
         plot_yieldrowbedlevel_queryset = paginator.page(page)
      except PageNotAnInteger:
         plot_yieldrowbedlevel_queryset = paginator.page(1)
      except EmptyPage:
         plot_yieldrowbedlevel_queryset = paginator.page(paginator.num_pages)

      context ={
            'object_list':plot_yieldrowbedlevel_queryset,
            'title':"List",
            'user_instance':user_instance
      }
      return render(request,'iwmiproject/iwmiproject_display/plot_yieldrowbedlevel_detail_display.html',context)
   

def edit_yieldrowbedlevel_specific_detail(request,plotID,personID,date,Crop):
   if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('signup:login'))

   user_instance = SystemUser.objects.get(user=request.user)
   if user_instance.role == 'RA' or user_instance.role == 'ST':user_village = user_instance.village
   elif user_instance.role == 'ALL':user_country = user_instance.country
   elif user_instance.role == 'RS':researcher = user_instance.country
   currency = pick_currency(user_instance)

   yieldrowbedlevel_instance = YieldRowBedLevel.objects.filter(farm=personID,plotID=Plot.objects.get(plotID=plotID,farm=personID))

   if request.method == 'POST':
      yieldrowbedlevel_form = YieldRowBedLevel_Form(request.POST)

      if yieldrowbedlevel_form.is_valid():
         date = yieldrowbedlevel_form.cleaned_data['date']
         farm = yieldrowbedlevel_form.cleaned_data['farm']
         plotID = yieldrowbedlevel_form.cleaned_data['plotID']
         Crop = yieldrowbedlevel_form.cleaned_data['Crop']
         harvesting_method = yieldrowbedlevel_form.cleaned_data['harvesting_method']
         fresh_dry = yieldrowbedlevel_form.cleaned_data['fresh_dry']
         row_number = yieldrowbedlevel_form.cleaned_data['row_number']
         marketable_produced = yieldrowbedlevel_form.cleaned_data['marketable_produced']
         ummarketable_produced = yieldrowbedlevel_form.cleaned_data['ummarketable_produced']
         marketable_produced_weight = yieldrowbedlevel_form.cleaned_data['marketable_produced_weight']
         unmarketable_produced_weight = yieldrowbedlevel_form.cleaned_data['unmarketable_produced_weight']

         '''
         try:Crop=Crop.objects.get(name=Crop)
         except Crop.DoesNotExist:
            crop_instance = Crop(name=Crop)
            crop_instance.save()
         finally:Crop=Crop.objects.get(name=Crop)
         '''
         try:
            plot_yieldrowbedlevel_instance = YieldRowBedLevel.objects.get(date=date,farm=farm,plotID=Plot.objects.get(plotID=plotID,farm=farm),Crop=Crop)
         except YieldRowBedLevel.DoesNotExist:
            plot_yieldrowbedlevel_instance = YieldRowBedLevel(date=date,Crop=Crop,farm=farm,plotID=Plot.objects.get(plotID=plotID,farm=farm),harvesting_method=harvesting_method,fresh_dry=fresh_dry,marketable_produced=marketable_produced,ummarketable_produced=ummarketable_produced,row_number=row_number,marketable_produced_weight=marketable_produced_weight,unmarketable_produced_weight=unmarketable_produced_weight,enteredpersonel=SystemUser.objects.get(user=request.user))
            plot_yieldrowbedlevel_instance.save()
         else:
            plot_yieldrowbedlevel_instance.date = date
            plot_yieldrowbedlevel_instance.Crop = Crop
            plot_yieldrowbedlevel_instance.harvesting_method = harvesting_method
            plot_yieldrowbedlevel_instance.fresh_dry = fresh_dry
            plot_yieldrowbedlevel_instance.row_number = row_number
            plot_yieldrowbedlevel_instance.marketable_produced = marketable_produced
            plot_yieldrowbedlevel_instance.ummarketable_produced = ummarketable_produced
            plot_yieldrowbedlevel_instance.marketable_produced_weight = marketable_produced_weight
            plot_yieldrowbedlevel_instance.unmarketable_produced_weight = unmarketable_produced_weight
            plot_yieldrowbedlevel_instance.save()
            
         message='saved'
         return render(request,'iwmiproject/saved.html',locals())
      else:
         return render(request,'iwmiproject/iwmiproject_edit/edit_plot_yieldrowbedlevel_specific_detail.html',locals())
   else:
      yieldrowbedlevel_instance = YieldRowBedLevel.objects.get(farm=personID,plotID=Plot.objects.get(plotID=plotID,farm=personID),date=date,Crop=Crop)
      yieldrowbedlevel_form = YieldRowBedLevel_Form(instance = yieldrowbedlevel_instance)

      return render(request,'iwmiproject/iwmiproject_edit/edit_plot_yieldrowbedlevel_specific_detail.html',locals())
   

#YieldPlantLevel_Form
def edit_plot_yieldplantlevel(request,plotID,personID):
   if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('signup:login'))

   user_instance = SystemUser.objects.get(user=request.user)
   if user_instance.role == 'RA' or user_instance.role == 'ST':user_village = user_instance.village
   elif user_instance.role == 'ALL':user_country = user_instance.country
   elif user_instance.role == 'RS':researcher = user_instance.country
   currency = pick_currency(user_instance)

   yieldplantlevel_instance = YieldPlantLevel.objects.filter(farm=personID,plotID=Plot.objects.get(plotID=plotID,farm=personID))

   if not yieldplantlevel_instance:
         return render(request,'iwmiproject/iwmiproject_display/none.html',locals())

   elif len(yieldplantlevel_instance) == 1:

      if request.method == 'POST':
         yieldplantlevel_form = YieldPlantLevel_Form(request.POST)

         if yieldplantlevel_form.is_valid():
            date = yieldplantlevel_form.cleaned_data['date']
            farm = yieldplantlevel_form.cleaned_data['farm']
            plotID = yieldplantlevel_form.cleaned_data['plotID']
            Crop = yieldplantlevel_form.cleaned_data['Crop']
            harvest_method = yieldplantlevel_form.cleaned_data['harvest_method']
            fresh_dry = yieldplantlevel_form.cleaned_data['fresh_dry']
            row_number = yieldplantlevel_form.cleaned_data['row_number']
            marketable_produced = yieldplantlevel_form.cleaned_data['marketable_produced']
            unmarketable_produced = yieldplantlevel_form.cleaned_data['unmarketable_produced']
            marketable_produced_weight = yieldplantlevel_form.cleaned_data['marketable_produced_weight']
            unmarketable_produced_weight = yieldplantlevel_form.cleaned_data['unmarketable_produced_weight']
            diameter_width_produced = yieldplantlevel_form.cleaned_data['diameter_width_produced']
            length = yieldplantlevel_form.cleaned_data['length']
            residual_biomass = yieldplantlevel_form.cleaned_data['residual_biomass']

            plot_yieldplantlevel_instance = YieldPlantLevel.objects.get(farm=personID,plotID=Plot.objects.get(plotID=plotID,farm=personID))

            plot_yieldplantlevel_instance.date = date
            plot_yieldplantlevel_instance.Crop = Crop
            plot_yieldplantlevel_instance.harvest_method = harvest_method
            plot_yieldplantlevel_instance.fresh_dry = fresh_dry
            plot_yieldplantlevel_instance.row_number = row_number
            plot_yieldplantlevel_instance.marketable_produced = marketable_produced
            plot_yieldplantlevel_instance.unmarketable_produced = unmarketable_produced
            plot_yieldplantlevel_instance.marketable_produced_weight = marketable_produced_weight
            plot_yieldplantlevel_instance.unmarketable_produced_weight = unmarketable_produced_weight
            plot_yieldplantlevel_instance.diameter_width_produced = diameter_width_produced
            plot_yieldplantlevel_instance.length = length
            plot_yieldplantlevel_instance.residual_biomass = residual_biomass
            
            plot_yieldplantlevel_instance.save()

            message='saved'
            return render(request,'iwmiproject/saved.html',locals())
         else:
            return render(request,'iwmiproject/iwmiproject_edit/edit_plot_yieldplantlevel_specific_detail.html',locals())
      else:
         yieldplantlevel_instance = YieldPlantLevel.objects.get(farm=personID,plotID=Plot.objects.get(plotID=plotID,farm=personID))
         yieldplantlevel_form = YieldPlantLevel_Form(instance = yieldplantlevel_instance)

         return render(request,'iwmiproject/iwmiproject_edit/edit_plot_yieldplantlevel_specific_detail.html',locals())
   else:
      if user_instance.role == 'RA' or user_instance.role == 'ST':
         user_village = user_instance.village
         plot_yieldplantlevel_queryset_list = YieldPlantLevel.objects.filter(enteredpersonel=user_instance,farm=personID,plotID=Plot.objects.get(plotID=plotID,farm=personID)).select_related()
      elif user_instance.role == 'ALL':
         user_country = user_instance.country
         plot_yieldplantlevel_queryset_list = YieldPlantLevel.objects.filter(farm=personID,plotID=Plot.objects.get(plotID=plotID,farm=personID)).select_related()
      elif user_instance.role == 'RS':
         researcher_country = user_instance.country
         plot_yieldplantlevel_queryset_list = YieldPlantLevel.objects.filter(farm__farmID__village__district__region__country=researcher_country).select_related()
      paginator = Paginator(plot_yieldplantlevel_queryset_list, 20)

      page = request.GET.get('page')
      try:
         plot_yieldplantlevel_queryset = paginator.page(page)
      except PageNotAnInteger:
         plot_yieldplantlevel_queryset = paginator.page(1)
      except EmptyPage:
         plot_yieldplantlevel_queryset = paginator.page(paginator.num_pages)

      context ={
            'object_list':plot_yieldplantlevel_queryset,
            'title':"List",
            'user_instance':user_instance
      }
      return render(request,'iwmiproject/iwmiproject_display/plot_yieldplantlevel_detail_display.html',context)
   
   
def edit_plot_yieldplantlevel_specific_detail(request,plotID,personID,date,Crop):
   if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('signup:login'))

   user_instance = SystemUser.objects.get(user=request.user)
   if user_instance.role == 'RA' or user_instance.role == 'ST':user_village = user_instance.village
   elif user_instance.role == 'ALL':user_country = user_instance.country
   elif user_instance.role == 'RS':researcher = user_instance.country
   currency = pick_currency(user_instance)

   yieldplantlevel_instance = YieldPlantLevel.objects.filter(farm=personID,plotID=Plot.objects.get(plotID=plotID,farm=personID))

   if request.method == 'POST':
      yieldplantlevel_form = YieldPlantLevel_Form(request.POST)

      if yieldplantlevel_form.is_valid():
         date = yieldplantlevel_form.cleaned_data['date']
         farm = yieldplantlevel_form.cleaned_data['farm']
         plotID = yieldplantlevel_form.cleaned_data['plotID']
         Crop = yieldplantlevel_form.cleaned_data['Crop']
         harvest_method = yieldplantlevel_form.cleaned_data['harvest_method']
         fresh_dry = yieldplantlevel_form.cleaned_data['fresh_dry']
         plant_number = yieldplantlevel_form.cleaned_data['plant_number']
         row_number = yieldplantlevel_form.cleaned_data['row_number']
         marketable_produced = yieldplantlevel_form.cleaned_data['marketable_produced']
         unmarketable_produced = yieldplantlevel_form.cleaned_data['unmarketable_produced']
         marketable_produced_weight = yieldplantlevel_form.cleaned_data['marketable_produced_weight']
         unmarketable_produced_weight = yieldplantlevel_form.cleaned_data['unmarketable_produced_weight']
         diameter_width_produced = yieldplantlevel_form.cleaned_data['diameter_width_produced']
         length = yieldplantlevel_form.cleaned_data['length']
         residual_biomass = yieldplantlevel_form.cleaned_data['residual_biomass']
         
         try:
            plot_yieldplantlevel_instance = YieldPlantLevel.objects.get(date=date,farm=farm,plotID=Plot.objects.get(plotID=plotID,farm=farm),Crop=Crop,row_number=row_number,plant_number=plant_number)
         except YieldPlantLevel.DoesNotExist:
            plot_yieldplantlevel_instance = YieldPlantLevel(date=date,Crop=Crop,farm=farm,plotID=Plot.objects.get(plotID=plotID,farm=farm),row_number=row_number,harvest_method=harvest_method,fresh_dry=fresh_dry,plant_number=plant_number,marketable_produced=marketable_produced,unmarketable_produced=unmarketable_produced,marketable_produced_weight=marketable_produced_weight,unmarketable_produced_weight=unmarketable_produced_weight,diameter_width_produced=diameter_width_produced,length=length,residual_biomass=residual_biomass,enteredpersonel=SystemUser.objects.get(user=request.user))
            plot_yieldplantlevel_instance.save()
         else:
            plot_yieldplantlevel_instance.date = date
            plot_yieldplantlevel_instance.Crop = Crop
            plot_yieldplantlevel_instance.harvest_method = harvest_method
            plot_yieldplantlevel_instance.fresh_dry = fresh_dry
            plot_yieldplantlevel_instance.row_number = row_number
            plot_yieldplantlevel_instance.marketable_produced = marketable_produced
            plot_yieldplantlevel_instance.unmarketable_produced = unmarketable_produced
            plot_yieldplantlevel_instance.marketable_produced_weight = marketable_produced_weight
            plot_yieldplantlevel_instance.unmarketable_produced_weight = unmarketable_produced_weight
            plot_yieldplantlevel_instance.diameter_width_produced = diameter_width_produced
            plot_yieldplantlevel_instance.length = length
            plot_yieldplantlevel_instance.residual_biomass = residual_biomass
            plot_yieldplantlevel_instance.save()
            
         message='saved'
         return render(request,'iwmiproject/saved.html',locals())
      else:
         return render(request,'iwmiproject/iwmiproject_edit/edit_plot_yieldplantlevel_specific_detail.html',locals())
   else:
      yieldplantlevel_instance = YieldPlantLevel.objects.get(farm=personID,plotID=Plot.objects.get(plotID=plotID,farm=personID),date=date,Crop=Crop)
      yieldplantlevel_form = YieldPlantLevel_Form(instance = yieldplantlevel_instance)

      return render(request,'iwmiproject/iwmiproject_edit/edit_plot_yieldplantlevel_specific_detail.html',locals())
   
#SoilProperty_Form
def edit_plot_soilproperty(request,plotID,personID):
   if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('signup:login'))

   user_instance = SystemUser.objects.get(user=request.user)
   if user_instance.role == 'RA' or user_instance.role == 'ST':user_village = user_instance.village
   elif user_instance.role == 'ALL':user_country = user_instance.country
   elif user_instance.role == 'RS':researcher = user_instance.country
   currency = pick_currency(user_instance)

   soilproperty_instance = SoilProperty.objects.filter(farm=personID,plotID=Plot.objects.get(plotID=plotID,farm=personID))

   if not soilproperty_instance:
         return render(request,'iwmiproject/iwmiproject_display/none.html',locals())

   elif len(soilproperty_instance) == 1:

      if request.method == 'POST':
         soilproperty_form = SoilProperty_Form(request.POST)

         if soilproperty_form.is_valid():
            date = soilproperty_form.cleaned_data['date']
            farm = soilproperty_form.cleaned_data['farm']
            plotID = soilproperty_form.cleaned_data['plotID']
            soilclass = soilproperty_form.cleaned_data['soilclass']
            soil_depth = soilproperty_form.cleaned_data['soil_depth']
            pH = soilproperty_form.cleaned_data['pH']
            ec = soilproperty_form.cleaned_data['ec']
            sand = soilproperty_form.cleaned_data['sand']
            clay = soilproperty_form.cleaned_data['clay']
            silt = soilproperty_form.cleaned_data['silt']
            cec = soilproperty_form.cleaned_data['cec']
            om = soilproperty_form.cleaned_data['om']
            tn = soilproperty_form.cleaned_data['tn']
            av_p = soilproperty_form.cleaned_data['av_p']
            fe = soilproperty_form.cleaned_data['fe']
            fc = soilproperty_form.cleaned_data['fc']
            pwp = soilproperty_form.cleaned_data['pwp']
            k = soilproperty_form.cleaned_data['k']
            bulkdensity = soilproperty_form.cleaned_data['bulkdensity']
            zn = soilproperty_form.cleaned_data['zn']
            se = soilproperty_form.cleaned_data['se']
            ca = soilproperty_form.cleaned_data['ca']
            s = soilproperty_form.cleaned_data['s']
            mg = soilproperty_form.cleaned_data['mg']
            na = soilproperty_form.cleaned_data['na']

            plot_soilproperty_instance = SoilProperty.objects.get(farm=personID,plotID=Plot.objects.get(plotID=plotID,farm=personID))

            plot_soilproperty_instance.date = date
            plot_soilproperty_instance.soilclass = soilclass
            plot_soilproperty_instance.soil_depth = soil_depth
            plot_soilproperty_instance.pH = pH
            plot_soilproperty_instance.ec = ec
            plot_soilproperty_instance.sand = sand
            plot_soilproperty_instance.clay = clay
            plot_soilproperty_instance.silt = silt
            plot_soilproperty_instance.cec = cec
            plot_soilproperty_instance.om = om
            plot_soilproperty_instance.tn = tn
            plot_soilproperty_instance.av_p = av_p
            plot_soilproperty_instance.fe = fe
            plot_soilproperty_instance.fc = fc
            plot_soilproperty_instance.pwp = pwp
            plot_soilproperty_instance.k = k
            plot_soilproperty_instance.bulkdensity = bulkdensity
            plot_soilproperty_instance.zn = zn
            plot_soilproperty_instance.se = se
            plot_soilproperty_instance.ca = ca
            plot_soilproperty_instance.s = s
            plot_soilproperty_instance.mg = mg
            plot_soilproperty_instance.na = na
            
            plot_soilproperty_instance.save()

            message='saved'
            return render(request,'iwmiproject/saved.html',locals())
         else:
            return render(request,'iwmiproject/iwmiproject_edit/edit_plot_soilproperty_specific_detail.html',locals())
      else:
         soilproperty_instance = SoilProperty.objects.get(farm=personID,plotID=Plot.objects.get(plotID=plotID,farm=personID))
         soilproperty_form = SoilProperty_Form(instance = soilproperty_instance)

         return render(request,'iwmiproject/iwmiproject_edit/edit_plot_soilproperty_specific_detail.html',locals())
   else:
      if user_instance.role == 'RA' or user_instance.role == 'ST':
         user_village = user_instance.village
         plot_soilproperty_queryset_list = SoilProperty.objects.filter(enteredpersonel=user_instance,farm=personID,plotID=Plot.objects.get(plotID=plotID,farm=personID)).select_related()
      elif user_instance.role == 'ALL':
         user_country = user_instance.country
         plot_soilproperty_queryset_list = SoilProperty.objects.filter(farm=personID,plotID=Plot.objects.get(plotID=plotID,farm=personID)).select_related()
      elif user_instance.role == 'RS':
         researcher_country = user_instance.country
         plot_soilproperty_queryset_list = SoilProperty.objects.filter(farm__farmID__village__district__region__country=researcher_country).select_related()
      paginator = Paginator(plot_soilproperty_queryset_list, 20)

      page = request.GET.get('page')
      try:
         plot_soilproperty_queryset = paginator.page(page)
      except PageNotAnInteger:
         plot_soilproperty_queryset = paginator.page(1)
      except EmptyPage:
         plot_soilproperty_queryset = paginator.page(paginator.num_pages)

      context ={
            'object_list':plot_soilproperty_queryset,
            'title':"List",
            'user_instance':user_instance
      }
      return render(request,'iwmiproject/iwmiproject_display/plot_soilproperty_detail_display.html',context)
   
def edit_plot_soilproperty_specific_detail(request,plotID,personID,date):
   if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('signup:login'))

   user_instance = SystemUser.objects.get(user=request.user)
   if user_instance.role == 'RA' or user_instance.role == 'ST':user_village = user_instance.village
   elif user_instance.role == 'ALL':user_country = user_instance.country
   elif user_instance.role == 'RS':researcher = user_instance.country
   currency = pick_currency(user_instance)

   soilproperty_instance = SoilProperty.objects.filter(farm=personID,plotID=Plot.objects.get(plotID=plotID,farm=personID))

   if request.method == 'POST':
      soilproperty_form = SoilProperty_Form(request.POST)

      if soilproperty_form.is_valid():
         date = soilproperty_form.cleaned_data['date']
         farm = soilproperty_form.cleaned_data['farm']
         plotID = soilproperty_form.cleaned_data['plotID']
         soilclass = soilproperty_form.cleaned_data['soilclass']
         soil_depth = soilproperty_form.cleaned_data['soil_depth']
         pH = soilproperty_form.cleaned_data['pH']
         ec = soilproperty_form.cleaned_data['ec']
         sand = soilproperty_form.cleaned_data['sand']
         clay = soilproperty_form.cleaned_data['clay']
         silt = soilproperty_form.cleaned_data['silt']
         cec = soilproperty_form.cleaned_data['cec']
         om = soilproperty_form.cleaned_data['om']
         tn = soilproperty_form.cleaned_data['tn']
         av_p = soilproperty_form.cleaned_data['av_p']
         fe = soilproperty_form.cleaned_data['fe']
         fc = soilproperty_form.cleaned_data['fc']
         pwp = soilproperty_form.cleaned_data['pwp']
         k = soilproperty_form.cleaned_data['k']
         bulkdensity = soilproperty_form.cleaned_data['bulkdensity']
         zn = soilproperty_form.cleaned_data['zn']
         se = soilproperty_form.cleaned_data['se']
         ca = soilproperty_form.cleaned_data['ca']
         s = soilproperty_form.cleaned_data['s']
         mg = soilproperty_form.cleaned_data['mg']
         na = soilproperty_form.cleaned_data['na']

         try:
            plot_soilproperty_instance = SoilProperty.objects.get(farm=personID,plotID=Plot.objects.get(plotID=plotID,farm=personID),date=date)
         except SoilProperty.DoesNotExist:
            plot_soilproperty_instance = SoilProperty(farm=farm,date=date,plotID=Plot.objects.get(plotID=plotID,farm=farm),soil_depth=soil_depth,soilclass=Soil.objects.get(name=soilclass),pH=pH,ec=ec,sand=sand,clay=clay,silt=silt,cec=cec,om=om,tn=tn,av_p=av_p,fe=fe,fc=fc,pwp=pwp,k=k,bulkdensity=bulkdensity,zn=zn,se=se,ca=ca,s=s,mg=mg,na=na,enteredpersonel=SystemUser.objects.get(user=request.user))
            plot_soilproperty_instance.save()
         else:
            plot_soilproperty_instance.date = date
            plot_soilproperty_instance.soilclass = soilclass
            plot_soilproperty_instance.soil_depth = soil_depth
            plot_soilproperty_instance.pH = pH
            plot_soilproperty_instance.ec = ec
            plot_soilproperty_instance.sand = sand
            plot_soilproperty_instance.clay = clay
            plot_soilproperty_instance.silt = silt
            plot_soilproperty_instance.cec = cec
            plot_soilproperty_instance.om = om
            plot_soilproperty_instance.tn = tn
            plot_soilproperty_instance.av_p = av_p
            plot_soilproperty_instance.fe = fe
            plot_soilproperty_instance.fc = fc
            plot_soilproperty_instance.pwp = pwp
            plot_soilproperty_instance.k = k
            plot_soilproperty_instance.bulkdensity = bulkdensity
            plot_soilproperty_instance.zn = zn
            plot_soilproperty_instance.se = se
            plot_soilproperty_instance.ca = ca
            plot_soilproperty_instance.s = s
            plot_soilproperty_instance.mg = mg
            plot_soilproperty_instance.na = na
            plot_soilproperty_instance.save()
         
         message='saved'
         return render(request,'iwmiproject/saved.html',locals())
      else:
         return render(request,'iwmiproject/iwmiproject_edit/edit_plot_soilproperty_specific_detail.html',locals())
   else:
      soilproperty_instance = SoilProperty.objects.get(farm=personID,plotID=Plot.objects.get(plotID=plotID,farm=personID),date=date)
      soilproperty_form = SoilProperty_Form(instance = soilproperty_instance)

      return render(request,'iwmiproject/iwmiproject_edit/edit_plot_soilproperty_specific_detail.html',locals())

#OtherWaterUsage_Form
def edit_plot_otherwaterusage(request,personID):
   if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('signup:login'))

   user_instance = SystemUser.objects.get(user=request.user)
   if user_instance.role == 'RA' or user_instance.role == 'ST':user_village = user_instance.village
   elif user_instance.role == 'ALL':user_country = user_instance.country
   elif user_instance.role == 'RS':researcher = user_instance.country
   currency = pick_currency(user_instance)

   otherwaterusage_instance = OtherWaterUsage.objects.filter(farm=personID)

   if not otherwaterusage_instance:
         return render(request,'iwmiproject/iwmiproject_display/none.html',locals())

   elif len(otherwaterusage_instance) == 1:

      if request.method == 'POST':
         otherwaterusage_form = OtherWaterUsage_Form(request.POST)

         if otherwaterusage_form.is_valid():
            date = otherwaterusage_form.cleaned_data['date']
            farm = otherwaterusage_form.cleaned_data['farm']
            plotID = otherwaterusage_form.cleaned_data['plotID']
            bucketnumber = otherwaterusage_form.cleaned_data['bucketnumber']
            bucketvolume = otherwaterusage_form.cleaned_data['bucketvolume']
            technology = otherwaterusage_form.cleaned_data['technology']
            usagepurpose = otherwaterusage_form.cleaned_data['usagepurpose']
            start_time = otherwaterusage_form.cleaned_data['start_time']
            end_time = otherwaterusage_form.cleaned_data['end_time']
            total_time = otherwaterusage_form.cleaned_data['total_time']
            totalvolume = otherwaterusage_form.cleaned_data['totalvolume']
            lifting_technology_yes_no = otherwaterusage_form.cleaned_data['lifting_technology_yes_no']

            plot_otherwaterusage_instance = OtherWaterUsage.objects.get(farm=personID)

            plot_otherwaterusage_instance.date = date
            plot_otherwaterusage_instance.bucketnumber = bucketnumber
            plot_otherwaterusage_instance.bucketvolume = bucketvolume
            plot_otherwaterusage_instance.technology = technology
            plot_otherwaterusage_instance.usagepurpose = usagepurpose
            plot_otherwaterusage_instance.start_time = start_time
            plot_otherwaterusage_instance.end_time = end_time
            plot_otherwaterusage_instance.total_time = total_time
            plot_otherwaterusage_instance.totalvolume = totalvolume
            plot_otherwaterusage_instance.lifting_technology_yes_no = lifting_technology_yes_no
       
            plot_otherwaterusage_instance.save()

            message='saved'
            return render(request,'iwmiproject/saved.html',locals())
         else:
            return render(request,'iwmiproject/iwmiproject_edit/edit_plot_otherwaterusage_specific_detail.html',locals())
      else:
         otherwaterusage_instance = OtherWaterUsage.objects.get(farm=personID)
         otherwaterusage_form = OtherWaterUsage_Form(instance = otherwaterusage_instance)

         return render(request,'iwmiproject/iwmiproject_edit/edit_plot_otherwaterusage_specific_detail.html',locals())
   else:
      if user_instance.role == 'RA' or user_instance.role == 'ST':
         user_village = user_instance.village
         plot_otherwaterusage_queryset_list = OtherWaterUsage.objects.filter(enteredpersonel=user_instance,farm=personID).select_related()
      elif user_instance.role == 'ALL':
         user_country = user_instance.country
         plot_otherwaterusage_queryset_list = OtherWaterUsage.objects.filter(farm=personID).select_related()
      elif user_instance.role == 'RS':
         researcher_country = user_instance.country
         plot_otherwaterusage_queryset_list = OtherWaterUsage.objects.filter(farm__farmID__village__district__region__country=researcher_country).select_related()
      paginator = Paginator(plot_otherwaterusage_queryset_list, 20)

      page = request.GET.get('page')
      try:
         plot_otherwaterusage_queryset = paginator.page(page)
      except PageNotAnInteger:
         plot_otherwaterusage_queryset = paginator.page(1)
      except EmptyPage:
         plot_otherwaterusage_queryset = paginator.page(paginator.num_pages)

      context ={
            'object_list':plot_otherwaterusage_queryset,
            'title':"List",
            'user_instance':user_instance
      }
      return render(request,'iwmiproject/iwmiproject_display/plot_otherwaterusage_detail_display.html',context)
      
      
   
def edit_plot_otherwaterusage_specific_detail(request,personID,date,start_time):
   if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('signup:login'))

   user_instance = SystemUser.objects.get(user=request.user)
   if user_instance.role == 'RA' or user_instance.role == 'ST':user_village = user_instance.village
   elif user_instance.role == 'ALL':user_country = user_instance.country
   elif user_instance.role == 'RS':researcher = user_instance.country
   currency = pick_currency(user_instance)

   if request.method == 'POST':
      otherwaterusage_form = OtherWaterUsage_Form(request.POST)

      if otherwaterusage_form.is_valid():
         date = otherwaterusage_form.cleaned_data['date']
         farm = otherwaterusage_form.cleaned_data['farm']
         bucketnumber = otherwaterusage_form.cleaned_data['bucketnumber']
         bucketvolume = otherwaterusage_form.cleaned_data['bucketvolume']
         technology = otherwaterusage_form.cleaned_data['technology']
         usagepurpose = otherwaterusage_form.cleaned_data['usagepurpose']
         start_time = otherwaterusage_form.cleaned_data['start_time']
         end_time = otherwaterusage_form.cleaned_data['end_time']
         total_time = otherwaterusage_form.cleaned_data['total_time']
         totalvolume = otherwaterusage_form.cleaned_data['totalvolume']
         lifting_technology_yes_no = otherwaterusage_form.cleaned_data['lifting_technology_yes_no']

         try:
            otherwaterusage_instance = OtherWaterUsage.objects.get(farm=personID,date=date,start_time=start_time,end_time=end_time)
         except OtherWaterUsage.DoesNotExist:
            if lifting_technology_yes_no == 'Yes':
               otherwaterusage_instance = OtherWaterUsage(date=date,farm=farm,bucketnumber=bucketnumber,bucketvolume=bucketvolume,technology=Technology.objects.get(name=technology),usagepurpose=usagepurpose,start_time=start_time,end_time=end_time,total_time=total_time,totalvolume=totalvolume,lifting_technology_yes_no=lifting_technology_yes_no)
            elif lifting_technology_yes_no == 'No':
               otherwaterusage_instance = OtherWaterUsage(date=date,farm=farm,bucketnumber=bucketnumber,bucketvolume=bucketvolume,technology=Technology.objects.get(name=technology),usagepurpose=usagepurpose,totalvolume=totalvolume,lifting_technology_yes_no=lifting_technology_yes_no)
            otherwaterusage_instance.save()
         else:
            otherwaterusage_instance.date = date 
            otherwaterusage_instance.bucketnumber = bucketnumber 
            otherwaterusage_instance.bucketvolume = bucketvolume
            otherwaterusage_instance.technology = technology
            otherwaterusage_instance.usagepurpose = usagepurpose
            otherwaterusage_instance.totalvolume = totalvolume
            otherwaterusage_instance.lifting_technology_yes_no = lifting_technology_yes_no
            if lifting_technology_yes_no == 'Yes':
               otherwaterusage_instance.start_time = start_time
               otherwaterusage_instance.end_time = end_time
               otherwaterusage_instance.total_time = total_time
            otherwaterusage_instance.save()
         
         message='saved'
         return render(request,'iwmiproject/saved.html',locals())
      else:
         return render(request,'iwmiproject/iwmiproject_edit/edit_plot_otherwaterusage_specific_detail.html',locals())
   else:
      otherwaterusage_instance = OtherWaterUsage.objects.get(farm=personID,date=date,start_time=start_time,end_time=end_time)
      otherwaterusage_form = OtherWaterUsage_Form(instance = otherwaterusage_instance)
      return render(request,'iwmiproject/iwmiproject_edit/edit_plot_otherwaterusage_specific_detail.html',locals())

#TissueNutrientAnalysis_Form
def edit_plot_tissuenutrientanalysis(request,personID,plotID):
   if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('signup:login'))
   user_instance = SystemUser.objects.get(user=request.user)
   tissuenutrientanalysis_instance = TissueNutrientAnalysis.objects.filter(farm=personID)

   if not tissuenutrientanalysis_instance:
         return render(request,'iwmiproject/iwmiproject_display/none.html',locals())

   elif len(tissuenutrientanalysis_instance) == 1:

      if request.method == 'POST':
         tissuenutrientanalysis_form = TissueNutrientAnalysis_Form(request.POST)

         if tissuenutrientanalysis_form.is_valid():
            date = tissuenutrientanalysis_form.cleaned_data['date']
            farm = tissuenutrientanalysis_form.cleaned_data['farm']
            plotID = tissuenutrientanalysis_form.cleaned_data['plotID']
            Crop = tissuenutrientanalysis_form.cleaned_data['Crop']
            plant_tissue_part = tissuenutrientanalysis_form.cleaned_data['plant_tissue_part']
            plantnumber = tissuenutrientanalysis_form.cleaned_data['plantnumber']
            bed_number = tissuenutrientanalysis_form.cleaned_data['bed_number']
            freshweight = tissuenutrientanalysis_form.cleaned_data['freshweight']
            dryweight = tissuenutrientanalysis_form.cleaned_data['dryweight']
            n = tissuenutrientanalysis_form.cleaned_data['n']
            p = tissuenutrientanalysis_form.cleaned_data['p']
            k = tissuenutrientanalysis_form.cleaned_data['k']
            s = tissuenutrientanalysis_form.cleaned_data['s']
            mg = tissuenutrientanalysis_form.cleaned_data['mg']
            ca = tissuenutrientanalysis_form.cleaned_data['ca']
            fe = tissuenutrientanalysis_form.cleaned_data['fe']
            zn = tissuenutrientanalysis_form.cleaned_data['zn']

            tissuenutrientanalysis_instance = TissueNutrientAnalysis.objects.get(farm=personID,plotID=Plot.objects.get(plotID=plotID,farm=personID))

            tissuenutrientanalysis_instance.date = date
            tissuenutrientanalysis_instance.Crop = Crop
            tissuenutrientanalysis_instance.plant_tissue_part = plant_tissue_part
            tissuenutrientanalysis_instance.plantnumber = plantnumber
            tissuenutrientanalysis_instance.freshweight = freshweight
            tissuenutrientanalysis_instance.dryweight = dryweight
            tissuenutrientanalysis_instance.n = n
            tissuenutrientanalysis_instance.p = p
            tissuenutrientanalysis_instance.k = k
            tissuenutrientanalysis_instance.s = s
            tissuenutrientanalysis_instance.mg = mg
            tissuenutrientanalysis_instance.ca = ca
            tissuenutrientanalysis_instance.fe = fe
            tissuenutrientanalysis_instance.zn = zn
            tissuenutrientanalysis_instance.save()

            message='saved'
            return render(request,'iwmiproject/saved.html',locals())
         else:
            return render(request,'iwmiproject/iwmiproject_edit/edit_plot_tissuenutrientanalysis_specific_detail.html',locals())
      else:
         tissuenutrientanalysis_instance = TissueNutrientAnalysis.objects.get(farm=personID,plotID=Plot.objects.get(plotID=plotID,farm=personID))
         tissuenutrientanalysis_form = TissueNutrientAnalysis_Form(instance = tissuenutrientanalysis_instance)

         return render(request,'iwmiproject/iwmiproject_edit/edit_plot_tissuenutrientanalysis_specific_detail.html',locals())
   else:
      if user_instance.role == 'RA' or user_instance.role == 'ST':
         user_village = user_instance.village
         plot_tissuenutrientanalysis_queryset_list = TissueNutrientAnalysis.objects.filter(enteredpersonel=user_instance,farm=personID).select_related()
      elif user_instance.role == 'ALL':
         user_country = user_instance.country
         plot_tissuenutrientanalysis_queryset_list = TissueNutrientAnalysis.objects.filter(farm=personID).select_related()
      elif user_instance.role == 'RS':
         researcher_country = user_instance.country
         plot_tissuenutrientanalysis_queryset_list = TissueNutrientAnalysis.objects.filter(farm__farmID__village__district__region__country=researcher_country).select_related()
      paginator = Paginator(plot_tissuenutrientanalysis_queryset_list, 20)

      page = request.GET.get('page')
      try:
         plot_tissuenutrientanalysis_queryset = paginator.page(page)
      except PageNotAnInteger:
         plot_tissuenutrientanalysis_queryset = paginator.page(1)
      except EmptyPage:
         plot_tissuenutrientanalysis_queryset = paginator.page(paginator.num_pages)

      context ={
            'object_list':plot_tissuenutrientanalysis_queryset,
            'title':"List",
            'user_instance':user_instance
      }
      return render(request,'iwmiproject/iwmiproject_display/plot_tissuenutrientanalysis_detail_display.html',context)
   
def edit_plot_tissuenutrientanalysis_specific_detail(request,personID,plotID,date,plantnumber,Crop,bed_number):
   if not request.user.is_authenticated():
      return HttpResponseRedirect(reverse('signup:login'))
   
   user_instance = SystemUser.objects.get(user=request.user)
   
   if request.method == 'POST':
      tissuenutrientanalysis_form = TissueNutrientAnalysis_Form(request.POST)

      if tissuenutrientanalysis_form.is_valid():
         date = tissuenutrientanalysis_form.cleaned_data['date']
         farm = tissuenutrientanalysis_form.cleaned_data['farm']
         plotID = tissuenutrientanalysis_form.cleaned_data['plotID']
         Crop = tissuenutrientanalysis_form.cleaned_data['Crop']
         plant_tissue_part = tissuenutrientanalysis_form.cleaned_data['plant_tissue_part']
         plantnumber = tissuenutrientanalysis_form.cleaned_data['plantnumber']
         bed_number = tissuenutrientanalysis_form.cleaned_data['bed_number']
         freshweight = tissuenutrientanalysis_form.cleaned_data['freshweight']
         dryweight = tissuenutrientanalysis_form.cleaned_data['dryweight']
         n = tissuenutrientanalysis_form.cleaned_data['n']
         p = tissuenutrientanalysis_form.cleaned_data['p']
         k = tissuenutrientanalysis_form.cleaned_data['k']
         s = tissuenutrientanalysis_form.cleaned_data['s']
         mg = tissuenutrientanalysis_form.cleaned_data['mg']
         ca = tissuenutrientanalysis_form.cleaned_data['ca']
         fe = tissuenutrientanalysis_form.cleaned_data['fe']
         zn = tissuenutrientanalysis_form.cleaned_data['zn']
         
         try:
            tissuenutrientanalysis_instance = TissueNutrientAnalysis.objects.get(farm=farm,date=date,plotID=Plot.objects.get(plotID=plotID,farm=farm),plantnumber=plantnumber,Crop=Crop,bed_number=bed_number)
         except TissueNutrientAnalysis.DoesNotExist:
            tissuenutrientanalysis_instance = TissueNutrientAnalysis(Crop=Crop,farm=farm,date=date,plotID=Plot.objects.get(plotID=plotID,farm=farm),plant_tissue_part=plant_tissue_part,plantnumber=plantnumber,bed_number=bed_number,freshweight=freshweight,dryweight=dryweight,n=n,p=p,k=k,s=s,mg=mg,ca=ca,fe=fe,zn=zn,enteredpersonel=SystemUser.objects.get(user=request.user))
            tissuenutrientanalysis_instance.save()
         else:
            tissuenutrientanalysis_instance.date = date
            tissuenutrientanalysis_instance.Crop = Crop
            tissuenutrientanalysis_instance.plant_tissue_part = plant_tissue_part
            tissuenutrientanalysis_instance.plantnumber = plantnumber
            tissuenutrientanalysis_instance.freshweight = freshweight
            tissuenutrientanalysis_instance.dryweight = dryweight
            tissuenutrientanalysis_instance.n = n
            tissuenutrientanalysis_instance.p = p
            tissuenutrientanalysis_instance.k = k
            tissuenutrientanalysis_instance.s = s
            tissuenutrientanalysis_instance.mg = mg
            tissuenutrientanalysis_instance.ca = ca
            tissuenutrientanalysis_instance.fe = fe
            tissuenutrientanalysis_instance.zn = zn
            tissuenutrientanalysis_instance.save()
            
         message='saved'
         return render(request,'iwmiproject/saved.html',locals())
      else:
            return render(request,'iwmiproject/iwmiproject_edit/edit_plot_tissuenutrientanalysis_specific_detail.html',locals())
   else:
         tissuenutrientanalysis_instance = TissueNutrientAnalysis.objects.get(farm=personID,plotID=Plot.objects.get(plotID=plotID,farm=personID),date=date,plantnumber=plantnumber,Crop=Crop,bed_number=bed_number)
         tissuenutrientanalysis_form = TissueNutrientAnalysis_Form(instance = tissuenutrientanalysis_instance)
         
         return render(request,'iwmiproject/iwmiproject_edit/edit_plot_tissuenutrientanalysis_specific_detail.html',locals())


#SaleHarvestedCrop_Form
def edit_plot_saleharvestedcrop(request,personID,plotID):
   if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('signup:login'))
   user_instance = SystemUser.objects.get(user=request.user)
   
   saleharvestedcrop_instance = SaleHarvestedCrop.objects.filter(farm=personID,plotID=Plot.objects.get(plotID=plotID,farm=personID))

   if not saleharvestedcrop_instance:
         return render(request,'iwmiproject/iwmiproject_display/none.html',locals())

   elif len(saleharvestedcrop_instance) == 1:

      if request.method == 'POST':
         harvestedcropsaleform = SaleHarvestedCrop_Form(request.POST)
         labourmanagement_form = LabourManagement_Form(request.POST)
         
         if harvestedcropsaleform.is_valid() and labourmanagement_form.is_valid():
            date = harvestedcropsaleform.cleaned_data['date']
            farm = harvestedcropsaleform.cleaned_data['farm']
            plotID = harvestedcropsaleform.cleaned_data['plotID']
            amount = harvestedcropsaleform.cleaned_data['amount']
            marketprice = harvestedcropsaleform.cleaned_data['marketprice']
            income = harvestedcropsaleform.cleaned_data['income']
            mode_of_transport = harvestedcropsaleform.cleaned_data['mode_of_transport']
            fare = harvestedcropsaleform.cleaned_data['fare']
            fuel_type = harvestedcropsaleform.cleaned_data['fuel_type']
            fuel_cost = harvestedcropsaleform.cleaned_data['fuel_cost']
            distance_to_the_market = harvestedcropsaleform.cleaned_data['distance_to_the_market']
            
            labour = labourmanagement_form.cleaned_data['labour']
            hired_female_number = labourmanagement_form.cleaned_data['hired_female_number']
            hired_female_time = labourmanagement_form.cleaned_data['hired_female_time']
            hired_male_number = labourmanagement_form.cleaned_data['hired_male_number']
            hired_male_time = labourmanagement_form.cleaned_data['hired_male_time']
            family_female_number = labourmanagement_form.cleaned_data['family_female_number']
            family_female_time = labourmanagement_form.cleaned_data['family_female_time']
            family_male_number = labourmanagement_form.cleaned_data['family_male_number']
            family_male_time = labourmanagement_form.cleaned_data['family_male_time']
            wage = labourmanagement_form.cleaned_data['wage']
            price_unit = labourmanagement_form.cleaned_data['price_unit']

            saleharvestedcrop_instance = SaleHarvestedCrop.objects.get(farm=personID,plotID=Plot.objects.get(plotID=plotID,farm=personID))
            
            print('date:{}'.format(saleharvestedcrop_instance.date))
            plot_labourmanagament_instance = LabourManagament.objects.get(farm=personID,areaID=plotID,date=saleharvestedcrop_instance.date,activity='Plot harvest sale')
            
            
            saleharvestedcrop_instance.date = date
            saleharvestedcrop_instance.amount = amount
            saleharvestedcrop_instance.income = income
            saleharvestedcrop_instance.marketprice = marketprice
            saleharvestedcrop_instance.mode_of_transport = mode_of_transport
            saleharvestedcrop_instance.distance_to_the_market = distance_to_the_market
            
            if mode_of_transport == 'Public transport':
               saleharvestedcrop_instance.fare = fare
            elif mode_of_transport == 'Own transportation':
               saleharvestedcrop_instance.fuel_type = fuel_type
               saleharvestedcrop_instance.fuel_cost = fuel_cost
            saleharvestedcrop_instance.save()
            
            areadescription='Plot'
            activity='Plot harvest sale'
            if labour == 'Family':
               labourmanagement(activity,labour,plot_labourmanagament_instance,areadescription,request.user,date,wage,family_female_number=family_female_number,family_female_time=family_female_time,family_male_number=family_male_number,family_male_time=family_male_time)
            elif labour == 'Hired':
               labourmanagement(activity,labour,plot_labourmanagament_instance,areadescription,request.user,date,wage,hired_female_number=hired_female_number,hired_female_time=hired_female_time,hired_male_number=hired_male_number,hired_male_time=hired_male_time)
            elif labour == 'FamilyHired':
               labourmanagement(activity,labour,plot_labourmanagament_instance,areadescription,request.user,date,wage,hired_female_number=hired_female_number,hired_female_time=hired_female_time,hired_male_number=hired_male_number,hired_male_time=hired_male_time,family_female_number=family_female_number,family_female_time=family_female_time,family_male_number=family_male_number,family_male_time=family_male_time)
               
            message='saved'
            return render(request,'iwmiproject/saved.html',locals())
         else:
            return render(request,'iwmiproject/iwmiproject_edit/edit_plot_saleharvestedcrop_specific_detail.html',locals())
      else:
         saleharvestedcrop_instance = SaleHarvestedCrop.objects.get(farm=personID,plotID=Plot.objects.get(plotID=plotID,farm=personID))
         harvestedcropsaleform = SaleHarvestedCrop_Form(instance = saleharvestedcrop_instance)
         
         plot_labourmanagament_instance = LabourManagament.objects.get(farm=personID,areaID=plotID,date=saleharvestedcrop_instance.date,activity='Plot harvest sale')
         labourmanagement_form = LabourManagement_Form(instance = plot_labourmanagament_instance)
         
         return render(request,'iwmiproject/iwmiproject_edit/edit_plot_saleharvestedcrop_specific_detail.html',locals())
   else:
      if user_instance.role == 'RA' or user_instance.role == 'ST':
         user_village = user_instance.village
         plot_saleharvestedcrop_queryset_list = SaleHarvestedCrop.objects.filter(enteredpersonel=user_instance,farm=personID).select_related()
      elif user_instance.role == 'ALL':
         user_country = user_instance.country
         plot_saleharvestedcrop_queryset_list = SaleHarvestedCrop.objects.filter(farm=personID).select_related()
      elif user_instance.role == 'RS':
         researcher_country = user_instance.country
         plot_saleharvestedcrop_queryset_list = SaleHarvestedCrop.objects.filter(farm__farmID__village__district__region__country=researcher_country).select_related()
      paginator = Paginator(plot_saleharvestedcrop_queryset_list, 20)

      page = request.GET.get('page')
      try:
         plot_saleharvestedcrop_queryset = paginator.page(page)
      except PageNotAnInteger:
         plot_saleharvestedcrop_queryset = paginator.page(1)
      except EmptyPage:
         plot_saleharvestedcrop_queryset = paginator.page(paginator.num_pages)

      context ={
            'object_list':plot_saleharvestedcrop_queryset,
            'title':"List",
            'user_instance':user_instance
      }
      return render(request,'iwmiproject/iwmiproject_display/plot_saleharvestedcrop_detail_display.html',context)
   
#SaleHarvestedCrop_Form
def edit_plot_saleharvestedcrop_specific_detail(request,personID,plotID,date):
   if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('signup:login'))
   user_instance = SystemUser.objects.get(user=request.user)
   currency = pick_currency(user_instance)
   
   if request.method == 'POST':
      labourmanagement_form = LabourManagement_Form(request.POST)
      harvestedcropsaleform = SaleHarvestedCrop_Form(request.POST)

      if harvestedcropsaleform.is_valid() and labourmanagement_form.is_valid():
         date = harvestedcropsaleform.cleaned_data['date']
         farm = harvestedcropsaleform.cleaned_data['farm']
         plotID = harvestedcropsaleform.cleaned_data['plotID']
         amount = harvestedcropsaleform.cleaned_data['amount']
         marketprice = harvestedcropsaleform.cleaned_data['marketprice']
         income = harvestedcropsaleform.cleaned_data['income']
         mode_of_transport = harvestedcropsaleform.cleaned_data['mode_of_transport']
         fare = harvestedcropsaleform.cleaned_data['fare']
         fuel_type = harvestedcropsaleform.cleaned_data['fuel_type']
         fuel_cost = harvestedcropsaleform.cleaned_data['fuel_cost']
         distance_to_the_market = harvestedcropsaleform.cleaned_data['distance_to_the_market']
         
         labour = labourmanagement_form.cleaned_data['labour']
         hired_female_number = labourmanagement_form.cleaned_data['hired_female_number']
         hired_female_time = labourmanagement_form.cleaned_data['hired_female_time']
         hired_male_number = labourmanagement_form.cleaned_data['hired_male_number']
         hired_male_time = labourmanagement_form.cleaned_data['hired_male_time']
         family_female_number = labourmanagement_form.cleaned_data['family_female_number']
         family_female_time = labourmanagement_form.cleaned_data['family_female_time']
         family_male_number = labourmanagement_form.cleaned_data['family_male_number']
         family_male_time = labourmanagement_form.cleaned_data['family_male_time']
         wage = labourmanagement_form.cleaned_data['wage']
         price_unit = labourmanagement_form.cleaned_data['price_unit']
         
         
         try:
            saleharvestedcrop_instance = SaleHarvestedCrop.objects.get(farm=farm,date=date,plotID=Plot.objects.get(plotID=plotID,farm=farm))
         except SaleHarvestedCrop.DoesNotExist:
            if mode_of_transport=='Public transport':
               saleharvestedcrop_instance = SaleHarvestedCrop(farm=farm,date=date,marketprice=marketprice,distance_to_the_market=distance_to_the_market,currency=currency,amount=amount,income=income,mode_of_transport=mode_of_transport,fare=fare,plotID=Plot.objects.get(plotID=plotID,farm=farm),enteredpersonel=SystemUser.objects.get(user=request.user))
            elif mode_of_transport=='Own transportation':
               saleharvestedcrop_instance = SaleHarvestedCrop(farm=farm,date=date,marketprice=marketprice,distance_to_the_market=distance_to_the_market,currency=currency,amount=amount,income=income,mode_of_transport=mode_of_transport,fuel_type=fuel_type,fuel_cost=fuel_cost,plotID=Plot.objects.get(plotID=plotID,farm=farm),enteredpersonel=SystemUser.objects.get(user=request.user))
            else:
               saleharvestedcrop_instance = SaleHarvestedCrop(farm=farm,date=date,marketprice=marketprice,distance_to_the_market=distance_to_the_market,currency=currency,amount=amount,income=income,mode_of_transport=mode_of_transport,plotID=Plot.objects.get(plotID=plotID,farm=farm),enteredpersonel=SystemUser.objects.get(user=request.user))
            saleharvestedcrop_instance.save()
         else:
            saleharvestedcrop_instance.date = date
            saleharvestedcrop_instance.amount = amount
            saleharvestedcrop_instance.income = income
            saleharvestedcrop_instance.marketprice = marketprice
            saleharvestedcrop_instance.mode_of_transport = mode_of_transport
            saleharvestedcrop_instance.distance_to_the_market = distance_to_the_market
            
            if mode_of_transport == 'Public transport':
               saleharvestedcrop_instance.fare = fare
            elif mode_of_transport == 'Own transportation':
               saleharvestedcrop_instance.fuel_type = fuel_type
               saleharvestedcrop_instance.fuel_cost = fuel_cost
            saleharvestedcrop_instance.save()

         areadescription='Plot'
         try:
            plot_labourmanagament_instance = LabourManagament.objects.get(farm=personID,areaID=plotID,date=saleharvestedcrop_instance.date,activity='Plot harvest sale')
         except LabourManagament.DoesNotExist:
            if labour == 'Family':
               plot_labourmanagament_instance = LabourManagament(date=date,family_female_time=family_female_time,family_male_time=family_male_time,farm=farm,areaID=plotID,areadescription='Plot',labour=labour,family_female_number=family_female_number,family_male_number=family_male_number,activity='Plot harvest sale',wage=wage,price_unit=currency,enteredpersonel=SystemUser.objects.get(user=request.user))
            elif labour == 'Hired':
               plot_labourmanagament_instance = LabourManagament(date=date,hired_female_time=hired_female_time,hired_male_time=hired_male_time,farm=farm,areaID=plotID,areadescription='Plot',labour=labour,hired_female_number=hired_female_number,hired_male_number=hired_male_number,activity='Plot harvest sale',wage=wage,price_unit=currency,enteredpersonel=SystemUser.objects.get(user=request.user))
            elif labour == 'FamilyHired':
               plot_labourmanagament_instance = LabourManagament(date=date,family_female_time=family_female_time,family_male_time=family_male_time,hired_female_time=hired_female_time,hired_male_time=hired_male_time,farm=farm,areaID=plotID,areadescription='Plot',labour=labour,hired_female_number=hired_female_number,hired_male_number=hired_male_number,family_female_number=family_female_number,family_male_number=family_male_number,activity='Plot harvest sale',wage=wage,price_unit=currency,enteredpersonel=SystemUser.objects.get(user=request.user))
            plot_labourmanagament_instance.save()
         else:
            activity='Plot harvest sale'
            if labour == 'Family':
               labourmanagement(activity,labour,plot_labourmanagament_instance,areadescription,request.user,date,wage,family_female_number=family_female_number,family_female_time=family_female_time,family_male_number=family_male_number,family_male_time=family_male_time)
            elif labour == 'Hired':
               labourmanagement(activity,labour,plot_labourmanagament_instance,areadescription,request.user,date,wage,hired_female_number=hired_female_number,hired_female_time=hired_female_time,hired_male_number=hired_male_number,hired_male_time=hired_male_time)
            elif labour == 'FamilyHired':
               labourmanagement(activity,labour,plot_labourmanagament_instance,areadescription,request.user,date,wage,hired_female_number=hired_female_number,hired_female_time=hired_female_time,hired_male_number=hired_male_number,hired_male_time=hired_male_time,family_female_number=family_female_number,family_female_time=family_female_time,family_male_number=family_male_number,family_male_time=family_male_time)

         message='saved'
         return render(request,'iwmiproject/saved.html',locals())
      else:
         return render(request,'iwmiproject/iwmiproject_edit/edit_plot_saleharvestedcrop_specific_detail.html',locals())
   else:
      saleharvestedcrop_instance = SaleHarvestedCrop.objects.get(farm=personID,plotID=Plot.objects.get(plotID=plotID,farm=personID),date=date)
      harvestedcropsaleform = SaleHarvestedCrop_Form(instance = saleharvestedcrop_instance)
      
      plot_labourmanagament_instance = LabourManagament.objects.get(farm=personID,areaID=plotID,date=saleharvestedcrop_instance.date,activity='Plot harvest sale')
      labourmanagement_form = LabourManagement_Form(instance = plot_labourmanagament_instance)
      return render(request,'iwmiproject/iwmiproject_edit/edit_plot_saleharvestedcrop_specific_detail.html',locals())





#CropMonitoringPlantHeight_Form
def edit_plot_cropmonitoringplantheight(request,personID,plotID):
   if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('signup:login'))
   user_instance = SystemUser.objects.get(user=request.user)
   
   cropmonitoringplantheight_instance = CropMonitoringPlantHeight.objects.filter(farm=personID,plotID=Plot.objects.get(plotID=plotID,farm=personID))

   if not cropmonitoringplantheight_instance:
         return render(request,'iwmiproject/iwmiproject_display/none.html',locals())

   elif len(cropmonitoringplantheight_instance) == 1:

      if request.method == 'POST':
         cropmonitoringplantheightform = CropMonitoringPlantHeight_Form(request.POST)

         if cropmonitoringplantheightform.is_valid():
            date = cropmonitoringplantheightform.cleaned_data['date']
            farm = cropmonitoringplantheightform.cleaned_data['farm']
            plotID = cropmonitoringplantheightform.cleaned_data['plotID']
            Crop = cropmonitoringplantheightform.cleaned_data['Crop']
            crop_stage = cropmonitoringplantheightform.cleaned_data['crop_stage']
            row_number = cropmonitoringplantheightform.cleaned_data['row_number']
            number_of_good_plants = cropmonitoringplantheightform.cleaned_data['number_of_good_plants']
            number_of_bad_plants = cropmonitoringplantheightform.cleaned_data['number_of_bad_plants']
            plant_density_per_bed = cropmonitoringplantheightform.cleaned_data['plant_density_per_bed']
            plant_density_per_sqm = cropmonitoringplantheightform.cleaned_data['plant_density_per_sqm']
            
            
            plant_number = cropmonitoringplantheightform.cleaned_data['plant_number']
            LAI = cropmonitoringplantheightform.cleaned_data['LAI']
            plant_height = cropmonitoringplantheightform.cleaned_data['plant_height']
            plant_canopy_width = cropmonitoringplantheightform.cleaned_data['plant_canopy_width']
            length_of_crop_stage = cropmonitoringplantheightform.cleaned_data['length_of_crop_stage']
            plant_leave_number = cropmonitoringplantheightform.cleaned_data['plant_leave_number']
            plant_leave_length = cropmonitoringplantheightform.cleaned_data['plant_leave_length']
            plant_leave_width = cropmonitoringplantheightform.cleaned_data['plant_leave_width']
            
            
            plant_number_two = cropmonitoringplantheightform.cleaned_data['plant_number_two']
            LAI_two = cropmonitoringplantheightform.cleaned_data['LAI_two']
            plant_height_two = cropmonitoringplantheightform.cleaned_data['plant_height_two']
            plant_canopy_width_two = cropmonitoringplantheightform.cleaned_data['plant_canopy_width_two']
            length_of_crop_stage_two = cropmonitoringplantheightform.cleaned_data['length_of_crop_stage_two']
            plant_leave_number_two = cropmonitoringplantheightform.cleaned_data['plant_leave_number_two']
            plant_leave_length_two = cropmonitoringplantheightform.cleaned_data['plant_leave_length_two']
            plant_leave_width_two = cropmonitoringplantheightform.cleaned_data['plant_leave_width_two']
         
            plant_number_three = cropmonitoringplantheightform.cleaned_data['plant_number_three']
            LAI_three = cropmonitoringplantheightform.cleaned_data['LAI_three']
            plant_height_three = cropmonitoringplantheightform.cleaned_data['plant_height_three']
            plant_canopy_width_three = cropmonitoringplantheightform.cleaned_data['plant_canopy_width_three']
            length_of_crop_stage_three = cropmonitoringplantheightform.cleaned_data['length_of_crop_stage_three']
            plant_leave_number_three = cropmonitoringplantheightform.cleaned_data['plant_leave_number_three']
            plant_leave_length_three = cropmonitoringplantheightform.cleaned_data['plant_leave_length_three']
            plant_leave_width_three = cropmonitoringplantheightform.cleaned_data['plant_leave_width_three']

            sub_plot_size = cropmonitoringplantheightform.cleaned_data['sub_plot_size']
            sub_plot_plant_number = cropmonitoringplantheightform.cleaned_data['sub_plot_plant_number']
            total_plant_number = cropmonitoringplantheightform.cleaned_data['total_plant_number']
            

            try:
               cropmonitoringplantheight_instance = CropMonitoringPlantHeight.objects.get(date=date,farm=farm,plotID=Plot.objects.get(plotID=plotID,farm=farm),crop_stage=crop_stage,row_number=row_number,Crop=Crop)
            except CropMonitoringPlantHeight.DoesNotExist:
               if total_plant_number == -999: #in case it's monocropping/intercropping and total plants obtained from planting method tab is None
                  cropmonitoringplantheight_instance=CropMonitoringPlantHeight(date=date,Crop=Crop,farm=farm,plotID=Plot.objects.get(plotID=plotID,farm=farm),crop_stage=crop_stage,row_number=row_number,number_of_good_plants=number_of_good_plants,number_of_bad_plants=number_of_bad_plants,plant_density_per_sqm=plant_density_per_sqm,plant_density_per_bed=plant_density_per_bed, \
                                                                         plant_number=1,LAI=LAI,plant_height=plant_height,plant_canopy_width=plant_canopy_width,length_of_crop_stage=length_of_crop_stage,plant_leave_number=plant_leave_number,plant_leave_length=plant_leave_length,plant_leave_width=plant_leave_width, \
                                                                         plant_number_two=2,LAI_two=LAI_two,plant_height_two=plant_height_two,plant_canopy_width_two=plant_canopy_width_two,length_of_crop_stage_two=length_of_crop_stage_two,plant_leave_number_two=plant_leave_number_two,plant_leave_length_two=plant_leave_length_two,plant_leave_width_two=plant_leave_width_two, \
                                                                         plant_number_three=3,LAI_three=LAI_three,plant_height_three=plant_height_three,plant_canopy_width_three=plant_canopy_width_three,length_of_crop_stage_three=lenght_of_crop_stage_three,plant_leave_number_three=plant_leave_number_three,plant_leave_length_three=plant_leave_length_three,plant_leave_width_three=plant_leave_width_three, \
                                                                         sub_plot_size=sub_plot_size,sub_plot_plant_number=sub_plot_plant_number,total_plant_number=total_plant_number,enteredpersonel=SystemUser.objects.get(user=request.user))
               else:
                  cropmonitoringplantheight_instance=CropMonitoringPlantHeight(date=date,Crop=Crop,farm=farm,plotID=Plot.objects.get(plotID=plotID,farm=farm),crop_stage=crop_stage,row_number=row_number,number_of_good_plants=number_of_good_plants,number_of_bad_plants=number_of_bad_plants,plant_density_per_sqm=plant_density_per_sqm,plant_density_per_bed=plant_density_per_bed, \
                                                                         plant_number=1,LAI=LAI,plant_height=plant_height,plant_canopy_width=plant_canopy_width,length_of_crop_stage=length_of_crop_stage,plant_leave_number=plant_leave_number,plant_leave_length=plant_leave_length,plant_leave_width=plant_leave_width, \
                                                                         plant_number_two=2,LAI_two=LAI_two,plant_height_two=plant_height_two,plant_canopy_width_two=plant_canopy_width_two,length_of_crop_stage_two=length_of_crop_stage_two,plant_leave_number_two=plant_leave_number_two,plant_leave_length_two=plant_leave_length_two,plant_leave_width_two=plant_leave_width_two, \
                                                                         plant_number_three=3,LAI_three=LAI_three,plant_height_three=plant_height_three,plant_canopy_width_three=plant_canopy_width_three,length_of_crop_stage_three=length_of_crop_stage_three,plant_leave_number_three=plant_leave_number_three,plant_leave_length_three=plant_leave_length_three,plant_leave_width_three=plant_leave_width_three, \
                                                                         enteredpersonel=SystemUser.objects.get(user=request.user))
                  cropmonitoringplantheight_instance.save()
            else:
               cropmonitoringplantheight_instance.date = date
               cropmonitoringplantheight_instance.Crop = Crop
               cropmonitoringplantheight_instance.crop_stage = crop_stage
               cropmonitoringplantheight_instance.row_number = row_number
               cropmonitoringplantheight_instance.number_of_good_plants = number_of_good_plants
               cropmonitoringplantheight_instance.number_of_bad_plants = number_of_bad_plants
               cropmonitoringplantheight_instance.plant_density_per_bed = plant_density_per_bed
               cropmonitoringplantheight_instance.plant_density_per_sqm = plant_density_per_sqm
               #crop one
               cropmonitoringplantheight_instance.plant_number = plant_number
               cropmonitoringplantheight_instance.LAI = LAI
               cropmonitoringplantheight_instance.plant_height = plant_height
               cropmonitoringplantheight_instance.plant_canopy_width = plant_canopy_width
               cropmonitoringplantheight_instance.length_of_crop_stage = length_of_crop_stage
               cropmonitoringplantheight_instance.plant_leave_number = plant_leave_number
               cropmonitoringplantheight_instance.plant_leave_length = plant_leave_length
               cropmonitoringplantheight_instance.plant_leave_width = plant_leave_width
               #crop two
               cropmonitoringplantheight_instance.plant_number_two = plant_number_two
               cropmonitoringplantheight_instance.LAI_two = LAI_two
               cropmonitoringplantheight_instance.plant_height_two = plant_height_two
               cropmonitoringplantheight_instance.plant_canopy_width_two = plant_canopy_width_two
               cropmonitoringplantheight_instance.length_of_crop_stage_two = length_of_crop_stage_two
               cropmonitoringplantheight_instance.plant_leave_number_two = plant_leave_number_two
               cropmonitoringplantheight_instance.plant_leave_length_two = plant_leave_length_two
               cropmonitoringplantheight_instance.plant_leave_width_two = plant_leave_width_two
               #crop three
               cropmonitoringplantheight_instance.plant_number_three = plant_number_three
               cropmonitoringplantheight_instance.LAI_three = LAI_three
               cropmonitoringplantheight_instance.plant_height_three = plant_height_three
               cropmonitoringplantheight_instance.plant_canopy_width_three = plant_canopy_width_three
               cropmonitoringplantheight_instance.length_of_crop_stage_three = length_of_crop_stage_three
               cropmonitoringplantheight_instance.plant_leave_number_three = plant_leave_number_three
               cropmonitoringplantheight_instance.plant_leave_length_three = plant_leave_length_three
               cropmonitoringplantheight_instance.plant_leave_width_three = plant_leave_width_three
               
               cropmonitoringplantheight_instance.sub_plot_size = sub_plot_size
               cropmonitoringplantheight_instance.sub_plot_plant_number = sub_plot_plant_number
               cropmonitoringplantheight_instance.total_plant_number = total_plant_number
               
               cropmonitoringplantheight_instance.save()
  
            message='saved'
            return render(request,'iwmiproject/saved.html',locals())
         else:
            return render(request,'iwmiproject/iwmiproject_edit/edit_plot_cropmonitoringplantheight_specific_detail.html',locals())
      else:
         cropmonitoringplantheight_instance = CropMonitoringPlantHeight.objects.get(farm=personID,plotID=Plot.objects.get(plotID=plotID,farm=personID))
         cropmonitoringplantheightform = CropMonitoringPlantHeight_Form(instance = cropmonitoringplantheight_instance)
         
         return render(request,'iwmiproject/iwmiproject_edit/edit_plot_cropmonitoringplantheight_specific_detail.html',locals())
   else:
      if user_instance.role == 'RA' or user_instance.role == 'ST':
         user_village = user_instance.village
         plot_cropmonitoringplantheight_queryset_list = CropMonitoringPlantHeight.objects.filter(enteredpersonel=user_instance,farm=personID).select_related()
      elif user_instance.role == 'ALL':
         user_country = user_instance.country
         plot_cropmonitoringplantheight_queryset_list = CropMonitoringPlantHeight.objects.filter(farm=personID).select_related()
      elif user_instance.role == 'RS':
         researcher_country = user_instance.country
         plot_cropmonitoringplantheight_queryset_list = CropMonitoringPlantHeight.objects.filter(farm__farmID__village__district__region__country=researcher_country).select_related()
      paginator = Paginator(plot_cropmonitoringplantheight_queryset_list, 20)

      page = request.GET.get('page')
      try:
         plot_cropmonitoringplantheight_queryset = paginator.page(page)
      except PageNotAnInteger:
         plot_cropmonitoringplantheight_queryset = paginator.page(1)
      except EmptyPage:
         plot_cropmonitoringplantheight_queryset = paginator.page(paginator.num_pages)

      context ={
            'object_list':plot_cropmonitoringplantheight_queryset,
            'title':"List",
            'user_instance':user_instance
      }
      return render(request,'iwmiproject/iwmiproject_display/plot_cropmonitoringplantheight_detail_display.html',context)
   
   
   
#CropMonitoringPlantHeight_Form
def edit_plot_cropmonitoringplantheight_specific_detail(request,personID,plotID,date,crop_stage,row_number,Crop):
   if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('signup:login'))
   user_instance = SystemUser.objects.get(user=request.user)
   
   if request.method == 'POST':
      cropmonitoringplantheightform = CropMonitoringPlantHeight_Form(request.POST)

      if cropmonitoringplantheightform.is_valid():
         date = cropmonitoringplantheightform.cleaned_data['date']
         farm = cropmonitoringplantheightform.cleaned_data['farm']
         plotID = cropmonitoringplantheightform.cleaned_data['plotID']
         Crop = cropmonitoringplantheightform.cleaned_data['Crop']
         crop_stage = cropmonitoringplantheightform.cleaned_data['crop_stage']
         row_number = cropmonitoringplantheightform.cleaned_data['row_number']
         number_of_good_plants = cropmonitoringplantheightform.cleaned_data['number_of_good_plants']
         number_of_bad_plants = cropmonitoringplantheightform.cleaned_data['number_of_bad_plants']
         plant_density_per_bed = cropmonitoringplantheightform.cleaned_data['plant_density_per_bed']
         plant_density_per_sqm = cropmonitoringplantheightform.cleaned_data['plant_density_per_sqm']
              
         plant_number = cropmonitoringplantheightform.cleaned_data['plant_number']
         LAI = cropmonitoringplantheightform.cleaned_data['LAI']
         plant_height = cropmonitoringplantheightform.cleaned_data['plant_height']
         plant_canopy_width = cropmonitoringplantheightform.cleaned_data['plant_canopy_width']
         length_of_crop_stage = cropmonitoringplantheightform.cleaned_data['length_of_crop_stage']
         plant_leave_number = cropmonitoringplantheightform.cleaned_data['plant_leave_number']
         plant_leave_length = cropmonitoringplantheightform.cleaned_data['plant_leave_length']
         plant_leave_width = cropmonitoringplantheightform.cleaned_data['plant_leave_width']
             
         plant_number_two = cropmonitoringplantheightform.cleaned_data['plant_number_two']
         LAI_two = cropmonitoringplantheightform.cleaned_data['LAI_two']
         plant_height_two = cropmonitoringplantheightform.cleaned_data['plant_height_two']
         plant_canopy_width_two = cropmonitoringplantheightform.cleaned_data['plant_canopy_width_two']
         length_of_crop_stage_two = cropmonitoringplantheightform.cleaned_data['length_of_crop_stage_two']
         plant_leave_number_two = cropmonitoringplantheightform.cleaned_data['plant_leave_number_two']
         plant_leave_length_two = cropmonitoringplantheightform.cleaned_data['plant_leave_length_two']
         plant_leave_width_two = cropmonitoringplantheightform.cleaned_data['plant_leave_width_two']
         
         plant_number_three = cropmonitoringplantheightform.cleaned_data['plant_number_three']
         LAI_three = cropmonitoringplantheightform.cleaned_data['LAI_three']
         plant_height_three = cropmonitoringplantheightform.cleaned_data['plant_height_three']
         plant_canopy_width_three = cropmonitoringplantheightform.cleaned_data['plant_canopy_width_three']
         length_of_crop_stage_three = cropmonitoringplantheightform.cleaned_data['length_of_crop_stage_three']
         plant_leave_number_three = cropmonitoringplantheightform.cleaned_data['plant_leave_number_three']
         plant_leave_length_three = cropmonitoringplantheightform.cleaned_data['plant_leave_length_three']
         plant_leave_width_three = cropmonitoringplantheightform.cleaned_data['plant_leave_width_three']

         sub_plot_size = cropmonitoringplantheightform.cleaned_data['sub_plot_size']
         sub_plot_plant_number = cropmonitoringplantheightform.cleaned_data['sub_plot_plant_number']
         total_plant_number = cropmonitoringplantheightform.cleaned_data['total_plant_number']
         
         try:
            cropmonitoringplantheight_instance = CropMonitoringPlantHeight.objects.get(date=date,farm=farm,plotID=Plot.objects.get(plotID=plotID,farm=farm),crop_stage=crop_stage,row_number=row_number,Crop=Crop)
         except CropMonitoringPlantHeight.DoesNotExist:
            if total_plant_number == -999: #in case it's monocropping/intercropping and total plants obtained from planting method tab is None
               cropmonitoringplantheight_instance=CropMonitoringPlantHeight(date=date,Crop=Crop,farm=farm,plotID=Plot.objects.get(plotID=plotID,farm=farm),crop_stage=crop_stage,row_number=row_number,number_of_good_plants=number_of_good_plants,number_of_bad_plants=number_of_bad_plants,plant_density_per_sqm=plant_density_per_sqm,plant_density_per_bed=plant_density_per_bed, \
                                                                         plant_number=1,LAI=LAI,plant_height=plant_height,plant_canopy_width=plant_canopy_width,length_of_crop_stage=length_of_crop_stage,plant_leave_number=plant_leave_number,plant_leave_length=plant_leave_length,plant_leave_width=plant_leave_width, \
                                                                         plant_number_two=2,LAI_two=LAI_two,plant_height_two=plant_height_two,plant_canopy_width_two=plant_canopy_width_two,length_of_crop_stage_two=length_of_crop_stage_two,plant_leave_number_two=plant_leave_number_two,plant_leave_length_two=plant_leave_length_two,plant_leave_width_two=plant_leave_width_two, \
                                                                         plant_number_three=3,LAI_three=LAI_three,plant_height_three=plant_height_three,plant_canopy_width_three=plant_canopy_width_three,length_of_crop_stage_three=lenght_of_crop_stage_three,plant_leave_number_three=plant_leave_number_three,plant_leave_length_three=plant_leave_length_three,plant_leave_width_three=plant_leave_width_three, \
                                                                         sub_plot_size=sub_plot_size,sub_plot_plant_number=sub_plot_plant_number,total_plant_number=total_plant_number,enteredpersonel=SystemUser.objects.get(user=request.user))
            else:
               cropmonitoringplantheight_instance=CropMonitoringPlantHeight(date=date,Crop=Crop,farm=farm,plotID=Plot.objects.get(plotID=plotID,farm=farm),crop_stage=crop_stage,row_number=row_number,number_of_good_plants=number_of_good_plants,number_of_bad_plants=number_of_bad_plants,plant_density_per_sqm=plant_density_per_sqm,plant_density_per_bed=plant_density_per_bed, \
                                                                         plant_number=1,LAI=LAI,plant_height=plant_height,plant_canopy_width=plant_canopy_width,length_of_crop_stage=length_of_crop_stage,plant_leave_number=plant_leave_number,plant_leave_length=plant_leave_length,plant_leave_width=plant_leave_width, \
                                                                         plant_number_two=2,LAI_two=LAI_two,plant_height_two=plant_height_two,plant_canopy_width_two=plant_canopy_width_two,length_of_crop_stage_two=length_of_crop_stage_two,plant_leave_number_two=plant_leave_number_two,plant_leave_length_two=plant_leave_length_two,plant_leave_width_two=plant_leave_width_two, \
                                                                         plant_number_three=3,LAI_three=LAI_three,plant_height_three=plant_height_three,plant_canopy_width_three=plant_canopy_width_three,length_of_crop_stage_three=length_of_crop_stage_three,plant_leave_number_three=plant_leave_number_three,plant_leave_length_three=plant_leave_length_three,plant_leave_width_three=plant_leave_width_three, \
                                                                         enteredpersonel=SystemUser.objects.get(user=request.user))
               cropmonitoringplantheight_instance.save()
         else:
            cropmonitoringplantheight_instance.date = date
            cropmonitoringplantheight_instance.Crop = Crop
            cropmonitoringplantheight_instance.crop_stage = crop_stage
            cropmonitoringplantheight_instance.row_number = row_number
            cropmonitoringplantheight_instance.number_of_good_plants = number_of_good_plants
            cropmonitoringplantheight_instance.number_of_bad_plants = number_of_bad_plants
            cropmonitoringplantheight_instance.plant_density_per_bed = plant_density_per_bed
            cropmonitoringplantheight_instance.plant_density_per_sqm = plant_density_per_sqm
            #crop one
            cropmonitoringplantheight_instance.plant_number = plant_number
            cropmonitoringplantheight_instance.LAI = LAI
            cropmonitoringplantheight_instance.plant_height = plant_height
            cropmonitoringplantheight_instance.plant_canopy_width = plant_canopy_width
            cropmonitoringplantheight_instance.length_of_crop_stage = length_of_crop_stage
            cropmonitoringplantheight_instance.plant_leave_number = plant_leave_number
            cropmonitoringplantheight_instance.plant_leave_length = plant_leave_length
            cropmonitoringplantheight_instance.plant_leave_width = plant_leave_width
            #crop two
            cropmonitoringplantheight_instance.plant_number_two = plant_number_two
            cropmonitoringplantheight_instance.LAI_two = LAI_two
            cropmonitoringplantheight_instance.plant_height_two = plant_height_two
            cropmonitoringplantheight_instance.plant_canopy_width_two = plant_canopy_width_two
            cropmonitoringplantheight_instance.length_of_crop_stage_two = length_of_crop_stage_two
            cropmonitoringplantheight_instance.plant_leave_number_two = plant_leave_number_two
            cropmonitoringplantheight_instance.plant_leave_length_two = plant_leave_length_two
            cropmonitoringplantheight_instance.plant_leave_width_two = plant_leave_width_two
            #crop three
            cropmonitoringplantheight_instance.plant_number_three = plant_number_three
            cropmonitoringplantheight_instance.LAI_three = LAI_three
            cropmonitoringplantheight_instance.plant_height_three = plant_height_three
            cropmonitoringplantheight_instance.plant_canopy_width_three = plant_canopy_width_three
            cropmonitoringplantheight_instance.length_of_crop_stage_three = length_of_crop_stage_three
            cropmonitoringplantheight_instance.plant_leave_number_three = plant_leave_number_three
            cropmonitoringplantheight_instance.plant_leave_length_three = plant_leave_length_three
            cropmonitoringplantheight_instance.plant_leave_width_three = plant_leave_width_three
               
            cropmonitoringplantheight_instance.sub_plot_size = sub_plot_size
            cropmonitoringplantheight_instance.sub_plot_plant_number = sub_plot_plant_number
            cropmonitoringplantheight_instance.total_plant_number = total_plant_number
               
            cropmonitoringplantheight_instance.save()
  
         message='saved'
         return render(request,'iwmiproject/saved.html',locals())
      else:
         return render(request,'iwmiproject/iwmiproject_edit/edit_plot_cropmonitoringplantheight_specific_detail.html',locals())
   else:
      cropmonitoringplantheight_instance = CropMonitoringPlantHeight.objects.get(date=date,farm=personID,plotID=Plot.objects.get(plotID=plotID,farm=personID),crop_stage=crop_stage,row_number=row_number,Crop=Crop)
      cropmonitoringplantheightform = CropMonitoringPlantHeight_Form(instance = cropmonitoringplantheight_instance)
      return render(request,'iwmiproject/iwmiproject_edit/edit_plot_cropmonitoringplantheight_specific_detail.html',locals())

#ConsumedCrops_Form
def edit_cropmonitoringplantheight(request,personID,plotID):
   if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('signup:login'))
   user_instance = SystemUser.objects.get(user=request.user)
   currency = pick_currency(user_instance)
   
   consumedcrops_instance = ConsumedCrops.objects.filter(farm=personID,plotID=Plot.objects.get(plotID=plotID,farm=personID))

   if not consumedcrops_instance:
         return render(request,'iwmiproject/iwmiproject_display/none.html',locals())

   elif len(consumedcrops_instance) == 1:

      if request.method == 'POST':
         consumedcropbyhouseholdform = ConsumedCrops_Form(request.POST)

         if consumedcropbyhouseholdform.is_valid():
            date = consumedcropbyhouseholdform.cleaned_data['date']
            farm = consumedcropbyhouseholdform.cleaned_data['farm']
            plotID = consumedcropbyhouseholdform.cleaned_data['plotID']
            where_consumed = consumedcropbyhouseholdform.cleaned_data['where_consumed']
            how_consumed = consumedcropbyhouseholdform.cleaned_data['how_consumed']
            quantity = consumedcropbyhouseholdform.cleaned_data['quantity']
            marketprice = consumedcropbyhouseholdform.cleaned_data['marketprice']
            totalvalue = consumedcropbyhouseholdform.cleaned_data['totalvalue']

            
            try:
               consumedcrops_instance = ConsumedCrops.objects.get(farm=farm,date=date,plotID=Plot.objects.get(plotID=plotID,farm=farm))
            except ConsumedCrops.DoesNotExist:
               consumedcrops_instance = ConsumedCrops(farm=farm,date=date,plotID=Plot.objects.get(plotID=plotID,farm=farm),where_consumed=where_consumed,how_consumed=how_consumed,quantity=quantity,marketprice=marketprice,totalvalue=totalvalue,currency=currency,enteredpersonel=SystemUser.objects.get(user=request.user))
               consumedcrops_instance.save()
            else:
               consumedcrops_instance.date = date
               consumedcrops_instance.where_consumed = where_consumed
               consumedcrops_instance.how_consumed = how_consumed
               consumedcrops_instance.quantity = quantity
               consumedcrops_instance.marketprice = marketprice
               consumedcrops_instance.totalvalue = totalvalue 
               consumedcrops_instance.save()
               
            message='saved'
            return render(request,'iwmiproject/saved.html',locals())
         else:
            return render(request,'iwmiproject/iwmiproject_edit/edit_consumedcropbyhousehold_specific_detail.html',locals())
      else:
         consumedcrops_instance = ConsumedCrops.objects.get(farm=personID,plotID=Plot.objects.get(plotID=plotID,farm=personID))
         consumedcropbyhouseholdform = ConsumedCrops_Form(instance = consumedcrops_instance)
         
         return render(request,'iwmiproject/iwmiproject_edit/edit_consumedcropbyhousehold_specific_detail.html',locals())
   else:
      if user_instance.role == 'RA' or user_instance.role == 'ST':
         user_village = user_instance.village
         plot_consumedcrops_queryset_list = ConsumedCrops.objects.filter(enteredpersonel=user_instance,farm=personID).select_related()
      elif user_instance.role == 'ALL':
         user_country = user_instance.country
         plot_consumedcrops_queryset_list = ConsumedCrops.objects.filter(farm=personID).select_related()
      elif user_instance.role == 'RS':
         researcher_country = user_instance.country
         plot_consumedcrops_queryset_list = ConsumedCrops.objects.filter(farm__farmID__village__district__region__country=researcher_country).select_related()
      paginator = Paginator(plot_consumedcrops_queryset_list, 20)

      page = request.GET.get('page')
      try:
         plot_consumedcrops_queryset = paginator.page(page)
      except PageNotAnInteger:
         plot_consumedcrops_queryset = paginator.page(1)
      except EmptyPage:
         plot_consumedcrops_queryset = paginator.page(paginator.num_pages)

      context ={
            'object_list':plot_consumedcrops_queryset,
            'title':"List",
            'user_instance':user_instance
      }
      return render(request,'iwmiproject/iwmiproject_display/plot_consumedcrops_detail_display.html',context)


def edit_consumedcropbyhousehold_specific_detail(request,personID,plotID,date):
   if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('signup:login'))
   user_instance = SystemUser.objects.get(user=request.user)
   currency = pick_currency(user_instance)
   
   if request.method == 'POST':
      consumedcropbyhouseholdform = ConsumedCrops_Form(request.POST)

      if consumedcropbyhouseholdform.is_valid():
         date = consumedcropbyhouseholdform.cleaned_data['date']
         farm = consumedcropbyhouseholdform.cleaned_data['farm']
         plotID = consumedcropbyhouseholdform.cleaned_data['plotID']
         where_consumed = consumedcropbyhouseholdform.cleaned_data['where_consumed']
         how_consumed = consumedcropbyhouseholdform.cleaned_data['how_consumed']
         quantity = consumedcropbyhouseholdform.cleaned_data['quantity']
         marketprice = consumedcropbyhouseholdform.cleaned_data['marketprice']
         totalvalue = consumedcropbyhouseholdform.cleaned_data['totalvalue']

         try:
            consumedcrops_instance = ConsumedCrops.objects.get(farm=farm,date=date,plotID=Plot.objects.get(plotID=plotID,farm=farm))
         except ConsumedCrops.DoesNotExist:
            consumedcrops_instance = ConsumedCrops(farm=farm,date=date,plotID=Plot.objects.get(plotID=plotID,farm=farm),where_consumed=where_consumed,how_consumed=how_consumed,quantity=quantity,marketprice=marketprice,totalvalue=totalvalue,currency=currency,enteredpersonel=SystemUser.objects.get(user=request.user))
            consumedcrops_instance.save()
         else:
            consumedcrops_instance.date = date
            consumedcrops_instance.where_consumed = where_consumed
            consumedcrops_instance.how_consumed = how_consumed
            consumedcrops_instance.quantity = quantity
            consumedcrops_instance.marketprice = marketprice
            consumedcrops_instance.totalvalue = totalvalue 
            consumedcrops_instance.save()
               
         message='saved'
         return render(request,'iwmiproject/saved.html',locals())
      else:
         return render(request,'iwmiproject/iwmiproject_edit/edit_consumedcropbyhousehold_specific_detail.html',locals())
   else:
      consumedcrops_instance = ConsumedCrops.objects.get(farm=personID,plotID=Plot.objects.get(plotID=plotID,farm=personID),date=date)
      consumedcropbyhouseholdform = ConsumedCrops_Form(instance = consumedcrops_instance)
         
      return render(request,'iwmiproject/iwmiproject_edit/edit_consumedcropbyhousehold_specific_detail.html',locals())

#TechnologyFailure_Form
def edit_technologyfailure(request,personID):
   if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('signup:login'))
   user_instance = SystemUser.objects.get(user=request.user)
   currency = pick_currency(user_instance)
   
   technologyfailure_instance = TechnologyFailure.objects.filter(farm=Farm.objects.get(farmID=personID))

   if not technologyfailure_instance:
         return render(request,'iwmiproject/iwmiproject_display/none.html',locals())

   elif len(technologyfailure_instance) == 1:

      if request.method == 'POST':
         technologyfailureform = TechnologyFailure_Form(request.POST)

         if technologyfailureform.is_valid():
            date = technologyfailureform.cleaned_data['date']
            farm = technologyfailureform.cleaned_data['farm']
            technology = technologyfailureform.cleaned_data['technology']
            reason = technologyfailureform.cleaned_data['reason']

            try:
               technologyfailure_instance = TechnologyFailure.objects.get(farm=Farm.objects.get(farmID=personID),date=date)
            except TechnologyFailure.DoesNotExist:
               technologyfailure_instance = TechnologyFailure(date=date,farm=Farm.objects.get(farmID=personID),technology=Technology.objects.get(name=technology),reason=reason,enteredpersonel=SystemUser.objects.get(user=request.user))
               consumedcropstechnologyfailure_instance_instance.save()
            else:
               technologyfailure_instance.date = date
               technologyfailure_instance.technology = technology
               technologyfailure_instance.reason = reason
               technologyfailure_instance.save()
               
            message='saved'
            return render(request,'iwmiproject/saved.html',locals())
         else:
            return render(request,'iwmiproject/iwmiproject_edit/edit_technologyfailure_specific_detail.html',locals())
      else:
         technologyfailure_instance = TechnologyFailure.objects.get(farm=Farm.objects.get(farmID=personID))
         technologyfailureform = TechnologyFailure_Form(instance = technologyfailure_instance)
         
         return render(request,'iwmiproject/iwmiproject_edit/edit_technologyfailure_specific_detail.html',locals())
   else:
      if user_instance.role == 'RA' or user_instance.role == 'ST':
         user_village = user_instance.village
         plot_technologyfailure_queryset_list = TechnologyFailure.objects.filter(enteredpersonel=user_instance,farm=Farm.objects.get(farmID=personID)).select_related()
      elif user_instance.role == 'ALL':
         user_country = user_instance.country
         plot_technologyfailure_queryset_list = TechnologyFailure.objects.filter(farm=Farm.objects.get(farmID=personID)).select_related()
      elif user_instance.role == 'RS':
         researcher_country = user_instance.country
         plot_technologyfailure_queryset_list = TechnologyFailure.objects.filter(farm__farmID__village__district__region__country=researcher_country).select_related()
      paginator = Paginator(plot_technologyfailure_queryset_list, 20)

      page = request.GET.get('page')
      try:
         plot_technologyfailure_queryset = paginator.page(page)
      except PageNotAnInteger:
         plot_technologyfailure_queryset = paginator.page(1)
      except EmptyPage:
         plot_technologyfailure_queryset = paginator.page(paginator.num_pages)

      context ={
            'object_list':plot_technologyfailure_queryset,
            'title':"List",
            'user_instance':user_instance
      }
      return render(request,'iwmiproject/iwmiproject_display/technologyfailure_detail_display.html',context)
   
def edit_technologyfailure_specific_detail(request,personID,date):
   if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('signup:login'))
   user_instance = SystemUser.objects.get(user=request.user)

   if request.method == 'POST':
      technologyfailureform = TechnologyFailure_Form(request.POST)

      if technologyfailureform.is_valid():
         date = technologyfailureform.cleaned_data['date']
         farm = technologyfailureform.cleaned_data['farm']
         technology = technologyfailureform.cleaned_data['technology']
         reason = technologyfailureform.cleaned_data['reason']

         try:
            technologyfailure_instance = TechnologyFailure.objects.get(farm=Farm.objects.get(farmID=personID),date=date)
         except TechnologyFailure.DoesNotExist:
            technologyfailure_instance = TechnologyFailure(date=date,farm=Farm.objects.get(farmID=personID),technology=Technology.objects.get(name=technology),reason=reason,enteredpersonel=SystemUser.objects.get(user=request.user))
            technologyfailure_instance.save()
         else:
            technologyfailure_instance.date = date
            technologyfailure_instance.technology = technology
            technologyfailure_instance.reason = reason
            technologyfailure_instance.save()
               
         message='saved'
         return render(request,'iwmiproject/saved.html',locals())
      else:
         return render(request,'iwmiproject/iwmiproject_edit/edit_technologyfailure_specific_detail.html',locals())
   else:
      technologyfailure_instance = TechnologyFailure.objects.get(farm=Farm.objects.get(farmID=personID),date=date)
      technologyfailureform = TechnologyFailure_Form(instance = technologyfailure_instance)
         
      return render(request,'iwmiproject/iwmiproject_edit/edit_technologyfailure_specific_detail.html',locals())


def edit_plot_fertilizer_specification(request,personID,plotID):
   if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('signup:login'))
   user_instance = SystemUser.objects.get(user=request.user)
   currency = pick_currency(user_instance)
   
   fertilizerspecification_instance = FertilizerSpecification.objects.filter(farm=personID,plotID=Plot.objects.get(plotID=plotID,farm=personID))

   if not fertilizerspecification_instance:
         return render(request,'iwmiproject/iwmiproject_display/none.html',locals())
   
   elif len(fertilizerspecification_instance) == 1:

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
               fertilizerspecification_instance = FertilizerSpecification.objects.get(farm=farm,plotID=Plot.objects.get(plotID=plotID,farm=farm),fertilizer=fertilizer)
            except FertilizerSpecification.DoesNotExist:
               try:
                  Fertilizer.objects.get(name=fertilizer)
               except Fertilizer.DoesNotExist:
                  fertilizer_instance = Fertilizer(name=fertilizer)
                  fertilizer_instance.save()
               fertilizerspecification_instance = FertilizerSpecification(farm=farm,plotID=Plot.objects.get(plotID=plotID,farm=farm),fertilizer=Fertilizer.objects.get(name=fertilizer),nitrogen=nitrogen,phosphorus=phosphorus,potassium=potassium,sulphur=sulphur,organic_matter=organic_matter,enteredpersonel=SystemUser.objects.get(user=request.user))
               fertilizerspecification_instance.save()
            else:
               #fertilizerspecification_instance.fertilizer= fertilizer
               fertilizerspecification_instance.nitrogen = nitrogen
               fertilizerspecification_instance.phosphorus = phosphorus
               fertilizerspecification_instance.potassium = potassium
               fertilizerspecification_instance.sulphur = sulphur
               fertilizerspecification_instance.organic_matter = organic_matter
               fertilizerspecification_instance.save()
               
            message='saved'
            return render(request,'iwmiproject/saved.html',locals())
         else:
            return render(request,'iwmiproject/iwmiproject_edit/edit_fertilizerspecification_specific_detail.html',locals())
      else:
         fertilizerspecification_instance = FertilizerSpecification.objects.get(farm=personID,plotID=Plot.objects.get(plotID=plotID,farm=personID))
         fertilizerspecificationform = FertilizerSpecificationForm(instance = fertilizerspecification_instance)
         
         return render(request,'iwmiproject/iwmiproject_edit/edit_fertilizerspecification_specific_detail.html',locals())
   else:
      if user_instance.role == 'RA' or user_instance.role == 'ST':
         user_village = user_instance.village
         plot_fertilizerspecification_queryset_list = FertilizerSpecification.objects.filter(enteredpersonel=user_instance,farm=Farm.objects.get(farmID=personID)).select_related()
      elif user_instance.role == 'ALL':
         user_country = user_instance.country
         plot_fertilizerspecification_queryset_list = FertilizerSpecification.objects.filter(farm=Farm.objects.get(farmID=personID)).select_related()
      elif user_instance.role == 'RS':
         researcher_country = user_instance.country
         plot_fertilizerspecification_queryset_list = FertilizerSpecification.objects.filter(farm__farmID__village__district__region__country=researcher_country).select_related()
      paginator = Paginator(plot_fertilizerspecification_queryset_list, 20)

      page = request.GET.get('page')
      try:
         plot_fertilizerspecification_queryset = paginator.page(page)
      except PageNotAnInteger:
         plot_fertilizerspecification_queryset = paginator.page(1)
      except EmptyPage:
         plot_fertilizerspecification_queryset = paginator.page(paginator.num_pages)

      context ={
            'object_list':plot_fertilizerspecification_queryset,
            'title':"List",
            'user_instance':user_instance
      }
      return render(request,'iwmiproject/iwmiproject_display/fertilizerspecification_detail_display.html',context)



def edit_fertilizer_specification_specific_detail(request,personID,plotID,fertilizer):
   if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('signup:login'))
   user_instance = SystemUser.objects.get(user=request.user)
   currency = pick_currency(user_instance)
   
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
            fertilizerspecification_instance = FertilizerSpecification.objects.get(farm=farm,plotID=Plot.objects.get(plotID=plotID,farm=farm),fertilizer=fertilizer)
         except FertilizerSpecification.DoesNotExist:
            try:
               Fertilizer.objects.get(name=fertilizer)
            except Fertilizer.DoesNotExist:
               fertilizer_instance = Fertilizer(name=fertilizer)
               fertilizer_instance.save()
            fertilizerspecification_instance = FertilizerSpecification(farm=farm,plotID=Plot.objects.get(plotID=plotID,farm=farm),fertilizer=Fertilizer.objects.get(name=fertilizer),nitrogen=nitrogen,phosphorus=phosphorus,potassium=potassium,sulphur=sulphur,organic_matter=organic_matter,enteredpersonel=SystemUser.objects.get(user=request.user))
            fertilizerspecification_instance.save()
         else:
            #fertilizerspecification_instance.fertilizer= fertilizer
            fertilizerspecification_instance.nitrogen = nitrogen
            fertilizerspecification_instance.phosphorus = phosphorus
            fertilizerspecification_instance.potassium = potassium
            fertilizerspecification_instance.sulphur = sulphur
            fertilizerspecification_instance.organic_matter = organic_matter
            fertilizerspecification_instance.save()
               
         message='saved'
         return render(request,'iwmiproject/saved.html',locals())
      else:
         return render(request,'iwmiproject/iwmiproject_edit/edit_fertilizerspecification_specific_detail.html',locals())
   else:
         fertilizerspecification_instance = FertilizerSpecification.objects.get(farm=personID,plotID=Plot.objects.get(plotID=plotID,farm=personID),fertilizer=fertilizer)
         fertilizerspecificationform = FertilizerSpecificationForm(instance = fertilizerspecification_instance)
         
         return render(request,'iwmiproject/iwmiproject_edit/edit_fertilizerspecification_specific_detail.html',locals())


'''
#SeedManagement_Form,BedNursery_Form,Nursery_Form
def edit_plot_saleharvestedcrop_specific_detail(request,personID,plotID,date):
   if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('signup:login'))
   user_instance = SystemUser.objects.get(user=request.user)
   currency = pick_currency(user_instance)
   
   if request.method == 'POST':
      labourmanagement_form = LabourManagement_Form(request.POST)
      SeedManagement_Form = SeedManagement_Form(request.POST)
      BedNursery_Form = BedNursery_Form(request.POST)
      Nursery_Form = Nursery_Form(request.POST)

      if harvestedcropsaleform.is_valid() and labourmanagement_form.is_valid():
         date = harvestedcropsaleform.cleaned_data['date']
         farm = harvestedcropsaleform.cleaned_data['farm']
         plotID = harvestedcropsaleform.cleaned_data['plotID']
         amount = harvestedcropsaleform.cleaned_data['amount']
         marketprice = harvestedcropsaleform.cleaned_data['marketprice']
         income = harvestedcropsaleform.cleaned_data['income']
         mode_of_transport = harvestedcropsaleform.cleaned_data['mode_of_transport']
         fare = harvestedcropsaleform.cleaned_data['fare']
         fuel_type = harvestedcropsaleform.cleaned_data['fuel_type']
         fuel_cost = harvestedcropsaleform.cleaned_data['fuel_cost']
         distance_to_the_market = harvestedcropsaleform.cleaned_data['distance_to_the_market']
         
         labour = labourmanagement_form.cleaned_data['labour']
         hired_female_number = labourmanagement_form.cleaned_data['hired_female_number']
         hired_female_time = labourmanagement_form.cleaned_data['hired_female_time']
         hired_male_number = labourmanagement_form.cleaned_data['hired_male_number']
         hired_male_time = labourmanagement_form.cleaned_data['hired_male_time']
         family_female_number = labourmanagement_form.cleaned_data['family_female_number']
         family_female_time = labourmanagement_form.cleaned_data['family_female_time']
         family_male_number = labourmanagement_form.cleaned_data['family_male_number']
         family_male_time = labourmanagement_form.cleaned_data['family_male_time']
         wage = labourmanagement_form.cleaned_data['wage']
         price_unit = labourmanagement_form.cleaned_data['price_unit']
         
         
         try:
            saleharvestedcrop_instance = SaleHarvestedCrop.objects.get(farm=farm,date=date,plotID=Plot.objects.get(plotID=plotID,farm=farm))
         except SaleHarvestedCrop.DoesNotExist:
            if mode_of_transport=='Public transport':
               saleharvestedcrop_instance = SaleHarvestedCrop(farm=farm,date=date,marketprice=marketprice,distance_to_the_market=distance_to_the_market,currency=currency,amount=amount,income=income,mode_of_transport=mode_of_transport,fare=fare,plotID=Plot.objects.get(plotID=plotID,farm=farm),enteredpersonel=SystemUser.objects.get(user=request.user))
            elif mode_of_transport=='Own transportation':
               saleharvestedcrop_instance = SaleHarvestedCrop(farm=farm,date=date,marketprice=marketprice,distance_to_the_market=distance_to_the_market,currency=currency,amount=amount,income=income,mode_of_transport=mode_of_transport,fuel_type=fuel_type,fuel_cost=fuel_cost,plotID=Plot.objects.get(plotID=plotID,farm=farm),enteredpersonel=SystemUser.objects.get(user=request.user))
            else:
               saleharvestedcrop_instance = SaleHarvestedCrop(farm=farm,date=date,marketprice=marketprice,distance_to_the_market=distance_to_the_market,currency=currency,amount=amount,income=income,mode_of_transport=mode_of_transport,plotID=Plot.objects.get(plotID=plotID,farm=farm),enteredpersonel=SystemUser.objects.get(user=request.user))
            saleharvestedcrop_instance.save()
         else:
            saleharvestedcrop_instance.date = date
            saleharvestedcrop_instance.amount = amount
            saleharvestedcrop_instance.income = income
            saleharvestedcrop_instance.marketprice = marketprice
            saleharvestedcrop_instance.mode_of_transport = mode_of_transport
            saleharvestedcrop_instance.distance_to_the_market = distance_to_the_market
            
            if mode_of_transport == 'Public transport':
               saleharvestedcrop_instance.fare = fare
            elif mode_of_transport == 'Own transportation':
               saleharvestedcrop_instance.fuel_type = fuel_type
               saleharvestedcrop_instance.fuel_cost = fuel_cost
            saleharvestedcrop_instance.save()

         areadescription='Plot'
         try:
            plot_labourmanagament_instance = LabourManagament.objects.get(farm=personID,areaID=plotID,date=saleharvestedcrop_instance.date,activity='Plot harvest sale')
         except LabourManagament.DoesNotExist:
            if labour == 'Family':
               plot_labourmanagament_instance = LabourManagament(date=date,family_female_time=family_female_time,family_male_time=family_male_time,farm=farm,areaID=plotID,areadescription='Plot',labour=labour,family_female_number=family_female_number,family_male_number=family_male_number,activity='Plot harvest sale',wage=wage,price_unit=currency,enteredpersonel=SystemUser.objects.get(user=request.user))
            elif labour == 'Hired':
               plot_labourmanagament_instance = LabourManagament(date=date,hired_female_time=hired_female_time,hired_male_time=hired_male_time,farm=farm,areaID=plotID,areadescription='Plot',labour=labour,hired_female_number=hired_female_number,hired_male_number=hired_male_number,activity='Plot harvest sale',wage=wage,price_unit=currency,enteredpersonel=SystemUser.objects.get(user=request.user))
            elif labour == 'FamilyHired':
               plot_labourmanagament_instance = LabourManagament(date=date,family_female_time=family_female_time,family_male_time=family_male_time,hired_female_time=hired_female_time,hired_male_time=hired_male_time,farm=farm,areaID=plotID,areadescription='Plot',labour=labour,hired_female_number=hired_female_number,hired_male_number=hired_male_number,family_female_number=family_female_number,family_male_number=family_male_number,activity='Plot harvest sale',wage=wage,price_unit=currency,enteredpersonel=SystemUser.objects.get(user=request.user))
            plot_labourmanagament_instance.save()
         else:
            activity='Plot harvest sale'
            if labour == 'Family':
               labourmanagement(activity,labour,plot_labourmanagament_instance,areadescription,request.user,date,wage,family_female_number=family_female_number,family_female_time=family_female_time,family_male_number=family_male_number,family_male_time=family_male_time)
            elif labour == 'Hired':
               labourmanagement(activity,labour,plot_labourmanagament_instance,areadescription,request.user,date,wage,hired_female_number=hired_female_number,hired_female_time=hired_female_time,hired_male_number=hired_male_number,hired_male_time=hired_male_time)
            elif labour == 'FamilyHired':
               labourmanagement(activity,labour,plot_labourmanagament_instance,areadescription,request.user,date,wage,hired_female_number=hired_female_number,hired_female_time=hired_female_time,hired_male_number=hired_male_number,hired_male_time=hired_male_time,family_female_number=family_female_number,family_female_time=family_female_time,family_male_number=family_male_number,family_male_time=family_male_time)

         message='saved'
         return render(request,'iwmiproject/saved.html',locals())
      else:
         return render(request,'iwmiproject/iwmiproject_edit/edit_plot_saleharvestedcrop_specific_detail.html',locals())
   else:
      saleharvestedcrop_instance = SaleHarvestedCrop.objects.get(farm=personID,plotID=Plot.objects.get(plotID=plotID,farm=personID),date=date)
      harvestedcropsaleform = SaleHarvestedCrop_Form(instance = saleharvestedcrop_instance)
      
      plot_labourmanagament_instance = LabourManagament.objects.get(farm=personID,areaID=plotID,date=saleharvestedcrop_instance.date,activity='Plot harvest sale')
      labourmanagement_form = LabourManagement_Form(instance = plot_labourmanagament_instance)
      return render(request,'iwmiproject/iwmiproject_edit/edit_plot_saleharvestedcrop_specific_detail.html',locals())
   
'''
'''
#SoilMoistureProfiler_Form,SoilMoistureMeasurementManagement_Form,GravimetricSoilMoisture_Form
def edit_plot_soilmoisture(request,personID,plotID):
   if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('signup:login'))
   user_instance = SystemUser.objects.get(user=request.user)
   
   soilmoistureprofiler_instance = SoilMoistureProfiler.objects.filter(farm=personID,plotID=Plot.objects.get(plotID=plotID,farm=personID))
   soilmoisturemanagement_instance = SoilMoistureMeasurementManagement.objects.filter(farm=personID,plotID=Plot.objects.get(plotID=plotID,farm=personID))
   gravimetricsoilmoisture_instance = GravimetricSoilMoisture.objects.filter(farm=personID,plotID=Plot.objects.get(plotID=plotID,farm=personID))
   
   if (not soilmoistureprofiler_instance) and (not soilmoisturemanagement_instance) and (not gravimetricsoilmoisture_instance):
         return render(request,'iwmiproject/iwmiproject_display/none.html',locals())

   elif len(saleharvestedcrop_instance) == 1:
      pass
   else:
      if user_instance.role == 'RA' or user_instance.role == 'ST':
         user_village = user_instance.village
         plot_saleharvestedcrop_queryset_list = SaleHarvestedCrop.objects.filter(enteredpersonel=user_instance,farm=personID).select_related()
      elif user_instance.role == 'ALL':
         user_country = user_instance.country
         plot_saleharvestedcrop_queryset_list = SaleHarvestedCrop.objects.filter(farm=personID).select_related()
      elif user_instance.role == 'RS':
         researcher_country = user_instance.country
         plot_saleharvestedcrop_queryset_list = SaleHarvestedCrop.objects.filter(farm__farmID__village__district__region__country=researcher_country).select_related()
      paginator = Paginator(plot_saleharvestedcrop_queryset_list, 20)

      page = request.GET.get('page')
      try:
         plot_saleharvestedcrop_queryset = paginator.page(page)
      except PageNotAnInteger:
         plot_saleharvestedcrop_queryset = paginator.page(1)
      except EmptyPage:
         plot_saleharvestedcrop_queryset = paginator.page(paginator.num_pages)

      context ={
            'object_list':plot_saleharvestedcrop_queryset,
            'title':"List",
            'user_instance':user_instance
      }
      return render(request,'iwmiproject/iwmiproject_display/plot_soilmoisture_detail_display.html',context)

'''
