from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.contrib.auth.forms import AuthenticationForm
from iwmiproject.models import FertilizerSpecification,TechnologyFailure,ConsumedCrops,SeedManagement,BedNursery,CropMonitoringPlantHeight,GravimetricSoilMoisture,SoilMoistureProfiler,SoilMoistureMeasurementManagement,SaleHarvestedCrop,TissueNutrientAnalysis,OtherWaterUsage,SoilProperty,YieldPlantLevel,YieldRowBedLevel,ResidualHandling,Weed,YieldFarmLevel,PesticideManagement,LabourManagament,FertilizerManagement,LandPreparation,LandClearance,Remark,People,PlotCrop,WaterManagement,CropVarieties, Furrow,Farm,BedPlot,Plot,PlotManagement,Nursery, Pump,Country,Region,District,Village,Crop,FarmGroup,Farm,Fertilizer,Pesticide,Technology,Seed,Fuel,Soil,Spaire,WaterSources,WaterSourceCategory
from django.contrib import admin
from django.forms import ModelForm
from django import forms
from django.forms import Select
from django.contrib.admin.widgets import AdminTimeWidget
from django.utils.safestring import mark_safe

from django.forms.widgets import TextInput
from django.conf import settings

#from transec.settings import DATE_INPUT_FORMATS

#from dal import autocomplete
CLIMATE_CHOICES=(
        ('','Choose...'),
        ('Rainy','Rainy'),
        ('Sunny','Sunny'),
        ('Cloudy','Cloudy'),
    )

IRRIGATE_WHOLE_OR_PER_PLANT_CHOICES=(
                        ('','Choose...'),
                        ('Perplant','Per plant'),
                        ('Wholefield','Whole field'),
    )


CURRENCY_CHOICES =(
        ('Tsh','Tsh'),
        ('birr','Birr'),
        ('cedi','Cedi'),
        ('Usd','Usd'),
)

DRY_FRESH_CHOICES=(
        ('','Choose..'),
        ('Dry','Dry'),
        ('Fresh','Fresh'),
)


LABOUR_CHOICES =(
        ('','Choose..'),
        ('Family','Family'),
        ('Hired','Hired'),
        ('FamilyHired','Family & Hired'),
)


WATER_SOURCE_CHOICES = (('','Choose..'),('Groundwater','Groundwater'),('Surface water','Surface water'),('Rainwater','Rainwater'),)

WATER_APPLICATION_CHOICES = (
        ('','Choose..'),
        ('Bucket','Bucket'),('Watering Can','Watering Can'),('Tank and hose','Tank and hose'),
        ('Furrow/bed','Furrow/bed'),('Sprinkler','Sprinkler'),('Drip','Drip'),
        ('Micro-basin','Micro-basin'),('Flood','Flood'),('UDS drip (Ghana)','UDS drip (Ghana)')
    )
PUMPING_SOURCE_CHOICES =(
        ('','Choose..'),('River','River'),('Lake','Lake'),('Reservoir','Reservoir'),('well','Well'),
    )
WATER_MANAGEMENT_METHOD_CHOICES = (
        ('','Choose..'),('Farmers practice','Farmers practice'),('TDR(soil moisture)','TDR(soil moisture)'),('WFD','WFD'),
        ('Cropwat','Cropwat'),('WFD WUA','WFD WUA'),
    )
SOIL_MOISTURE_CHOICES=(
        ('','Choose..'),('gravimetric','gravimetric'),('TDR','TDR'),
        ('Soil moisture profiler','Soil moisture profiler'),('Other','Other, please specify')
    )
TECHNOLOGY_CHOICES=(
        ('','Choose..'),('Rope and washer','Rope and washer'),
        ('petrol motorized pump','Petrol motorized pump'),('solar pump','Solar pump'),
        ('tractor mounted pump','Tractor mounted pump'),
        ('Pulley','Pulley'),
        ('Diesel motorized pump','Diesel motorized pump')
        #('','Choose..'),('Pulley','Pulley'),('Pulley with tank','Pulley with tank'),('Rope and washer','Rope and washer'),
        #('Rope and washer with hose','Rope and washer with hose'),('Diesel motorized pump','Diesel motorized pump'),('Solar pump','Solar pump'),
        #('Drip','Drip'),('drip+mounted motorized pump','drip+mounted motorized pump'),('UDS drip (Ghana)','UDS drip (Ghana)')
    )

FIELD_TYPE_CHOICES=(
        ('','choose...'),
        ('FP','Farmer plot'),
        ('PG','Pocket garden'),
        ('RP','Research plot')
)

PLANTING_METHOD_CHOICES=(
        ('','choose...'),
        ('direct seeding','Direct seeding'),
        ('transplanting','Transplanting'),
        #('RP','Research plot')
)
CROP_VARIETY_CHOICES=(
        ('','Choose..'),
        ('Local variety','Local variety'),
        ('Hybrid variety','Hybrid variety')
)

MULCHING_CHOICES =(
        ('','Choose..'),
        ('No mulching','No mulching'),
        ('Mulching','Mulching')
)

class PlantingMethodForm(forms.Form):
        farmer =  forms.ModelChoiceField(queryset = People.objects.all(),widget=Select(attrs={'class': 'form-control seleckpicker'}),empty_label="Select Farmer")
        plotID =  forms.ModelChoiceField(queryset = Plot.objects.all(),widget=Select(attrs={'disabled':'True','class': 'form-control seleckpicker'}),empty_label="Choose Plot")
        #planting_method = forms.ChoiceField(choices = PLANTING_METHOD_CHOICES, widget=forms.Select(attrs={'disabled':'True','class': 'form-control seleckpicker'}))  
        transplanting_date_one = forms.DateField(widget=forms.TextInput(attrs={'placeholder': '#transplanting date','class':'form-control'}))
        transplanting_date_two = forms.DateField(widget=forms.TextInput(attrs={'placeholder': '#transplanting date','class':'form-control'}))
        #nursery_query = Nursery.objects.values_list('NurseryID', flat=True).distinct()
        #nursery_query_choices = [('', 'Choose nursery')] + [(nurseryID, nurseryID) for nurseryID in nursery_query]
        #nurseryID_one = forms.ChoiceField(nursery_query_choices,required=False, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        #nurseryID_two = forms.ChoiceField(nursery_query_choices,required=False, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        nurseryID_one = forms.ModelChoiceField(queryset = Nursery.objects.all(),required=False,widget=Select(attrs={'class': 'form-control seleckpicker'}),empty_label="Choose nursery")
        nurseryID_two = forms.ModelChoiceField(queryset = Nursery.objects.all(),required=False,widget=Select(attrs={'class': 'form-control seleckpicker'}),empty_label="Choose nursery")       
        seeding_date = forms.DateField(widget=forms.TextInput(attrs={'placeholder': '#seeding date','class':'form-control'}))
        seed_quantity = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#seed rate','class':'form-control'}))
        seeding_date2 = forms.DateField(widget=forms.TextInput(attrs={'placeholder': '#seeding date','class':'form-control'}))
        seed_quantity2 = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#seed rate','class':'form-control'}))      
        number_of_plants_per_row = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '#seed/plant per row','class':'form-control'}))
        spacing_within_a_row = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#spacing within a row','class':'form-control'}))
        spacing_btn_a_row = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#seed spacing btn a row','class':'form-control'}))      
        number_of_plants_per_row_two= forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '#seed/plant per row','class':'form-control'}))
        spacing_within_a_row_two = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#spacing within a row','class':'form-control'}))      
        labour  = forms.ChoiceField(choices = LABOUR_CHOICES, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        hired_female_number = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder':'#hired females','class':'form-control','required':'False'}))
        hired_male_number = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '#hired males','class':'form-control','required':'False'}))
        family_female_number = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '#family females','class':'form-control','required':'False'}))
        family_male_number = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '#family males','class':'form-control','required':'False'}))
        #labour_time_taken = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#time taken','class':'form-control','required':'False'}))
        total_plants = forms.CharField(widget=forms.TextInput(attrs={'readonly':'True','placeholder': '#total plants','class':'form-control','required':'False'}))
        total_seed_quantity = forms.IntegerField(widget=forms.TextInput(attrs={'readonly':'True','placeholder': '#total seed quantity','class':'form-control','required':'False'})) 
        wage = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#wage price','class':'form-control'}))
        #currency = forms.ChoiceField(choices = CURRENCY_CHOICES, widget=forms.Select(attrs={'class': 'seleckpicker'}))
        ######
        family_female_time = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#time taken','class':'form-control','required':'False'}))
        family_male_time = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#time taken','class':'form-control','required':'False'}))
        hired_female_time = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#time taken','class':'form-control','required':'False'}))
        hired_male_time = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#time taken','class':'form-control','required':'False'}))
        
        CroppingSystem = forms.CharField(widget=forms.HiddenInput(attrs={'readonly':'True','class':'form-control'}),max_length=30)
        crop1_plantingMethod = forms.CharField(widget=forms.HiddenInput(attrs={'readonly':'True','class':'form-control'}),max_length=30)
        crop2_plantingMethod = forms.CharField(widget=forms.HiddenInput(attrs={'readonly':'True','class':'form-control'}),max_length=30)
        
CROPPING_SYSTEM_CHOICES = (
        ('','Choose..'),
        ('Monocropping','Monocropping '),
        ('Intercropping','Intercropping')
)

PLOT_OWNERSHIP_CHOICE_SELECT = (
    ('','Choose...'),
    ('Owned','Owned'),
    ('Rented','Rented'),
)
PAYMENT_CHOICES = (
        (' ', 'Choose'),
        ('Monetary','Monetary'),
        ('Other','Other'),
)
LATITUDE_DIRECTION_CHOICES = (
    ('','Choose...'),
    ('North','North'),
    ('South','South'),
)

LONGITUDE_DIRECTION_CHOICES = (
    ('','Choose...'),
    ('East','East'),
    ('West','West'),
)


FIELDTYPE_CHOICES = (
    ('','Choose...'),
    ('Farm','Farm'),
    ('Pocket garden','Pocket garden'),
    ('Conventional plot','Conventional plot'),
)
class FarmInfoForm(forms.Form):
        #date = forms.DateField(widget=forms.TextInput(attrs={'placeholder': '#date','class':'form-control'}))
        farmer =  forms.ModelChoiceField(queryset = People.objects.all(),widget=Select(attrs={'class': 'form-control seleckpicker'}),empty_label="Select Farmer")
        plotID = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '#FieldID','class':'form-control'}),max_length=40)
        fieldtype = forms.ChoiceField(choices =FIELDTYPE_CHOICES, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        
        #nurseryID = forms.ModelChoiceField(queryset = Nursery.objects.all(),widget=Select(attrs={'disabled':'True','class': 'form-control seleckpicker'}),empty_label="Choose nursery")
        ######
        farm_ownership_status = forms.CharField(widget=forms.TextInput(attrs={'readonly':'True','class':'form-control'}),max_length=30)
        landownership = forms.ChoiceField(choices =PLOT_OWNERSHIP_CHOICE_SELECT, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        
        field_latitude_degree = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#degree','class':'form-control'}))
        field_latitude_minute = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#minute','class':'form-control'}))
        field_latitude_second = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#second','class':'form-control'}))
        field_latitude_direction = forms.ChoiceField(choices =LATITUDE_DIRECTION_CHOICES, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        
        field_longitude_degree = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#degree','class':'form-control'}))
        field_longitude_minute = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#minute','class':'form-control'}))
        field_longitude_second = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#second','class':'form-control'}))
        field_longitude_direction = forms.ChoiceField(choices =LONGITUDE_DIRECTION_CHOICES, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        
        #crop = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '#crop','class':'form-control'}))
        
        cropping_system = forms.ChoiceField(choices = CROPPING_SYSTEM_CHOICES, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        
        crop1 = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '#first crop','class':'form-control'}))
        crop_variety1 = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '#crop variety','class':'form-control'}))
        variety_type1 = forms.ChoiceField(choices = CROP_VARIETY_CHOICES, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        crop1_planting_method = forms.ChoiceField(choices = PLANTING_METHOD_CHOICES, widget=forms.Select(attrs={'class': 'form-control seleckpicker'})) 
        crop1_rootdepth = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#Rootzone depth assumed','class':'form-control'}))
        crop1_management_practice = forms.ChoiceField(choices = MULCHING_CHOICES, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        crop1_mulching_type = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '#mulching type','class':'form-control','required':'False'}))
        crop1_mulching_quantity = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '#mulching quantity','class':'form-control','required':'False'}))
        
        crop2 = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '#second crop','class':'form-control'}))
        crop_variety2 = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '#crop variety','class':'form-control'}))
        variety_type2 = forms.ChoiceField(choices = CROP_VARIETY_CHOICES, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        crop2_planting_method = forms.ChoiceField(choices = PLANTING_METHOD_CHOICES, widget=forms.Select(attrs={'class': 'form-control seleckpicker'})) 
        crop2_rootdepth = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#Rootzone depth assumed','class':'form-control'}))
        crop2_management_practice = forms.ChoiceField(choices = MULCHING_CHOICES, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        crop2_mulching_type = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '#mulching type','class':'form-control','required':'False'}))
        crop2_mulching_quantity = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '#mulching quantity','class':'form-control','required':'False'}))
        
        fieldsize = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#field size','class':'form-control'}))
        water_application = forms.ChoiceField(choices = WATER_APPLICATION_CHOICES, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        water_management_method = forms.ChoiceField(choices = WATER_MANAGEMENT_METHOD_CHOICES, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        #seed_date = forms.DateField(widget=forms.TextInput(attrs={'placeholder': '#seeding date','class':'form-control'}))
        bed_length = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#bed length','class':'form-control'}))
        bed_width = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#bed width','class':'form-control'}))
        bednumber = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '#bed number','class':'form-control'}))
        ##
        furrow_length = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#furrow length','class':'form-control'}))
        furrow_width = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#furrow width','class':'form-control'}))
        nfurrow  = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '#number of furrow','class':'form-control'}))
        WFD_yellow_depth = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#WFD yellow depth','class':'form-control'}))
        WFD_red_depth = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#WFD red depth','class':'form-control'}))
        TDR_length = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#TDR_length','class':'form-control'}))
        elevation = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#elevation','class':'form-control'}))
        seasonstart = forms.DateField(widget=forms.TextInput(attrs={'placeholder': '#season start','class':'form-control'}))
        
        lease_duration = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#lease duration','class':'form-control'}))
        payment_option  = forms.ChoiceField(choices = PAYMENT_CHOICES, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        payement_other = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'placeholder': '#other payment method','class':'form-control'}))
        payment_monetary = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#monetary','class':'form-control'}))
        
        #currency = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','required':'False'}))
        #management_practice = forms.ChoiceField(choices = MULCHING_CHOICES, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        #mulching_type = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '#mulching type','class':'form-control','required':'False'}))
        #mulching_quantity = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '#mulching quantity','class':'form-control','required':'False'}))


class NurseryForm(forms.Form):
        date = forms.DateField(widget=forms.TextInput(attrs={'placeholder': '#date','class':'datepicker form-control'})) 
        nurseryID  = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '#NurseryID','class':'form-control'}),max_length=25)
        area = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#nursery area','class':'form-control'}))
        farm = forms.ModelChoiceField(queryset = People.objects.all(),widget=Select(attrs={'class': 'form-control seleckpicker'}),empty_label="Choose farm")
        date_bed_preparation = forms.DateField(widget=forms.TextInput(attrs={'placeholder': '#bed preparation date','class':'datepicker form-control'})) 
        seedprice  = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#seed price','class':'form-control'}))
        #= forms.DateField(widget=forms.TextInput(attrs={'placeholder': '#seedprice','class':'form-control'})) 
        bed_length = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#bed length','class':'form-control'}))
        bed_width = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#bed width','class':'form-control'}))
        bednumber = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '#bed number','class':'form-control'}))    
        seeding_date = forms.DateField(widget=forms.TextInput(attrs={'placeholder': '#seeding date','class':'datepicker form-control'})) 
        seed_per_bed = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#seed per bed','class':'form-control'})) 
        seedtype = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '#seedtype','class':'form-control','required':'False'}))
        #seedtype = forms.ModelChoiceField(queryset = Seed.objects.all(),widget=Select(attrs={'class': 'form-control seleckpicker'}),empty_label="Choose seed")
        labour  = forms.ChoiceField(choices = LABOUR_CHOICES, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        hired_female_number = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder':'#hired females','class':'form-control','required':'False'}))
        hired_male_number = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '#hired males','class':'form-control','required':'False'}))
        family_female_number = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '#family females','class':'form-control','required':'False'}))
        family_male_number = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '#family males','class':'form-control','required':'False'}))
        #labour_time_taken = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#time taken','class':'form-control','required':'False'}))
        wage = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#wage price','class':'form-control'}))
        #currency = forms.ChoiceField(choices = CURRENCY_CHOICES, widget=forms.Select(attrs={'class': 'seleckpicker'}))
        #seedrate = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#seedrate','class':'form-control'}))
        seed_spacing_within_a_bed = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#seed spacing within a bed','class':'form-control'}))
        seed_spacing_btn_bed = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#seed spacing btn bed','class':'form-control'}))
        quantity = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#quantity','class':'form-control'}))
        family_female_time = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#time taken','class':'form-control','required':'False'}))
        family_male_time = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#time taken','class':'form-control','required':'False'}))
        hired_female_time = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#time taken','class':'form-control','required':'False'}))
        hired_male_time = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#time taken','class':'form-control','required':'False'}))
        
        
class TransplantingForm(forms.Form):
        farm = forms.ModelChoiceField(queryset = People.objects.all(),widget=Select(attrs={'class': 'form-control seleckpicker'}),empty_label="Choose farm")
        plot =  forms.ModelChoiceField(queryset = Plot.objects.all(),widget=Select(attrs={'class': 'form-control seleckpicker'}),empty_label="Choose Plot")
        nurseryID = forms.ModelChoiceField(queryset = Nursery.objects.all(),widget=Select(attrs={'disabled':'True','class': 'form-control seleckpicker'}),empty_label="Choose nursery")
        #seedprice  = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#seed price','class':'form-control'}))
        #= forms.DateField(widget=forms.TextInput(attrs={'placeholder': '#seedprice','class':'form-control'}))
        trasplanting_date = forms.DateField(widget=forms.TextInput(attrs={'placeholder': '#trasplanting date','class':'form-control'}))
        plants_transplanted  = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#number of plants transplanted','class':'form-control'}))
        number_of_plants_per_row= forms.ModelChoiceField(queryset = Technology.objects.all(),widget=Select(attrs={'class': 'form-control seleckpicker'}),empty_label="Choose Technology")
        plant_spacing_btn_plants_within_rows = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#plant spacing btn plants within rows','class':'form-control'}))
        plant_spacing_btn_rows = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#plant spacing btn rows','class':'form-control'}))
        labour  = forms.ChoiceField(choices = LABOUR_CHOICES, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        hired_female_number = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder':'#hired females','class':'form-control','required':'False'}))
        hired_male_number = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '#hired males','class':'form-control','required':'False'}))
        family_female_number = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '#family females','class':'form-control','required':'False'}))
        family_male_number = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '#family males','class':'form-control','required':'False'}))
        wage = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#wage price','class':'form-control'}))
        currency = forms.ChoiceField(choices = CURRENCY_CHOICES, widget=forms.Select(attrs={'class': 'seleckpicker'}))
        number_of_plants_per_row = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#wage price','class':'form-control'}))
        

class NurseryIrrigationForm(forms.Form):
        date = forms.DateField(widget=forms.TextInput(attrs={'placeholder': '#nursery irrigation date','class':'form-control'})) 
        climate = forms.ChoiceField(choices =CLIMATE_CHOICES, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        farm = forms.ModelChoiceField(queryset = People.objects.all(),widget=Select(attrs={'class': 'form-control seleckpicker'}),empty_label="Choose farm")
        nurseryID = forms.ModelChoiceField(queryset = Nursery.objects.all(),widget=Select(attrs={'disabled':'True','class': 'form-control seleckpicker'}),empty_label="Choose nursery")
        time_started  = forms.TimeField(widget=forms.TimeInput(attrs={'placeholder': '#time_started','format':'%H:%M:%S','class':'form-control timepicker'}))
        time_ended  = forms.TimeField(widget=forms.TimeInput(attrs={'placeholder': '#time_ended','format':'%H:%M:%S','class':'form-control timepicker'}))
        total_time = forms.FloatField(widget=forms.TextInput(attrs={'readonly':'True','placeholder': '','class':'form-control'}))
        #event = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#event','class':'form-control'}))
        bucket_volume = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#standard_volume','class':'form-control'}))
        bucket_numbers = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#number of buckets','class':'form-control'}))
        total_volume = forms.FloatField(widget=forms.TextInput(attrs={'readonly':'True','placeholder': '','class':'form-control'}))
        #discharge = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#discharge','class':'form-control'}))
        labour  = forms.ChoiceField(choices = LABOUR_CHOICES, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        hired_female_number = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder':'#hired females','class':'form-control','required':'False'}))
        hired_male_number = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '#hired males','class':'form-control','required':'False'}))
        family_female_number = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '#family females','class':'form-control','required':'False'}))
        family_male_number = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '#family males','class':'form-control','required':'False'}))
        irrigation_depth = forms.FloatField(widget=forms.TextInput(attrs={'readonly':'True','placeholder': ' ','class':'form-control','required':'False'}))
        #labour_time_taken = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#time taken','class':'form-control','required':'False'}))
        wage = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#wage price','class':'form-control'}))
        #currency = forms.ChoiceField(choices = CURRENCY_CHOICES, widget=forms.Select(attrs={'class': 'seleckpicker'}))
        family_female_time = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#time taken','class':'form-control','required':'False'}))
        family_male_time = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#time taken','class':'form-control','required':'False'}))
        hired_female_time = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#time taken','class':'form-control','required':'False'}))
        hired_male_time = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#time taken','class':'form-control','required':'False'}))
        
FERTILIZER_TYPES_CHOICES = (
        ('','Choose..'),
        ("farmer's practice","farmer's practice"),
        ("DAP","DAP"),("NPS","NPS"),
        ("DAP-UREA","DAP-UREA"),("UREA","UREA"),("Compost","Compost")
    )

FERTILIZER_MANAGEMENT_CHOICES = (
        ('','Choose..'),
        ("farmer's practice","Farmer's practice"),
        ("scientific experiment","Scientific experiment")
    )

CROP_STAGE_CHOICES = (
        ('','Choose..'),
        ('initial','Initial'),
        ('development','Development'),
        ('flowering','Flowering'),
        ('fruiting','Fruiting'),
        
    )
FORM_CHOICES=(
        ('','Choose..'),
        ('Liquid','Liquid'),
        ('Solid','Solid'),
    )

CHOICES = (
        ('','Choose..'),
        ('Nursery','Nursery'),
        ('Field','Field')
)

class FertilizerApplicationForm(forms.Form):
        date = forms.DateField(widget=forms.TextInput(attrs={'placeholder': '12/02/1989','class':'form-control'})) 
        farm =  forms.ModelChoiceField(queryset = Farm.objects.all(),widget=Select(attrs={'class': 'form-control seleckpicker'}),empty_label="Choose Farm")
        #choice = forms.ChoiceField(choices = CHOICES, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        #nursery  =  forms.ModelChoiceField(queryset = Nursery.objects.all(),widget=Select(attrs={'class': 'form-control seleckpicker'}),empty_label="Choose Plot")
        plot =  forms.ModelChoiceField(queryset = Plot.objects.all(),widget=Select(attrs={'disabled':'True','class': 'form-control seleckpicker'}),empty_label="Choose Plot")
        fertilizer = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '#fertilizer','class':'form-control','required':'False'}))
        fertilizer_management = forms.ChoiceField(choices = FERTILIZER_MANAGEMENT_CHOICES, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        quantity_kg = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#Quantity in Kg','class':'form-control'}))
        crop_stage  = forms.ChoiceField(choices = CROP_STAGE_CHOICES, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        #nitrogen = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#nitrogen','class':'form-control'}))
        #phosphorus = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#phosphorus','class':'form-control'}))
        #potassium = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#potassium','class':'form-control'}))
        #sulphur = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#sulphur','class':'form-control'}))
        #organic_matter = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#organic_matter','class':'form-control'}))
        cost = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#cost','class':'form-control'}))
        labour  = forms.ChoiceField(choices = LABOUR_CHOICES, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        hired_female_number = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder':'#hired females','class':'form-control','required':'False'}))
        hired_male_number = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '#hired males','class':'form-control','required':'False'}))
        family_female_number = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '#family females','class':'form-control','required':'False'}))
        family_male_number = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '#family males','class':'form-control','required':'False'}))
        wage = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#wage price','class':'form-control'}))
        #currency = forms.ChoiceField(choices = CURRENCY_CHOICES, widget=forms.Select(attrs={'class': 'seleckpicker'}))
        #labour_time_taken = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#time taken','class':'form-control','required':'False'}))
        family_female_time = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#time taken','class':'form-control','required':'False'}))
        family_male_time = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#time taken','class':'form-control','required':'False'}))
        hired_female_time = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#time taken','class':'form-control','required':'False'}))
        hired_male_time = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#time taken','class':'form-control','required':'False'}))
        compost_kind = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '#compost kind','class':'form-control','required':'False'}))
        
class PesticideApplicationForm(forms.Form):
        date = forms.DateField(widget=forms.TextInput(attrs={'placeholder': '12/02/1989','class':'form-control'})) 
        farm =  forms.ModelChoiceField(queryset = Farm.objects.all(),widget=Select(attrs={'class': 'form-control seleckpicker'}),empty_label="Choose Farm")
        plot =  forms.ModelChoiceField(queryset = Plot.objects.all(),widget=Select(attrs={'disabled':'True','class': 'form-control seleckpicker'}),empty_label="Choose Plot")
        pesticide = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '#pesticide','class':'form-control'}))
        #forms.ModelChoiceField(queryset = Pesticide.objects.all(),widget=Select(attrs={'class': 'form-control seleckpicker'}),empty_label="Choose..")
        form  = forms.ChoiceField(choices = FORM_CHOICES, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        crop_stage  = forms.ChoiceField(choices = CROP_STAGE_CHOICES, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        quantity_lt = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#Quantity in Litre','class':'form-control'}))
        quantity_kg = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#Quantity in Kg','class':'form-control'}))
        water_volume = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#water volume','class':'form-control'}))
        cost = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#cost','class':'form-control'}))
        #applied_personels =forms.ModelMultipleChoiceField(queryset=People.objects.all(),widget=forms.SelectMultiple(attrs={'class': 'form-control seleckpicker'}),required=True)
        labour  = forms.ChoiceField(choices = LABOUR_CHOICES, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        hired_female_number = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder':'#hired females','class':'form-control','required':'False'}))
        hired_male_number = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '#hired males','class':'form-control','required':'False'}))
        family_female_number = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '#family females','class':'form-control','required':'False'}))
        family_male_number = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '#family males','class':'form-control','required':'False'}))
        wage = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#wage price','class':'form-control'}))
        #currency = forms.ChoiceField(choices = CURRENCY_CHOICES, widget=forms.Select(attrs={'class': 'seleckpicker'}))
        #labour_time_taken = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#time taken','class':'form-control','required':'False'}))
        family_female_time = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#time taken','class':'form-control','required':'False'}))
        family_male_time = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#time taken','class':'form-control','required':'False'}))
        hired_female_time = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#time taken','class':'form-control','required':'False'}))
        hired_male_time = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#time taken','class':'form-control','required':'False'}))
GENDER_CHOICE=(
        ('','Choose gender..'),
        ('M','Male'),
        ('F','Female'), 
    )#widget=forms.widgets.DateInput(format="%m/%d/%Y"))
       
AGE_GROUP_CHOICES=(
        ('','Choose..'),
        ('Youth (<18)','Youth (<18)'),
        ('Youth (>18)','Youth (>18)')
)      
class WaterLiftingCalibrationForm(forms.Form):
        date = forms.DateField(widget=forms.TextInput(attrs={'placeholder': '12/02/1989','class':'form-control'})) 
        farm = forms.ModelChoiceField(queryset = Farm.objects.all(),widget=Select(attrs={'class': 'form-control seleckpicker'}),empty_label="Choose Farm")
        #plot = forms.ModelChoiceField(queryset = Plot.objects.all(),widget=Select(attrs={'Disabled':'True','class': 'form-control seleckpicker'}),empty_label="Choose Plot")
        technology = forms.CharField(widget=forms.TextInput(attrs={'readonly':'True','placeholder': '#technology','class':'form-control'}))
        #repetition = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '#repetition','class':'form-control'}))
        bucketvolume = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#bucketvolume','class':'form-control'}))
        start_time = forms.TimeField(widget=forms.TimeInput(attrs={'placeholder': '#start time','format':'%H:%M','class':'form-control timepicker'}))
        end_time  = forms.TimeField(widget=forms.TimeInput(attrs={'placeholder': '#end time','format':'%H:%M','class':'form-control timepicker'}))
        waterlevel = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#water level','class':'form-control'}),required=False)
        #forms.TimeField(widget=forms.TimeInput(format='%H:%M'))
        #forms.TimeField(widget=forms.TimeInput(format='%H:%M'))
        total_time  = forms.FloatField(widget=forms.TextInput(attrs={'readonly': 'True','class':'form-control'}))
        discharge = forms.FloatField(widget=forms.TextInput(attrs={'readonly': 'True','placeholder': '','class':'form-control'}))   
        gender = forms.ChoiceField(choices = GENDER_CHOICE, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        age_group = forms.ChoiceField(choices = AGE_GROUP_CHOICES, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        

conveyance_efficiency_range = range(60, 71, 5)    
CONVEYANCE_EFFICIENCY_CHOICES = [('','choose conveyance efficiency')] + [ (i,i) for i in conveyance_efficiency_range ]

field_efficiency_range = range(60,81, 5)
FIELD_EFFICIENCY_CHOICES = [('','choose field efficiency')] + [ (i,i) for i in field_efficiency_range ]

CALIBRATION_METHOD_CHOICE=(
        ('','Choose..'),
        ('Calibration cup','Calibration cup'),
        ('Full field tanker','Full field tanker')
)

class ApplicationCalibrationForm(forms.Form):
        date = forms.DateField(widget=forms.TextInput(attrs={'placeholder': '12/02/1989','class':'form-control'})) 
        farm = forms.ModelChoiceField(queryset = Farm.objects.all(),widget=Select(attrs={'class': 'form-control seleckpicker'}),empty_label="Choose Farm")
        plot = forms.ModelChoiceField(queryset = Plot.objects.all(),widget=Select(attrs={'Disabled':'True','class': 'form-control seleckpicker'}),empty_label="Choose Plot")
        water_application = forms.CharField(widget=forms.TextInput(attrs={'readonly':'True','placeholder': '','class':'form-control'}))
        bucketdiameter = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#bucketdiameter','class':'form-control'}))
        bucketvolume = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#bucketvolume','class':'form-control'}))
        start_time = forms.TimeField(widget=forms.TimeInput(attrs={'placeholder': '#start time','format':'%H:%M','class':'form-control timepicker'}))
        end_time  = forms.TimeField(widget=forms.TimeInput(attrs={'placeholder': '#end time','format':'%H:%M','class':'form-control timepicker'}))
        total_time  = forms.FloatField(widget=forms.TextInput(attrs={'readonly':'True','placeholder': '#total time','class':'form-control'}))
        discharge = forms.FloatField(widget=forms.TextInput(attrs={'readonly':'True','placeholder': '#application rate','class':'form-control'}))   
        bucketnumbers = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '#Integer','class':'form-control'})) 
        waterheight = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#waterheight','class':'form-control'}))
        topfurrowwidth = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#topfurrowwidth','class':'form-control'}))
        buttonfurrowwidth = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#buttonfurrowwidth','class':'form-control'}))
        wetteddiameteraroundplant = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#wetteddiameteraroundplant','class':'form-control'}))
        irrigate_whole_or_per_plant  = forms.ChoiceField(choices = IRRIGATE_WHOLE_OR_PER_PLANT_CHOICES, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        field_efficiency = forms.ChoiceField(choices = FIELD_EFFICIENCY_CHOICES , widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        conveyance_efficiency = forms.ChoiceField(choices = CONVEYANCE_EFFICIENCY_CHOICES, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        dripline_numbers = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '#number of drip lines','class':'form-control'}))
        dripline_length = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#dripline length','class':'form-control'}))
        dripline_spacing = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#dripline spacing','class':'form-control'}))
        emitter_spacing = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#emitter spacing','class':'form-control'}))
        driptank_volume = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#drip tank volume','class':'form-control'}))
        calibrationcup_volume = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#calibration cup volume','class':'form-control'}))
        emitter_wetted_diameter = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#emitter wetted diameter','class':'form-control'}))
        calibration_method = forms.ChoiceField(choices = CALIBRATION_METHOD_CHOICE, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        calibration_cup_time = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#calibration cup time','class':'form-control'}))
        tankvolume = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#tank volume','class':'form-control'}))
        #tanknumber = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#tank number','class':'form-control'}))
        #tankdiameter = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#tank diameter','class':'form-control'}))
        
WFD_IRRIGATION_CHOICES =(
        ('','Choose...'),
        ('Yes','Yes'),
        ('No','No'),
)


ANY_SERVICE_PROVIDER = (
        ('','Choose..'),
        ('Yes','Yes'),
        ('No','No')       
        )

class FarmIrrigationForm(forms.Form):
        date = forms.DateField(widget=forms.DateInput(attrs={'input_formats':['%d-%m-%Y'],'placeholder': '15/02/1989','class':'form-control'})) 
        farm = forms.ModelChoiceField(queryset = Farm.objects.all(),widget=Select(attrs={'class': 'form-control seleckpicker'}),empty_label="Choose Farm")
        plot = forms.ModelChoiceField(queryset = Plot.objects.all(),widget=Select(attrs={'Disabled':'True','class': 'form-control seleckpicker'}),empty_label="Choose Plot")      
        start_time = forms.TimeField(widget=forms.TimeInput(attrs={'placeholder': '#start time','class':'form-control timepicker'}))
        end_time  = forms.TimeField(widget=forms.TimeInput(attrs={'placeholder': '#end time','class':'form-control timepicker'}))
        
        service_provider = forms.ChoiceField(choices = ANY_SERVICE_PROVIDER, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        #quantification_method = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '#Quantification method','class':'form-control'}),max_length=30)
        #flume_location  = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '#Flume location','class':'form-control'}),max_length=30)
        #waterlevel1 = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#water level 1','class':'form-control'})) 
        #waterlevel2 = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#water level 1','class':'form-control'}))
        furrow_irr_time = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#furrow irrigation time','class':'form-control'})) 
        nfurrorws_irrigated_once = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '#furrow numbers','class':'form-control'}))
        discharge = forms.FloatField(widget=forms.TextInput(attrs={'readonly':'True','placeholder': '#application rate','class':'form-control'}))
        #quantity_of_units  = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#quantity of units','class':'form-control'}))
        yellow_WFD_before_irrigation  = forms.ChoiceField(choices = WFD_IRRIGATION_CHOICES, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        red_WFD_before_irrigation = forms.ChoiceField(choices = WFD_IRRIGATION_CHOICES, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        yellow_WFD_time_after_irrigation  = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#yellow WFD time after irrigation','class':'form-control'})) 
        red_WFD_time_after_irrigation = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#red WFD time after irrigation','class':'form-control'}))
        climate   = forms.ChoiceField(choices =CLIMATE_CHOICES, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        fuel = forms.ModelChoiceField(queryset = Fuel.objects.all(),widget=Select(attrs={'class': 'form-control seleckpicker'}),empty_label="Choose Fuel")
        fuelcost = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#fuel cost','class':'form-control'}))
        #currency = forms.ChoiceField(choices = CURRENCY_CHOICES, widget=forms.Select(attrs={'class': 'seleckpicker'}))
        amount_used  = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#amount used','class':'form-control'}))
        refilled_amount  = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#refilled amount','class':'form-control'}))
        water_application = forms.CharField(widget=forms.TextInput(attrs={'readonly':'True','placeholder': '#water_application','class':'form-control'}),max_length=30)
        irrigate_whole_or_per_plant  = forms.ChoiceField(choices = IRRIGATE_WHOLE_OR_PER_PLANT_CHOICES, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        water_management = forms.CharField(widget=forms.HiddenInput(attrs={'readonly':'True','class':'form-control'}),max_length=30)
        buttonfurrowwidth = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#buttonfurrowwidth','class':'form-control'}))
        topfurrowwidth = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#topfurrowwidth','class':'form-control'}))
        waterheight = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#waterheight','class':'form-control'}))
        #bucketdiameter = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#bucketdiameter','class':'form-control'}))
        bucketvolume = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#bucketvolume','class':'form-control'}))
        bucketnumbers = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '#number of bucket(s)','class':'form-control'})) 
        wetteddiameteraroundplant = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#wetteddiameteraroundplant','class':'form-control'}))
        total_time  = forms.FloatField(widget=forms.TextInput(attrs={'readonly':'True','placeholder': '#total time','class':'form-control'}))
        field_efficiency = forms.ChoiceField(choices = FIELD_EFFICIENCY_CHOICES , widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        conveyance_efficiency = forms.ChoiceField(choices = CONVEYANCE_EFFICIENCY_CHOICES, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        #dripline_length = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#dripline length','class':'form-control'}))
        #dripline_spacing = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#dripline spacing','class':'form-control'}))
        #emitter_spacing = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#emitter spacing','class':'form-control'}))
        driptank_volume = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#drip tank volume','class':'form-control'}))
        #calibrationcup_volume = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#calibration cup volume','class':'form-control'}))
        #emitter_wetted_diameter = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#emitter wetted diameter','class':'form-control'}))
        irrigation_depth = forms.FloatField(widget=forms.TextInput(attrs={'readonly':'True','placeholder': '#irrigation depth','class':'form-control'}))
        tanknumber = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '#number of tanks','class':'form-control'}))
        gender  = forms.ChoiceField(choices = GENDER_CHOICE, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        distance_from_water_source = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#distance from water source','class':'form-control'}))
        time_to_fetch_water = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#time to fetch water','class':'form-control'}))
        technology = forms.CharField(widget=forms.TextInput(attrs={'readonly':'True','placeholder': 'technology','class':'form-control'}))
        #forms.CharField(widget=forms.HiddenInput(attrs={'class':'form-control'}))
        water_level_bf_filling = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#water level before filling','class':'form-control','required':'False'}))
        water_level_aftr_filling = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#water level after filling','class':'form-control','required':'False'}))
        time_to_fill_water_tank = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#time to fill water tank','class':'form-control','required':'False'}))
        
        labour  = forms.ChoiceField(choices = LABOUR_CHOICES, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        hired_female_number = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder':'#number of hired female','class':'form-control','required':'False'}))
        hired_male_number = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '#number of hired male','class':'form-control','required':'False'}))
        family_female_number = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '#number of family female','class':'form-control','required':'False'}))
        family_male_number = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '#number of family male','class':'form-control','required':'False'}))
        wage =  forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#payment','class':'form-control'}))
        family_female_time = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#time taken','class':'form-control','required':'False'}))
        family_male_time = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#time taken','class':'form-control','required':'False'}))
        hired_female_time = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#time taken','class':'form-control','required':'False'}))
        hired_male_time = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#time taken','class':'form-control','required':'False'}))
        
        
class SoilForm(forms.Form):
        date = forms.DateField(widget=forms.TextInput(attrs={'placeholder': '12/02/1989','class':'form-control'}))
        farm =  forms.ModelChoiceField(queryset = Farm.objects.all(),widget=Select(attrs={'class': 'form-control seleckpicker'}),empty_label="Choose Farm")
        plot =  forms.ModelChoiceField(queryset = Plot.objects.all(),widget=Select(attrs={'disabled':'True','class': 'form-control seleckpicker'}),empty_label="Choose Plot")
        soilclass = forms.ModelChoiceField(queryset = Soil.objects.all(),widget=Select(attrs={'class': 'form-control seleckpicker'}),empty_label="Choose Soil class")
        pH = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#soil pH','class':'form-control'}))
        ec = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#Electrical conductivity','class':'form-control'}))
        sand = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#Sand','class':'form-control'}))
        clay = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#Clay','class':'form-control'}))
        silt = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#Silt','class':'form-control'}))
        cec = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#CEC','class':'form-control'}))
        om = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#om','class':'form-control'}))
        tn = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#tn','class':'form-control'}))
        av_p = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#av_p','class':'form-control'}))
        fe = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#fe','class':'form-control'}))
        fc = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#fc','class':'form-control'}))
        pwp = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#pwp','class':'form-control'}))
        k = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#k','class':'form-control'}))
        bulkdensity = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#bulkdensity','class':'form-control'}))
        zn = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#zn','class':'form-control'}))
        se = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#se','class':'form-control'}))
        ca = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#ca','class':'form-control'}))
        s = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#s','class':'form-control'}))
        mg = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#mg','class':'form-control'}))
        na = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#na','class':'form-control'}))
        soil_depth = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#soil_depth','class':'form-control'}))

SOIL_MOISTURE_CHOICES=(
        ('','Choose..'),('gravimetric','Gravimetric'),('TDR','TDR'),('SoilMoistureProfiler','SoilMoistureProfiler')
        #('Soil moisture profiler','Soil moisture profiler'),('Other','Other, please specify')
    )

class SoilMoistureMeasurementForm(forms.Form):
        measurement_option  = forms.ChoiceField(choices = SOIL_MOISTURE_CHOICES, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        date = forms.DateField(widget=forms.TextInput(attrs={'placeholder': '12/02/1989','class':'form-control'}))
        farm =  forms.ModelChoiceField(queryset = Farm.objects.all(),widget=Select(attrs={'class': 'form-control seleckpicker'}),empty_label="Choose Farm")
        plot =  forms.ModelChoiceField(queryset = Plot.objects.all(),widget=Select(attrs={'disabled':'True','class': 'form-control seleckpicker'}),empty_label="Choose Plot")
        ##event = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '#event number','class':'form-control'}))
        measurement_one = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#First tdr measurement','class':'form-control'}))
        measurement_two = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#Second tdr measurement','class':'form-control'}))
        measurement_three = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#Third tdr measurement','class':'form-control'}))
        measurement_four = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#Fourth tdr measurement','class':'form-control'}))
        measurement_five = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#Fifth tdr measurement','class':'form-control'}))
        measurement_six = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#Sixth tdr measurement','class':'form-control'}))
        measurement_seven = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#Seventh tdr measurement','class':'form-control'}))
        measurement_eigth = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#Eighth tdr measurement','class':'form-control'}))
        measurement_nine = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#Ninth tdr measurement','class':'form-control'}))
        measurement_ten = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#Tenth tdr measurement','class':'form-control'}))
        measurement_depth = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#depth of measurement','class':'form-control'}))
        time  = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#time taken','class':'form-control'}))
        depth_sample  = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#Depth sample','class':'form-control'}))
        volume_core_used  = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#volume core used','class':'form-control'}))
        weight_core_used = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#weight core used','class':'form-control'}))
        wet_weight = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#wet weight','class':'form-control'}))
        dry_weight = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#dry weight','class':'form-control'}))
        bulk_density = forms.FloatField(widget=forms.TextInput(attrs={'readonly':'True','placeholder': '#bulk density','class':'form-control'}))
        gravimetric_moisture_content = forms.FloatField(widget=forms.TextInput(attrs={'readonly':'True','placeholder': '#gravimetric moisture content','class':'form-control'}))
        volumetric_moisture_content = forms.FloatField(widget=forms.TextInput(attrs={'readonly':'True','placeholder': '#volumetric moisture content','class':'form-control'}))
        depth_10 = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#depth','class':'form-control'}))
        depth_20 = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#depth','class':'form-control'}))
        depth_30 = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#depth','class':'form-control'}))
        depth_40 = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#depth','class':'form-control'}))
        depth_60 = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#depth','class':'form-control'}))
        depth_100 = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#depth','class':'form-control'}))
        
PLANT_TISSUE_PART_CHOICES=(
        ('','Choose..'), ('leaf','Leaf'),
        ('stem','Stem'),('roots','Fruit'),
)

PLANT_NUMBER_CHOICES=(
        ('','Choose...'),
        (1,'One'),
        (2,'Two'),
        (3,'Three'),
)

BED_NUMBER_CHOICES=(
        ('','Choose...'),
        (1,1),
        (2,2),
        (3,3),
)

ROW_NUMBER_CHOICES=(
        ('','Choose...'),
        (1,'One'),
        (2,'Two'),
        (3,'Three'),
        (4,'Four'),
        (5,'Five')
)

class TissueNutrientAnalysisForm(forms.Form):
        date = forms.DateField(widget=forms.TextInput(attrs={'placeholder': '12/02/1989','class':'form-control'}))
        farm =  forms.ModelChoiceField(queryset = Farm.objects.all(),widget=Select(attrs={'class': 'form-control seleckpicker'}),empty_label="Choose Farm")
        plot =  forms.ModelChoiceField(queryset = Plot.objects.all(),widget=Select(attrs={'disabled':'True','class': 'form-control seleckpicker'}),empty_label="Choose Plot")
        Crop =  forms.ModelChoiceField(queryset = Crop.objects.all(),widget=Select(attrs={'class': 'form-control seleckpicker'}),empty_label="Choose Crop..")
        plant_tissue_part = forms.ChoiceField(choices = PLANT_TISSUE_PART_CHOICES, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        plant_number= forms.ChoiceField(choices =PLANT_NUMBER_CHOICES, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        bed_number= forms.ChoiceField(choices = BED_NUMBER_CHOICES, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        fresh_weight = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#fresh weight','class':'form-control'}))
        dry_weight = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#dry weight','class':'form-control'}))
        n = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#nitrogen','class':'form-control'}))
        p = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#phosphorus','class':'form-control'}))
        k = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#potassium','class':'form-control'}))
        s = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#sulphur','class':'form-control'}))
        mg = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#magnesium','class':'form-control'}))
        ca = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#calcium','class':'form-control'}))
        fe = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#iron','class':'form-control'}))
        zn = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#zinc','class':'form-control'}))


class TechnologyFailureForm(forms.Form):
        date = forms.DateField(widget=forms.TextInput(attrs={'placeholder': '12/02/1989','class':'form-control'}))
        farm =  forms.ModelChoiceField(queryset = Farm.objects.all(),widget=Select(attrs={'class': 'form-control seleckpicker'}),empty_label="Choose Farm")
        technology = forms.CharField(widget=forms.TextInput(attrs={'readonly':'True','placeholder': '#technology','class':'form-control'}))
        reason = forms.CharField(widget=forms.Textarea(attrs={'placeholder': '#write down reason(s) for failure','class':'form-control'}))


class HorizRadioRenderer(forms.RadioSelect.renderer):
    """ this overrides widget method to put radio buttons horizontally
        instead of vertically.
    """
    def render(self):
            """Outputs radios"""
            return mark_safe(u'\n'.join([u'%s\n' % w for w in self]))
        
class FarmYieldLevelForm(forms.Form):
        date = forms.DateField(widget=forms.TextInput(attrs={'placeholder': '12/02/1989','class':'form-control'}))
        farm =  forms.ModelChoiceField(queryset = Farm.objects.all(),widget=Select(attrs={'class': 'form-control seleckpicker'}),empty_label="Choose Farm")
        #area = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#area','class':'form-control'}))
        plot =  forms.ModelChoiceField(queryset = Plot.objects.all(),widget=Select(attrs={'disabled':'True','class': 'form-control seleckpicker'}),empty_label="Choose Plot")
        Crop =  forms.ModelChoiceField(queryset = Crop.objects.all(),widget=Select(attrs={'class': 'form-control seleckpicker'}),empty_label="Choose Crop..")
        
        #fresh = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class':'form-control','default':'True'}))
        #dry = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class':'form-control','default':'False'}))
        marketable_yield = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#marketable yield','class':'form-control'}))
        unmarketable_yield = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#unmarketable yield','class':'form-control'}))
        biomas = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#biomas','class':'form-control'}))
        dry_fresh = forms.ChoiceField(choices = DRY_FRESH_CHOICES, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        quantity_harvested = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#quantity harvested','class':'form-control'}))
        #labour_time_taken = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#time taken','class':'form-control','required':'False'}))
        #forms.ChoiceField(required = True, choices = DRY_FRESH_CHOICES, widget=forms.RadioSelect(attrs={'class' : 'radio-inline form-control'}))
        payement =  forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#payement','class':'form-control'}))
        labour  = forms.ChoiceField(choices = LABOUR_CHOICES, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        hired_female_number = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder':'#number of hired female','class':'form-control','required':'False'}))
        hired_male_number = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '#number of hired male','class':'form-control','required':'False'}))
        family_female_number = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '#number of family female','class':'form-control','required':'False'}))
        family_male_number = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '#number of family male','class':'form-control','required':'False'}))
        #currency = forms.ChoiceField(choices = CURRENCY_CHOICES, widget=forms.Select(attrs={'class': 'seleckpicker'}))
        #labour_time_taken = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#time taken','class':'form-control','required':'False'}))
        family_female_time = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#time taken','class':'form-control','required':'False'}))
        family_male_time = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#time taken','class':'form-control','required':'False'}))
        hired_female_time = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#time taken','class':'form-control','required':'False'}))
        hired_male_time = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#time taken','class':'form-control','required':'False'}))
        
    
ROW_CHOICES =(
        ('','Choose...'),
        (1,'One'),
        (2,'Two'),
        (3,'Three')
)

HARVESTING_METHOD_CHOICES=(
        ('','Choose...'),
        ('rowlevel','Row level'),
        ('bedlevel','Bed level')
)



class BedYieldLevelForm(forms.Form):
        date = forms.DateField(widget=forms.TextInput(attrs={'placeholder': '12/02/1989','class':'form-control'}))
        farm =  forms.ModelChoiceField(queryset = Farm.objects.all(),widget=Select(attrs={'class': 'form-control seleckpicker'}),empty_label="Choose Farm")  
        plot  = forms.ModelChoiceField(queryset = Plot.objects.all(),widget=Select(attrs={'disabled':'True','class': 'form-control seleckpicker'}),empty_label="Choose plots")
        Crop =  forms.ModelChoiceField(queryset = Crop.objects.all(),widget=Select(attrs={'class': 'form-control seleckpicker'}),empty_label="Choose Crop..")
        harvesting_method  = forms.ChoiceField(choices = HARVESTING_METHOD_CHOICES, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        dry_fresh = forms.ChoiceField(choices = DRY_FRESH_CHOICES, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        #dry_fresh =  forms.ChoiceField(widget=forms.RadioSelect(attrs={'class' : 'radio-inline form-control'},renderer=HorizRadioRenderer),choices=DRY_FRESH_CHOICES)
        #area = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#area','class':'form-control'}))
        marketable_produce = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '#number of marketable produce','class':'form-control'}))
        unmarketable_produce= forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '#number of unmarketable produce','class':'form-control'}))
        marketable_produce_weight = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#weight of marketable produce','class':'form-control'}))
        unmarketable_produce_weight= forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#weight of unmarketable produce','class':'form-control'}))
        data_row_number = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '#row number','class':'form-control'}))
    
class PlantLevelYieldForm(forms.Form):
        date = forms.DateField(widget=forms.TextInput(attrs={'placeholder': '12/02/1989','class':'form-control'}))
        farm =  forms.ModelChoiceField(queryset = Farm.objects.all(),widget=Select(attrs={'class': 'form-control seleckpicker'}),empty_label="Choose Farm")
        harvesting_method  = forms.ChoiceField(choices = HARVESTING_METHOD_CHOICES, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        dry_fresh = forms.ChoiceField(choices = DRY_FRESH_CHOICES, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        #=  forms.ChoiceField(widget=forms.RadioSelect(attrs={'class' : 'radio-inline form-control'},renderer=HorizRadioRenderer),choices=DRY_FRESH_CHOICES)
        plot  = forms.ModelChoiceField(queryset = Plot.objects.all(),widget=Select(attrs={'disabled':'True','class': 'form-control seleckpicker'}),empty_label="Choose plots")
        Crop =  forms.ModelChoiceField(queryset = Crop.objects.all(),widget=Select(attrs={'class': 'form-control seleckpicker'}),empty_label="Choose Crop..")
        plant_number  = forms.ChoiceField(choices = PLANT_NUMBER_CHOICES, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        row_number = forms.ChoiceField(choices = ROW_NUMBER_CHOICES, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        marketable_produced = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '#marketable produce','class':'form-control'}))
        unmarketable_produced = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '#unmarketable produce','class':'form-control'}))
        marketable_produced_weight = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#weight of marketable produce','class':'form-control'}))
        unmarketable_produced_weight = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#weight of unmarketable produce','class':'form-control'}))
        diameter_width_produced =  forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#diameter/width produced','class':'form-control'}))
        length =  forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#length','class':'form-control'}))
        residual_biomass =  forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#residual biomas','class':'form-control'}))
        
CROP_CHOICES=[
        ('','Choose..'),
]

class CropMonitoringPlantHeightForm(forms.Form):
        date = forms.DateField(widget=forms.TextInput(attrs={'placeholder': '12/02/1989','class':'form-control'}))
        farm =  forms.ModelChoiceField(queryset = Farm.objects.all(),widget=Select(attrs={'class': 'form-control seleckpicker'}),empty_label="Choose Farm")
        crop_stage  = forms.ChoiceField(choices = CROP_STAGE_CHOICES, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        plot =  forms.ModelChoiceField(queryset = Plot.objects.all(),widget=Select(attrs={'disabled':'True','class': 'form-control seleckpicker'}),empty_label="Choose Plot")
        
        sub_plot_size = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#sub plot size','class':'form-control'}))
        sub_plot_plant_number =  forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '#Number of plants in the sub-plot','class':'form-control'}))
        total_plant_number =  forms.IntegerField(widget=forms.TextInput(attrs={'readonly':'True','placeholder': '#total plant number','class':'form-control'}))
        
        totalPlant = forms.IntegerField(widget=forms.HiddenInput(attrs={'readonly':'True','class':'form-control'}))
        plant_density_per_bed =  forms.IntegerField(widget=forms.TextInput(attrs={'readonly':'True','placeholder': '#plant density per bed','class':'form-control'}))
        plant_density_per_sqm =  forms.FloatField(widget=forms.TextInput(attrs={'readonly':'True','placeholder': '#plant density per sqm','class':'form-control'}))
        
        #plant_density_per_bed =  forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#plant density per bed','class':'form-control'}))
        #plant_density_per_sqm  =  forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#plant density per sqm','class':'form-control'}))
        #Crop = forms.ChoiceField(choices = CROP_CHOICES, widget=forms.Select(attrs={'readonly':'True','class': 'form-control seleckpicker'}))
        Crop =  forms.ModelChoiceField(queryset = Crop.objects.all(),widget=Select(attrs={'class': 'form-control seleckpicker'}),empty_label="Choose Crop..")
        
        row_number = forms.ChoiceField(choices = ROW_NUMBER_CHOICES, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        number_of_good_plants  =  forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '#number of good plants','class':'form-control'}))
        number_of_bad_plants  =  forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '#number of bad plants','class':'form-control'}))

        LAI_one = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#leaf area index (LAI) ','class':'form-control'}))
        #plant_number_one = forms.ChoiceField(choices = PLANT_NUMBER_CHOICES, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        plant_height_one = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#plant height','class':'form-control'}))
        plant_canopy_width_one = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#plant canopy width','class':'form-control'}))
        lenght_of_crop_stage_one = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#lenght_of_crop_stage','class':'form-control'}))
        plant_leave_number_one = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '#plant leave number','class':'form-control'}))
        plant_leave_length_one = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#plant leave length','class':'form-control'}))
        plant_leave_width_one = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#plant leave width','class':'form-control'}))

        LAI_two = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#leaf area index (LAI) ','class':'form-control'}))
        #plant_number_two = forms.ChoiceField(choices = PLANT_NUMBER_CHOICES, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        plant_height_two = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#plant height','class':'form-control'}))
        plant_canopy_width_two = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#plant canopy width','class':'form-control'}))
        lenght_of_crop_stage_two = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#lenght_of_crop_stage','class':'form-control'}))
        plant_leave_number_two = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '#plant leave number','class':'form-control'}))
        plant_leave_length_two = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#plant leave length','class':'form-control'}))
        plant_leave_width_two = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#plant leave width','class':'form-control'}))

        LAI_three = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#leaf area index (LAI) ','class':'form-control'}))
        #plant_number_three = forms.ChoiceField(choices = PLANT_NUMBER_CHOICES, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        plant_height_three = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#plant height','class':'form-control'}))
        plant_canopy_width_three = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#plant canopy width','class':'form-control'}))
        lenght_of_crop_stage_three = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#lenght_of_crop_stage','class':'form-control'}))
        plant_leave_number_three = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '#plant leave number','class':'form-control'}))
        plant_leave_length_three = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#plant leave length','class':'form-control'}))
        plant_leave_width_three = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#plant leave width','class':'form-control'}))

                
WEED_ACTIVITY_CHOICE=(
        ('','Choose...'),
        ('Hoe','Hoe'),
        ('Hand weeding','Hand weeding'),
        ('Mechanical weeding','Mechanical weeding'),
        ('Hand weeding + loosen the soil manually around plants','Hand weeding + loosen the soil manually around plants')
)
class WeedingForm(forms.Form):
        date = forms.DateField(widget=forms.TextInput(attrs={'placeholder': '12/02/1989','class':'form-control'}))
        farm =  forms.ModelChoiceField(queryset = Farm.objects.all(),widget=Select(attrs={'class': 'form-control seleckpicker'}),empty_label="Choose Farm")
        weed_activities = forms.ChoiceField(choices = WEED_ACTIVITY_CHOICE, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        plot  = forms.ModelChoiceField(queryset = Plot.objects.all(),widget=Select(attrs={'disabled':'True','class': 'form-control seleckpicker'}),empty_label="Choose plots")
        #time =  forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#time taken','class':'form-control'}))
        #payment =  forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#payment','class':'form-control'}))
        labour  = forms.ChoiceField(choices = LABOUR_CHOICES, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        hired_female_number = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder':'#number of hired female','class':'form-control','required':'False'}))
        hired_male_number = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '#number of hired male','class':'form-control','required':'False'}))
        family_female_number = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '#number of family female','class':'form-control','required':'False'}))
        family_male_number = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '#number of family male','class':'form-control','required':'False'}))
        wage = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#wage price','class':'form-control'}))
        #currency = forms.ChoiceField(choices = CURRENCY_CHOICES, widget=forms.Select(attrs={'class': 'seleckpicker'}))
        #labour_time_taken = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#time taken','class':'form-control','required':'False'}))
        family_female_time = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#time taken','class':'form-control','required':'False'}))
        family_male_time = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#time taken','class':'form-control','required':'False'}))
        hired_female_time = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#time taken','class':'form-control','required':'False'}))
        hired_male_time = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#time taken','class':'form-control','required':'False'}))
        
BROKEN_TECHNOLOGY_CHOICES=(
        ('','Choose..'),
        ('Diesel motorized pump','Diesel motorized pump'),
        ('Drip','Drip'),
        ('Petrol motorized pump','Petrol motorized pump'),
        ('Pulley','Pulley'),
        ('Rope and washer','Rope and washer'),
        ('Solar pump','Solar pump'),
        ('Sprinkler','Sprinkler'),
        ('Tractor mounted pump','Tractor mounted pump'),
        ('Tank and hose','Tank and hose'),
)

MAINTENANCE_PLACE_CHOICES =(
        ('','Choose...'),
        ('Farm/home','Farm/home'),
        ('Repair shop','Repair shop')
)
REPAIR_PERSONEL_CHOICE=(
        ('','Choose..'),
        ('Yourself','Yourself'),
        ('Technician','Technician'),
)

REPAIR_TYPEL_CHOICE=(
        ('','Choose..'),
        ('Maintenance','Maintenance'),
        ('Repair','Repair'),
)
class ServiceRepaireForm(forms.Form):
        date = forms.DateField(widget=forms.TextInput(attrs={'placeholder': '12/02/1989','class':'form-control'}))
        farm = forms.ModelChoiceField(queryset = Farm.objects.all(),widget=Select(attrs={'class': 'form-control seleckpicker'}),empty_label="Choose Farm")
        repaire_type  = forms.ChoiceField(choices = REPAIR_TYPEL_CHOICE, widget=forms.Select(attrs={'class': 'form-control seleckpicker'})) 
        #= forms.CharField(widget=forms.TextInput(attrs={'placeholder': '#Type of repaires','class':'form-control'}),max_length=100)
        spaire = forms.ModelMultipleChoiceField(queryset=Spaire.objects.all(),widget=forms.SelectMultiple(attrs={'class': 'form-control seleckpicker'}),required=True)
        technology_broken = forms.ChoiceField(choices = BROKEN_TECHNOLOGY_CHOICES, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        maintenance_place = forms.ChoiceField(choices = MAINTENANCE_PLACE_CHOICES, widget=forms.Select(attrs={'class': 'form-control seleckpicker'})) 
        price = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#Price of spaire parts','class':'form-control'}))
        #currency = forms.ChoiceField(choices = CURRENCY_CHOICES, widget=forms.Select(attrs={'class': 'seleckpicker'}))
        distance_to_shop = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#distance to shop','class':'form-control'}))
        travel_cost = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#travel cost','class':'form-control'}))
        repair_personel = forms.ChoiceField(choices = REPAIR_PERSONEL_CHOICE, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        time_taken = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#time taken','class':'form-control'}))
        #models.FloatField('Price of spaire parts (Tsh)')
        #total_cost = models.FloatField('Total repaire cost (Tsh)')

LAND_PREPARATION_TOOL_CHOICES=(
        ('','Choose..'),
        ('Hoe','Hoe'),
        ('Oxen&plough','Oxen and plough'),
        ('Cutlass','Cutlass'),
        ('Tractor','Tractor'),
        ('Hand','Hand'),
        ('Other','Other'),
)      

class LandPreparationForm(forms.Form):
        date = forms.DateField(widget=forms.TextInput(attrs={'placeholder': '12/02/1989','class':'form-control'}))
        farm =  forms.ModelChoiceField(queryset = Farm.objects.all(),widget=Select(attrs={'class': 'form-control seleckpicker'}),empty_label="Choose Farm")
        plot =  forms.ModelChoiceField(queryset = Plot.objects.all(),widget=Select(attrs={'disabled':'True','class': 'form-control seleckpicker'}),empty_label="Choose Plot")
        landpreparationtool = forms.ChoiceField(choices =LAND_PREPARATION_TOOL_CHOICES, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        other  = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '#other','class':'form-control','required':'False'}))
        labour  = forms.ChoiceField(choices = LABOUR_CHOICES, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        hired_female_number = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder':'#number of hired female','class':'form-control','required':'False'}))
        hired_male_number = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '#number of hired male','class':'form-control','required':'False'}))
        family_female_number = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '#number of family female','class':'form-control','required':'False'}))
        family_male_number = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '#number of family male','class':'form-control','required':'False'}))
        wage =  forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#payment','class':'form-control'}))
        #currency = forms.ChoiceField(choices = CURRENCY_CHOICES, widget=forms.Select(attrs={'readonly':'True','class': 'seleckpicker'}))
        #labour_time_taken = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#time taken','class':'form-control','required':'False'}))
        family_female_time = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#time taken','class':'form-control','required':'False'}))
        family_male_time = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#time taken','class':'form-control','required':'False'}))
        hired_female_time = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#time taken','class':'form-control','required':'False'}))
        hired_male_time = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#time taken','class':'form-control','required':'False'}))
        
        
LAND_CLEARANCE_CHOICES=(
        ('','Choose..'),
        ('ManualClearance','Manual clearance'),
        ('Burning','Burning'),
        ('HerbicicdeApplication','Herbicide application'),
        ('Mechanical','Mechanical'),
)      
    

class LabourForm(forms.Form):
        labour  = forms.ChoiceField(choices = LABOUR_CHOICES, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        hired_female_number = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder':'#number of hired female','class':'form-control','required':'False'}))
        hired_male_number = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '#number of hired male','class':'form-control','required':'False'}))
        family_female_number = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '#number of family female','class':'form-control','required':'False'}))
        family_male_number = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '#number of family male','class':'form-control','required':'False'}))
        wage =  forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#payment','class':'form-control'}))
        currency = forms.ChoiceField(choices = CURRENCY_CHOICES, widget=forms.Select(attrs={'readonly':'True','class': 'seleckpicker'}))
        #labour_time_taken = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#time taken','class':'form-control','required':'False'}))
        family_female_time = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#time taken','class':'form-control','required':'False'}))
        family_male_time = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#time taken','class':'form-control','required':'False'}))
        hired_female_time = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#time taken','class':'form-control','required':'False'}))
        hired_male_time = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#time taken','class':'form-control','required':'False'}))
        
class LandCleareanceForm(forms.Form):
        date = forms.DateField(widget=forms.TextInput(attrs={'placeholder': '12/02/1989','class':'form-control'}))
        farm =  forms.ModelChoiceField(queryset = Farm.objects.all(),widget=Select(attrs={'class': 'form-control seleckpicker'}),empty_label="Choose Farm")
        plot =  forms.ModelChoiceField(queryset = Plot.objects.all(),widget=Select(attrs={'disabled':'True','class': 'form-control seleckpicker'}),empty_label="Choose Plot")
        landpreparationtool = forms.ChoiceField(choices =LAND_CLEARANCE_CHOICES, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        labour  = forms.ChoiceField(choices = LABOUR_CHOICES, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        hired_female_number = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder':'#number of hired female','class':'form-control','required':'False'}))
        hired_male_number = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '#number of hired male','class':'form-control','required':'False'}))
        family_female_number = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '#number of family female','class':'form-control','required':'False'}))
        family_male_number = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '#number of family male','class':'form-control','required':'False'}))
        wage =  forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#payment','class':'form-control'}))
        #currency = forms.ChoiceField(choices = CURRENCY_CHOICES, widget=forms.Select(attrs={'readonly':'True','class': 'seleckpicker'}))
        #labour_time_taken = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#time taken','class':'form-control','required':'False'}))
        family_female_time = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#time taken','class':'form-control','required':'False'}))
        family_male_time = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#time taken','class':'form-control','required':'False'}))
        hired_female_time = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#time taken','class':'form-control','required':'False'}))
        hired_male_time = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#time taken','class':'form-control','required':'False'}))
        
        
CONSUMED_CROP_CURRENCY_CHOICES=(
        ('','Choose....'),
        ('Tsh','Tsh'),
        ('birr','Birr'),
        ('cedi','Cedi'),
        ('Usd','Usd'),
        )

WHERE_CONSUMED_CHOICES=(
        ('','Choose....'),
        ('Own family','Own family'),
        ('Friends','Friends'),
        ('Neighbor','Neighbor'),
        )

HOW_CONSUMED_CHOICES=(
        ('','Choose....'),
        ('Fresh(green)','Fresh(green)'),
        ('Dry','Dry'),
        )
 
class ConsumedCropbyHouseholdForm(forms.Form):
        date = forms.DateField(widget=forms.TextInput(attrs={'placeholder': '12/02/1989','class':'form-control'}))
        farm =  forms.ModelChoiceField(queryset = Farm.objects.all(),widget=Select(attrs={'class': 'form-control seleckpicker'}),empty_label="Choose Farm")
        plot =  forms.ModelChoiceField(queryset = Plot.objects.all(),widget=Select(attrs={'disabled':'True','class': 'form-control seleckpicker'}),empty_label="Choose Plot")
        quantity =  forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#quantity','class':'form-control'}))
        marketprice =  forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#marketprice','class':'form-control'}))
        totalvalue =  forms.FloatField(widget=forms.TextInput(attrs={'readonly':'True','placeholder': '#totalvalue','class':'form-control'}))
        #currency = forms.ChoiceField(choices = CONSUMED_CROP_CURRENCY_CHOICES, widget=forms.Select(attrs={'readonly':'True','class': 'form-control seleckpicker'}))
        where_consumed = forms.ChoiceField(choices = WHERE_CONSUMED_CHOICES, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        how_consumed = forms.ChoiceField(choices = HOW_CONSUMED_CHOICES, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        
RESIDUAL_ACTIVITY_CHOICES=(
        ('','Choose..'),
        ('Burnt','Burnt'),
        ('Cut and fed to livestock','Cut and fed to livestock'),
        ('Left on the field','Left on the field'),
        ('Removed and used in another field','Removed and used in another field'),
        ('Other','other (please specify in remarks)'),
)      

class ResidueHandlingForm(forms.Form):
        date = forms.DateField(widget=forms.TextInput(attrs={'placeholder': '12/02/1989','class':'form-control'}))
        farm =  forms.ModelChoiceField(queryset = Farm.objects.all(),widget=Select(attrs={'class': 'form-control seleckpicker'}),empty_label="Choose Farm")
        residual_activities = forms.ChoiceField(choices = RESIDUAL_ACTIVITY_CHOICES, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        other  = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '#other','class':'form-control','required':'False'}))
        plot  = forms.ModelChoiceField(queryset = Plot.objects.all(),widget=Select(attrs={'disabled':'True','class': 'form-control seleckpicker'}),empty_label="Choose plots")
        time =  forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#time taken','class':'form-control'}))
        #payment =  forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#payment','class':'form-control'}))
        labour  = forms.ChoiceField(choices = LABOUR_CHOICES, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        hired_female_number = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder':'#number of hired female','class':'form-control','required':'False'}))
        hired_male_number = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '#number of hired male','class':'form-control','required':'False'}))
        family_female_number = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '#number of family female','class':'form-control','required':'False'}))
        family_male_number = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '#number of family male','class':'form-control','required':'False'}))
        #labour_time_taken = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#time taken','class':'form-control','required':'False'}))
        wage = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#wage price','class':'form-control'}))
        #currency = forms.ChoiceField(choices = CURRENCY_CHOICES, widget=forms.Select(attrs={'class': 'seleckpicker'}))
        #delivery_time = forms.TimeField(widget=forms.TimeInput(attrs={'placeholder': '#wage price','class':'form-control','format':'%H:%M'}))
        family_female_time = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#time taken','class':'form-control','required':'False'}))
        family_male_time = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#time taken','class':'form-control','required':'False'}))
        hired_female_time = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#time taken','class':'form-control','required':'False'}))
        hired_male_time = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#time taken','class':'form-control','required':'False'}))
        
                       
USAGE_PURPORSE_CHOICE=(
        ('','Choose..'),
        ('Brick making','Brick making'),
        ('Drinking','Drinking'),
        ('Domestic(cookin. cleaning, washing etc)','Domestic(cooking,cleaning, washing etc)'),
        ('Irrigation of non project related crops','Irrigation of non project related crops'),
        ('Livestock drinking','Livestock drinking')
)
        
YES_NO_CHOICES =(
        ('','Choose...'),
        ('Yes','Yes'),
        ('No','No'),
)
class OtherWaterUsageForm(forms.Form):
        date = forms.DateField(widget=forms.TextInput(attrs={'placeholder': '12/02/1989','class':'form-control'}))
        farm =  forms.ModelChoiceField(queryset = Farm.objects.all(),widget=Select(attrs={'class': 'form-control seleckpicker'}),empty_label="Choose Farmer")
       # plot  = forms.ModelChoiceField(queryset = Plot.objects.all(),widget=Select(attrs={'disabled':'True','class': 'form-control seleckpicker'}),empty_label="Choose plots")
        bucketnumber = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#number of buckets','class':'form-control'}))
        bucketvolume = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#bucket volume','class':'form-control'}))
        technology = forms.CharField(widget=forms.TextInput(attrs={'readonly':'True','placeholder': '#technology','class':'form-control'}))
        usagepurpose = forms.ChoiceField(choices = USAGE_PURPORSE_CHOICE, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        start_time = forms.TimeField(widget=forms.TimeInput(attrs={'placeholder': '#start time','class':'form-control timepicker'}))
        end_time  = forms.TimeField(widget=forms.TimeInput(attrs={'placeholder': '#end time','class':'form-control timepicker'}))
        total_time = forms.FloatField(widget=forms.TextInput(attrs={'readonly': 'true','class':'form-control'}))
        totalvolume = forms.FloatField(widget=forms.TextInput(attrs={'readonly': 'true','class':'form-control'}))
        lifting_technology_yes_no = forms.ChoiceField(choices = YES_NO_CHOICES, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        
HarvestedCrop_CURRENCY_CHOICES=(
        ('','Choose..'),
        ('Tsh','Tsh'),
        ('Birr','Birr'),
        ('Cedi','Cedi'),
        ('Usd','Usd'),
)
MODE_OF_TRANSPORT_CHOICES=(
        ('','Choose..'),
        ('Foot','Foot'),
        ('Public transport','Public transport'),
        ('Own transportation','Own transportation'),
)
class HarvestedCropSaleForm(forms.Form):
        date = forms.DateField(widget=forms.TextInput(attrs={'placeholder': '12/02/1989','class':'form-control'}))
        farm =  forms.ModelChoiceField(queryset = Farm.objects.all(),widget=Select(attrs={'class': 'form-control seleckpicker'}),empty_label="Choose Farm")
        plot =  forms.ModelChoiceField(queryset = Plot.objects.all(),widget=Select(attrs={'disabled':'True','class': 'form-control seleckpicker'}),empty_label="Choose Plot")
        quantity =  forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#quantity','class':'form-control'}))
        marketprice =  forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#marketprice','class':'form-control'}))
        totalvalue =  forms.FloatField(widget=forms.TextInput(attrs={'readonly':'True','placeholder': '#totalvalue','class':'form-control'}))
        mode_of_transport  = forms.ChoiceField(choices = MODE_OF_TRANSPORT_CHOICES, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        distance_to_the_market =  forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#distance to the market','class':'form-control'}))
        labour  = forms.ChoiceField(choices = LABOUR_CHOICES, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        hired_female_number = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder':'#number of hired female','class':'form-control','required':'False'}))
        hired_male_number = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '#number of hired male','class':'form-control','required':'False'}))
        family_female_number = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '#number of family female','class':'form-control','required':'False'}))
        family_male_number = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '#number of family male','class':'form-control','required':'False'}))
        #labour_time_taken = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#time taken','class':'form-control','required':'False'}))
        wage = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#wage price','class':'form-control'}))
        #currency = forms.ChoiceField(choices = HarvestedCrop_CURRENCY_CHOICES, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        #delivery_time = forms.TimeField(widget=forms.TimeInput(attrs={'placeholder': '#wage price','class':'form-control','format':'%H:%M'}))
        family_female_time = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#time taken','class':'form-control','required':'False'}))
        family_male_time = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#time taken','class':'form-control','required':'False'}))
        hired_female_time = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#time taken','class':'form-control','required':'False'}))
        hired_male_time = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#time taken','class':'form-control','required':'False'}))
        fare = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#fare','class':'form-control','required':'False'}))
        fuel_type = forms.ModelChoiceField(queryset = Fuel.objects.all(),widget=Select(attrs={'class': 'form-control seleckpicker'}),empty_label="Choose Fuel")
        fuel_cost = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#fuel cost','class':'form-control','required':'False'}))
        

STRESS_CHOICES=(
        ('','Choose..'),
        ('Livestock grazing','Livestock grazing'),('Flood damage','Flood damage'),
        ('Fertilizer shortage','Fertilizer shortage'),('Disease','Disease'),('Water stress','Water stress'),
        ('Other','Other')   
)

SEVERNESS_CHOICES=(
        ('','Choose..'), ('0-5%','0-5%'),
        ('6-10%','6-10%'),('11-25%','11-25%'),
        ('26-50%','26-50%'),('51-75%','51-75%'),('>76%','>76%'),  
)

class RemarkForm(forms.Form):
        start_date = forms.DateField(widget=forms.TextInput(attrs={'placeholder': '12/02/1989','class':'form-control'}))
        end_date = forms.DateField(widget=forms.TextInput(attrs={'placeholder': '12/02/1989','class':'form-control'}))
        farm =  forms.ModelChoiceField(queryset = Farm.objects.all(),widget=Select(attrs={'class': 'form-control seleckpicker'}),empty_label="Choose Farm")
        plot =  forms.ModelChoiceField(queryset = Plot.objects.all(),widget=Select(attrs={'disabled':'True','class': 'form-control seleckpicker'}),empty_label="Choose Plot")
        stress = forms.ChoiceField(choices = STRESS_CHOICES, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        severness = forms.ChoiceField(choices = SEVERNESS_CHOICES, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        other  = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '#other','class':'form-control','required':'False'}))
        

class PlotForm(forms.ModelForm):
        fieldtype = forms.ChoiceField(choices =FIELDTYPE_CHOICES, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        
        class Meta:
                model=Plot
                exclude=('',)
        def __init__(self, *args, **kwargs):
                super(PlotForm, self).__init__(*args, **kwargs)
                self.fields['fieldtype'].widget.attrs['class'] = 'form-control'
                self.fields['latitude'].widget.attrs['class'] = 'form-control'
                self.fields['longitude'].widget.attrs['class'] = 'form-control'
        

class PlotManagementForm(forms.ModelForm):
        water_application = forms.ChoiceField(required=True, choices=WATER_APPLICATION_CHOICES)
        cropping_system = forms.ChoiceField(required=True, choices=CROPPING_SYSTEM_CHOICES)

        class Meta:
                model=PlotManagement
                exclude=('enteredpersonel',)

        def __init__(self, *args, **kwargs):
                super(PlotManagementForm, self).__init__(*args, **kwargs)
                #self.data.update({ 'farm': self.instance.farm })
                self.fields['farm'].widget.attrs['readonly'] = True
                self.fields['farm'].widget.attrs['class'] = 'form-control'
                self.fields['plotID'].widget.attrs['readonly'] = True
                self.fields['plotID'].widget.attrs['class'] = 'form-control'
                #self.fields['plotID'].widget = TextInput(attrs={'class':'form-control'})
                #self.fields['crop'].widget.attrs['class'] = 'form-control'
                self.fields['crop'].required = False
                self.fields['elevation'].widget.attrs['class'] = 'form-control'
                self.fields['plot_size'].widget.attrs['class'] = 'form-control'
                self.fields['seasonstart'].widget.attrs['class'] = 'form-control'
                self.fields['cropping_system'].widget.attrs['class'] = 'form-control'
                self.fields['water_application'].widget.attrs['class'] = 'form-control'
                self.fields['rootdepth'].widget.attrs['class'] = 'form-control'
                
        '''
        def clean_plotID(self):
                instance = getattr(self,'instance', None)
                if instance and instance.pk:
                        return instance.plotID
                else:
                        return self.cleaned_data['plotID']
        '''
class CropVarietiesForm(forms.ModelForm):
        varietytype = forms.ChoiceField(required=True, choices=CROP_VARIETY_CHOICES)
        class Meta:
                model=CropVarieties
                fields = '__all__'
        def __init__(self, *args, **kwargs):
                super(CropVarietiesForm, self).__init__(*args, **kwargs)
                self.fields['variety'].widget.attrs['class'] = 'form-control'
                self.fields['varietytype'].widget.attrs['class'] = 'form-control'
                #self.fields['varietytype'].choices = CROP_VARIETY_CHOICES

class PlotCropForm(forms.ModelForm):
        crop1_varietytype = forms.ChoiceField(required=True, choices=CROP_VARIETY_CHOICES)
        crop2_varietytype = forms.ChoiceField(required=True, choices=CROP_VARIETY_CHOICES)
        class Meta:
                model=PlotCrop
                fields = '__all__'
        def __init__(self, *args, **kwargs):
                super(PlotCropForm, self).__init__(*args, **kwargs)
                self.fields['crop1'].widget.attrs['class'] = 'form-control'
                self.fields['crop1_variety'].widget.attrs['class'] = 'form-control'
                self.fields['crop1_varietytype'].widget.attrs['class'] = 'form-control'
                self.fields['crop2'].widget.attrs['class'] = 'form-control'
                self.fields['crop2_variety'].widget.attrs['class'] = 'form-control'
                self.fields['crop2_varietytype'].widget.attrs['class'] = 'form-control'
                
                
class BedPlotForm(forms.ModelForm):
        class Meta:
                model=BedPlot
                exclude=('plotID',)
        def __init__(self, *args, **kwargs):
                super(BedPlotForm, self).__init__(*args, **kwargs)
                self.fields['length'].widget.attrs['class'] = 'form-control'
                self.fields['width'].widget.attrs['class'] = 'form-control'
                self.fields['numbers'].widget.attrs['class'] = 'form-control'

class FurrowForm(forms.ModelForm):
        class Meta:
                model=Furrow
                exclude=('plotID',)
        def __init__(self, *args, **kwargs):
                super(FurrowForm, self).__init__(*args, **kwargs)
                self.fields['length'].widget.attrs['class'] = 'form-control'
                self.fields['width'].widget.attrs['class'] = 'form-control'
                self.fields['numbers'].widget.attrs['class'] = 'form-control'
                
class WaterManagementForm(forms.ModelForm):
        water_management_method = forms.ChoiceField(required=True, choices=WATER_MANAGEMENT_METHOD_CHOICES)
        
        class Meta:
                model=WaterManagement
                exclude=('enteredpersonel',)
        def __init__(self, *args, **kwargs):
                super(WaterManagementForm, self).__init__(*args, **kwargs)
                self.fields['water_management_method'].widget.attrs['class'] = 'form-control'
                self.fields['yellow_depth_detector'].widget.attrs['class'] = 'form-control'
                self.fields['red_depth_detector'].widget.attrs['class'] = 'form-control'
                self.fields['rods_length'].widget.attrs['class'] = 'form-control'


class Remark_Form(forms.ModelForm):
        severness = forms.ChoiceField(required=True, choices=SEVERNESS_CHOICES)
        stress = forms.ChoiceField(required=True, choices=STRESS_CHOICES)
        other  = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '#other','class':'form-control','required':'False'}))
        #start_date = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS)
        #end_date = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS)
        class Meta:
                model=Remark
                exclude=('enteredpersonel',)
        def __init__(self, *args, **kwargs):
                super(Remark_Form, self).__init__(*args, **kwargs)
                self.fields['start_date'].widget.attrs['class'] = 'form-control'
                self.fields['end_date'].widget.attrs['class'] = 'form-control'
                #self.fields['date'].widget.attrs['readonly'] = True
                self.fields['farm'].widget.attrs['class'] = 'form-control'
                self.fields['farm'].widget.attrs['readonly'] = True
                self.fields['plot'].widget.attrs['class'] = 'form-control'
                self.fields['plot'].widget.attrs['readonly'] = True
                self.fields['stress'].widget.attrs['class'] = 'form-control'
                self.fields['severness'].widget.attrs['class'] = 'form-control'
        
        
class LandClearance_Form(forms.ModelForm):
        landclearanceoption = forms.ChoiceField(choices =LAND_CLEARANCE_CHOICES, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        class Meta:
                model = LandClearance
                exclude=('enteredpersonel',)
        
        def __init__(self, *args, **kwargs):
                super(LandClearance_Form, self).__init__(*args, **kwargs)
                self.fields['date'].widget.attrs['class'] = 'form-control'
                #self.fields['date'].widget.attrs['readonly'] = True
                self.fields['farm'].widget.attrs['class'] = 'form-control'
                self.fields['farm'].widget.attrs['readonly'] = True
                self.fields['plotID'].widget.attrs['class'] = 'form-control'
                self.fields['plotID'].widget.attrs['readonly'] = True
                self.fields['landclearanceoption'].widget.attrs['class'] = 'form-control'
        

class LabourManagement_Form(forms.ModelForm):
        labour  = forms.ChoiceField(choices = LABOUR_CHOICES, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        class Meta:
                model = LabourManagament
                exclude=('enteredpersonel','farm','areaID','date','activity')
        def __init__(self, *args, **kwargs):
                super(LabourManagement_Form, self).__init__(*args, **kwargs)
                self.fields['labour'].widget.attrs['class'] = 'form-control'
                self.fields['hired_female_number'].widget.attrs['class'] = 'form-control'
                self.fields['hired_female_time'].widget.attrs['class'] = 'form-control'
                self.fields['hired_male_number'].widget.attrs['class'] = 'form-control'
                self.fields['hired_male_time'].widget.attrs['class'] = 'form-control'
                self.fields['family_female_number'].widget.attrs['class'] = 'form-control'
                self.fields['family_male_number'].widget.attrs['class'] = 'form-control'
                self.fields['wage'].widget.attrs['class'] = 'form-control'
                self.fields['family_female_time'].widget.attrs['class'] = 'form-control'
                self.fields['family_male_time'].widget.attrs['class'] = 'form-control'
                #self.fields['price_unit'].widget.attrs['class'] = 'form-control'
                
class LandPreparation_Form(forms.ModelForm):
        other  = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '#other','class':'form-control','required':'False'}))
        landpreparationtool = forms.ChoiceField(choices =LAND_PREPARATION_TOOL_CHOICES, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        class Meta:
                model = LandPreparation
                exclude=('enteredpersonel',)
        
        def __init__(self, *args, **kwargs):
                super(LandPreparation_Form, self).__init__(*args, **kwargs)
                self.fields['date'].widget.attrs['class'] = 'form-control'
                self.fields['farm'].widget.attrs['class'] = 'form-control'
                self.fields['farm'].widget.attrs['readonly'] = True
                self.fields['plotID'].widget.attrs['class'] = 'form-control'
                self.fields['plotID'].widget.attrs['readonly'] = True
                self.fields['landpreparationtool'].widget.attrs['class'] = 'form-control'
                
                

class FertilizerManagement_Form(forms.ModelForm):
        #fertilizer = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '#fertilizer','class':'form-control','required':'False'}))
        fertilizer_management = forms.ChoiceField(choices = FERTILIZER_MANAGEMENT_CHOICES, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        crop_stage  = forms.ChoiceField(choices = CROP_STAGE_CHOICES, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        class Meta:
                model = FertilizerManagement
                exclude=('enteredpersonel',)
        
        def __init__(self, *args, **kwargs):
                super(FertilizerManagement_Form, self).__init__(*args, **kwargs)
                self.fields['date'].widget.attrs['class'] = 'form-control'
                self.fields['farm'].widget.attrs['class'] = 'form-control'
                self.fields['farm'].widget.attrs['readonly'] = True
                self.fields['plotID'].widget.attrs['class'] = 'form-control'
                self.fields['plotID'].widget.attrs['readonly'] = True
                self.fields['compost_kind'].widget.attrs['class'] = 'form-control'
                self.fields['crop_stage'].widget.attrs['class'] = 'form-control'
                self.fields['fertilizer'] = forms.CharField()
                self.fields['fertilizer'].widget.attrs['class'] = 'form-control'
                self.fields['quantity_in_kg'].widget.attrs['class'] = 'form-control'
                self.fields['fertilizer_management'].widget.attrs['class'] = 'form-control'
                self.fields['price'].widget.attrs['class'] = 'form-control'
                #self.fields['price_unit'].widget.attrs['class'] = 'form-control'

class PesticideManagement_Form(forms.ModelForm):
        form  = forms.ChoiceField(choices = FORM_CHOICES, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        crop_stage  = forms.ChoiceField(choices = CROP_STAGE_CHOICES, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        class Meta:
                model = PesticideManagement
                exclude=('enteredpersonel',)
        
        def __init__(self, *args, **kwargs):
                super(PesticideManagement_Form, self).__init__(*args, **kwargs)
                self.fields['date'].widget.attrs['class'] = 'form-control'
                self.fields['farm'].widget.attrs['class'] = 'form-control'
                self.fields['farm'].widget.attrs['readonly'] = True
                self.fields['plotID'].widget.attrs['class'] = 'form-control'
                self.fields['plotID'].widget.attrs['readonly'] = True
                self.fields['name'] = forms.CharField()
                self.fields['name'].widget.attrs['class'] = 'form-control'
                
                self.fields['crop_stage'].widget.attrs['class'] = 'form-control'
                self.fields['form'].widget.attrs['class'] = 'form-control'
                self.fields['water_volume'].widget.attrs['class'] = 'form-control'
                self.fields['quantity_in_litre'].widget.attrs['class'] = 'form-control'
                self.fields['quantity_in_kg'].widget.attrs['class'] = 'form-control'
                self.fields['price'].widget.attrs['class'] = 'form-control'
                #self.fields['price_unit'].widget.attrs['class'] = 'form-control'

class Weeding_Form(forms.ModelForm):
        weed_activities = forms.ChoiceField(choices = WEED_ACTIVITY_CHOICE, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        class Meta:
                model = Weed
                exclude=('enteredpersonel',)
        def __init__(self, *args, **kwargs):
                super(Weeding_Form, self).__init__(*args, **kwargs)
                self.fields['date'].widget.attrs['class'] = 'form-control'
                self.fields['farm'].widget.attrs['class'] = 'form-control'
                self.fields['farm'].widget.attrs['readonly'] = True
                self.fields['plotID'].widget.attrs['class'] = 'form-control'
                self.fields['plotID'].widget.attrs['readonly'] = True
                self.fields['weed_activities'].widget.attrs['class'] = 'form-control'

class YieldFarmLevel_Form(forms.ModelForm):
        fresh_dry = forms.ChoiceField(choices = DRY_FRESH_CHOICES, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        class Meta:
                model = YieldFarmLevel
                exclude=('enteredpersonel',)

        def __init__(self, *args, **kwargs):
                super(YieldFarmLevel_Form, self).__init__(*args, **kwargs)
                self.fields['date'].widget.attrs['class'] = 'form-control'
                self.fields['farm'].widget.attrs['class'] = 'form-control'
                self.fields['farm'].widget.attrs['readonly'] = True
                self.fields['plotID'].widget.attrs['class'] = 'form-control'
                self.fields['plotID'].widget.attrs['readonly'] = True
                self.fields['Crop'].widget.attrs['class'] = 'form-control'
                self.fields['quantity_harvested'].widget.attrs['class'] = 'form-control'
                self.fields['fresh_dry'].widget.attrs['class'] = 'form-control'
                self.fields['marketable_yield'].widget.attrs['class'] = 'form-control'
                self.fields['unmarketable_yield'].widget.attrs['class'] = 'form-control'
                self.fields['biomas'].widget.attrs['class'] = 'form-control'

class ResidualHandling_Form(forms.ModelForm):
        residual_activities = forms.ChoiceField(choices = RESIDUAL_ACTIVITY_CHOICES, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        other  = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '#other','class':'form-control','required':'False'}))
        class Meta:
                model = ResidualHandling
                exclude=('enteredpersonel',)

        def __init__(self, *args, **kwargs):
                super(ResidualHandling_Form, self).__init__(*args, **kwargs)
                self.fields['date'].widget.attrs['class'] = 'form-control'
                self.fields['farm'].widget.attrs['class'] = 'form-control'
                self.fields['farm'].widget.attrs['readonly'] = True
                self.fields['plotID'].widget.attrs['class'] = 'form-control'
                self.fields['plotID'].widget.attrs['readonly'] = True
                self.fields['residual_activities'].widget.attrs['class'] = 'form-control'
                self.fields['time'].widget.attrs['class'] = 'form-control'


class YieldRowBedLevel_Form(forms.ModelForm):
        fresh_dry = forms.ChoiceField(choices = DRY_FRESH_CHOICES, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        harvesting_method  = forms.ChoiceField(choices = HARVESTING_METHOD_CHOICES, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        class Meta:
                model = YieldRowBedLevel
                exclude=('enteredpersonel',)

        def __init__(self, *args, **kwargs):
                super(YieldRowBedLevel_Form, self).__init__(*args, **kwargs)
                self.fields['date'].widget.attrs['class'] = 'form-control'
                self.fields['farm'].widget.attrs['class'] = 'form-control'
                self.fields['farm'].widget.attrs['readonly'] = True
                self.fields['plotID'].widget.attrs['class'] = 'form-control'
                self.fields['plotID'].widget.attrs['readonly'] = True
                #self.fields['Crop'] = forms.CharField()
                self.fields['Crop'].widget.attrs['class'] = 'form-control'
                self.fields['harvesting_method'].widget.attrs['class'] = 'form-control'
                self.fields['fresh_dry'].widget.attrs['class'] = 'form-control'
                self.fields['row_number'].widget.attrs['class'] = 'form-control'
                self.fields['marketable_produced'].widget.attrs['class'] = 'form-control'
                self.fields['ummarketable_produced'].widget.attrs['class'] = 'form-control'
                self.fields['marketable_produced_weight'].widget.attrs['class'] = 'form-control'
                self.fields['unmarketable_produced_weight'].widget.attrs['class'] = 'form-control'


class YieldPlantLevel_Form(forms.ModelForm):
        plant_number  = forms.ChoiceField(choices = PLANT_NUMBER_CHOICES, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        row_number = forms.ChoiceField(choices = ROW_NUMBER_CHOICES, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        fresh_dry = forms.ChoiceField(choices = DRY_FRESH_CHOICES, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        harvest_method  = forms.ChoiceField(choices = HARVESTING_METHOD_CHOICES, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        class Meta:
                model = YieldPlantLevel
                exclude=('enteredpersonel',)

        def __init__(self, *args, **kwargs):
                super(YieldPlantLevel_Form, self).__init__(*args, **kwargs)
                self.fields['date'].widget.attrs['class'] = 'form-control'
                self.fields['farm'].widget.attrs['class'] = 'form-control'
                self.fields['farm'].widget.attrs['readonly'] = True
                self.fields['plotID'].widget.attrs['class'] = 'form-control'
                self.fields['plotID'].widget.attrs['readonly'] = True
                #self.fields['Crop'] = forms.CharField()
                self.fields['Crop'].widget.attrs['class'] = 'form-control'
                self.fields['harvest_method'].widget.attrs['class'] = 'form-control'
                self.fields['fresh_dry'].widget.attrs['class'] = 'form-control'
                self.fields['row_number'].widget.attrs['class'] = 'form-control'
                self.fields['plant_number'].widget.attrs['class'] = 'form-control'
                self.fields['marketable_produced'].widget.attrs['class'] = 'form-control'
                self.fields['unmarketable_produced'].widget.attrs['class'] = 'form-control'
                self.fields['marketable_produced_weight'].widget.attrs['class'] = 'form-control'
                self.fields['unmarketable_produced_weight'].widget.attrs['class'] = 'form-control'
                self.fields['diameter_width_produced'].widget.attrs['class'] = 'form-control'
                self.fields['length'].widget.attrs['class'] = 'form-control'
                self.fields['residual_biomass'].widget.attrs['class'] = 'form-control'

class SoilProperty_Form(forms.ModelForm):
        class Meta:
                model = SoilProperty
                exclude=('enteredpersonel',)
        def __init__(self, *args, **kwargs):
                super(SoilProperty_Form, self).__init__(*args, **kwargs)
                self.fields['date'].widget.attrs['class'] = 'form-control'
                self.fields['farm'].widget.attrs['class'] = 'form-control'
                self.fields['farm'].widget.attrs['readonly'] = True
                self.fields['plotID'].widget.attrs['class'] = 'form-control'
                self.fields['plotID'].widget.attrs['readonly'] = True
                self.fields['soilclass'].widget.attrs['class'] = 'form-control'
                self.fields['soil_depth'].widget.attrs['class'] = 'form-control'
                self.fields['pH'].widget.attrs['class'] = 'form-control'
                self.fields['ec'].widget.attrs['class'] = 'form-control'
                self.fields['sand'].widget.attrs['class'] = 'form-control'
                self.fields['clay'].widget.attrs['class'] = 'form-control'
                self.fields['silt'].widget.attrs['class'] = 'form-control'
                self.fields['cec'].widget.attrs['class'] = 'form-control'
                self.fields['om'].widget.attrs['class'] = 'form-control'
                self.fields['tn'].widget.attrs['class'] = 'form-control'
                self.fields['av_p'].widget.attrs['class'] = 'form-control'
                self.fields['fe'].widget.attrs['class'] = 'form-control'
                self.fields['fc'].widget.attrs['class'] = 'form-control'
                self.fields['pwp'].widget.attrs['class'] = 'form-control'
                self.fields['k'].widget.attrs['class'] = 'form-control'
                self.fields['bulkdensity'].widget.attrs['class'] = 'form-control'
                self.fields['zn'].widget.attrs['class'] = 'form-control'
                self.fields['se'].widget.attrs['class'] = 'form-control'
                self.fields['ca'].widget.attrs['class'] = 'form-control'
                self.fields['s'].widget.attrs['class'] = 'form-control'
                self.fields['mg'].widget.attrs['class'] = 'form-control'
                self.fields['na'].widget.attrs['class'] = 'form-control'
                
                
class OtherWaterUsage_Form(forms.ModelForm):
    
    class Meta:
        model = OtherWaterUsage
        exclude=('enteredpersonel',)

        def __init__(self, *args, **kwargs):
                super(OtherWaterUsage_Form, self).__init__(*args, **kwargs)
                self.fields['date'].widget.attrs['class'] = 'form-control'
                self.fields['farm'].widget.attrs['class'] = 'form-control'
                self.fields['farm'].widget.attrs['readonly'] = True
                self.fields['bucketnumber'].widget.attrs['class'] = 'form-control'
                self.fields['bucketvolume'].widget.attrs['class'] = 'form-control'
                self.fields['technology'].widget.attrs['class'] = 'form-control'
                self.fields['usagepurpose'].widget.attrs['class'] = 'form-control'
                self.fields['start_time'].widget.attrs['class'] = 'form-control'
                self.fields['end_time'].widget.attrs['class'] = 'form-control'
                self.fields['total_time'].widget.attrs['class'] = 'form-control'
                self.fields['totalvolume'].widget.attrs['class'] = 'form-control'
                self.fields['lifting_technology_yes_no'].widget.attrs['class'] = 'form-control'
                
class TissueNutrientAnalysis_Form(forms.ModelForm):
        plantnumber= forms.ChoiceField(choices =PLANT_NUMBER_CHOICES, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        bed_number= forms.ChoiceField(choices = BED_NUMBER_CHOICES, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        plant_tissue_part = forms.ChoiceField(choices = PLANT_TISSUE_PART_CHOICES, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        class Meta:
                model = TissueNutrientAnalysis
                exclude=('enteredpersonel',)
                
        def __init__(self, *args, **kwargs):
                super(TissueNutrientAnalysis_Form, self).__init__(*args, **kwargs)
                self.fields['date'].widget.attrs['class'] = 'form-control'
                self.fields['farm'].widget.attrs['class'] = 'form-control'
                self.fields['farm'].widget.attrs['readonly'] = True
                self.fields['plotID'].widget.attrs['class'] = 'form-control'
                self.fields['plotID'].widget.attrs['readonly'] = True
                self.fields['Crop'].widget.attrs['class'] = 'form-control'
                self.fields['plant_tissue_part'].widget.attrs['class'] = 'form-control'
                self.fields['plantnumber'].widget.attrs['class'] = 'form-control'
                self.fields['bed_number'].widget.attrs['class'] = 'form-control'
                self.fields['freshweight'].widget.attrs['class'] = 'form-control'
                self.fields['dryweight'].widget.attrs['class'] = 'form-control'
                self.fields['n'].widget.attrs['class'] = 'form-control'
                self.fields['p'].widget.attrs['class'] = 'form-control'
                self.fields['k'].widget.attrs['class'] = 'form-control'
                self.fields['s'].widget.attrs['class'] = 'form-control'
                self.fields['mg'].widget.attrs['class'] = 'form-control'
                self.fields['ca'].widget.attrs['class'] = 'form-control'
                self.fields['fe'].widget.attrs['class'] = 'form-control'
                self.fields['zn'].widget.attrs['class'] = 'form-control'
                

class SaleHarvestedCrop_Form(forms.ModelForm):
        mode_of_transport  = forms.ChoiceField(choices = MODE_OF_TRANSPORT_CHOICES, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        class Meta:
                model = SaleHarvestedCrop
                exclude=('enteredpersonel',)
        
        def __init__(self, *args, **kwargs):
                super(SaleHarvestedCrop_Form, self).__init__(*args, **kwargs)
                self.fields['date'].widget.attrs['class'] = 'form-control'
                self.fields['farm'].widget.attrs['class'] = 'form-control'
                self.fields['farm'].widget.attrs['readonly'] = True
                self.fields['plotID'].widget.attrs['class'] = 'form-control'
                self.fields['plotID'].widget.attrs['readonly'] = True
                self.fields['amount'].widget.attrs['class'] = 'form-control'
                self.fields['income'].widget.attrs['class'] = 'form-control'
                self.fields['income'].widget.attrs['readonly'] = True
                self.fields['marketprice'].widget.attrs['class'] = 'form-control'
                self.fields['mode_of_transport'].widget.attrs['class'] = 'form-control'
                self.fields['fare'].widget.attrs['class'] = 'form-control'
                self.fields['fuel_type'].widget.attrs['class'] = 'form-control'
                self.fields['fuel_type'].empty_label = "Choose Fuel"
                self.fields['fuel_cost'].widget.attrs['class'] = 'form-control'
                self.fields['distance_to_the_market'].widget.attrs['class'] = 'form-control'

class SoilMoistureProfiler_Form(forms.ModelForm):
        class Meta:
                model = SoilMoistureProfiler
                exclude=('enteredpersonel',)
        
        def __init__(self, *args, **kwargs):
                super(SoilMoistureProfiler_Form, self).__init__(*args, **kwargs)
                self.fields['date'].widget.attrs['class'] = 'form-control'
                self.fields['farm'].widget.attrs['class'] = 'form-control'
                self.fields['farm'].widget.attrs['readonly'] = True
                self.fields['plotID'].widget.attrs['class'] = 'form-control'
                self.fields['plotID'].widget.attrs['readonly'] = True
                self.fields['event'].widget.attrs['class'] = 'form-control'
                self.fields['depth_10'].widget.attrs['class'] = 'form-control'
                self.fields['depth_20'].widget.attrs['class'] = 'form-control'
                self.fields['depth_30'].widget.attrs['class'] = 'form-control'
                self.fields['depth_40'].widget.attrs['class'] = 'form-control'
                self.fields['depth_60'].widget.attrs['class'] = 'form-control'
                self.fields['depth_100'].widget.attrs['class'] = 'form-control'
    

class SoilMoistureMeasurementManagement_Form(forms.ModelForm):
        class Meta:
                model = SoilMoistureMeasurementManagement
                exclude=('enteredpersonel',)
        
        def __init__(self, *args, **kwargs):
                super(SoilMoistureMeasurementManagement_Form, self).__init__(*args, **kwargs)
                self.fields['date'].widget.attrs['class'] = 'form-control'
                self.fields['farm'].widget.attrs['class'] = 'form-control'
                self.fields['farm'].widget.attrs['readonly'] = True
                self.fields['plotID'].widget.attrs['class'] = 'form-control'
                self.fields['plotID'].widget.attrs['readonly'] = True
                self.fields['measurement_option'].widget.attrs['class'] = 'form-control'


class GravimetricSoilMoisture_Form(forms.ModelForm):
        class Meta:
                model = GravimetricSoilMoisture
                exclude=('enteredpersonel',)
        
        def __init__(self, *args, **kwargs):
                super(GravimetricSoilMoisture_Form, self).__init__(*args, **kwargs)
                self.fields['date'].widget.attrs['class'] = 'form-control'
                self.fields['farm'].widget.attrs['class'] = 'form-control'
                self.fields['farm'].widget.attrs['readonly'] = True
                self.fields['plotID'].widget.attrs['class'] = 'form-control'
                self.fields['plotID'].widget.attrs['readonly'] = True
                self.fields['event'].widget.attrs['class'] = 'form-control'
                self.fields['time_taken'].widget.attrs['class'] = 'form-control'
                self.fields['volume_core_used'].widget.attrs['class'] = 'form-control'
                self.fields['weight_core_used'].widget.attrs['class'] = 'form-control'
                self.fields['wet_weight'].widget.attrs['class'] = 'form-control'
                self.fields['dry_weight'].widget.attrs['class'] = 'form-control'
                self.fields['bulk_density'].widget.attrs['class'] = 'form-control'
                self.fields['gravimetric_moisture_content'].widget.attrs['class'] = 'form-control'
                self.fields['volumetric_moisture_content'].widget.attrs['class'] = 'form-control'
 


class CropMonitoringPlantHeight_Form(forms.ModelForm):
        row_number = forms.ChoiceField(choices = ROW_NUMBER_CHOICES, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        crop_stage  = forms.ChoiceField(choices = CROP_STAGE_CHOICES, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        totalPlant = forms.IntegerField(widget=forms.HiddenInput(attrs={'readonly':'True','class':'form-control'}))
        class Meta:
                model = CropMonitoringPlantHeight
                exclude=('enteredpersonel',)
        
        def __init__(self, *args, **kwargs):
                super(CropMonitoringPlantHeight_Form, self).__init__(*args, **kwargs)
                self.fields['date'].widget.attrs['class'] = 'form-control'
                self.fields['farm'].widget.attrs['class'] = 'form-control'
                self.fields['farm'].widget.attrs['readonly'] = True
                self.fields['plotID'].widget.attrs['class'] = 'form-control'
                self.fields['plotID'].widget.attrs['readonly'] = True
                self.fields['Crop'].widget.attrs['class'] = 'form-control'
                self.fields['crop_stage'].widget.attrs['class'] = 'form-control'
                self.fields['row_number'].widget.attrs['class'] = 'form-control'
                self.fields['number_of_good_plants'].widget.attrs['class'] = 'form-control'
                self.fields['number_of_bad_plants'].widget.attrs['class'] = 'form-control'
                self.fields['plant_density_per_bed'].widget.attrs['class'] = 'form-control'
                self.fields['plant_density_per_sqm'].widget.attrs['class'] = 'form-control'
                
                self.fields['plant_number'].widget.attrs['class'] = 'form-control'
                self.fields['LAI'].widget.attrs['class'] = 'form-control'
                self.fields['plant_height'].widget.attrs['class'] = 'form-control'
                self.fields['plant_canopy_width'].widget.attrs['class'] = 'form-control'
                self.fields['length_of_crop_stage'].widget.attrs['class'] = 'form-control'
                self.fields['plant_leave_number'].widget.attrs['class'] = 'form-control'
                self.fields['plant_leave_length'].widget.attrs['class'] = 'form-control'
                self.fields['plant_leave_width'].widget.attrs['class'] = 'form-control'
                
                self.fields['plant_number_two'].widget.attrs['class'] = 'form-control'
                self.fields['LAI_two'].widget.attrs['class'] = 'form-control'
                self.fields['plant_height_two'].widget.attrs['class'] = 'form-control'
                self.fields['plant_canopy_width_two'].widget.attrs['class'] = 'form-control'
                self.fields['length_of_crop_stage_two'].widget.attrs['class'] = 'form-control'
                self.fields['plant_leave_number_two'].widget.attrs['class'] = 'form-control'
                self.fields['plant_leave_length_two'].widget.attrs['class'] = 'form-control'
                self.fields['plant_leave_width_two'].widget.attrs['class'] = 'form-control'
                
                self.fields['plant_number_three'].widget.attrs['class'] = 'form-control'
                self.fields['LAI_three'].widget.attrs['class'] = 'form-control'
                self.fields['plant_height_three'].widget.attrs['class'] = 'form-control'
                self.fields['plant_canopy_width_three'].widget.attrs['class'] = 'form-control'
                self.fields['length_of_crop_stage_three'].widget.attrs['class'] = 'form-control'
                self.fields['plant_leave_number_three'].widget.attrs['class'] = 'form-control'
                self.fields['plant_leave_length_three'].widget.attrs['class'] = 'form-control'
                self.fields['plant_leave_width_three'].widget.attrs['class'] = 'form-control'
                
                self.fields['sub_plot_size'].widget.attrs['class'] = 'form-control'
                self.fields['sub_plot_plant_number'].widget.attrs['class'] = 'form-control'
                self.fields['total_plant_number'].widget.attrs['class'] = 'form-control'


class Nursery_Form(forms.ModelForm):
        class Meta:
                model = Nursery
                exclude=('enteredpersonel',)
        
        def __init__(self, *args, **kwargs):
                super(Nursery_Form, self).__init__(*args, **kwargs)
                self.fields['NurseryID'].widget.attrs['class'] = 'form-control'
                self.fields['area'].widget.attrs['class'] = 'form-control'
                self.fields['farm'].widget.attrs['readonly'] = True
                self.fields['seed'].widget.attrs['class'] = 'form-control'
                self.fields['date_bed_preparation'].widget.attrs['class'] = 'form-control'


class BedNursery_Form(forms.ModelForm):
        class Meta:
                model = BedNursery
                exclude=('enteredpersonel',)

        def __init__(self, *args, **kwargs):
                super(BedNursery_Form, self).__init__(*args, **kwargs)
                self.fields['length'].widget.attrs['class'] = 'form-control'
                self.fields['width'].widget.attrs['class'] = 'form-control'
                self.fields['area'].widget.attrs['class'] = 'form-control'
                self.fields['nursery'].widget.attrs['class'] = 'form-control'
                self.fields['numbers'].widget.attrs['class'] = 'form-control'
                self.fields['planting_density_per_bed'].widget.attrs['class'] = 'form-control'
                self.fields['seedrate'].widget.attrs['class'] = 'form-control'
                self.fields['seed_spacing_within_a_bed'].widget.attrs['class'] = 'form-control'
                self.fields['seed_spacing_btn_bed'].widget.attrs['class'] = 'form-control'


class SeedManagement_Form(forms.ModelForm):
        class Meta:
                model = SeedManagement
                exclude=('enteredpersonel',)

        def __init__(self, *args, **kwargs):
                super(SeedManagement_Form, self).__init__(*args, **kwargs)
                self.fields['date'].widget.attrs['class'] = 'form-control'
                self.fields['nursery'].widget.attrs['class'] = 'form-control'
                self.fields['seed'].widget.attrs['class'] = 'form-control'
                self.fields['quantity'].widget.attrs['class'] = 'form-control'
                self.fields['total_cost'].widget.attrs['class'] = 'form-control'
                self.fields['price_per_unit'].widget.attrs['class'] = 'form-control'



class ConsumedCrops_Form(forms.ModelForm):
        where_consumed = forms.ChoiceField(choices = WHERE_CONSUMED_CHOICES, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        how_consumed = forms.ChoiceField(choices = HOW_CONSUMED_CHOICES, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        class Meta:
                model = ConsumedCrops
                exclude=('enteredpersonel',)

        def __init__(self, *args, **kwargs):
                super(ConsumedCrops_Form, self).__init__(*args, **kwargs)
                self.fields['date'].widget.attrs['class'] = 'form-control'
                self.fields['farm'].widget.attrs['class'] = 'form-control'
                self.fields['plotID'].widget.attrs['class'] = 'form-control'
                self.fields['plotID'].widget.attrs['readonly'] = True
                self.fields['where_consumed'].widget.attrs['class'] = 'form-control'
                self.fields['how_consumed'].widget.attrs['class'] = 'form-control'
                self.fields['quantity'].widget.attrs['class'] = 'form-control'
                self.fields['marketprice'].widget.attrs['class'] = 'form-control'
                self.fields['totalvalue'].widget.attrs['class'] = 'form-control'

class TechnologyFailure_Form(forms.ModelForm):
        class Meta:
                model = TechnologyFailure
                exclude=('enteredpersonel',)

        def __init__(self, *args, **kwargs):
                super(TechnologyFailure_Form, self).__init__(*args, **kwargs)
                self.fields['date'].widget.attrs['class'] = 'form-control'
                self.fields['farm'].widget.attrs['class'] = 'form-control'
                self.fields['technology'].widget.attrs['class'] = 'form-control'
                self.fields['reason'].widget.attrs['class'] = 'form-control'



class FertilizerSpecificationForm(forms.ModelForm):
        farm =  forms.ModelChoiceField(queryset = Farm.objects.all(),widget=Select(attrs={'class': 'form-control seleckpicker'}),empty_label="Select Farmer")
        plotID =  forms.ModelChoiceField(queryset = Plot.objects.all(),widget=Select(attrs={'disabled':'True','class': 'form-control seleckpicker'}),empty_label="Choose Plot")
        class Meta:
                model = FertilizerSpecification
                exclude=('enteredpersonel',)

        def __init__(self, *args, **kwargs):
                super(FertilizerSpecificationForm, self).__init__(*args, **kwargs)
                self.fields['plotID'].widget.attrs['class'] = 'form-control'
                self.fields['farm'].widget.attrs['class'] = 'form-control'
                self.fields['fertilizer'].widget.attrs['class'] = 'form-control'
                self.fields['fertilizer'].widget.attrs['readonly'] = True
                self.fields['nitrogen'].widget.attrs['class'] = 'form-control'
                self.fields['phosphorus'].widget.attrs['class'] = 'form-control'
                self.fields['potassium'].widget.attrs['class'] = 'form-control'
                self.fields['sulphur'].widget.attrs['class'] = 'form-control'
                self.fields['organic_matter'].widget.attrs['class'] = 'form-control'





def validate_file_extension(value):
   if not value.name.endswith('.csv'):
      raise forms.ValidationError("Only CSV file is accepted")
   
class UploadFileForm(forms.Form):
        #title = forms.CharField(max_length=50)
        csv_file = forms.FileField()#label='Select a file',validators=[validate_file_extension])
   
'''

class PointOfInterestForm(forms.ModelForm):
        class Meta:
                model=PointOfInterest
                fields = ['name','position']
        def __init__(self, *args, **kwargs):
                super(PointOfInterestForm, self).__init__(*args, **kwargs)
                self.fields['name'].widget.attrs['class'] = 'form-control'
                self.fields['position'].widget.attrs['class'] = 'form-control'
'''




#class RemarkForm(forms.ModelForm):
        