from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.contrib.auth.forms import AuthenticationForm
from iwmiproject.models import People, RelationManager, Country,Region,District,Village,WaterSources,WaterSourceCategory,Technology
from django.contrib import admin
from django.forms import ModelForm
from django import forms
from django.forms import Select


class LoginForm(AuthenticationForm):#(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'username','class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'password','class':'form-control','render_value':'False'}))
    #forms.CharField(label=(u'password'), widget=forms.PasswordInput(render_value=False))
    remember_me = forms.BooleanField(required=False, widget=forms.CheckboxInput())


'''
class PeopleForm(admin.ModelAdmin):
    class Meta:
        model = People
        field = ['personID','firstname','middlename','lastname','gender','role','village']
'''
GENDER_CHOICE=(
        ('','Choose gender..'),
        ('M','Male'),
        ('F','Female'), 
    )

ROLE_CHOICES=(
        ('','Choose role..'),
        ('ST','Students'),
        ('RA','Research assistant'),
        #('TR','Team leader'),
        ('RS','Researcher'),
        #('Image','Image Adder')
    )

INSTITUTION_CHOICE=(
        ('','Choose institution..'),
        ('BDU','BDU'),
        ('IFPRI','IFPRI'),
        ('ILRI','ILRI'),
        ('IWMI','IWMI'),
        ('NCAT','NCAT'),
        ('SUA','SUA'),
        ('TexasA&M','TexasA&M'),
        ('UDS','UDS'),
        ('USAID','USAID')
        
    )

TECHNOLOGY_CHOICES=(
        ('','Choose..'),('Rope and bucket','Rope and bucket'),('pulley and bucket','Pulley and bucket'),('pulley and tank','Pulley and tank'),('Rope and washer','Rope and washer'),
        ('petrol motorized pump','Petrol motorized pump'),('solar pump','Solar pump'),
        ('tractor mounted pump','Tractor mounted pump'),
        #('','Choose..'),('Pulley','Pulley'),('Pulley with tank','Pulley with tank'),('Rope and washer','Rope and washer'),
        #('Rope and washer with hose','Rope and washer with hose'),('Diesel motorized pump','Diesel motorized pump'),('Solar pump','Solar pump'),
        #('Drip','Drip'),('drip+mounted motorized pump','drip+mounted motorized pump'),('UDS drip (Ghana)','UDS drip (Ghana)')
    )

FARMER_ROLE_CHOICES=(
        ('','Choose role..'),
        ('HH','Household head'),
        ('SHH','Spouse of the household head'),
        ('FM','Family member'),
       )

AGE_GROUP_CHOICES =(
        ('','Choose age group..'),
        ('B21','15 to 21'),
        ('B30','21 to 30'),
        ('B40','31 to 40'),
        ('B50','41 to 50'),
        ('B60','51 to 60'),
        ('A60','61 and above'),
       )

REGISTER_NUMBER_CHOICES=(
    ('','Choose..'),
    (1,'One'),
    (2,'Two'),
    (3,'Three'),
    (4,'Four'),
    (5,'Five')
    
)
REGISTER_SELECT_CHOICES=(
    ('','Choose..'),
    ('Yes','Yes'),
    ('No','No'),
)
GROUP_CHOICE_SELECT = (
    ('','Choose...'),
    ('Yes','Yes'),
    ('No','No'),
)
my_default_errors = {
    #'required': 'This field is required',
    #^\d{4}\d{3}\d{3}$
    'invalid': 'Enter a valid phone(e.g 0712112234)'
}
LANDOWNERSHIP_CHOICE_SELECT = (
    ('','Choose...'),
    ('All owned','All owned'),
    ('Partly owned','Partly owned'),
    ('All rented','All rented'),
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
#'error_messages':'my_default_errors',+255 717 665 567,+16 590 165 367
class PeopleForm(forms.Form):
    register_select  = forms.ChoiceField(choices =REGISTER_SELECT_CHOICES, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
    #register_number_choice = forms.ChoiceField(choices =REGISTER_NUMBER_CHOICES, widget=forms.Select(attrs={'readonly':'True','class': 'form-control seleckpicker'}))
    group =  forms.CharField(widget=forms.TextInput(attrs={'placeholder': '#group','class':'form-control'}),max_length=45)
    #personID =  forms.CharField(widget=forms.TextInput(attrs={'placeholder': '#farmerID','class':'form-control'}),max_length=45)
    firstname = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '#First Name','class':'form-control'}),max_length=80)
    middlename = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '#Middle Name','class':'form-control'}),max_length=80,required=False)
    lastname = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '#Last Name','class':'form-control'}),max_length=80)
    gender = forms.ChoiceField(choices = GENDER_CHOICE, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'pattern':"^\d{4}\d{3}\d{3}$",'placeholder': '0717112233','class':'form-control'}),max_length=50,required=False)
    #phone  = forms.RegexField(regex=r'^\+?1?\d{9,15}$', error_message = ("Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."))
    role = forms.ChoiceField(choices =FARMER_ROLE_CHOICES, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
    age_group = forms.ChoiceField(choices =AGE_GROUP_CHOICES, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
    groupchoice  = forms.ChoiceField(choices =GROUP_CHOICE_SELECT, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
    #institution = forms.ChoiceField(choices = INSTITUTION_CHOICE, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
    
    water_source = forms.ModelChoiceField(queryset = WaterSources.objects.all(),widget=Select(attrs={'class': 'form-control seleckpicker'}),empty_label="Choose water source")
    pumping_source = forms.ModelChoiceField(queryset = WaterSourceCategory.objects.all(),widget=Select(attrs={'disabled':'True','class': 'form-control seleckpicker'}),empty_label="Choose pumping source")
    technology = forms.ModelChoiceField(queryset = Technology.objects.all(),widget=Select(attrs={'class': 'form-control seleckpicker'}),empty_label="Choose technology")
    #= forms.ChoiceField(choices = TECHNOLOGY_CHOICES, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
    technology_date = forms.DateField(widget=forms.TextInput(attrs={'placeholder': '#technology installation date','class':'form-control'})) 
    well_latitude_degree = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#degree','class':'form-control'}))
    well_latitude_minutes = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#minutes','class':'form-control'}))
    well_latitude_seconds = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#seconds','class':'form-control'}))
    well_latitude_direction = forms.ChoiceField(choices =LATITUDE_DIRECTION_CHOICES, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
    
    well_longitude_degree = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#degree','class':'form-control'}))
    well_longitude_minutes = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#minutes','class':'form-control'}))
    well_longitude_seconds = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#seconds','class':'form-control'}))
    well_longitude_direction = forms.ChoiceField(choices =LONGITUDE_DIRECTION_CHOICES, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
    
    elevation = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#elevation','class':'form-control'}))
    well_depth = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#well depth','class':'form-control'}))
    well_diameter = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#well diameter','class':'form-control'}))
    household_members = forms.ModelMultipleChoiceField(queryset=People.objects.all(),widget=forms.SelectMultiple(attrs={'readonly':'True','class': 'form-control seleckpicker'}),required=False)
    
   #total_land_holding = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#total land holding','class':'form-control'}))
    #total_irrigated_plots_land = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#total irrigated land','class':'form-control'}))
    #total_irrigated_plots  = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#number of irrigated plots','class':'form-control'}))
    
    number_of_plots = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#number of plots','class':'form-control'}))
    landownership = forms.ChoiceField(choices =LANDOWNERSHIP_CHOICE_SELECT, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
    rented_land = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#rented land','class':'form-control'}))
    owned_land = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#owned land','class':'form-control'}))
    #partly_owned_land = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#partly owned','class':'form-control'}))
    total_irrigated_owned_land = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#irrigated owned land','class':'form-control'}))
    total_irrigated_rented_land = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#irrigated rented land','class':'form-control'}))
    irrigated_plots = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#total irrigated plots','class':'form-control'}))

#number_of_plots,landownership,rented_land,owned_land,total_irrigated_owned_land,total_irrigated_rented_land,irrigated_plots

class LocationForm(forms.Form):
    country =  forms.ModelChoiceField(queryset = Country.objects.all(),widget=Select(attrs={'class': 'form-control seleckpicker'}),empty_label="Choose Country")
    region =  forms.ModelChoiceField(queryset = Region.objects.all(),widget=Select(attrs={'disabled':'True','class': 'form-control seleckpicker'}),empty_label="Choose Region")
    district =  forms.ModelChoiceField(queryset = District.objects.all(),widget=Select(attrs={'disabled':'True','class': 'form-control seleckpicker'}),empty_label="Choose District")
    village =  forms.ModelChoiceField(queryset = Village.objects.all(),widget=Select(attrs={'disabled':'True','class': 'form-control seleckpicker'}),empty_label="Choose Village",to_field_name="village")

class HouseForm(forms.Form):
    house_latitude_degree = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#degree','class':'form-control'}))
    house_latitude_minute = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#minutes','class':'form-control'}))
    house_latitude_second = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#seconds','class':'form-control'}))
    house_latitude_direction = forms.ChoiceField(choices =LATITUDE_DIRECTION_CHOICES, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
    
    house_longitude_degree = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#degree','class':'form-control'}))
    house_longitude_minute = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#minutes','class':'form-control'}))
    house_longitude_second = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#seconds','class':'form-control'}))
    house_longitude_direction = forms.ChoiceField(choices =LONGITUDE_DIRECTION_CHOICES, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
    
    House_elevation= forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '#house elevation','class':'form-control'}))
    
class registerUserForm(forms.Form):
    username =  forms.CharField(widget=forms.TextInput(attrs={'placeholder': '#username','class':'form-control'}),max_length=45)
    firstname = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '#First Name','class':'form-control'}),max_length=80)
    middlename = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '#Middle Name','class':'form-control'}),max_length=80,required=False)
    lastname = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '#Last Name','class':'form-control'}),max_length=80)
    gender = forms.ChoiceField(choices = GENDER_CHOICE, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '0717112233','class':'form-control'}),max_length=50)
    role = forms.ChoiceField(choices = ROLE_CHOICES, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
    institution = forms.ChoiceField(choices = INSTITUTION_CHOICE, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
    #village =  forms.ModelChoiceField(queryset = Village.objects.all(),widget=Select(attrs={'class': 'form-control seleckpicker'}),empty_label="Choose village")
    country =  forms.ModelChoiceField(queryset = Country.objects.all(),widget=Select(attrs={'class': 'form-control seleckpicker'}),empty_label="Choose Country")
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': '#email','class':'form-control'}),max_length=45)

    

