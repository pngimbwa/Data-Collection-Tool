from django.db import models
from django.contrib.auth.models import User #help us to access User object
#from geoposition.fields import GeopositionField
import datetime
from data_importer.importers import CSVImporter



# Create your models here.
class Country(models.Model):
    name = models.CharField('Name',primary_key=True,max_length=50)
    
    class Meta:
        ordering =['name']
        
    def __str__(self):
        return '{}'.format(self.name)

class Region(models.Model):
    country = models.ForeignKey(Country,verbose_name='country')
    region = models.CharField('region',primary_key=True,max_length=45)
    
    class Meta:
        ordering = ['region']
        
    def __str__(self):
        return '{}'.format(self.region)
        
class District(models.Model):
    region = models.ForeignKey(Region, verbose_name="region")
    district = models.CharField('district',primary_key=True,max_length=45)
        
    class Meta:
        ordering = ['district']
        
    def __str__(self):
        return '{}'.format(self.district)
    
class Village(models.Model):
    district = models.ForeignKey(District, verbose_name="district")
    village = models.CharField('village',primary_key=True,max_length=45)
    
    class Meta:
        ordering = ['village']
    
    def __str__(self):
        return '{}'.format(self.village)

class FarmGroup(models.Model):
    name =models.CharField('Name',max_length=45)
    village = models.ForeignKey(Village, verbose_name="Village")
    
    class Meta:
        ordering = ['name']
        unique_together = ('name','village')
        
        
    def __str__(self):
        return '{}'.format(self.name)
    
class Crop(models.Model):
    name = models.CharField('Name',primary_key=True, max_length=20)
    #variety_type = models.ForeignKey(CropVariety, verbose_name="Variety type")
    
    class Meta:
        ordering = ['name']
        
    def __str__(self):
        return '{}'.format(self.name)
    
    
class SystemUser(models.Model):
    user = models.OneToOneField(User,related_name="custom_user_profile",primary_key=True) 
    firstname = models.CharField('First name',max_length=80)
    middlename = models.CharField('Middle name',max_length=80,null=True, blank=True)
    lastname = models.CharField('Last name',max_length=80)
    role = models.CharField('Role',max_length=40)
    phone = models.CharField('Phone',max_length=50,null=True, blank=True)
    gender = models.CharField('Gender',max_length=10)#,choices=GENDER_CHOICE)
    institution = models.CharField('Institution',max_length=100)
    village = models.ForeignKey(Village, verbose_name="Village",null=True, blank=True)
    country = models.ForeignKey(Country, verbose_name="Country")
    
    class Meta:
        ordering = ['user']
        permissions = (
            ("image", "Can add image"),
        )
        
    def __str__(self):
        return '{}'.format(self.user)

class People(models.Model):
    personID = models.CharField('Person ID',primary_key=True,max_length=45)
    firstname = models.CharField('First name',max_length=80)
    middlename = models.CharField('Middle name',max_length=80,null=True, blank=True)
    lastname = models.CharField('Last name',max_length=80)
    gender = models.CharField('Gender',max_length=10)#,choices=GENDER_CHOICE)
    group = models.ForeignKey(FarmGroup, verbose_name="FarmGroup",null=True, blank=True)
    age_group = models.CharField('Age group',max_length=10,null=True, blank=True)
    role = models.CharField('Role',max_length=40)
    phone = models.CharField('Phone',max_length=50,null=True, blank=True)
    village = models.ForeignKey(Village, verbose_name="Village")
    
    class Meta:
        ordering = ['personID']
        
    def diplay(self):
        return self.personID
    
    def __str__(self):
        return '{}'.format(self.personID)
    
class House(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    elevation  = models.FloatField(null=True, blank=True)
    owner = models.ForeignKey(People,verbose_name='Owner(Farmer)')
    #enteredpersonel = models.ForeignKey(SystemUser,verbose_name='Entered by')
    
    class Meta:
        ordering = ['owner']
        
    def __str__(self):
        return '{}'.format(self.owner)
   
class RelationManager(models.Model):
    RELATION_CHOICES=(
        ('Family','Family'),
        ('Labour','Labour'),
    )
    farmer = models.CharField('farmer',max_length=25)
    family_member = models.ManyToManyField(People,verbose_name="Household members")
    relation = models.CharField('Relation',max_length=20,default='Family')
    
    class Meta:
        ordering = ['farmer']
        
    def __str__(self):
        return '{}'.format(self.farmer)
    
    def display_family_member(self):
        return ', '.join([ family_member.firstname for family_member in self.family_member.all() ])
    display_family_member.short_description = 'Family member'
    display_family_member.allow_tags = True

class Farm(models.Model):
    farmID = models.OneToOneField(People,primary_key=True,to_field='personID',related_name='farms')
    landownership = models.CharField('Landownership',max_length=20,null=True, blank=True)
    fieldsize = models.FloatField('Field Size (hactre)')
    number = models.IntegerField('Total plot numbers')
    rented_land = models.FloatField('rented land(hactre)',null=True, blank=True)
    owned_land = models.FloatField('Owned land(hactre)',null=True, blank=True)
    total_irrigated_owned_land = models.FloatField('Total irrigated owned land(hactre)',null=True, blank=True)
    total_irrigated_rented_land = models.FloatField('Field Size (hactre)',null=True, blank=True)
    irrigated_plots = models.FloatField('Total irrigated rented land(hactre)',null=True, blank=True)
    #total_irrigated_plots_land_area = models.FloatField('Total irrigated plots land area (hactre)')
    #total_irrigated_plots = models.IntegerField('Number of irrigated plots')
    enteredpersonel = models.ForeignKey(SystemUser,verbose_name='Entered by',null=True, blank=True)
    
    class Meta:
        ordering = ['farmID']
    
    def __int__(self):
        return self.number
    
    def __str__(self):
        return '{}'.format(self.farmID)

class Plot(models.Model):
    farm = models.ForeignKey(Farm,verbose_name='FarmID')
    plotID = models.CharField('PlotID',max_length=50)
    fieldtype =  models.CharField('Fieldtype',max_length=20,null=True, blank=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    landownership = models.CharField('Plot Ownership',max_length=10,null=True, blank=True)
    lease_duration = models.FloatField('Lease duration(months)',null=True, blank=True)
    payment_option = models.CharField('Payment Option',max_length=10,null=True, blank=True)
    payment_monetary = models.FloatField('Payment',null=True, blank=True)
    currency = models.CharField('Currency',max_length=5,null=True, blank=True)
    payement_other = models.CharField('Other payment method',max_length=50,null=True, blank=True)
    enteredpersonel = models.ForeignKey(SystemUser,verbose_name='Entered by',null=True, blank=True)
    #village = models.ForeignKey(Village, verbose_name="Village")
#lease_duration,  payment_option,payment_monetary,currency,payement_other
    class Meta:
        ordering = ['plotID']
        unique_together = ('plotID','farm')
         
    def __str__(self):
        return '{}'.format(self.plotID)

class CropVarieties(models.Model):
    farm = models.ForeignKey(Farm,verbose_name='FarmID',null=True, blank=True)
    plotID= models.ForeignKey(Plot,verbose_name='PlotID')
    cropname = models.ForeignKey(Crop,verbose_name='Crop Name')
    variety = models.CharField('Crop variety',max_length=70)
    varietytype = models.CharField('Variety Type',max_length=20)
    #crop1 = models.CharField('Crop1',max_length=30,null=True, blank=True)
    #crop1_variety = models.CharField('Crop1 variety',max_length=70,null=True, blank=True)
    #crop1_varietytype = models.CharField('Crop1 variety Type',max_length=20,null=True, blank=True)
    #crop2 = models.CharField('Crop2',max_length=30,null=True, blank=True)
    #crop2_variety = models.CharField('Crop2 variety',max_length=70,null=True, blank=True)
    #crop2_varietytype = models.CharField('Crop2 variety Type',max_length=20,null=True, blank=True)
        
    class Meta:
        ordering = ['cropname']
        
    def __str__(self):
        return '{}'.format(self.variety)

class PlotCrop(models.Model):
    farm = models.ForeignKey(Farm,verbose_name='FarmID',null=True, blank=True)
    plotID= models.ForeignKey(Plot,verbose_name='PlotID')
    cropping_system = models.CharField('Cropping System',max_length=20,null=True, blank=True)
    crop1 = models.CharField('Crop One',max_length=30,null=True, blank=True)
    crop1_variety = models.CharField('Crop one variety',max_length=70,null=True, blank=True)
    crop1_varietytype = models.CharField('Crop one variety Type',max_length=20,null=True, blank=True)
    crop1_planting_method = models.CharField('Crop one planting Method',max_length=20,null=True,blank=True)
    crop1_rootdepth = models.FloatField('Crop one rootdepth(m)',null=True,blank=True) 
    crop1_management_practice = models.CharField('Crop one Management practice',max_length =15,null=True,blank=True)
    crop1_mulching_type = models.CharField('Crop one Mulching type',max_length =45,null=True,blank=True)
    crop1_mulching_quantity = models.FloatField('Crop one Mulching quantity',null=True,blank=True)
    crop2 = models.CharField('Crop Two',max_length=30,null=True, blank=True)
    crop2_variety = models.CharField('Crop two variety',max_length=70,null=True, blank=True)
    crop2_varietytype = models.CharField('Crop two variety Type',max_length=20,null=True, blank=True)
    crop2_planting_method = models.CharField('Crop two planting Method',max_length=20,null=True,blank=True)
    crop2_rootdepth = models.FloatField('Crop two rootdepth(m)',null=True,blank=True) 
    crop2_management_practice = models.CharField('Crop two management practice',max_length =15,null=True,blank=True)
    crop2_mulching_type = models.CharField('Crop two mulching type',max_length =45,null=True,blank=True)
    crop2_mulching_quantity = models.FloatField('Crop two mulching quantity',null=True,blank=True)
    enteredpersonel = models.ForeignKey(SystemUser,verbose_name='Entered by',null=True, blank=True)

    #crop1_rootdepth,crop1_management_practice,crop1_mulching_type,crop1_mulching_quantity
    #crop2_rootdepth,crop2_management_practice,crop2_mulching_type,crop2_mulching_quantity
    class Meta:
        ordering = ['farm']
        
    def __str__(self):
        return '{}'.format(self.plotID)

class PlotManagement(models.Model):
    date = models.DateField('Date',null=True,blank=True)
    farm = models.ForeignKey(Farm,verbose_name='FieldID')
    plotID = models.ForeignKey(Plot,verbose_name='PlotID')
    elevation = models.FloatField('elevation',null=True,blank=True)
    plot_size = models.FloatField('Plot size(sq.m)')
    cropping_system = models.CharField('Cropping System',max_length=20,null=True, blank=True)
    crop = models.ManyToManyField(Crop,verbose_name='Crop Name')
    #management_practice = models.CharField('Management practice',max_length =10,null=True,blank=True)
    #mulching_type = models.CharField('Mulching type',max_length =45,null=True,blank=True)
    #mulching_quantity = models.FloatField('Mulching quantity (Kg)',null=True,blank=True)
    ###
    water_application = models.CharField('Water Application',max_length =80)
    seasonstart = models.DateField('Season started',null=True,blank=True)
    #seasonend = models.DateField('Season ended',null=True,blank=True)
    #growinglength = models.IntegerField('Growing length(days)',null=True,blank=True)
    rootdepth = models.FloatField('rootdepth(m)',null=True,blank=True) 
    enteredpersonel = models.ForeignKey(SystemUser,verbose_name='Entered by',null=True, blank=True)
    
    class Meta:
        ordering = ['farm']
        
    def __str__(self):
        return '{}'.format(self.farm)
    
    def display_crop(self):
        return ', '.join([ crop.name for crop in self.crop.all() ])
    display_crop.short_description = 'Crop(s)'
    display_crop.allow_tags = True
    
class WaterManagement(models.Model):
    farm = models.ForeignKey(Farm,verbose_name='Farm(s)',null=True,blank=True)
    plotID = models.ForeignKey(Plot,verbose_name='PlotID')
    water_management_method = models.CharField('Water management method',max_length = 80)#,choices=PUMPING_SOURCE_CHOICES)
    yellow_depth_detector = models.FloatField('yellow_depth_detector(m)',null=True,blank=True)
    red_depth_detector = models.FloatField('red_depth_detector(m)',null=True,blank=True)
    rods_length = models.FloatField('red_depth_detector(m)',null=True,blank=True)
    
    class Meta:
        ordering = ['plotID']
        
    def __str__(self):
        return '{}'.format(self.water_management_method)
    
class PumpingSource(models.Model):
    date = models.DateField('date',null=True,blank=True)
    farm = models.ForeignKey(Farm,verbose_name='Farm(s)')
    source = models.CharField('Name',max_length=80)
    latitude = models.FloatField("Source's latitude")
    longitude = models.FloatField("Source's longitude")
    elevation = models.FloatField("Source's longitude",null=True,blank=True)
    depth = models.FloatField('Depth(m)',null=True,blank=True)
    diameter = models.FloatField('Diameter(m)',null=True,blank=True)
    enteredpersonel = models.ForeignKey(SystemUser,verbose_name='Entered by',null=True, blank=True)
    
    class Meta:
        ordering = ['depth']
        #unique_together = (('latitude','longitude'),)
        
    #def __str__(self):
        #return self.farm
'''  
class FarmFields(models.Model):
    farmID = models.CharField('FarmID',primary_key=True, max_length=40)
    fields = models.ManyToManyField(Farm, verbose_name="Field(s)")
    
    class Meta:
        ordering = ['farmID']
        
    def __str__(self):
        return self.farmID
'''

class PlotOperation(models.Model): 
    ACTIVITY_CHOICES =(
        ('FA','Fertilizer application'),
        ('PA','Pesticide application'), 
        )
    date = models.DateField('Date activity was performed')
    farm = models.ForeignKey(Farm,verbose_name='Farm(s)',null=True, blank=True)
    plotID = models.ForeignKey(Plot,verbose_name='PlotID')
    activity = models.TextField('Activity',max_length=200)#,choices=ACTIVITY_CHOICES)
    number = models.IntegerField('Number of people')
    
    class Meta:
        ordering = ['date']
        
    def __str__(self):
        return '{}'.format(self.farm)

class PlotCultivation(models.Model): 
    date = models.DateField('Cultivation date')
    farm = models.ForeignKey(Farm,verbose_name='Farm(s)',null=True, blank=True)
    plotID = models.ForeignKey(Plot,verbose_name='PlotID')
    cultivation_method = models.CharField('Method of Cultivation',max_length=80)
    enteredpersonel = models.ForeignKey(SystemUser,verbose_name='Entered by',null=True, blank=True)
    
    class Meta:
        ordering = ['date']
        
    def __str__(self):
        return '{}'.format(self.farm)
    
 
class Pump(models.Model):
    name = models.CharField('Name',primary_key=True,max_length=45)
    
    class Meta:
        ordering = ['name']
        
    def __str__(self):
        return '{}'.format(self.name)
    
class PumpOwnership(models.Model):
    group = models.ForeignKey(FarmGroup,verbose_name='FarmGroup')
    name = models.ForeignKey(Pump,verbose_name='Name',null=True,blank=True)
    size = models.CharField('size',max_length=50)
    price = models.FloatField('Bought price',null=True,blank=True)
    date = models.DateField('Bought date',null=True,blank=True)
    enteredpersonel = models.ForeignKey(SystemUser,verbose_name='Entered by',null=True, blank=True)
    
    class Meta:
        ordering = ['date']
        
    def __str__(self):
        return '{}'.format(self.name)
    
 
class Spaire(models.Model):
    name = models.CharField('name',primary_key=True,max_length=45)
    pump = models.ManyToManyField(Pump, verbose_name="Pump")
    
    class Meta:
        ordering = ['name']
        
    def __str__(self):
        return '{}'.format(self.name)

class SpaireManagement(models.Model):
    group = models.ForeignKey(FarmGroup,verbose_name='FarmGroup')
    spaire = models.ForeignKey(Spaire,verbose_name='Spaire')
    price = models.FloatField('Bought price (Tsh)',null=True,blank=True)
    date = models.DateField('Bought date',null=True,blank=True)
    
    class Meta:
        ordering = ['group']
        
    def __str__(self):
        return '{}'.format(self.group)

    
class Service(models.Model):
    date = models.DateField('date')
    farm = models.ForeignKey(Farm,verbose_name='Farm',null=True,blank=True)
    ##group = models.ForeignKey(FarmGroup,verbose_name='FarmGroup',null=True,blank=True)
    repaire_type = models.TextField('Type of repaires',max_length=100)
    spaire = models.ManyToManyField(Spaire, verbose_name="Required spaire")
    ##price = models.FloatField('Price of spaire parts',null=True,blank=True)
    time_taken = models.FloatField('Time taken(hr)',null=True,blank=True)
    total_cost = models.FloatField('Total repaire cost',null=True,blank=True)
    currency = models.CharField('Price Unit',max_length=10,null=True,blank=True)
    maintenance_place = models.CharField('Maintenance place',max_length=70,null=True,blank=True)
    technology_broken = models.CharField('Technology broken',max_length=70,null=True,blank=True)
    distance_to_shop = models.FloatField('Distance to shop(km)',null=True,blank=True)
    travel_cost = models.FloatField('Travel cost',null=True,blank=True)
    enteredpersonel = models.ForeignKey(SystemUser,verbose_name='Entered by',null=True, blank=True)
    
    class Meta:
        ordering = ['date']

    def __str__(self):
        return '{}'.format(self.farm)
    
class FarmCost(models.Model):
    year = models.IntegerField('Year')
    farm = models.ForeignKey(Farm,verbose_name='Farm')
    landpreparation = models.FloatField('Land preparation cost (Tsh)')
    landpulverization = models.FloatField('land pulverization cost (Tsh)')
    transplanting = models.FloatField('Transplanting cost (Tsh)')
    
    class Meta:
        ordering = ['farm']
        
    def __str__(self):
        return '{}'.format(self.farm)
    
class PlotCropProperty(models.Model):
    farm = models.ForeignKey(Farm,verbose_name='Farm',null=True,blank=True)
    plotID = models.ForeignKey(Plot,verbose_name='Plot ID',null=True,blank=True)
    name = models.ForeignKey(Crop,verbose_name="Crop")
    root_depth = models.FloatField('Root depth (m)')
    planting_spacing = models.FloatField('Planting space(cm)')
    
    class Meta:
        ordering = ['plotID']
        
    def __str__(self):
        return '{}'.format(self.name)
    
class BedPlot(models.Model):
    farm = models.ForeignKey(Farm,verbose_name='Farm',null=True,blank=True)
    plotID = models.ForeignKey(Plot,verbose_name='Plot ID',null=True,blank=True)
    length = models.FloatField('Length(m)')
    width = models.FloatField('Width(m)')
    numbers = models.IntegerField('Number of beds')
    #planting_density = models.IntegerField('Planting density')
    
    class Meta:
        ordering = ['plotID']
        
    def __str__(self):
        return '{}'.format(self.plotID)
 

class Furrow(models.Model):
    farm = models.ForeignKey(Farm,verbose_name='Farm',null=True,blank=True)
    plotID = models.ForeignKey(Plot,verbose_name='Plot ID',null=True,blank=True)
    length = models.FloatField('Length(m)')
    width = models.FloatField('Width(m)')
    numbers = models.IntegerField('Number of furrows')
 
    class Meta:
        ordering = ['plotID']
        
    def __str__(self):
        return '{}'.format(self.plotID)

class Technology(models.Model):
    TECHNOLOGY_CHOICES=(
        ('Pulley','Pulley'),('Pulley with tank','Pulley with tank'),('Rope and washer','Rope and washer'),
        ('Rope and washer with hose','Rope and washer with hose'),('Diesel motorized pump','Diesel motorized pump'),('Solar pump','Solar pump'),
        ('Drip','Drip'),('drip+mounted motorized pump','drip+mounted motorized pump'),('UDS drip (Ghana)','UDS drip (Ghana)')
    )
    name =models.CharField('Technology',primary_key=True,max_length = 100)
    
    class Meta:
        ordering = ['name']
        
    def __str__(self):
        return '{}'.format(self.name)
    
class TechnologyManagement(models.Model):
    date = models.DateField('Received date',null=True,blank=True)
    technology = models.ForeignKey(Technology,verbose_name='Technology')
    farm = models.ForeignKey(Farm,verbose_name='Farm',null=True,blank=True)
    enteredpersonel = models.ForeignKey(SystemUser,verbose_name='Entered by',null=True, blank=True)
    
    class Meta:
        ordering = ['date']
        
    def __str__(self):
        return '{}'.format(self.technology)
    
class TechnologyFailure(models.Model):
    date = models.DateField('Failure date')
    farm = models.ForeignKey(Farm,verbose_name='Farm',null=True,blank=True)
    technology = models.ForeignKey(Technology,verbose_name='Technology')
    reason = models.TextField('Reason',max_length=100)
    enteredpersonel = models.ForeignKey(SystemUser,verbose_name='Entered by',null=True, blank=True)
    
    class Meta:
        ordering = ['date']
        
    def __str__(self):
        return '{}'.format(self.technology)

class TechnologyCalibration(models.Model):
    date = models.DateField('Calibration Date')
    farm = models.ForeignKey(Farm,verbose_name='Farm',null=True,blank=True)
    technology = models.ForeignKey(Technology,verbose_name='Calibrated Technology')
    repetition = models.IntegerField('Repetition')
    bucketvolume = models.FloatField('Bucket volume (litre)',null=True,blank=True)
    start_time = models.TimeField('Start time')
    end_time = models.TimeField('End time')
    total_time = models.FloatField('Total time')
    discharge = models.FloatField('Discharge(m3/s)',null=True,blank=True)
    enteredpersonel = models.ForeignKey(SystemUser,verbose_name='Entered by',null=True, blank=True)
    
    class Meta:
        ordering = ['date']
        
    def __str__(self):
        return '{}'.format(self.technology)
    

class YieldFarmLevel(models.Model):
    date = models.DateField('Harvesting Date')
    farm = models.ForeignKey(Farm,verbose_name='Farm',null=True,blank=True)
    plotID = models.ForeignKey(Plot,verbose_name='Plot ID',null=True,blank=True)
    Crop = models.ForeignKey(Crop,verbose_name='Crop',null=True,blank=True)
    #area = models.FloatField('Area (sq.m)')
    quantity_harvested = models.FloatField('Harvested Amount (kg)',null=True,blank=True)
    fresh_dry = models.CharField('Fresh/Dry',max_length=10,null=True,blank=True)
    marketable_yield = models.FloatField('Marketable yield (Kg)')
    unmarketable_yield = models.FloatField('Unmarketable yield (Kg)')
    biomas = models.FloatField('Biomas (Kg)')
    enteredpersonel = models.ForeignKey(SystemUser,verbose_name='Entered by',null=True, blank=True)
    
    
    class Meta:
        ordering = ['date']
        
    def __str__(self):
        return '{}'.format(self.farm)
  

class CropMonitoringPlantHeight(models.Model):
    date = models.DateField('Monitoring Date')
    farm = models.ForeignKey(Farm,verbose_name='Farm',null=True,blank=True)
    plotID = models.ForeignKey(Plot,verbose_name='Plot',null=True,blank=True)
    Crop = models.ForeignKey(Crop,verbose_name='Crop',null=True,blank=True)
    crop_stage = models.CharField('Crop Stage',max_length=50)
    row_number = models.IntegerField('Row number',null=True,blank=True)
    number_of_good_plants = models.IntegerField('Number of good plants',null=True,blank=True)
    number_of_bad_plants = models.IntegerField('Number of bad plants',null=True,blank=True)
    plant_density_per_bed = models.IntegerField('Plant density per bed',null=True,blank=True)
    plant_density_per_sqm = models.FloatField('plant density per sq.m',null=True,blank=True)
    
    plant_number = models.IntegerField('Plant Number',null=True,blank=True)
    LAI = models.FloatField('leaf area index (LAI) ',null=True,blank=True)
    plant_height = models.FloatField('Plant height(m)',null=True,blank=True)
    plant_canopy_width = models.FloatField('Plant canopy width(m)',null=True,blank=True)
    length_of_crop_stage = models.FloatField('Length of crop stage(days)',null=True,blank=True)
    plant_leave_number = models.IntegerField('Leaves per plant',null=True,blank=True)
    plant_leave_length = models.FloatField('Plant leave length(cm)',null=True,blank=True)
    plant_leave_width = models.FloatField('Plant leave width(cm)',null=True,blank=True)

    plant_number_two = models.IntegerField('Plant Number two',null=True,blank=True)
    LAI_two = models.FloatField('leaf area index (LAI) for plant two ',null=True,blank=True)
    plant_height_two = models.FloatField('Plant two height(m)',null=True,blank=True)
    plant_canopy_width_two = models.FloatField('Plant two canopy width(m)',null=True,blank=True)
    length_of_crop_stage_two = models.FloatField('Length of crop two stage(days)',null=True,blank=True)
    plant_leave_number_two = models.IntegerField('Leaves per plant two',null=True,blank=True)
    plant_leave_length_two = models.FloatField('Plant two leave length(cm)',null=True,blank=True)
    plant_leave_width_two = models.FloatField('Plant two leave width(cm)',null=True,blank=True)
    
    plant_number_three = models.IntegerField('Plant Number three',null=True,blank=True)
    LAI_three = models.FloatField('leaf area index (LAI)  for plant three',null=True,blank=True)
    plant_height_three = models.FloatField('Plant three height(m)',null=True,blank=True)
    plant_canopy_width_three = models.FloatField('Plant three canopy width(m)',null=True,blank=True)
    length_of_crop_stage_three = models.FloatField('Length of crop three stage(days)',null=True,blank=True)
    plant_leave_number_three = models.IntegerField('Leaves per plant three',null=True,blank=True)
    plant_leave_length_three = models.FloatField('Plant three leave length(cm)',null=True,blank=True)
    plant_leave_width_three = models.FloatField('Plant three leave width(cm)',null=True,blank=True)
    
    sub_plot_size = models.FloatField('Sub plot size(sq.m)',null=True,blank=True)
    sub_plot_plant_number = models.FloatField('Number of plants in the sub-plot',null=True,blank=True)
    total_plant_number = models.IntegerField('Total number of plants',null=True,blank=True)
    
    enteredpersonel = models.ForeignKey(SystemUser,verbose_name='Entered by',null=True, blank=True)
    
    class Meta:
        ordering = ['date']
        
    def __str__(self):
        return '{}'.format(self.farm)

class YieldRowBedLevel(models.Model):
    date = models.DateField('Harvesting Date')
    farm = models.ForeignKey(Farm,verbose_name='Farm',null=True,blank=True)
    plotID = models.ForeignKey(Plot,verbose_name='PlotID',null=True,blank=True)
    Crop = models.ForeignKey(Crop,verbose_name='Crop',null=True,blank=True)
    harvesting_method = models.CharField('Harvesting method',max_length=80)
    fresh_dry = models.CharField('Fresh/Dry',max_length=10,blank=True,null=True)
    #area = models.FloatField('area(sq.m)',blank=True,null=True)
    row_number = models.IntegerField('Row number',null=True,blank=True)
    marketable_produced = models.FloatField('Marketable produced',blank=True,null=True)
    ummarketable_produced = models.FloatField('Unmarketable produced',blank=True,null=True)
    marketable_produced_weight = models.FloatField('Weight of marketable produced(kg)',blank=True,null=True)
    unmarketable_produced_weight= models.FloatField(' Weight of unmarketable produced(kg)',blank=True,null=True)
    enteredpersonel = models.ForeignKey(SystemUser,verbose_name='Entered by',null=True, blank=True)
    
    
    class Meta:
        ordering = ['date']
        
    def __str__(self):
        return '{}'.format(self.farm)


class YieldPlantLevel(models.Model):
    date = models.DateField('Date')
    farm = models.ForeignKey(Farm,verbose_name='Farm',null=True,blank=True)
    plotID = models.ForeignKey(Plot,verbose_name='PlotID',null=True,blank=True)
    Crop = models.ForeignKey(Crop,verbose_name='Crop',null=True,blank=True)
    harvest_method = models.CharField('Harvest Method',max_length=50)
    fresh_dry = models.CharField('Fresh/Dry',max_length=15,blank=True,null=True)
    row_number = models.IntegerField('Row number',null=True,blank=True)
    plant_number = models.IntegerField('Plant number',null=True,blank=True)
    marketable_produced = models.FloatField('Number of marketable produced',null=True,blank=True)
    unmarketable_produced = models.FloatField('Number of unmarketable produced',null=True,blank=True)
    marketable_produced_weight = models.FloatField('Total weight of marketable produced(kg)',null=True,blank=True)
    unmarketable_produced_weight= models.FloatField(' Total weight of unmarketable produced(kg)',null=True,blank=True)
    diameter_width_produced =  models.FloatField('Diameter/width produce',null=True,blank=True)
    length =  models.FloatField('Length produced(cm)',null=True,blank=True)
    residual_biomass =  models.FloatField('Residual biomass(Kg)',null=True,blank=True)
    enteredpersonel = models.ForeignKey(SystemUser,verbose_name='Entered by',null=True, blank=True)
    
    
    class Meta:
        ordering = ['date']
        
    def __str__(self):
        return '{}'.format(self.farm)

 
 
class Seed(models.Model):
    name = models.CharField('Seed',primary_key=True,max_length=35)
    
    class Meta:
        ordering = ['name']
        
    def __str__(self):
        return '{}'.format(self.name)


class Nursery(models.Model):
    NurseryID = models.CharField('Nursery ID',primary_key=True,max_length =25)
    area = models.FloatField('Area(sq.m)')
    farm = models.ForeignKey(Farm,verbose_name='Farm')
    seed = models.ForeignKey(Seed,verbose_name ='seed',null=True, blank=True)
    date_bed_preparation = models.DateField('Bed Preparation date')
    #date_trasplanting = models.DateField('Transplanting date')
    enteredpersonel = models.ForeignKey(SystemUser,verbose_name='Entered by',null=True, blank=True)
    
    
    class Meta:
        ordering = ['NurseryID']
        
    def __str__(self):
        return '{}'.format(self.NurseryID)

    
class Fertilizer(models.Model):
    name = models.CharField('Name',primary_key=True,max_length=50)
    
    class Meta:
        ordering = ['name']
        
    def __str__(self):
        return '{}'.format(self.name)

    
class FertilizerManagement(models.Model):

    FERTILIZER_MANAGEMENT_CHOICES = (
        ("farmer's practice","farmer's practice"),
        ("DAP","DAP"),("NPS","NPS"),
        ("DAP-UREA","DAP-UREA"),("UREA","UREA"),("Compost","Compost")
    )
    date = models.DateField('Application Date')
    farm = models.ForeignKey(Farm,verbose_name='Farm',null=True,blank=True)
    plotID = models.ForeignKey(Plot,verbose_name='Plot ID',null=True,blank=True)
    nurseryID = models.ForeignKey(Nursery,verbose_name='nurseryID',null=True,blank=True)
    crop_stage = models.CharField('Crop Stage',max_length=40)
    fertilizer = models.ForeignKey(Fertilizer,verbose_name='Fertilizer')
    compost_kind = models.CharField('Compost kind',max_length=45,default='None')
    quantity_in_kg = models.FloatField('Quantity(Kg)',null=True,blank=True)
    fertilizer_management = models.CharField('Fertilizer Management',max_length = 75)
    price = models.FloatField('Price',null=True,blank=True)
    price_unit = models.CharField('Price Unit',max_length=10,null=True,blank=True)
    enteredpersonel = models.ForeignKey(SystemUser,verbose_name='Entered by',null=True, blank=True)
    
    class Meta:
        ordering = ['date']
        
    def __str__(self):
        return '{}'.format(self.plotID)

class FertilizerSpecification(models.Model):
    farm = models.ForeignKey(Farm,verbose_name='Farm',null=True,blank=True)
    plotID = models.ForeignKey(Plot,verbose_name='Plot ID',null=True,blank=True)
    fertilizer = models.ForeignKey(Fertilizer,verbose_name='Fertilizer')
    nitrogen = models.FloatField('N content (%)',null=True,blank=True)
    phosphorus = models.FloatField('Phosphorus (ppm)',null=True,blank=True)
    potassium = models.FloatField('Potassium (ppm)',null=True,blank=True)
    sulphur = models.FloatField('Sulphur(g/kg)',null=True, blank=True)
    organic_matter = models.FloatField('Organic Matter (%)',null=True,blank=True)
    enteredpersonel = models.ForeignKey(SystemUser,verbose_name='Entered by',null=True, blank=True)
    
    class Meta:
        ordering = ['plotID']
        
    def __str__(self):
        return '{}'.format(self.plotID)

class Pesticide(models.Model):
    name = models.CharField('Name',primary_key=True, max_length=85)
    
    class Meta:
        ordering = ['name']
        
    def __str__(self):
        return '{}'.format(self.name)
    
class PesticideManagement(models.Model):
    UNIT_CHOICES=(
        ('Litre','Litre'),
        ('Kg','Kg'),
    )
    FORM_CHOICES=(
        ('Liquid','Liquid'),
        ('Solid','Solid'),
    )
    date = models.DateField('Application Date')
    farm = models.ForeignKey(Farm,verbose_name='Farm',null=True,blank=True)
    plotID = models.ForeignKey(Plot,verbose_name='Plot ID',null=True,blank=True)
    name = models.ForeignKey(Pesticide, verbose_name='Name')
    crop_stage = models.CharField('Crop Stage',max_length=40)
    form = models.CharField('Form',max_length=20)
    water_volume = models.FloatField('Water volume(L)',null=True,blank=True)
    quantity_in_litre = models.FloatField('Quantity(Litre)',null=True,blank=True)
    quantity_in_kg = models.FloatField('Quantity(Kg)',null=True,blank=True)
    price = models.FloatField('Price',null=True,blank=True)
    price_unit = models.CharField('Price Unit',max_length=10,null=True,blank=True)
    enteredpersonel = models.ForeignKey(SystemUser,verbose_name='Entered by',null=True, blank=True)
    
    class Meta:
        ordering = ['name']
        
    def __str__(self):
        return '{}'.format(self.name)
    
    

class PlantingMethod(models.Model):
    PLANTING_METHOD_CHOICES = (
           ('Directseeding','Direct seeding'),
            ('Transplanting','Transplanting'),
    )
    farm = models.ForeignKey(Farm,verbose_name='Farm',null=True,blank=True)
    plotID = models.ForeignKey(Plot,verbose_name='PlotID',null=True,blank=True)
    CroppingSystem = models.CharField('Cropping System',max_length=20,null=True,blank=True)
    planting_method = models.CharField('Planting Method',max_length=100,null=True,blank=True)#,choices=PLANTING_METHOD_CHOICES)
    date_one = models.DateField('transplanting/seeding date for crop One',null=True,blank=True)
    spacing_within_a_row = models.FloatField('Plant/seed spacing within a row for first crop(cm)',null=True,blank=True)
    nurseryID_one = models.CharField('nurseryID for Crop One',null=True,blank=True,max_length=45)
    spacing_btn_a_row = models.FloatField('Plant/seed spacing btn a row(cm)',null=True,blank=True)
    seed_quantity = models.FloatField('seeding quantity for crop one',null=True,blank=True)
    plantsnumber_per_row_one = models.IntegerField('Plant number per row for crop one',null=True,blank=True)
    date_two = models.DateField('transplanting/seeding date for crop two',null=True,blank=True)
    spacing_within_a_row_two = models.FloatField('Plant/seed spacing within a row for second crop(cm)',null=True,blank=True)
    nurseryID_two = models.CharField('nurseryID for Crop Two',null=True,blank=True,max_length=45)
    plantsnumber_per_row_two= models.IntegerField('Plant number per row for crop two',null=True,blank=True)
    total_plants = models.FloatField('Total number of plants',null=True,blank=True)
    total_seed_quantity = models.IntegerField('Total seed quantity',null=True,blank=True)
    seed_quantity2 = models.FloatField('seeding quantity for crop two',null=True,blank=True)
    enteredpersonel = models.ForeignKey(SystemUser,verbose_name='Entered by',null=True, blank=True)
 
    class Meta:
        ordering =['plotID']
        
    def __str__(self):
        return '{}'.format(self.planting_method)

'''
class Transplanting(models.Model):
    date = models.DateField('transplanting date')
    nurseryID = models.ForeignKey(Nursery,verbose_name='nurseryID',null=True,blank=True)
    plotID = models.ForeignKey(Plot,verbose_name='PlotID',null=True,blank=True)
    plantsnumber = models.IntegerField('Total number of plants transplanted')
    plant_spacing_btn_row = models.FloatField('Plant spacing between row(cm)')
    plant_spacing_btn_plants_within_rows = models.FloatField('Plant spacing between plants within rows(cm)')
    plantsnumber_per_row = models.IntegerField('Plant number per row')
    enteredpersonel = models.ForeignKey(SystemUser,verbose_name='Entered by',null=True, blank=True)
       
    class Meta:
        ordering =['plotID']
        
    def __str__(self):
        return '{}'.format(self.plotID)   
    
'''
class SeedManagement(models.Model):
    date = models.DateField('Date')
    nursery = models.ForeignKey(Nursery,verbose_name='Nursery planted on')
    seed = models.ForeignKey(Seed,verbose_name='Seed')
    quantity = models.FloatField('Quantity (kg)')
    total_cost = models.FloatField('Total cost')
    price_per_unit = models.FloatField('Price per unit')
    currency = models.CharField('Currency',max_length=10,default='Tsh')
    enteredpersonel = models.ForeignKey(SystemUser,verbose_name='Entered by',null=True, blank=True)
    
    class Meta:
        ordering = ['date']
        
    def __str__(self):
        return '{}'.format(self.seed)
    
    
class BedNursery(models.Model):
    length = models.FloatField('Length(m)')
    width = models.FloatField('Width(m)')
    area = models.FloatField('Area (sq.m)')
    nursery = models.ForeignKey(Nursery,verbose_name='NuseryID')
    numbers = models.IntegerField('Numbers of bed(s)')
    planting_density_per_bed = models.FloatField('Planting density per bed')
    seedrate = models.FloatField('Seed rate (kg/ha)')
    seed_spacing_within_a_bed = models.FloatField('seed spacing within a bed/row(cm)',null=True, blank=True)
    seed_spacing_btn_bed = models.FloatField('seed spacing btn bed/row(cm)',null=True, blank=True)
    enteredpersonel = models.ForeignKey(SystemUser,verbose_name='Entered by',null=True, blank=True)
    #seedling_yield_per_bed = models.FloatField('Seedling yield per bed')
    
    class Meta:
        ordering = ['nursery']
        
    def __str__(self):
        return '{}'.format(self.nursery)
  
    
class CropPropertyNursery(models.Model):
    nursery = models.ForeignKey(Nursery,verbose_name='Nursery')
    name = models.ForeignKey(Crop,verbose_name="Crop")
    root_depth = models.FloatField('Root depth (m)')
    planting_spacing = models.FloatField()
    
    class Meta:
        ordering = ['name']
        
    def __str__(self):
        return '{}'.format(self.name)
    

class NurseryIrrigationEvent(models.Model):
    CLIMATE_CHOICES=(
        ('Rainy','Rainy'),
        ('Sunny','Sunny'),
        ('Cloudy','Cloudy'),
    )
    date = models.DateField('Irrigation Date')
    nursery = models.ForeignKey(Nursery,verbose_name='Nursery')
    time_started = models.TimeField('Time started')
    time_ended =  models.TimeField('Time ended')
    total_time = models.FloatField('Total time(minutes)')
    event = models.IntegerField('Event number')
    irrigation_depth= models.FloatField('Irrigation depth',null=True, blank=True)
    #discharge = models.FloatField('Discharge(m3/s)')
    #standard_volume = models.FloatField('Standard Volume (Litre or m3/s)')
    quantity = models.FloatField('Quantity(Number of buckets)',null=True, blank=True)
    climate = models.CharField('Climate',max_length=30)#choices=CLIMATE_CHOICES
    total_volume = models.FloatField('Total Volume (Litre)')
    enteredpersonel = models.ForeignKey(SystemUser,verbose_name='Entered by',null=True, blank=True)
    
    class Meta:
        ordering = ['nursery']
        
    def __str__(self):
        return '{}'.format(self.nursery)
    
    
class Fuel(models.Model):
    name = models.CharField('Name',primary_key=True,max_length=35)
    
    class Meta:
        ordering = ['name']
        
    def __str__(self):
        return '{}'.format(self.name)
    
class FuelManagement(models.Model):
    date = models.DateField('Date of use')
    fuel = models.ForeignKey(Fuel,verbose_name='Fuel')
    farm = models.ForeignKey(Farm,verbose_name='Farm')
    initial_time = models.TimeField('Initial Time')
    final_time = models.TimeField('Final Time')
    amount_used = models.FloatField('Amount Used (Litre)')
    refilled_amount = models.FloatField('Refilled amount (Litre)')
    enteredpersonel = models.ForeignKey(SystemUser,verbose_name='Entered by',null=True, blank=True)
    
    class Meta:
        ordering = ['fuel']
        
    def __str__(self):
        return '{}'.format(self.fuel)


class Soil(models.Model):
    name = models.CharField('Name',primary_key=True,max_length=50)
    
    class Meta:
        ordering = ['name']
        
    def __str__(self):
        return '{}'.format(self.name)
    
class SoilProperty(models.Model):
    date = models.DateField('Measurement Date')
    farm = models.ForeignKey(Farm,verbose_name='Farm',null=True,blank=True)
    plotID = models.ForeignKey(Plot,verbose_name='PlotID',null=True,blank=True)
    soilclass = models.ForeignKey(Soil,verbose_name='Soil class')
    soil_depth = models.FloatField('soil depth(cm)',null=True, blank=True)
    pH = models.FloatField('pH',null=True, blank=True)
    ec = models.FloatField('Electrical conductivity (dS/m)',null=True, blank=True)
    sand = models.FloatField('Sand (%)',null=True, blank=True)
    clay = models.FloatField('Clay(%)',null=True, blank=True)
    silt = models.FloatField('Silt(%)',null=True, blank=True)
    cec = models.FloatField('CEC',null=True, blank=True)
    om = models.FloatField('OM(%)',null=True, blank=True)
    tn = models.FloatField('TN(%)',null=True, blank=True)
    av_p = models.FloatField('Av.p (ppm)',null=True, blank=True)
    fe = models.FloatField('Fe (ppm)',null=True, blank=True)
    fc = models.FloatField('Fe (ppm)',null=True, blank=True)
    pwp = models.FloatField('pwp(%)',null=True, blank=True)
    k = models.FloatField('K(cmol/kg)',null=True, blank=True)
    bulkdensity = models.FloatField('bulk density (g/cm3)',null=True, blank=True)
    zn = models.FloatField('Zn(g/kg)',null=True, blank=True)
    se = models.FloatField('Se(g/kg)',null=True, blank=True)
    ca = models.FloatField('Ca(g/kg)',null=True, blank=True)
    s = models.FloatField('S(g/kg)',null=True, blank=True)
    mg = models.FloatField('Mg(g/kg)',null=True, blank=True)
    na = models.FloatField('Na(g/kg)',null=True, blank=True)
    enteredpersonel = models.ForeignKey(SystemUser,verbose_name='Entered by',null=True, blank=True)
    
    class Meta:
        ordering = ['date']
        
    def __str__(self):
        return '{}'.format(self.soilclass)


class TDRMeasurement(models.Model):
    date = models.DateField('Measurement Date')
    farm = models.ForeignKey(Farm,verbose_name='Farm',null=True,blank=True)
    plotID = models.ForeignKey(Plot,verbose_name='PlotID',null=True,blank=True)
    event  = models.IntegerField('Event number',null=True, blank=True)
    measurement_one = models.FloatField('First Measurement(%)',null=True, blank=True)
    measurement_two = models.FloatField('Second Measurement(%)',null=True, blank=True)
    measurement_three = models.FloatField('Third Measurement(%)',null=True, blank=True)
    measurement_four = models.FloatField('Fourth Measurement(%)',null=True, blank=True)
    measurement_five = models.FloatField('Fifth Measurement(%)',null=True, blank=True)
    measurement_six = models.FloatField('Sixth Measurement(%)',null=True, blank=True)
    measurement_seven = models.FloatField('Seventh Measurement(%)',null=True, blank=True)
    measurement_eigth = models.FloatField('Eighth Measurement(%)',null=True, blank=True)
    measurement_nine = models.FloatField('Ninth Measurement(%)',null=True, blank=True)
    measurement_ten = models.FloatField('Tenth Measurement(%)',null=True, blank=True)
    measurement_depth = models.FloatField('Measurement depth (cm)',null=True, blank=True)
    enteredpersonel = models.ForeignKey(SystemUser,verbose_name='Entered by',null=True, blank=True)
    

    class Meta:
        ordering = ['date']
        
    def __str__(self):
        return '{}'.format(self.plotID)
    
class GravimetricSoilMoisture(models.Model):
    date = models.DateField('Measurement Date')
    farm = models.ForeignKey(Farm,verbose_name='Farm',null=True,blank=True)
    plotID = models.ForeignKey(Plot,verbose_name='PlotID',null=True,blank=True)
    event  = models.IntegerField('Event number',null=True, blank=True)
    time_taken = models.FloatField('Time taken(mins)',null=True, blank=True)
    depth = models.FloatField('Depth sample',null=True, blank=True)
    volume_core_used = models.FloatField('Volume core used (cm3)',null=True, blank=True)
    weight_core_used = models.FloatField('Weight core used (g)',null=True, blank=True)
    wet_weight = models.FloatField('Wet weight (g)',null=True, blank=True)
    dry_weight = models.FloatField('Dry weight(g)',null=True, blank=True)
    bulk_density = models.FloatField('Bulk density(g/cm3)',null=True, blank=True)
    gravimetric_moisture_content = models.FloatField('Gravimetric moisture content',null=True, blank=True)
    volumetric_moisture_content = models.FloatField('Volumetric moisture content',null=True, blank=True)
    enteredpersonel = models.ForeignKey(SystemUser,verbose_name='Entered by',null=True, blank=True)
    
    class Meta:
        ordering = ['date']
        
    def __str__(self):
        return '{}'.format(self.plotID)



class SoilMoistureProfiler(models.Model):
    date = models.DateField('Measurement Date')
    farm = models.ForeignKey(Farm,verbose_name='Farm',null=True,blank=True)
    plotID = models.ForeignKey(Plot,verbose_name='PlotID',null=True,blank=True)
    event  = models.IntegerField('Event number',null=True, blank=True)
    depth_10  = models.FloatField('Measurement at 10cm(%)',null=True, blank=True)
    depth_20  = models.FloatField('VMeasurement at 20cm(%)',null=True, blank=True)
    depth_30  = models.FloatField('Measurement at 30cm(%)',null=True, blank=True)
    depth_40  = models.FloatField('Measurement at 40cm(%)',null=True, blank=True)
    depth_60  = models.FloatField('Measurement at 60cm(%)',null=True, blank=True)
    depth_100 = models.FloatField('Measurement at 100cm(%)',null=True, blank=True)
    enteredpersonel = models.ForeignKey(SystemUser,verbose_name='Entered by',null=True, blank=True)
    
    
    class Meta:
        ordering = ['date']
        
    def __str__(self):
        return '{}'.format(self.farm)

class SoilMoistureMeasurementManagement(models.Model):
    date = models.DateField('Measurement Date')
    farm = models.ForeignKey(Farm,verbose_name='Farm',null=True,blank=True)
    plotID = models.ForeignKey(Plot,verbose_name='PlotID',null=True,blank=True)
    measurement_option = models.CharField('Soil measurement used(option)',max_length=75)
    enteredpersonel = models.ForeignKey(SystemUser,verbose_name='Entered by',null=True, blank=True)
    
    class Meta:
        ordering = ['date']
        
    def __str__(self):
        return '{}'.format(self.measurement_used)
    
    
class TissueNutrientAnalysis(models.Model):
    date = models.DateField('Measurement Date')
    farm = models.ForeignKey(Farm,verbose_name='Farm',null=True,blank=True)
    plotID = models.ForeignKey(Plot,verbose_name='PlotID',null=True,blank=True)
    Crop = models.ForeignKey(Crop,verbose_name='Crop',null=True,blank=True)
    plant_tissue_part = models.CharField('Plant tissue part',max_length=30)
    plantnumber = models.IntegerField('Plant number')
    bed_number = models.IntegerField('Bed/Row number',null=True,blank=True)
    freshweight = models.FloatField('Fresh weight(kg)')
    dryweight = models.FloatField('Dry weight(kg)')
    n = models.FloatField('Nitrogen(%)')
    p = models.FloatField('Phosphorus(%)')
    k = models.FloatField('Potassium(%)')
    s = models.FloatField('Sulphur(%)')
    mg = models.FloatField('Magnesium(%)')
    ca = models.FloatField('Calcium(%)')
    fe = models.FloatField('Iron(%)')
    zn = models.FloatField('Zinc(%)')
    enteredpersonel = models.ForeignKey(SystemUser,verbose_name='Entered by',null=True, blank=True)
    
    
    class Meta:
        ordering = ['date']
        
    def __str__(self):
        return '{}'.format(self.farm)
    
    
class PlotIrrigationEvent(models.Model):
    CLIMATE_CHOICES=(
        ('Rainy','Rainy'),
        ('Sunny','Sunny'),
        ('Cloudy','Cloudy'),
    )
    date = models.DateField('Date')
    farm = models.ForeignKey(Farm,verbose_name='Farm',null=True,blank=True)
    plotID = models.ForeignKey(Plot,verbose_name='PlotID',null=True,blank=True)
    irrigation_event = models.IntegerField('Irrigation Event')
    start_time = models.TimeField('Start time',null=True, blank=True)
    end_time = models.TimeField('End time',null=True, blank=True)
    total_time = models.FloatField('Total time(mins)',null=True, blank=True)
    application_rate = models.FloatField('Application rate(mm/hr)',null=True, blank=True)
    quantity_of_units = models.IntegerField('Quantity of unit',null=True, blank=True)
    water_application = models.CharField('Water Application',max_length =80,null=True, blank=True)
    wetteddiameteraroundplant = models.FloatField('Wetted diameter around plant(cm)',null=True, blank=True)
    irrigate_whole_or_per_plant = models.CharField('Irrigate whole or per plant',max_length=20,null=True, blank=True)
    irrigated_depth = models.FloatField('Irrigated depth(mm)',null=True, blank=True)
    service_provider = models.CharField('Service Provider',max_length=4,null=True, blank=True)
    '''
    #furrow
    '''
    quantification_method = models.CharField('Quantification method',max_length=30,null=True, blank=True)
    flume_location = models.CharField('Flume location',max_length=30,null=True, blank=True)
    waterlevel1 = models.FloatField('Water level 1',null=True, blank=True)
    waterlevel2 = models.FloatField('Water level 2',null=True, blank=True)
    furrow_irr_time = models.FloatField('Time to irrigate one furrow (mins)',null=True, blank=True)
    nfurrorws_irrigated_once = models.FloatField('Number of furrow irrigated at once',null=True, blank=True)
    waterheight = models.FloatField('Water height(cm)',null=True, blank=True)
    topfurrowwidth = models.FloatField('Top furrow width(cm)',null=True, blank=True)
    buttonfurrowwidth = models.FloatField('Button furrow width(cm)',null=True, blank=True)
    field_efficiency = models.FloatField('Field efficiency(%)',null=True, blank=True)
    conveyance_efficiency = models.FloatField('Conveyance efficiency(%)',null=True, blank=True)
    '''
    drip
    '''
    #dripline_length = models.FloatField('Drip line length(cm)',null=True, blank=True)
    #dripline_spacing = models.FloatField('Drip line spacing(cm)',null=True, blank=True)
    #emitter_spacing = models.FloatField('Emitter spacing(cm)',null=True, blank=True)
    driptank_volume = models.FloatField('Drip tank volume (L)',null=True, blank=True)
    #calibrationcup_volume = models.FloatField('Calibration cup volume(L)',null=True, blank=True)
    #emitter_wetted_diameter = models.FloatField('Emitter wetted diameter(cm)',null=True, blank=True)
    #bucket
    #bucketdiameter  = models.FloatField('Bucket diameter(cm)',null=True, blank=True)
    bucketvolume  = models.FloatField('Bucket volume(L)',null=True, blank=True)
    bucketnumbers = models.FloatField('Number of buckets',null=True, blank=True)
    '''
    WFD
    '''
    yellow_WFD_before_irrigation = models.CharField('Yellow WFD before irrigation',max_length=4,null=True, blank=True)
    red_WFD_before_irrigation= models.CharField('Red WFD before irrigation',max_length=4,null=True, blank=True)
    yellow_WFD_time_after_irrigation =  models.FloatField('Yellow WFD time after irrigation',null=True, blank=True)
    red_WFD_time_after_irrigation =  models.FloatField('Red WFD time after irrigation',null=True, blank=True)
    #enteredperson
    enteredpersonel = models.ForeignKey(SystemUser,verbose_name='Entered by',null=True, blank=True)
    ##
    climate = models.CharField('Climate',max_length=20)
    tanknumber =  models.IntegerField('Number of Tanks',null=True, blank=True)
    ##tractor mounted pump##petrol motorized pump
    technology = models.ForeignKey(Technology,verbose_name='Farm Technology',null=True, blank=True)
    gender = models.CharField('Gender',null=True, blank=True,max_length=10)
    distance_from_water_source  =  models.FloatField('Distance from water source(km)',null=True, blank=True)
    time_to_fetch_water  =  models.FloatField('Time taken to fetch water',null=True, blank=True)
    fuel = models.ForeignKey(Fuel,verbose_name='Fuel',null=True, blank=True)
    fuelcost = models.FloatField('Total income',null=True,blank=True)
    currency = models.CharField('Currency',max_length=10,null=True,blank=True)
    amount_used = models.FloatField('Amount Used (Litre)',null=True, blank=True)
    refilled_amount = models.FloatField('Refilled amount (Litre)',null=True, blank=True)
    water_level_bf_filling = models.FloatField('Water level before filling(cm)',null=True, blank=True)
    water_level_aftr_filling = models.FloatField('Water level after filling(cm)',null=True, blank=True)
    time_to_fill_water_tank = models.FloatField('Total time to fill water tank(mins)',null=True, blank=True)
    
    class Meta:
        ordering = ['date']
        
    def __str__(self):
        return '{}'.format(self.plotID)
    

class Weed(models.Model):
    date = models.DateField('Weeding date')
    farm = models.ForeignKey(Farm,verbose_name='Farm',null=True,blank=True)
    plotID = models.ForeignKey(Plot,verbose_name='PlotID',null=True,blank=True)
    weed_activities = models.CharField('What they do',max_length=80)#,choices=WEEDING_ACTIVITIES)
    #time = models.FloatField('Time taken')
    enteredpersonel = models.ForeignKey(SystemUser,verbose_name='Entered by',null=True, blank=True)
    
    class Meta:
        ordering = ['date']
        
    def __str__(self):
        return '{}'.format(self.weed_activities)
    
class ResidualHandling(models.Model): 
    date = models.DateField('Weeding date')
    farm = models.ForeignKey(Farm,verbose_name='Farm',null=True,blank=True)
    plotID = models.ForeignKey(Plot,verbose_name='PlotID',null=True,blank=True)
    residual_activities = models.CharField('What they do',max_length=80)#,choices=WEEDING_ACTIVITIES)
    time = models.FloatField('Time taken')
    enteredpersonel = models.ForeignKey(SystemUser,verbose_name='Entered by',null=True, blank=True)
    
    class Meta:
        ordering = ['date']
        
    def __str__(self):
        return '{}'.format(self.residual_activities)
    
    
class Harvest(models.Model): 
    date = models.DateField('Harvest date')
    farm = models.ForeignKey(Farm,verbose_name='Farm',null=True,blank=True)
    plotID = models.ForeignKey(Plot,verbose_name='Harvested farm',null=True,blank=True)
    time = models.FloatField('Time taken')
    crop = models.ForeignKey(Crop,verbose_name='Harvested crop')
    amount = models.FloatField('Harvest amount')
    amount_for_home = models.FloatField('Harvest amount for home(Kg)')
    amount_for_sell = models.FloatField('Harvest amount for sell(Kg)')
    enteredpersonel = models.ForeignKey(SystemUser,verbose_name='Entered by',null=True, blank=True)
    
    class Meta:
        ordering = ['plotID']
        unique_together = (('plotID','date'),)
        
    def __str__(self):
        return '{},{}'.format(self.date,self.plotID)


class SaleHarvestedCrop(models.Model): 
    date = models.DateField('Selling date')
    farm = models.ForeignKey(Farm,verbose_name='Farm',null=True,blank=True)
    plotID = models.ForeignKey(Plot,verbose_name="PlotID",null=True,blank=True)
    marketprice = models.FloatField('Market price',null=True,blank=True)
    amount = models.IntegerField('Amount sold',null=True,blank=True)
    #crop = models.ForeignKey(Crop,verbose_name='crop',null=True,blank=True)
    income = models.IntegerField('Total income',null=True,blank=True)
    mode_of_transport = models.CharField('Total income',max_length=22,null=True,blank=True)
    fare = models.FloatField('Fare',null=True,blank=True)
    fuel_type =  models.ForeignKey(Fuel,verbose_name='Fuel',null=True,blank=True)
    fuel_cost = models.FloatField('Total income',null=True,blank=True)
    #expenditure = models.FloatField('Expenditure (Tsh)',null=True,blank=True)
    #net_income = models.FloatField('Net income (Tsh)',null=True,blank=True)
    currency = models.CharField('Currency',max_length=10,null=True,blank=True)
    distance_to_the_market= models.FloatField('distance to the market(km)',null=True,blank=True)
    enteredpersonel = models.ForeignKey(SystemUser,verbose_name='Entered by',null=True, blank=True)
   
    class Meta:
        ordering = ['date']
        
    def __str__(self):
        return '{}'.format(self.farm)
    
class ResidueManagement(models.Model):
    date = models.DateField('Date')
    farm = models.ForeignKey(Farm,verbose_name="Farm")
    time_taken = models.FloatField('Time taken')
    burnt = models.BooleanField('Burnt',default=False)
    livestock = models.BooleanField('Used for livestock', default=False)
    purpose = models.TextField('Purpose',max_length=100)
    crop = models.ForeignKey(Crop,verbose_name='crop')
    enteredpersonel = models.ForeignKey(SystemUser,verbose_name='Entered by',null=True, blank=True)
    
    class Meta:
        ordering = ['date']
        
    def __str__(self):
        return '{}'.format(self.farm)

class ConsumedCrops(models.Model):
    date = models.DateField('Sell date')
    farm = models.ForeignKey(Farm,verbose_name='Farm',null=True,blank=True)
    plotID = models.ForeignKey(Plot,verbose_name='PlotID',null=True,blank=True)
    where_consumed = models.CharField('Where consumed',max_length=20,null=True,blank=True)
    how_consumed = models.CharField('How consumed',max_length=20,null=True,blank=True)
    quantity = models.FloatField('Quantity',null=True,blank=True)
    marketprice = models.FloatField('Market price',null=True,blank=True)
    totalvalue = models.FloatField('Total value',null=True,blank=True)
    currency  = models.CharField('Currency',max_length=10,null=True,blank=True)
    enteredpersonel = models.ForeignKey(SystemUser,verbose_name='Entered by',null=True, blank=True)
    
    class Meta:
        ordering = ['date']
        
    def __str__(self):
        return '{}'.format(self.totalvalue)
    

class LabourManagament(models.Model):
    LABOUR_CHOICES=(
        ('Family','Family'),
        ('Hired','Hired'),
        ('Family&Hired','Family and Hired')
    )
    
    ACTIVITY_CHOICES = (
        ('Fertilizer','Fertilizer'),
        ('Pesticide','Pesticide'),
        ('Landpreparation','Land preparation'),
        ('Landclearance','Land clearance'),
        ('Harvest','Harvest')
    )
    AREA_DESCRIPTION_CHOICES =(
        ('Nursery','Nursery'),
        ('Plot','Plot'),
        ('Bed','Bed'),
        ('Furrow','Furrow'),
    )
    
    date = models.DateField('Date',null=True,blank=True)
    farm = models.ForeignKey(Farm,verbose_name="Farm")
    areaID = models.CharField('AreaID',max_length=60,null=True,blank=True)
    #models.ForeignKey(Plot,verbose_name='PlotID',null=True,blank=True)
    areadescription = models.CharField('Area description',max_length=40,null=True,blank=True)
    labour = models.CharField('Labour',max_length=45)
    hired_female_number = models.IntegerField('Numbe of hired female labour',null=True,blank=True)
    hired_female_time = models.FloatField('Time taken for hired female',null=True,blank=True)
    hired_male_number = models.IntegerField('Number of hired male labour',null=True,blank=True)
    hired_male_time = models.FloatField('Time taken for hired male',null=True,blank=True)
    family_female_number = models.IntegerField('Number of family female labour',null=True,blank=True)
    family_female_time = models.FloatField('Time taken for family female',null=True,blank=True)
    family_male_number = models.IntegerField('Number of family male labour',null=True,blank=True)
    family_male_time = models.FloatField('Time taken fo family male',null=True,blank=True)
    #time_taken = models.FloatField('Time taken',null=True,blank=True)
    activity = models.CharField('Performed activity',max_length=100)
    wage = models.FloatField('Daily wage',null=True,blank=True)
    price_unit = models.CharField('Currency',max_length=10,null=True,blank=True)
    enteredpersonel = models.ForeignKey(SystemUser,verbose_name='Entered by',null=True, blank=True)
    

    class Meta:
        ordering = ['date']
        
    def __str__(self):
        return '{}'.format(self.farm)


class WaterSources(models.Model):
    ID  = models.CharField('Water source ID',primary_key=True,max_length=10)
    name = models.CharField('Water source type',max_length=50)
    #name = models.CharField('Water source ',primary_key=True,max_length=50)
    class Meta:
        ordering = ['name']
        
    def __str__(self):
        return '{}'.format(self.name)
    
class WaterSourceCategory(models.Model):
    watersourcetype = models.ForeignKey(WaterSources,verbose_name='Water source type')
    category  = models.CharField('Pumping Source',primary_key=True,max_length=50)
    
    
    class Meta:
        ordering = ['category']
        
    def __str__(self):
        return '{}'.format(self.category)


class LandClearance(models.Model):
    date = models.DateField('Date')
    farm = models.ForeignKey(Farm,verbose_name='Farm',null=True,blank=True)
    plotID = models.ForeignKey(Plot,verbose_name='PlotID',null=True,blank=True)
    landclearanceoption = models.CharField('Land clearance option',max_length=50)
    enteredpersonel = models.ForeignKey(SystemUser,verbose_name='Entered by',null=True, blank=True)
    
    class Meta:
        ordering = ['plotID']
        
    def __str__(self):
        return '{}'.format(self.plotID)
    
    
class LandPreparation(models.Model):
    date = models.DateField('Land preparation date')
    farm = models.ForeignKey(Farm,verbose_name='Farm',null=True,blank=True)
    plotID = models.ForeignKey(Plot,verbose_name='PlotID',null=True,blank=True)
    landpreparationtool = models.CharField('Land preparation tool',max_length=50)
    enteredpersonel = models.ForeignKey(SystemUser,verbose_name='Entered by',null=True, blank=True)
    
    class Meta:
        ordering = ['plotID']
        
    def __str__(self):
        return '{}'.format(self.plotID)


class WaterliftingCalibrations(models.Model):
    date = models.DateField('Date')
    farm = models.ForeignKey(Farm,verbose_name='Farm',null=True,blank=True)
    #plot = models.ForeignKey(Plot,verbose_name="Plot",default='dd')
    technology = models.ForeignKey(Technology,verbose_name='Technology')
    event = models.IntegerField('Event number',null=True, blank=True)
    waterlevel = models.FloatField('Water level(m)',null=True, blank=True)
    gender = models.CharField('Gender',null=True, blank=True,max_length=10)
    age_group = models.CharField('Age group',null=True, blank=True,max_length=15)
    start_time = models.TimeField('Start time')
    end_time = models.TimeField('End time')
    total_time = models.FloatField('Total time(mins)')
    bucket_volume = models.FloatField('Bucket volume',null=True, blank=True)
    discharge = models.FloatField('Discharge(L/s)',null=True, blank=True)
    enteredpersonel = models.ForeignKey(SystemUser,verbose_name='Entered by',null=True, blank=True)
    
    class Meta:
        ordering = ['date']
        
    def __str__(self):
        return '{}'.format(self.farm)

class ApplicationCalibration(models.Model):
    date = models.DateField('Date')
    farm = models.ForeignKey(Farm,verbose_name='Farm',null=True,blank=True)
    plot = models.ForeignKey(Plot,verbose_name="Plot")
    water_application = models.CharField('Water Application',max_length =80)
    bucketdiameter  = models.FloatField('Bucket/Tank diameter(cm)',null=True, blank=True)
    bucketvolume  = models.FloatField('Bucket/Tank volume(L)',null=True, blank=True)
    start_time = models.TimeField('Start time',null=True, blank=True)
    end_time = models.TimeField('End time',null=True, blank=True)
    total_time = models.FloatField('Total time(mins)',null=True, blank=True)
    application_rate = models.FloatField('Application rate(mm/hr)',null=True, blank=True)
    bucketnumbers = models.FloatField('Number of buckets/Tanks',null=True, blank=True)
    waterheight = models.FloatField('Water height(cm)',null=True, blank=True)
    topfurrowwidth = models.FloatField('Top furrow width(cm)',null=True, blank=True)
    irrigated_depth = models.FloatField('Irrigated depth(cm)',null=True, blank=True)
    buttonfurrowwidth = models.FloatField('Button furrow width(cm)',null=True, blank=True)
    wetteddiameteraroundplant = models.FloatField('Wetted diameter around plant(cm)',null=True, blank=True)
    irrigate_whole_or_per_plant = models.CharField('Irrigate whole or per plant',max_length=20,null=True, blank=True)
    field_efficiency = models.FloatField('Field efficiency(%)',null=True, blank=True)
    conveyance_efficiency = models.FloatField('Conveyance efficiency(%)',null=True, blank=True)
    dripline_numbers = models.IntegerField('Number of drip lines',null=True, blank=True)
    calibration_cup_time = models.IntegerField('Calibration cup time(mins)',null=True, blank=True)
    calibration_method = models.CharField('Calibration method',null=True, blank=True,max_length=20)
    dripline_length = models.FloatField('Drip line length(m)',null=True, blank=True)
    dripline_spacing = models.FloatField('Drip line spacing(cm)',null=True, blank=True)
    emitter_spacing = models.FloatField('Emitter spacing(cm)',null=True, blank=True)
    driptank_volume = models.FloatField('Drip tank volume (L)',null=True, blank=True)
    calibrationcup_volume = models.FloatField('Calibration cup volume(L)',null=True, blank=True)
    emitter_wetted_diameter = models.FloatField('Emitter wetted diameter(cm)',null=True, blank=True)
    enteredpersonel = models.ForeignKey(SystemUser,verbose_name='Entered by',null=True, blank=True)

    
    '''
    ApplicationCalibration(date,plot,water_application,bucketdiameter,bucketvolume,start_time,end_time,total_time,application_rate,bucketnumbers,waterheight,
    topfurrowwidth,buttonfurrowwidth,buttonfurrowwidth,wetteddiameteraroundplant,irrigate_whole_or_per_plant,field_efficiency,
    conveyance_efficiency,dripline_length,dripline_spacing,emitter_spacing,driptank_volume,calibrationcup_volume,emitter_wetted_diameter)
    '''
    class Meta:
        ordering = ['date']
        
    def __str__(self):
        return '{}'.format(self.plot)
    
class OtherWaterUsage(models.Model):
    date = models.DateField('Date')
    farm = models.ForeignKey(Farm,verbose_name="Farm")
    #plot = models.ForeignKey(Plot,verbose_name="Plot")
    bucketnumber  = models.FloatField('Bucket number',null=True, blank=True)
    bucketvolume = models.FloatField('Bucket volume (L)',null=True, blank=True)
    technology = models.ForeignKey(Technology,verbose_name='Technology')
    usagepurpose = models.CharField('Usage',null=True, blank=True,max_length=45)
    start_time = models.TimeField('Start time',null=True, blank=True)
    end_time  = models.TimeField('End time',null=True, blank=True)
    total_time = models.FloatField('Total time',null=True, blank=True)
    totalvolume = models.FloatField('Total volume (L)',null=True, blank=True)
    lifting_technology_yes_no = models.CharField('Lifting technology (Yes/No)',null=True, blank=True,max_length=4)
    enteredpersonel = models.ForeignKey(SystemUser,verbose_name='Entered by',null=True, blank=True)
    
class Remark(models.Model):
    start_date = models.DateField('Stress start date',null=True, blank=True)
    end_date = models.DateField('Stress end Date',null=True, blank=True)
    farm = models.ForeignKey(Farm,verbose_name="Farm")
    plot = models.ForeignKey(Plot,verbose_name="Plot")
    stress = models.CharField('Stress',null=True, blank=True,max_length=25)
    severness = models.CharField('Severness',null=True, blank=True,max_length=8)
    enteredpersonel = models.ForeignKey(SystemUser,verbose_name='Entered by',null=True, blank=True)
    
    class Meta:
        ordering = ['plot']
        
    def __str__(self):
        return '{}'.format(self.farm)


class MyTestModel(models.Model):
    name = models.CharField(max_length=150)
    age = models.IntegerField()
    length = models.FloatField()
    
    class Meta:
        ordering =['name']
        
    def __str__(self):
        return self.name
    
    
#from adaptor.model import CsvModel
'''   
class MyTestModelCSVModel(CsvModel):
    name = CharField(match="name")
    age = IntegerField(match="age")
    length = FloatField(match="length")
    
    class Meta:
        delimiter = ";"
        dbModel = MyTestModel
 
'''

'''
class MyCSVImporterModel(CSVImporter):
    fields =["S/N","STUDENT'S NAME","REG. NO","MARKS (%)"]
    class Meta:
        delimiter = ","
    
'''
'''

'''
'''  
class PointOfInterest(models.Model):
    name = models.CharField(max_length=100)
    position = GeopositionField()
    
    class Meta:
        ordering = ['name']
        
    def __str__(self):
        return '{}'.format(self.name)
        
 
class Author(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    

class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Book(models.Model):
    name = models.CharField('Book name', max_length=100)
    author = models.ForeignKey(Author, blank=True, null=True)
    author_email = models.EmailField('Author email', max_length=75,blank=True)
    imported = models.BooleanField(default=False)
    published = models.DateField('Published',blank=True,null=True)
    price = models.DecimalField(max_digits=10,decimal_places = 2,null=True,blank=True)
    categories = models.ManyToManyField(Category,blank=True)
    
    def __str__(self):
        return self.name
'''
   
