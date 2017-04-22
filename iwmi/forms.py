from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.contrib.auth.forms import AuthenticationForm
from iwmi.models import People, Farm,Plot,Nursery, Pump,Country,Region,District,Village,Crop,Group,Farm,Fertilizer,Pesticide,Technology,Seed,Fuel,Soil,Spaire,WaterSources,WaterSourceCategory
from django.contrib import admin
from django.forms import ModelForm
from django import forms
from django.forms import Select
from django.contrib.admin.widgets import AdminTimeWidget
from django.utils.safestring import mark_safe

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
                        ('wholefield','Whole field'),
    )


CURRENCY_CHOICES =(
        ('Tsh','Tsh'),
        ('birr','Birr'),
        ('cedi','Cedi'),
        ('Usd','Usd'),
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

class FarmInfoForm(forms.Form):
        farmer =  forms.ModelChoiceField(queryset = People.objects.all().filter(role='Farmer'),widget=Select(attrs={'class': 'form-control seleckpicker'}),empty_label="Select Farmer")
        fieldID =  forms.ModelChoiceField(queryset = Plot.objects.all(),widget=Select(attrs={'disabled':'True','class': 'form-control seleckpicker'}),empty_label="Choose Region")
        #fieldID = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '#FieldID','class':'form-control'}),max_length=40)
        #field_type = forms.ChoiceField(choices = FIELD_TYPE_CHOICES, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        field_latitude = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#field latitude','class':'form-control'}))
        field_longitude = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#field longitude','class':'form-control'}))
        crop  = forms.ModelChoiceField(queryset = Crop.objects.all(),widget=Select(attrs={'class': 'form-control seleckpicker'}),empty_label="Choose crop")
        planting_method = forms.ChoiceField(choices = PLANTING_METHOD_CHOICES, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        planting_date = forms.DateField(widget=forms.TextInput(attrs={'placeholder': '#planting date','class':'form-control'}))
        fieldsize = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#field size','class':'form-control'}))
        water_application = forms.ChoiceField(choices = WATER_APPLICATION_CHOICES, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        water_management_method = forms.ChoiceField(choices = WATER_MANAGEMENT_METHOD_CHOICES, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        seed_rate = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#seed rate','class':'form-control'}))
        seed_date = forms.DateField(widget=forms.TextInput(attrs={'placeholder': '#seeding date','class':'form-control'}))
        bed_length = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#bed length','class':'form-control'}))
        bed_width = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#bed width','class':'form-control'}))
        bednumber = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '#bed number','class':'form-control'}))
        furrow_length = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#furrow length','class':'form-control'}))
        furrow_width = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#furrow width','class':'form-control'}))
        nfurrow  = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '#number of furrow','class':'form-control'}))
        WFD_yellow_depth = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#WFD yellow depth','class':'form-control'}))
        WFD_red_depth = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#WFD red depth','class':'form-control'}))
        TDR_length = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#TDR_length','class':'form-control'}))
        rootzone_depth  = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#Rootzone depth assumed','class':'form-control'}))
        #number_of_plots  = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '#number of plots','class':'form-control'}))
        
                
class NurseryForm(forms.Form):
        nurseryID  = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '#NurseryID','class':'form-control'}),max_length=25)
        area = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#nursery area','class':'form-control'}))
        plot = forms.ModelChoiceField(queryset = Plot.objects.all(),widget=Select(attrs={'class': 'form-control seleckpicker'}),empty_label="Choose Plot")
        date_bed_preparation = forms.DateField(widget=forms.TextInput(attrs={'placeholder': '#bed preparation date','class':'form-control'})) 
        seedprice  = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#seed price','class':'form-control'}))
        #= forms.DateField(widget=forms.TextInput(attrs={'placeholder': '#seedprice','class':'form-control'})) 
        bed_length = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#bed length','class':'form-control'}))
        bed_width = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#bed width','class':'form-control'}))
        bednumber = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '#bed number','class':'form-control'}))    
        seeding_date = forms.DateField(widget=forms.TextInput(attrs={'placeholder': '#seeding date','class':'form-control'})) 
        seed_per_bed = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '#seed per bed','class':'form-control'})) 
        seedtype = forms.ModelChoiceField(queryset = Seed.objects.all(),widget=Select(attrs={'class': 'form-control seleckpicker'}),empty_label="Choose seed")
        #technology = forms.ModelChoiceField(queryset = Technology.objects.all(),widget=Select(attrs={'class': 'form-control seleckpicker'}),empty_label="Choose Technology")
        #plant_spacing_btn_plants_within_rows = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#plant spacing btn plants within rows','class':'form-control'}))
        #plant_spacing_btn_rows = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#plant spacing btn rows','class':'form-control'}))
        labour  = forms.ChoiceField(choices = LABOUR_CHOICES, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        hired_female_number = forms.IntegerField(widget=forms.TextInput(attrs={'readonly':'True','placeholder':'#hired females','class':'form-control','required':'False'}))
        hired_male_number = forms.IntegerField(widget=forms.TextInput(attrs={'readonly':'True','placeholder': '#hired males','class':'form-control','required':'False'}))
        family_female_number = forms.IntegerField(widget=forms.TextInput(attrs={'readonly':'True','placeholder': '#family females','class':'form-control','required':'False'}))
        family_male_number = forms.IntegerField(widget=forms.TextInput(attrs={'readonly':'True','placeholder': '#family males','class':'form-control','required':'False'}))
        wage = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#wage price','class':'form-control'}))
        currency = forms.ChoiceField(choices = CURRENCY_CHOICES, widget=forms.Select(attrs={'class': 'seleckpicker'}))
      
class TransplantingForm(forms.Form):
        plot = forms.ModelChoiceField(queryset = Plot.objects.all(),widget=Select(attrs={'class': 'form-control seleckpicker'}),empty_label="Choose Plot")
        seedprice  = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#seed price','class':'form-control'}))
        #= forms.DateField(widget=forms.TextInput(attrs={'placeholder': '#seedprice','class':'form-control'}))
        trasplanting_date = forms.DateField(widget=forms.TextInput(attrs={'placeholder': '#trasplanting date','class':'form-control'}))
        plants_transplanted  = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#number of plants transplanted','class':'form-control'}))
        number_of_plants_per_row= forms.ModelChoiceField(queryset = Technology.objects.all(),widget=Select(attrs={'class': 'form-control seleckpicker'}),empty_label="Choose Technology")
        plant_spacing_btn_plants_within_rows = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#plant spacing btn plants within rows','class':'form-control'}))
        plant_spacing_btn_rows = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#plant spacing btn rows','class':'form-control'}))
        labour  = forms.ChoiceField(choices = LABOUR_CHOICES, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        hired_female_number = forms.IntegerField(widget=forms.TextInput(attrs={'readonly':'True','placeholder':'#hired females','class':'form-control','required':'False'}))
        hired_male_number = forms.IntegerField(widget=forms.TextInput(attrs={'readonly':'True','placeholder': '#hired males','class':'form-control','required':'False'}))
        family_female_number = forms.IntegerField(widget=forms.TextInput(attrs={'readonly':'True','placeholder': '#family females','class':'form-control','required':'False'}))
        family_male_number = forms.IntegerField(widget=forms.TextInput(attrs={'readonly':'True','placeholder': '#family males','class':'form-control','required':'False'}))
        wage = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#wage price','class':'form-control'}))
        currency = forms.ChoiceField(choices = CURRENCY_CHOICES, widget=forms.Select(attrs={'class': 'seleckpicker'}))
        number_of_plants_per_row = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#wage price','class':'form-control'}))
      

class NurseryIrrigationForm(forms.Form):
        date = forms.DateField(widget=forms.TextInput(attrs={'placeholder': '#nursery irrigation date','class':'form-control'})) 
        climate = forms.ChoiceField(choices =CLIMATE_CHOICES, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        nurseryID = forms.ModelChoiceField(queryset = Nursery.objects.all(),widget=Select(attrs={'class': 'form-control seleckpicker'}),empty_label="Choose nursery")
        time_started  = forms.TimeField(widget=forms.TimeInput(attrs={'placeholder': '#time_started','format':'%H:%M','class':'form-control timepicker'}))
        time_ended  = forms.TimeField(widget=forms.TimeInput(attrs={'placeholder': '#time_ended','format':'%H:%M','class':'form-control timepicker'}))
        total_time = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#total_time','class':'form-control'}))
        event = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#event','class':'form-control'}))
        bucket_volume = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#standard_volume','class':'form-control'}))
        bucket_numbers = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#number of buckets','class':'form-control'}))
        total_volume = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#total_volume','class':'form-control'}))
        #discharge = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#discharge','class':'form-control'}))
        labour  = forms.ChoiceField(choices = LABOUR_CHOICES, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        hired_female_number = forms.IntegerField(widget=forms.TextInput(attrs={'readonly':'True','placeholder':'#hired females','class':'form-control','required':'False'}))
        hired_male_number = forms.IntegerField(widget=forms.TextInput(attrs={'readonly':'True','placeholder': '#hired males','class':'form-control','required':'False'}))
        family_female_number = forms.IntegerField(widget=forms.TextInput(attrs={'readonly':'True','placeholder': '#family females','class':'form-control','required':'False'}))
        family_male_number = forms.IntegerField(widget=forms.TextInput(attrs={'readonly':'True','placeholder': '#family males','class':'form-control','required':'False'}))
        wage = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#wage price','class':'form-control'}))
        currency = forms.ChoiceField(choices = CURRENCY_CHOICES, widget=forms.Select(attrs={'class': 'seleckpicker'}))

FERTILIZER_TYPES_CHOICES = (
        ('','Choose..'),
        ("farmer's practice","farmer's practice"),
        ("DAP","DAP"),("NPS","NPS"),
        ("DAP-UREA","DAP-UREA"),("UREA","UREA"),("Compost","Compost")
    )

FERTILIZER_MANAGEMENT_CHOICES = (
        ('','Choose..'),
        ("farmer's practice","farmer's practice"),
        ("DAP","DAP"),("NPS","NPS"),("NPK","NPK"),
        ("DAP-UREA","DAP-UREA"),("UREA","UREA"),("Compost","Compost")
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

class FertilizerApplicationForm(forms.Form):
        date = forms.DateField(widget=forms.TextInput(attrs={'placeholder': '12/02/1989','class':'form-control'})) 
        farm = forms.ModelChoiceField(queryset = Farm.objects.all(),widget=Select(attrs={'class': 'form-control seleckpicker'}),empty_label="Choose Farm")
        fertilizer = forms.ModelChoiceField(queryset = Fertilizer.objects.all(),widget=Select(attrs={'class': 'form-control seleckpicker'}),empty_label="Choose..")
        fertilizer_management = forms.ChoiceField(choices = FERTILIZER_MANAGEMENT_CHOICES, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        quantity_kg = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#Quantity in Kg','class':'form-control'}))
        crop_stage  = forms.ChoiceField(choices = CROP_STAGE_CHOICES, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        nitrogen = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#nitrogen','class':'form-control'}))
        phosphorus = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#phosphorus','class':'form-control'}))
        potassium = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#potassium','class':'form-control'}))
        sulphur = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#sulphur','class':'form-control'}))
        organic_matter = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#organic_matter','class':'form-control'}))
        cost = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#cost','class':'form-control'}))
        labour  = forms.ChoiceField(choices = LABOUR_CHOICES, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        hired_female_number = forms.IntegerField(widget=forms.TextInput(attrs={'readonly':'True','placeholder':'#hired females','class':'form-control','required':'False'}))
        hired_male_number = forms.IntegerField(widget=forms.TextInput(attrs={'readonly':'True','placeholder': '#hired males','class':'form-control','required':'False'}))
        family_female_number = forms.IntegerField(widget=forms.TextInput(attrs={'readonly':'True','placeholder': '#family females','class':'form-control','required':'False'}))
        family_male_number = forms.IntegerField(widget=forms.TextInput(attrs={'readonly':'True','placeholder': '#family males','class':'form-control','required':'False'}))
        wage = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#wage price','class':'form-control'}))
        currency = forms.ChoiceField(choices = CURRENCY_CHOICES, widget=forms.Select(attrs={'class': 'seleckpicker'}))
        
class PesticideApplicationForm(forms.Form):
        date = forms.DateField(widget=forms.TextInput(attrs={'placeholder': '12/02/1989','class':'form-control'})) 
        farm = forms.ModelChoiceField(queryset = Farm.objects.all(),widget=Select(attrs={'class': 'form-control seleckpicker'}),empty_label="Choose Farm")
        pesticide = forms.ModelChoiceField(queryset = Pesticide.objects.all(),widget=Select(attrs={'class': 'form-control seleckpicker'}),empty_label="Choose..")
        form  = forms.ChoiceField(choices = FORM_CHOICES, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        crop_stage  = forms.ChoiceField(choices = CROP_STAGE_CHOICES, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        quantity_lt = forms.FloatField(widget=forms.TextInput(attrs={'readonly':'True','placeholder': '#Quantity in Litre','class':'form-control'}))
        quantity_kg = forms.FloatField(widget=forms.TextInput(attrs={'readonly':'True','placeholder': '#Quantity in Kg','class':'form-control'}))
        cost = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#cost','class':'form-control'}))
        #applied_personels =forms.ModelMultipleChoiceField(queryset=People.objects.all(),widget=forms.SelectMultiple(attrs={'class': 'form-control seleckpicker'}),required=True)
        labour  = forms.ChoiceField(choices = LABOUR_CHOICES, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        hired_female_number = forms.IntegerField(widget=forms.TextInput(attrs={'readonly':'True','placeholder':'#hired females','class':'form-control','required':'False'}))
        hired_male_number = forms.IntegerField(widget=forms.TextInput(attrs={'readonly':'True','placeholder': '#hired males','class':'form-control','required':'False'}))
        family_female_number = forms.IntegerField(widget=forms.TextInput(attrs={'readonly':'True','placeholder': '#family females','class':'form-control','required':'False'}))
        family_male_number = forms.IntegerField(widget=forms.TextInput(attrs={'readonly':'True','placeholder': '#family males','class':'form-control','required':'False'}))
        wage = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#wage price','class':'form-control'}))
        currency = forms.ChoiceField(choices = CURRENCY_CHOICES, widget=forms.Select(attrs={'class': 'seleckpicker'}))

class WaterLiftingCalibrationForm(forms.Form):
        date = forms.DateField(widget=forms.TextInput(attrs={'placeholder': '12/02/1989','class':'form-control'})) 
        farm = forms.ModelChoiceField(queryset = Farm.objects.all(),widget=Select(attrs={'class': 'form-control seleckpicker'}),empty_label="Choose Farm")
        technology = forms.ModelChoiceField(queryset = Technology.objects.all(),widget=Select(attrs={'class': 'form-control seleckpicker'}),empty_label="Choose Group")
        #repetition = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '#repetition','class':'form-control'}))
        bucketvolume = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#bucketvolume','class':'form-control'}))
        start_time = forms.TimeField(widget=forms.TimeInput(attrs={'placeholder': '#start time','format':'%H:%M','class':'form-control timepicker'}))
        end_time  = forms.TimeField(widget=forms.TimeInput(attrs={'placeholder': '#end time','format':'%H:%M','class':'form-control timepicker'}))
        #forms.TimeField(widget=forms.TimeInput(format='%H:%M'))
        #forms.TimeField(widget=forms.TimeInput(format='%H:%M'))
        total_time  = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#total time','class':'form-control'}))
        discharge = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#discharge','class':'form-control'}))   
    

class ApplicationCalibrationForm(forms.Form):
        date = forms.DateField(widget=forms.TextInput(attrs={'placeholder': '12/02/1989','class':'form-control'})) 
        farm = forms.ModelChoiceField(queryset = Farm.objects.all(),widget=Select(attrs={'class': 'form-control seleckpicker'}),empty_label="Choose Farm")
        water_application  = forms.ChoiceField(choices = WATER_APPLICATION_CHOICES, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        #repetition = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '#repetition','class':'form-control'}))
        bucketvolume = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#bucketvolume','class':'form-control'}))
        start_time = forms.TimeField(widget=forms.TimeInput(attrs={'placeholder': '#start time','format':'%H:%M','class':'form-control timepicker'}))
        end_time  = forms.TimeField(widget=forms.TimeInput(attrs={'placeholder': '#end time','format':'%H:%M','class':'form-control timepicker'}))
        #forms.TimeField(widget=forms.TimeInput(format='%H:%M'))
        #forms.TimeField(widget=forms.TimeInput(format='%H:%M'))
        total_time  = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#total time','class':'form-control'}))
        discharge = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#discharge','class':'form-control'}))   
        bucketnumbers = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '#Integer','class':'form-control'}))   
        furrowefficiency = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#furrowefficiency','class':'form-control'}))
        waterheight = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#waterheight','class':'form-control'}))
        topfurrowwidth = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#topfurrowwidth','class':'form-control'}))
        buttonfurrowwidth = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#buttonfurrowwidth','class':'form-control'}))
        wetteddiameteraroundplant = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#wetteddiameteraroundplant','class':'form-control'}))
        irrigate_whole_or_per_plant  = forms.ChoiceField(choices = IRRIGATE_WHOLE_OR_PER_PLANT_CHOICES, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        
WFD_IRRIGATION_CHOICES =(
        ('','Choose...'),
        ('Yes','Yes'),
        ('No','No'),
)

class FarmIrrigationForm(forms.Form):
        date = forms.DateField(widget=forms.TextInput(attrs={'placeholder': '12/02/1989','class':'form-control'})) 
        farm = forms.ModelChoiceField(queryset = Farm.objects.all(),widget=Select(attrs={'class': 'form-control seleckpicker'}),empty_label="Choose Farm")
        #irrigation_event = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '#irrigation event','class':'form-control'}))
        #technology = forms.ModelChoiceField(queryset = Technology.objects.all(),widget=Select(attrs={'class': 'form-control seleckpicker'}),empty_label="Choose technology")       
        start_time = forms.TimeField(widget=forms.TimeInput(attrs={'placeholder': '#start time','class':'form-control timepicker'}))
        end_time  = forms.TimeField(widget=forms.TimeInput(attrs={'placeholder': '#end time','class':'form-control timepicker'}))
        #total_time = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#total time','class':'form-control'}))
        quantification_method = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '#Quantification method','class':'form-control'}),max_length=30)
        flume_location  = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '#Flume location','class':'form-control'}),max_length=30)
        waterlevel1 = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#water level 1','class':'form-control'})) 
        waterlevel2 = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#water level 1','class':'form-control'}))
        furrow_irr_time = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#furrow irrigation time','class':'form-control'})) 
        nfurrorws_irrigated_once = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '#furrow numbers','class':'form-control'}))
        discharge = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#dicharge','class':'form-control'}))
        standardvolume  = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#standard volume','class':'form-control'}))
        quantity_of_units  = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#quantity of units','class':'form-control'}))
        yellow_WFD_before_irrigation  = forms.ChoiceField(choices = WFD_IRRIGATION_CHOICES, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        red_WFD_before_irrigation = forms.ChoiceField(choices = WFD_IRRIGATION_CHOICES, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        yellow_WFD_time_after_irrigation  = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#yellow WFD time after irrigation','class':'form-control'})) 
        red_WFD_time_after_irrigation = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#red WFD time after irrigation','class':'form-control'}))
        climate   = forms.ChoiceField(choices =CLIMATE_CHOICES, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        fuel = forms.ModelChoiceField(queryset = Fuel.objects.all(),widget=Select(attrs={'class': 'form-control seleckpicker'}),empty_label="Choose Fuel")
        fuelcost = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#fuel cost','class':'form-control'}))
        currency = forms.ChoiceField(choices = CURRENCY_CHOICES, widget=forms.Select(attrs={'class': 'seleckpicker'}))
        amount_used  = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#amount used','class':'form-control'}))
        refilled_amount  = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#refilled amount','class':'form-control'}))
        water_application = forms.ChoiceField(choices = WATER_APPLICATION_CHOICES, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        irrigate_whole_or_per_plant  = forms.ChoiceField(choices = IRRIGATE_WHOLE_OR_PER_PLANT_CHOICES, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        
        
class SoilForm(forms.Form):
        date = forms.DateField(widget=forms.TextInput(attrs={'placeholder': '12/02/1989','class':'form-control'}))
        farm =  forms.ModelChoiceField(queryset = Farm.objects.all(),widget=Select(attrs={'class': 'form-control seleckpicker'}),empty_label="Choose Farm")
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
        

SOIL_MOISTURE_CHOICES=(
        ('','Choose..'),('gravimetric','Gravimetric'),('TDR','TDR'),
        #('Soil moisture profiler','Soil moisture profiler'),('Other','Other, please specify')
    )
class SoilMoistureMeasurementForm(forms.Form):
        measurement_option  = forms.ChoiceField(choices = SOIL_MOISTURE_CHOICES, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        date = forms.DateField(widget=forms.TextInput(attrs={'placeholder': '12/02/1989','class':'form-control'}))
        farm =  forms.ModelChoiceField(queryset = Farm.objects.all(),widget=Select(attrs={'class': 'form-control seleckpicker'}),empty_label="Choose Farm")
        #event = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '#event number','class':'form-control'}))
        measurement = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#tdr measurement','class':'form-control'}))
        time  = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#time taken','class':'form-control'}))
        depth_sample  = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#Depth sample','class':'form-control'}))
        volume_core_used  = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#volume core used','class':'form-control'}))
        weight_core_used = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#weight core used','class':'form-control'}))
        wet_weight = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#wet weight','class':'form-control'}))
        dry_weight = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#dry weight','class':'form-control'}))
        bulk_density = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#bulk density','class':'form-control'}))
        gravimetric_moisture_content = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#gravimetric moisture content','class':'form-control'}))
        volumetric_moisture_content = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#volumetric moisture content','class':'form-control'}))

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
class TissueNutrientAnalysisForm(forms.Form):
        date = forms.DateField(widget=forms.TextInput(attrs={'placeholder': '12/02/1989','class':'form-control'}))
        farm =  forms.ModelChoiceField(queryset = Farm.objects.all(),widget=Select(attrs={'class': 'form-control seleckpicker'}),empty_label="Choose Farm")
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
        technology =  forms.ModelChoiceField(queryset = Technology.objects.all(),widget=Select(attrs={'class': 'form-control seleckpicker'}),empty_label="Choose Farm")
        reason = forms.CharField(widget=forms.Textarea(attrs={'placeholder': '#write down reason(s) for failure','class':'form-control'}))

DRY_FRESH_CHOICES=(
        ('dry','Dry'),
        ('fresh','Fresh')
)


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
        area = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#area','class':'form-control'}))
        #fresh = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class':'form-control','default':'True'}))
        #dry = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class':'form-control','default':'False'}))
        marketable_yield = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#marketable yield','class':'form-control'}))
        unmarketable_yield = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#unmarketable yield','class':'form-control'}))
        biomas = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#biomas','class':'form-control'}))
        dry_fresh =  forms.ChoiceField(widget=forms.RadioSelect(attrs={'class' : 'radio-inline form-control'},renderer=HorizRadioRenderer),choices=DRY_FRESH_CHOICES)
        quantity_harvested = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#quantity harvested','class':'form-control'}))
        #forms.ChoiceField(required = True, choices = DRY_FRESH_CHOICES, widget=forms.RadioSelect(attrs={'class' : 'radio-inline form-control'}))
        payement =  forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#payement','class':'form-control'}))
        labour  = forms.ChoiceField(choices = LABOUR_CHOICES, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        hired_female_number = forms.IntegerField(widget=forms.TextInput(attrs={'readonly':'True','placeholder':'#number of hired female','class':'form-control','required':'False'}))
        hired_male_number = forms.IntegerField(widget=forms.TextInput(attrs={'readonly':'True','placeholder': '#number of hired male','class':'form-control','required':'False'}))
        family_female_number = forms.IntegerField(widget=forms.TextInput(attrs={'readonly':'True','placeholder': '#number of family female','class':'form-control','required':'False'}))
        family_male_number = forms.IntegerField(widget=forms.TextInput(attrs={'readonly':'True','placeholder': '#number of family male','class':'form-control','required':'False'}))
        
    
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
        plot = forms.ModelChoiceField(queryset = Farm.objects.all(),widget=Select(attrs={'disabled':'True','class': 'form-control seleckpicker'}),empty_label="Choose Plot")
        harvesting_method  = forms.ChoiceField(choices = HARVESTING_METHOD_CHOICES, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        dry_fresh =  forms.ChoiceField(widget=forms.RadioSelect(attrs={'class' : 'radio-inline form-control'},renderer=HorizRadioRenderer),choices=DRY_FRESH_CHOICES)
        area = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#area','class':'form-control'}))
        marketable_produce = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '#number of marketable produce','class':'form-control'}))
        unmarketable_produce= forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '#number of unmarketable produce','class':'form-control'}))
        marketable_produce_weight = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '#weight of marketable produce','class':'form-control'}))
        unmarketable_produce_weight= forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '#weight of unmarketable produce','class':'form-control'}))
    
    
class PlantLevelYieldForm(forms.Form):
        date = forms.DateField(widget=forms.TextInput(attrs={'placeholder': '12/02/1989','class':'form-control'}))
        farm =  forms.ModelChoiceField(queryset = Farm.objects.all(),widget=Select(attrs={'class': 'form-control seleckpicker'}),empty_label="Choose Farm")
        harvesting_method  = forms.ChoiceField(choices = HARVESTING_METHOD_CHOICES, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        dry_fresh =  forms.ChoiceField(widget=forms.RadioSelect(attrs={'class' : 'radio-inline form-control'},renderer=HorizRadioRenderer),choices=DRY_FRESH_CHOICES)
        plot = forms.ModelChoiceField(queryset = Farm.objects.all(),widget=Select(attrs={'disabled':'True','class': 'form-control seleckpicker'}),empty_label="Choose Plot")
        plant_number  = forms.ChoiceField(choices = PLANT_NUMBER_CHOICES, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        marketable_produced = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '#marketable produce','class':'form-control'}))
        unmarketable_produced = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '#unmarketable produce','class':'form-control'}))
        marketable_produced_weight = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#weight of marketable produce','class':'form-control'}))
        unmarketable_produced_weight = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#weight of unmarketable produce','class':'form-control'}))
        diameter_width_produced =  forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#diameter/width produced','class':'form-control'}))
        length =  forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#length','class':'form-control'}))
        residual_biomass =  forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#residual biomas','class':'form-control'}))
        

class CropMonitoringPlantHeightForm(forms.Form):
        date = forms.DateField(widget=forms.TextInput(attrs={'placeholder': '12/02/1989','class':'form-control'}))
        farm =  forms.ModelChoiceField(queryset = Farm.objects.all(),widget=Select(attrs={'class': 'form-control seleckpicker'}),empty_label="Choose Farm")
        crop_stage  = forms.ChoiceField(choices = CROP_STAGE_CHOICES, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        plot = forms.ModelChoiceField(queryset = Farm.objects.all(),widget=Select(attrs={'disabled':'True','class': 'form-control seleckpicker'}),empty_label="Choose Plot")
        plant_density_per_bed =  forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#plant density per bed','class':'form-control'}))
        plant_density_per_sqm  =  forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#plant density per sqm','class':'form-control'}))
        number_of_good_plants  =  forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '#number of good plants','class':'form-control'}))
        number_of_bad_plants  =  forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '#number of bad plants','class':'form-control'}))
        plant_number = forms.ChoiceField(choices = PLANT_NUMBER_CHOICES, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        plant_height = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#plant height','class':'form-control'}))
        plant_canopy_width = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#plant canopy width','class':'form-control'}))
        lenght_of_crop_stage = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#lenght_of_crop_stage','class':'form-control'}))
        plant_leave_number = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '#plant leave number','class':'form-control'}))
        plant_leave_length = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#plant leave length','class':'form-control'}))
        plant_leave_width = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#plant leave width','class':'form-control'}))

    

class WeedingForm(forms.Form):
        date = forms.DateField(widget=forms.TextInput(attrs={'placeholder': '12/02/1989','class':'form-control'}))
        farm =  forms.ModelChoiceField(queryset = Farm.objects.all(),widget=Select(attrs={'class': 'form-control seleckpicker'}),empty_label="Choose Farm")
        weed_activities = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '#weed activity','class':'form-control'}),max_length=40)
        crop  = forms.ModelChoiceField(queryset = Crop.objects.all(),widget=Select(attrs={'class': 'form-control seleckpicker'}),empty_label="Choose crop")
        time =  forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#time taken','class':'form-control'}))
        payment =  forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#payment','class':'form-control'}))
        labour  = forms.ChoiceField(choices = LABOUR_CHOICES, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        hired_female_number = forms.IntegerField(widget=forms.TextInput(attrs={'readonly':'True','placeholder':'#number of hired female','class':'form-control','required':'False'}))
        hired_male_number = forms.IntegerField(widget=forms.TextInput(attrs={'readonly':'True','placeholder': '#number of hired male','class':'form-control','required':'False'}))
        family_female_number = forms.IntegerField(widget=forms.TextInput(attrs={'readonly':'True','placeholder': '#number of family female','class':'form-control','required':'False'}))
        family_male_number = forms.IntegerField(widget=forms.TextInput(attrs={'readonly':'True','placeholder': '#number of family male','class':'form-control','required':'False'}))
        wage = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#wage price','class':'form-control'}))
        currency = forms.ChoiceField(choices = CURRENCY_CHOICES, widget=forms.Select(attrs={'class': 'seleckpicker'}))
    

class ServiceRepaireForm(forms.Form):
        date = forms.DateField(widget=forms.TextInput(attrs={'placeholder': '12/02/1989','class':'form-control'}))
        group = forms.ModelChoiceField(queryset = Group.objects.all(),widget=Select(attrs={'class': 'form-control seleckpicker'}),empty_label="Choose Farm")
        repaire_type = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '#Type of repaires','class':'form-control'}),max_length=100)
        spaire = forms.ModelMultipleChoiceField(queryset=Spaire.objects.all(),widget=forms.SelectMultiple(attrs={'class': 'form-control seleckpicker'}),required=True)
        pump = forms.ModelChoiceField(queryset = Pump.objects.all(),widget=Select(attrs={'class': 'form-control seleckpicker'}),empty_label="Choose Pump")
        price = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#Price of spaire parts','class':'form-control'}))
        currency = forms.ChoiceField(choices = CURRENCY_CHOICES, widget=forms.Select(attrs={'class': 'seleckpicker'}))
        #models.FloatField('Price of spaire parts (Tsh)')
        #total_cost = models.FloatField('Total repaire cost (Tsh)')

LAND_PREPARATION_TOOL_CHOICES=(
        ('','Choose..'),
        ('Hoe','Hoe'),
        ('Oxen&plough','Oxen and plough'),
        ('Cutlass','Cutlass'),
        ('Tractor','Tractor'),
)      

class LandPreparationForm(forms.Form):
        date = forms.DateField(widget=forms.TextInput(attrs={'placeholder': '12/02/1989','class':'form-control'}))
        farm =  forms.ModelChoiceField(queryset = Farm.objects.all(),widget=Select(attrs={'class': 'form-control seleckpicker'}),empty_label="Choose Farm")
        plot =  forms.ModelChoiceField(queryset = Plot.objects.all(),widget=Select(attrs={'class': 'form-control seleckpicker'}),empty_label="Choose Plot")
        landpreparationtool = forms.ChoiceField(choices =LAND_PREPARATION_TOOL_CHOICES, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        labour  = forms.ChoiceField(choices = LABOUR_CHOICES, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        hired_female_number = forms.IntegerField(widget=forms.TextInput(attrs={'readonly':'True','placeholder':'#number of hired female','class':'form-control','required':'False'}))
        hired_male_number = forms.IntegerField(widget=forms.TextInput(attrs={'readonly':'True','placeholder': '#number of hired male','class':'form-control','required':'False'}))
        family_female_number = forms.IntegerField(widget=forms.TextInput(attrs={'readonly':'True','placeholder': '#number of family female','class':'form-control','required':'False'}))
        family_male_number = forms.IntegerField(widget=forms.TextInput(attrs={'readonly':'True','placeholder': '#number of family male','class':'form-control','required':'False'}))
        wage =  forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#payment','class':'form-control'}))
        currency = forms.ChoiceField(choices = CURRENCY_CHOICES, widget=forms.Select(attrs={'readonly':'True','class': 'seleckpicker'}))

LAND_CLEARANCE_CHOICES=(
        ('','Choose..'),
        ('ManualClearance','Manual clearance'),
        ('Burning','Burning'),
        ('HerbicicdeApplication','Herbicide application'),
        ('Mechanical','Mechanical'),
)      
    

class LandCleareanceForm(forms.Form):
        date = forms.DateField(widget=forms.TextInput(attrs={'placeholder': '12/02/1989','class':'form-control'}))
        farm =  forms.ModelChoiceField(queryset = Farm.objects.all(),widget=Select(attrs={'class': 'form-control seleckpicker'}),empty_label="Choose Farm")
        plot =  forms.ModelChoiceField(queryset = Plot.objects.all(),widget=Select(attrs={'class': 'form-control seleckpicker'}),empty_label="Choose Plot")
        landpreparationtool = forms.ChoiceField(choices =LAND_CLEARANCE_CHOICES, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        labour  = forms.ChoiceField(choices = LABOUR_CHOICES, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        hired_female_number = forms.IntegerField(widget=forms.TextInput(attrs={'readonly':'True','placeholder':'#number of hired female','class':'form-control','required':'False'}))
        hired_male_number = forms.IntegerField(widget=forms.TextInput(attrs={'readonly':'True','placeholder': '#number of hired male','class':'form-control','required':'False'}))
        family_female_number = forms.IntegerField(widget=forms.TextInput(attrs={'readonly':'True','placeholder': '#number of family female','class':'form-control','required':'False'}))
        family_male_number = forms.IntegerField(widget=forms.TextInput(attrs={'readonly':'True','placeholder': '#number of family male','class':'form-control','required':'False'}))
        wage =  forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#payment','class':'form-control'}))
        currency = forms.ChoiceField(choices = CURRENCY_CHOICES, widget=forms.Select(attrs={'readonly':'True','class': 'seleckpicker'}))
        
