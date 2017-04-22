from iwmiproject.models import FertilizerSpecification,LandPreparation,ResidualHandling,Remark,FertilizerManagement,PlotCrop,BedNursery,Pesticide,Seed,CropVarieties,TechnologyManagement,BedPlot,Fertilizer,ApplicationCalibration,Country,PlotManagement,WaterManagement,FarmGroup,WaterliftingCalibrations,PlantingMethod,Region, Village, District,Crop,Farm,WaterSources,WaterSourceCategory,People,Nursery,Plot,TechnologyManagement
from django import template
from django.core.context_processors import csrf
from django.core import serializers
from django.http import Http404, HttpResponse 
from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect
from itertools import chain


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
    return HttpResponse(json_models, content_type="application/javascript")


def plotmanagement_info(request,farm,plot):
    try:
        PlantingMethod.objects.get(plotID__pk=plot,farm=farm)
    except PlantingMethod.DoesNotExist:
        plot_cropping_system = None
        total_plants = None
        crops= None
    else:
        plantingmethod_instance = PlantingMethod.objects.get(plotID__pk=plot,farm=farm)
        plotmanagement_instance = PlotManagement.objects.get(plotID__pk=plot,farm=farm)
        plot_cropping_system = plantingmethod_instance.CroppingSystem
        if plot_cropping_system == 'Intercropping' and plantingmethod_instance.total_plants==None:
          total_plants = None
        elif plot_cropping_system == 'Monocropping' and plantingmethod_instance.total_plants==None:
            total_plants = None
        else:
            total_plants = plantingmethod_instance.total_plants
        crops = [i.name for i in plotmanagement_instance.crop.all()]
    plotmanagement_info = [plot_cropping_system,total_plants,crops]
    return HttpResponse(json.dumps(plotmanagement_info),content_type="application/json")

'''    
def plotmanagement_info(request,farm,plot):
    plotmanagement_instance = PlotManagement.objects.get(plotID__pk=plot,farm=farm)
    plot_cropping_system = plotmanagement_instance.cropping_system
    crops = [i.name for i in plotmanagement_instance.crop.all()]
    plotmanagement_info = [plot_cropping_system,crops]
    return HttpResponse(json.dumps(plotmanagement_info),content_type="application/json")
'''
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


def fertilizerspecification(request,farm,plotID):
    fertizer_instance = FertilizerManagement.objects.filter(plotID__pk=plotID,farm=farm)
    if not fertizer_instance:
        plot_fertilizer = None
    else:
        plot_fertilizer = list(set([str(i.fertilizer) for i in fertizer_instance]))
    return HttpResponse(json.dumps(plot_fertilizer),content_type="application/json")



def edit_fertilizerspecification(request,farm,plotID,fertilizer):
    fertizer_instance = FertilizerSpecification.objects.filter(plotID__pk=plotID,farm=farm,fertilizer=fertilizer)
    plot_fertilizer = list(set([str(i.fertilizer) for i in fertizer_instance]))
    return HttpResponse(json.dumps(plot_fertilizer),content_type="application/json")



'''
def plot_select(request,farm):
    plots= Farm.objects.get(farm=farm).__int__()
    return HttpResponse(json.dumps(plots), content_type="application/json")
''' 
def pumping_source_select(request,watersource):
    pumping_sources= WaterSourceCategory.objects.filter(watersourcetype=watersource).order_by('category')
    json_models = serializers.serialize("json",pumping_sources)
    return HttpResponse(json_models, content_type="application/javascript")

def household_member_select(request,village):
    household_members= People.objects.filter(village=village).order_by('firstname')
    #print('household_members:{}'.format(household_members))
    json_models = serializers.serialize("json",household_members)
    return HttpResponse(json_models, content_type="application/javascript")

def farmer_select(request,village):
    farmers= People.objects.filter(village=village).order_by('firstname')
    json_models = serializers.serialize("json",farmers)
    return HttpResponse(json_models, content_type="application/javascript")

def nursery_select(request,farm):
    nurseries = Nursery.objects.filter(farm__farmID=farm).order_by('NurseryID')
    json_models = serializers.serialize("json",nurseries)
    return HttpResponse(json_models, content_type="application/javascript")

def fieldplot_select(request,farm):
    plots = Plot.objects.filter(farm__farmID=farm).order_by('plotID')
    json_models = serializers.serialize("json",plots)
    return HttpResponse(json_models, content_type="application/javascript")

def technology_select(request,farm):
    technologies = str(TechnologyManagement.objects.get(farm__farmID=farm).technology)
    return HttpResponse(json.dumps(technologies),content_type="application/json")
    
def farm_technology_select(request,farm,plot):
    technologies = str(TechnologyManagement.objects.get(farm__farmID=farm).technology)
    try:
        print('first')
        PlotManagement.objects.get(plotID__pk=plot,farm=farm)
    except PlotManagement.DoesNotExist:
        print('second')
        water_application='NONE'
    else:
        print('third')
        water_application = str(PlotManagement.objects.get(plotID__pk=plot,farm=farm).water_application)
    finally:plot_water_technology_info = [technologies, water_application]
    return HttpResponse(json.dumps(plot_water_technology_info),content_type="application/json")
    #return HttpResponse(json.dumps(technologies),content_type="application/json")

def water_application_select(request,plot,farm):
    try:
        PlotManagement.objects.get(plotID__pk=plot,farm=farm).water_application
        print('In the try')
    except PlotManagement.DoesNotExist:
        water_application='NONE'
        print('in the except')
    else:
        plotmanagement_instance = PlotManagement.objects.get(plotID__pk=plot,farm=farm)
        water_application = str(plotmanagement_instance.water_application)
        fieldsize =  plotmanagement_instance.plot_size
        dischargelist = [i.discharge for i in WaterliftingCalibrations.objects.filter(farm=farm)]
        print('*******')
        try:
            plantingmethod_instance = PlantingMethod.objects.get(farm=farm,plotID=(Plot.objects.get(plotID=Plot.objects.get(pk=plot),farm=farm)))
        except PlantingMethod.DoesNotExist:
            plantsnumber='NONE'
        else:
            '''
            if plantingmethod_instance.total_plants == None:
                try:
                    cropmonitoring_instance = CropMonitoringPlantHeight.objects.get(plotID__pk=plot,farm=farm)
                except CropMonitoringPlantHeight.DoesNotExist:
                    tplantsnumber='NONE'
                else:
                    if not cropmonitoring_instance.total_plants:
                       plantsnumber='NONE'
                    else:
                        plantsnumber = cropmonitoring_instance.total_plants
            else:
                plantsnumber = plantingmethod_instance.total_plants
            '''
            plantsnumber = plantingmethod_instance.total_plants
        print('in the else')
        #plotirrigationevent_instance=PlotIrrigationEvent.objects.get(plotID=(Plot.objects.get(plotID=Plot.objects.get(pk=plot),farm=farm)))
        #plantingmethod_instance = PlantingMethod.objects.get(plotID=(Plot.objects.get(plotID=Plot.objects.get(pk=plot),farm=farm)))
        
        #wetteddiameteraroundplant=plotirrigationevent_instance.wetteddiameteraroundplant
        
        print('plantsnumber:{}'.format(plantsnumber))
        if not dischargelist:
            average_discharge = 'NONE'
        else:
            average_discharge = sum(dischargelist)/len(dischargelist)       
        plotlist = [water_application,fieldsize,average_discharge,plantsnumber]#,wetteddiameteraroundplant,plantsnumber]
        print('plotlist:{}'.format(plotlist))
    finally:
        return HttpResponse(json.dumps(plotlist),content_type="application/json")
        #json_models = serializers.serialize("json",plotlist)
        #return HttpResponse(json_models, content_type="application/javascript")

def nurseryarea_select(request,nursery,farm):
    bednursery_instance = BedNursery.objects.get(nursery=Nursery.objects.get(NurseryID=nursery,farm=farm))
    nursery_bed_area = bednursery_instance.area
    print('nursery_bed_area:{}'.format(nursery_bed_area))
    nursery_bed_area= [nursery_bed_area]
    return HttpResponse(json.dumps(nursery_bed_area),content_type="application/json")

def farm_nursery(request,farm):
    nurseries = Nursery.objects.filter(farm__farmID=farm).order_by('NurseryID')
    json_models = serializers.serialize("json",nurseries)
    return HttpResponse(json_models, content_type="application/javascript")

def group_select(request,village):
    groups = FarmGroup.objects.filter(village=village).order_by('name')
    json_models = serializers.serialize("json",groups)
    return HttpResponse(json_models, content_type="application/javascript")
    
    
def water_application_and_water_management_select(request,plot,farm):
    print('aaaaaaaaaaaaaaaaaaaa')
    try:
       
        PlotManagement.objects.get(plotID__pk=plot,farm=farm).water_application
    except PlotManagement.DoesNotExist:
      
        water_application='NONE'
        fieldsize='NONE'
        water_application_and_water_management = [water_application]
    else:
        plot_fieldtype = Plot.objects.get(pk=plot,farm=farm).fieldtype
        plotmanagement_instance = PlotManagement.objects.get(plotID__pk=plot,farm=farm)
        bedplot_instance = BedPlot.objects.get(plotID__pk=plot,farm=farm)
        fieldsize = bedplot_instance.length * bedplot_instance.width
        water_application = str(plotmanagement_instance.water_application)
        #fieldsize =  plotmanagement_instance.plot_size
        
        print('fieldsize:{}'.format(fieldsize))
        try:
         
            #plantingmethod_instance = PlantingMethod.objects.get(farm=farm,plotID=(Plot.objects.get(plotID=Plot.objects.get(pk=plot),farm=farm)))
            #plantingmethod_instance = PlantingMethod.objects.get(farm=farm,plotID=Plot.objects.get(pk=plot,farm=farm))
            plantingmethod_instance = PlantingMethod.objects.get(farm=farm,plotID__pk=plot)
          
        except PlantingMethod.DoesNotExist:
            
            total_plants='NONE'
        else:
           
            total_plants = plantingmethod_instance.total_plants
        try:
            
            WaterManagement.objects.get(plotID__pk=plot,farm=farm)
            #WaterManagement.objects.get(plotID=Plot.objects.get(pk=plot,farm=farm),farm=farm)
            #WaterManagement.objects.get(plotID=(Plot.objects.get(plotID=(Plot.objects.get(plotID=Plot.objects.get(pk=plot),farm=farm)))))
        except WaterManagement.DoesNotExist:
            #print('second_second')
            watermanagement='NONE'
        else:
            
            watermanagement =  str(WaterManagement.objects.get(plotID__pk=plot,farm=farm).water_management_method)
        #applicationrate_list = [i.application_rate for i in ApplicationCalibration.objects.filter(farm=farm,plot=(Plot.objects.get(plotID=Plot.objects.get(pk=plot),farm=farm)))]
        #applicationrate_list = [i.application_rate for i in ApplicationCalibration.objects.filter(farm=farm,plot=Plot.objects.get(pk=plot,farm=farm))]
        applicationrate_list = [i.application_rate for i in ApplicationCalibration.objects.filter(farm=farm,plot__pk=plot)]
        
        dischargelist =[i.discharge for i in WaterliftingCalibrations.objects.filter(farm=farm)]
        
        if not dischargelist:
            average_discharge = 'NONE'
        else:
            average_discharge = sum(dischargelist)/len(dischargelist)
        if not applicationrate_list:
            application_rate = 'NONE'
            water_application_and_water_management = [water_application,watermanagement,average_discharge,fieldsize,application_rate]
        else:
            
            applicationrate_volume_list = [(i.dripline_numbers,i.dripline_length,i.emitter_spacing,i.emitter_wetted_diameter) for i in ApplicationCalibration.objects.filter(farm=farm,plot__pk=plot)]
            
            application_rate = sum(applicationrate_list)/len(applicationrate_list)
            
            if len(applicationrate_volume_list) == 1:
                
                if not applicationrate_volume_list[0][0]: # check if the value is none or not
                    dripline_numbers = 'NONE'
                else:
                    dripline_numbers= applicationrate_volume_list[0][0]
                    
                if not applicationrate_volume_list[0][1]:
                    dripline_length ='NONE'
                else:
                    dripline_length= applicationrate_volume_list[0][1]
                    
                if not applicationrate_volume_list[0][2]:
                    emitter_spacing = 'NONE'
                else:
                    emitter_spacing= applicationrate_volume_list[0][2]

                if not applicationrate_volume_list[0][3]:
                    emitter_wetted_diameter = 'NONE'
                else:
                    emitter_wetted_diameter= applicationrate_volume_list[0][3]
                water_application_and_water_management = [water_application,watermanagement,average_discharge,fieldsize,application_rate,total_plants,plot_fieldtype,dripline_numbers,dripline_length,emitter_spacing,emitter_wetted_diameter]
                
            elif len(applicationrate_volume_list) != 1:
                
                dripline_numbers_list_all_value = [i[0] for i in applicationrate_volume_list] #group values together from tuples 
                dripline_length_list_all_value = [i[1] for i in applicationrate_volume_list]
                emitter_spacing_list_all_value = [i[2] for i in applicationrate_volume_list]
                emitter_wetted_diameter_list_all_value = [i[3] for i in applicationrate_volume_list]
                
                dripline_numbers_list = list(filter(lambda x: x!=None, dripline_numbers_list_all_value)) # remove none value from list
                dripline_length_list = list(filter(lambda x: x!=None, dripline_length_list_all_value))
                emitter_spacing_list = list(filter(lambda x: x!=None, emitter_spacing_list_all_value))
                emitter_wetted_diameter_list = list(filter(lambda x: x!=None, emitter_wetted_diameter_list_all_value))
                
                if not dripline_numbers_list: # if list is empty
                    dripline_numbers = 'NONE'
                else:
                    dripline_numbers = sum(dripline_numbers_list)/len(dripline_numbers_list)
                    
                if not dripline_length_list:
                    dripline_length = 'NONE'
                else:
                    dripline_length = sum(dripline_length_list)/len(dripline_length_list)
                if not emitter_spacing_list:
                    emitter_spacing = 'NONE'
                else:
                    emitter_spacing = sum(emitter_spacing_list)/len(emitter_spacing_list)
                    
                if not emitter_wetted_diameter_list:
                    emitter_wetted_diameter = 'NONE'
                else:
                    emitter_wetted_diameter = sum(emitter_wetted_diameter_list)/len(emitter_wetted_diameter_list)
            
                water_application_and_water_management = [water_application,watermanagement,average_discharge,fieldsize,application_rate,total_plants,plot_fieldtype,dripline_numbers,dripline_length,emitter_spacing,emitter_wetted_diameter]
    finally:
        return HttpResponse(json.dumps(water_application_and_water_management),content_type="application/json")
    

def pesticide_select(request):
    if request.is_ajax:
        qs = request.GET.get('term','')
        pesticide_list = Pesticide.objects.filter(name__icontains=qs)
        results =[]
        for pesticide in pesticide_list:
            pesticide_json={}
            pesticide_json['label'] = pesticide.name
            pesticide_json['value'] = pesticide.name
            results.append(pesticide_json)
        data_json = json.dumps(results)
    else:
        data_json='fail'
    mimetype='application/json'
    return HttpResponse(data_json,mimetype)

def stress_select(request):
    if request.is_ajax:
        qs = request.GET.get('term','')
        remark_list = Remark.objects.filter(stress__icontains=qs)
        results =[]
        for remark in remark_list:
            remark_json={}
            remark_json['label'] = remark.stress
            remark_json['value'] = remark.stress
            results.append(remark_json)
        data_json = json.dumps(results)
    else:
        data_json='fail'
    mimetype='application/json'
    return HttpResponse(data_json,mimetype)

def fertilizer_select(request):
    if request.is_ajax:
        qs = request.GET.get('term','')
        fertilizer_list = Fertilizer.objects.filter(name__icontains=qs)
        results =[]
        for fertilizer in fertilizer_list:
            fertilizer_json={}
            fertilizer_json['label'] = fertilizer.name
            fertilizer_json['value'] = fertilizer.name
            results.append(fertilizer_json)
        data_json = json.dumps(results)
    else:
        data_json='fail'
    mimetype='application/json'
    return HttpResponse(data_json,mimetype)

def crop_select(request):
    if request.is_ajax:
        qs = request.GET.get('term','')
        crop_list = Crop.objects.filter(name__icontains=qs)
        results =[]
        for crop in crop_list:
            crop_json={}
            crop_json['label'] = crop.name
            crop_json['value'] = crop.name
            results.append(crop_json)
        data_json = json.dumps(results)
    else:
        data_json='fail'
    mimetype='application/json'
    return HttpResponse(data_json,mimetype)

def crop1_variety(request):
    if request.is_ajax:
        qs = request.GET.get('term','')
        crop1_variety_list = PlotCrop.objects.filter(crop1_variety__icontains=qs)
        results =[]
        for crop_variety in crop1_variety_list:
            crop_variety_json={}
            crop_variety_json['label'] = crop_variety.crop1_variety
            crop_variety_json['value'] = crop_variety.crop1_variety
            results.append(crop_variety_json)
        data_json = json.dumps(results)
    else:
        data_json='fail'
    mimetype='application/json'
    return HttpResponse(data_json,mimetype)

def crop2_variety(request):
    if request.is_ajax:
        qs = request.GET.get('term','')
        crop2_variety_list = PlotCrop.objects.filter(crop2_variety__icontains=qs)
        results =[]
        for crop_variety in crop2_variety_list:
            crop_variety_json={}
            crop_variety_json['label'] = crop_variety.crop2_variety
            crop_variety_json['value'] = crop_variety.crop2_variety
            results.append(crop_variety_json)
        data_json = json.dumps(results)
    else:
        data_json='fail'
    mimetype='application/json'
    return HttpResponse(data_json,mimetype)

def waterapplication_select(request,plot,farm):
    try:
        PlotManagement.objects.get(plotID__pk=plot,farm=farm)
    except PlotManagement.DoesNotExist:
        water_application='NONE'
        plotlist = [water_application]
    else:
        plotfieldtype = Plot.objects.get(pk=plot,farm=farm).fieldtype
        plotmanagement_instance = PlotManagement.objects.get(plotID__pk=plot,farm=farm)
        water_application = str(plotmanagement_instance.water_application)
        bed_instance =BedPlot.objects.get(plotID=(Plot.objects.get(plotID=Plot.objects.get(pk=plot),farm=farm)))
        bedlength = bed_instance.length
        bedwidth = bed_instance.width
        bednumber = bed_instance.numbers
        plotlist = [water_application,bedlength,bedwidth,bednumber,str(plotfieldtype)]
    finally:
        return HttpResponse(json.dumps(plotlist),content_type="application/json")
        #json_models = serializers.serialize("json",plotlist)
        #return HttpResponse(json_models, content_type="application/javascript")

def select_all(request):
    farmers= People.objects.all().order_by('firstname')
    json_models = serializers.serialize("json",farmers)
    return HttpResponse(json_models, content_type="application/javascript")


def seedtype_select(request):
    if request.is_ajax:
        qs = request.GET.get('term','')
        seedvariety_list = Seed.objects.filter(name__icontains=qs)
        results =[]
        for seedvariety in seedvariety_list:
            seedvariety_json={}
            seedvariety_json['label'] = seedvariety.name
            seedvariety_json['value'] = seedvariety.name
            results.append(seedvariety_json)
        data_json = json.dumps(results)
    else:
        data_json='fail'
    mimetype='application/json'
    return HttpResponse(data_json,mimetype)


def plot_croppingsystem(request,plot,farm):
    try:
        PlotManagement.objects.get(plotID__pk=plot,farm=farm)
    except PlotManagement.DoesNotExist:
        croppingsystem='NONE'
    else:
        plotmanagement_instance = PlotManagement.objects.get(plotID__pk=plot,farm=farm)
        plotcrop_instance = PlotCrop.objects.get(plotID__pk=plot,farm=farm)
        croppingsystem =  plotmanagement_instance.cropping_system
        crop1_planting_method = plotcrop_instance.crop1_planting_method
        crop2_planting_method = plotcrop_instance.crop2_planting_method
        if croppingsystem == 'Monocropping':
            crops = list(plotmanagement_instance.crop.values_list('name',flat=True))
        elif croppingsystem == 'Intercropping':
            crops = list(plotmanagement_instance.crop.values_list('name',flat=True))
    finally:
        print('crops: {}'.format(crops))
        if croppingsystem == 'NONE': plot_detail = [croppingsystem]
        else:plot_detail = [croppingsystem,crop1_planting_method,crop2_planting_method] + crops
        #print('crop1_planting_method: {}'.format(crop1_planting_method))
        #print('crop2_planting_method: {}'.format(crop2_planting_method))
        return HttpResponse(json.dumps(plot_detail),content_type="application/json")
    
def get_plot_name(request,plot,farm):
    plot_instance = Plot.objects.get(pk=plot,farm=farm)
    plot_name = [plot_instance.plotID]
    return HttpResponse(json.dumps(plot_name),content_type="application/json")

    
    
def get_farm_name(request,farm):
    #district_obj = District.objects.get(district=district)
    farmers = Farmer.objects.all().filter(village=village).order_by('first_name')
    json_models = serializers.serialize("json",farmers)
    return HttpResponse(json_models, content_type="application/javascript")

def farm_ownership(request,farm):
    farm_ownership = [Farm.objects.get(farmID=farm).landownership]
    return HttpResponse(json.dumps(farm_ownership),content_type="application/json")


def get_farmer_name(request,farmID):
    farmer_instance =  People.objects.get(personID=farmID)
    farmer_name = [farmer_instance.personID,farmer_instance.firstname,farmer_instance.middlename,farmer_instance.lastname]
    return HttpResponse(json.dumps(farmer_name),content_type="application/json")

def get_plot_name(request,plotID):
    plot_instance =  Plot.objects.get(pk=plotID)
    plot_name = [plot_instance.pk,plot_instance.plotID]
    return HttpResponse(json.dumps(plot_name),content_type="application/json")

def get_plot_stress(request,plotID,farm,start_date,end_date):
    remark_instance = Remark.objects.get(plot__pk=plotID,farm=farm,start_date=start_date,end_date=end_date)
    plot_stress = [remark_instance.stress]
    return HttpResponse(json.dumps(plot_stress),content_type="application/json")

def get_plot_landpreparationtool(request,plotID,farm,date):
    landpreparation_instance = LandPreparation.objects.get(plotID__pk=plotID,farm=farm,date=date)
    landpreparation_instance = [landpreparation_instance.landpreparationtool]
    return HttpResponse(json.dumps(landpreparation_instance),content_type="application/json")

def get_plot_compost_kind(request,plotID,farm,date):
    fertilizermanagement_instance = FertilizerManagement.objects.get(plotID__pk=plotID,farm=farm,date=date)
    plot_compost_kind = [fertilizermanagement_instance.compost_kind]
    return HttpResponse(json.dumps(plot_compost_kind),content_type="application/json")

def get_plot_residual_activities(request,plotID,farm,date):
    residualhandling_instance = ResidualHandling.objects.get(plotID__pk=plotID,farm=farm,date=date)
    plot_residual_activities = [residualhandling_instance.residual_activities]
    return HttpResponse(json.dumps(plot_residual_activities),content_type="application/json")

'''
Concatenating Querysets in Django

Queryset + Queryset

queryset1 = MyModel.objects.all()[0:3]
queryset2 = MyModel.objects.all()[4:7]
 
from itertools import chain
merged_qs = list(chain(queryset1, queryset2))
Object + Queryset

myobj = MyModel.objects.get(pk=1)
queryset = MyModel.objects.all()
 
from itertools import chain
merged_qs = list(chain([mobj], queryset))
'''



def is_None(x):
    answer = bool((lambda h: h is None, x[0][3]))
    return answer


    
    
    