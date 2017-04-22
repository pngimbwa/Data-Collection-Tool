from django.db import models
from django.contrib.auth.models import User #help us to access User object

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
        return self.village
    
class Group(models.Model):
    GroupID = models.CharField('ID',primary_key=True,max_length=10)
    name =models.CharField('Name',max_length=45)
    #village = models.ForeignKey(Village, verbose_name="Village")
    
    class Meta:
        ordering = ['GroupID']
        
    def __str__(self):
        return '{}'.format(self.name)
    
'''   
class CropVariety(models.Model):
    variety = models.CharField('Variety',primary_key=True, max_length=20)
    
    class Meta:
        ordering = ['variety']
        
    def __str__(self):
        return '{}'.format(self.variety)
'''

class Crop(models.Model):
    name = models.CharField('Name',primary_key=True, max_length=20)
    #variety_type = models.ForeignKey(CropVariety, verbose_name="Variety type")
    
    class Meta:
        ordering = ['name']
        
    def __str__(self):
        return '{}'.format(self.name)
       
class SystemUser(models.Model):
    user = models.OneToOneField(User,related_name="user_profile",primary_key=True) 
    firstname = models.CharField('First name',max_length=80)
    middlename = models.CharField('Middle name',max_length=80,null=True, blank=True)
    lastname = models.CharField('Last name',max_length=80)
    role = models.CharField('Role',max_length=40)
    phone = models.CharField('Phone',max_length=50,null=True, blank=True)
    gender = models.CharField('Gender',max_length=10)#,choices=GENDER_CHOICE)
    institution = models.CharField('Institution',max_length=100)
    village = models.ForeignKey(Village, verbose_name="Village")
    country = models.ForeignKey(Country, verbose_name="Country")
    
    
    class Meta:
        ordering = ['user']
        
    def __str__(self):
        return '{}'.format(self.user)

    
class People(models.Model):
    personID = models.CharField('Person ID',primary_key=True,max_length=45)
    firstname = models.CharField('First name',max_length=80)
    middlename = models.CharField('Middle name',max_length=80,null=True, blank=True)
    lastname = models.CharField('Last name',max_length=80)
    gender = models.CharField('Gender',max_length=10)#,choices=GENDER_CHOICE)
    group = models.ForeignKey(Group, verbose_name="Group",null=True, blank=True)
    #age_group = models.CharField('Age group',max_length=10)
    role = models.CharField('Role',max_length=40)
    phone = models.CharField('Phone',max_length=50,null=True, blank=True)
    village = models.ForeignKey(Village, verbose_name="Village")
    
    class Meta:
        ordering = ['personID']
        #managed = False
        #db_table = 'Peoples'
        #verbose_name = 'People'
        
    def diplay(self):
        return self.personID
    
    def __str__(self):
        return '{} {}'.format(self.firstname, self.lastname)
    
class House(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    owner = models.ForeignKey(People,verbose_name='Owner(Farmer)')
    
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
    family_member = models.ManyToManyField(People,verbose_name="Household family members")
    relation = models.CharField('Relation',max_length=20,default='Household member')
    
    class Meta:
        ordering = ['farmer']
        
    def __str__(self):
        return '{}'.format(self.farmer)

class Farm(models.Model):
    farmID = models.OneToOneField(People,primary_key=True,to_field='personID',related_name='farms')
    number = models.IntegerField('Total plot numbers',default=4)
    fieldsize = models.FloatField('Field Size (sq.m)')
    total_irrigated_plots_land_area = models.FloatField('Total irrigated plots land area (sq.m)')
    total_irrigated_plots = models.IntegerField('Number of irrigated plots')
    
    
    class Meta:
        ordering = ['farmID']
    
    def __int__(self):
        return self.number
    
    def __str__(self):
        return self.farmID

'''
class FarmTotalPlotNumber(models.Model):
    date = models.DateField('Date')
    number = models.IntegerField('Total plot numbers')
    farm = models.ManyToManyField(Farm,verbose_name="Farm(s)")
    
    class Meta:
        ordering = ['number']
         
    def __int__(self):
        return self.number
    def __str__(self):
        return self.number
'''

class Plot(models.Model):
    farm = models.ForeignKey(Farm,verbose_name='FarmID')
    plotID = models.CharField('PlotID',max_length=50)
    latitude = models.FloatField()
    longitude = models.FloatField()
    village = models.ForeignKey(Village, verbose_name="Village")
    
    class Meta:
        ordering = ['plotID']
        unique_together = ('farm','plotID')
         
    def __str__(self):
        return '{}'.format(self.plotID)

    
class PlantingMethod(models.Model):
    PLANTING_METHOD_CHOICES = (
           ('Directseeding','Direct seeding'),
            ('Transplanting','Transplanting'),
    )
    plotID = models.ForeignKey(Plot,verbose_name='PlotID',null=True,blank=True)
    planting_method = models.CharField('Planting Method',max_length=100)#,choices=PLANTING_METHOD_CHOICES)
    seeding_date = models.DateField('Seeding Date',null=True,blank=True)
    planting_date = models.DateField('Planting date',null=True,blank=True)
    seeding_rate = models.FloatField('seeding rate',null=True,blank=True)
    seed_spacing_within_a_row = models.FloatField('seed spacing within a row(cm)',null=True,blank=True)
    seed_spacing_btn_a_row = models.FloatField('seed spacing btn a row(cm)',null=True,blank=True)
    
    class Meta:
        ordering =['plotID']
        
    def __str__(self):
        return '{}'.format(self.plotID)


class PlotManagement(models.Model):
    date = models.DateField('Date')
    farm = models.ForeignKey(Farm,verbose_name='FieldID')
    plotID = models.ForeignKey(Plot,verbose_name='PlotID')
    elevation = models.FloatField('elevation',null=True,blank=True)
    plot_size = models.FloatField('Plot size(sq.m)')
    crop = models.ForeignKey(Crop,verbose_name='Crop')
    water_management_method = models.CharField('Water management method',max_length = 80)#,choices=PUMPING_SOURCE_CHOICES)
    water_source = models.CharField('Water Source',max_length = 80)#,choices=WATER_SOURCE_CHOICES)
    water_application = models.CharField('Water Application',max_length =80)#,choices=WATER_APPLICATION_CHOICES)
  
    class Meta:
        ordering = ['farm']
        
    def __str__(self):
        return '{}'.format(self.farm)
    
class PumpingSource(models.Model):
    date = models.DateField('date')
    farm = models.ForeignKey(Farm,verbose_name='Farm(s)')
    source = models.CharField('Name',max_length=80)
    latitude = models.FloatField("Source's latitude")
    longitude = models.FloatField("Source's longitude")
    depth = models.FloatField('Depth(m)',null=True,blank=True)
    diameter = models.FloatField('Diameter(m)',null=True,blank=True)
    
    
    class Meta:
        ordering = ['depth']
        unique_together = (('latitude','longitude'),)
        
    def __str__(self):
        return '{}'.format(self.farm)

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
    plotID = models.ForeignKey(Plot,verbose_name='PlotID')
    activity = models.TextField('Activity',max_length=200)#,choices=ACTIVITY_CHOICES)
    number = models.IntegerField('Number of people')
    
    class Meta:
        ordering = ['date']
        
    def __str__(self):
        return '{}'.format(self.farm)

class PlotCultivation(models.Model): 
    date = models.DateField('Cultivation date')
    plotID = models.ForeignKey(Plot,verbose_name='PlotID')
    cultivation_method = models.CharField('Method of Cultivation',max_length=80)
    
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
    group = models.ForeignKey(Group,verbose_name='Group')
    name = models.ForeignKey(Pump,verbose_name='Name',null=True,blank=True)
    size = models.CharField('size',max_length=50)
    price = models.FloatField('Bought price',null=True,blank=True)
    date = models.DateField('Bought date',null=True,blank=True)

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
    group = models.ForeignKey(Group,verbose_name='Group')
    spaire = models.ForeignKey(Spaire,verbose_name='Spaire')
    price = models.FloatField('Bought price (Tsh)',null=True,blank=True) ########################
    date = models.DateField('Bought date',null=True,blank=True)
    
    class Meta:
        ordering = ['group']
        
    def __str__(self):
        return '{}'.format(self.group)

    
class Service(models.Model):
    date = models.DateField('date')
    group = models.ForeignKey(Group,verbose_name='Group')
    repaire_type = models.TextField('Type of repaires',max_length=100)
    spaire = models.ManyToManyField(Spaire, verbose_name="Required spaire")
    pump = models.ManyToManyField(Pump, verbose_name="Pump")
    price = models.FloatField('Price of spaire parts (Tsh)')
    total_cost = models.FloatField('Total repaire cost (Tsh)')
    
    class Meta:
        ordering = ['date']


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
    ##farm = models.ForeignKey(Farm,verbose_name='Farm')
    plotID = models.ForeignKey(Plot,verbose_name='Plot ID',null=True,blank=True)
    name = models.ForeignKey(Crop,verbose_name="Crop")
    root_depth = models.FloatField('Root depth (m)')
    planting_spacing = models.FloatField('Planting space(cm)')
    
    class Meta:
        ordering = ['plotID']
        
    def __str__(self):
        return '{}'.format(self.name)
    
class BedPlot(models.Model):
    #farm = models.ForeignKey(Farm,verbose_name='Farm')
    plotID = models.ForeignKey(Plot,verbose_name='Plot ID',null=True,blank=True)
    length = models.FloatField('Length(m)')
    width = models.FloatField('Width(m)')
    numbers = models.IntegerField('Number of beds')
    planting_density = models.IntegerField('Planting density')
    
    class Meta:
        ordering = ['plotID']
        
    def __str__(self):
        return '{}'.format(self.plotID)
    

'''
class Well(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    name = models.CharField('Name',max_length=80)
    depth = models.FloatField('Depth(m)')
    diameter = models.FloatField('Diameter(m)')
    
    class Meta:
        ordering =[depth]
        unique_together = (('latitude','longitude'),)
        
    def __str__(self):
        return '{}'.format(self.name)

class WellManagement(models.Model):
    name = models.ForeignKey(Well,verbose_name='Well')
    farm = models.ForeignKey(Farm,verbose_name='Farm(s)')
    
    class Meta:
        ordering = ['name']
        
    def __str__(self):
        return '{}'.format(self.name)

    
class Well(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    depth = models.FloatField('Depth(m)')
    diameter = models.FloatField('Diameter(m)')
    farm = models.ManyToManyField(Farm,verbose_name='Farm(s)')
    
    class Meta:
        ordering = ['depth']
        
    def __str__(self):
        return '{}'.format(self.depth)

'''

class Furrow(models.Model):
    #farm = models.ForeignKey(Farm,verbose_name='Farm')
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
    date = models.DateField('Received date')
    technology = models.ForeignKey(Technology,verbose_name='Technology')
    farm = models.ForeignKey(Farm,verbose_name='Farm',null=True,blank=True)
    
    class Meta:
        ordering = ['date']
        
    def __str__(self):
        return '{}'.format(self.technology)
    
class TechnologyFailure(models.Model):
    date = models.DateField('Failure date')
    farm = models.ForeignKey(Farm,verbose_name='Farm',null=True,blank=True)
    technology = models.ForeignKey(Technology,verbose_name='Technology')
    reason = models.TextField('Reason',max_length=100)
    
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
    
    class Meta:
        ordering = ['date']
        
    def __str__(self):
        return '{}'.format(self.technology)
    
    
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
    plotID = models.ForeignKey(Plot,verbose_name='Plot ID',null=True,blank=True)
    crop_stage = models.CharField('Crop Stage',max_length=40)
    fertilizer = models.ForeignKey(Fertilizer,verbose_name='Fertilizer')
    quantity_in_kg = models.FloatField('Quantity(Kg)',null=True,blank=True)
    fertilizer_management = models.CharField('Fertilizer Management',max_length = 75)
    nitrogen = models.FloatField('N content (%)')
    phosphorus = models.FloatField('Phosphorus (ppm)')
    potassium = models.FloatField('Potassium (ppm)')
    sulphur = models.FloatField('Sulphur(g/kg)',null=True, blank=True)
    organic_matter = models.FloatField('Organic Matter (%)')
    price = models.FloatField('Price',null=True,blank=True)
    price_unit = models.FloatField('Price Unit',null=True,blank=True)
    
    class Meta:
        ordering = ['date']
        
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
    #farm = models.ForeignKey(Farm,verbose_name='Farm')
    plotID = models.ForeignKey(Plot,verbose_name='Plot ID',null=True,blank=True)
    name = models.ForeignKey(Pesticide, verbose_name='Name')
    crop_stage = models.CharField('Crop Stage',max_length=40)
    form = models.CharField('Form',max_length=20)
    quantity_in_litre = models.FloatField('Quantity(Litre)',null=True,blank=True)
    quantity_in_kg = models.FloatField('Quantity(Kg)',null=True,blank=True)
    price = models.FloatField('Price',null=True,blank=True)
    price_unit = models.FloatField('Price Unit',null=True,blank=True)
    
    class Meta:
        ordering = ['name']
        
    def __str__(self):
        return '{}'.format(self.name)
    
    
class YieldFarmLevel(models.Model):
    date = models.DateField('Harvesting Date')
    farm = models.ForeignKey(Farm,verbose_name='Farm')
    area = models.FloatField('Area (sq.m)')
    fresh_dry = models.CharField('Fresh/Dry',max_length=10,null=True,blank=True)
    #dry = models.BooleanField(default=False)
    marketable_yield = models.FloatField('Marketable yield (Kg)')
    unmarketable_yield = models.FloatField('Unmarketable yield (Kg)')
    biomas = models.FloatField('Biomas (Kg)')
    
    class Meta:
        ordering = ['date']
        
    def __str__(self):
        return '{}'.format(self.farm)
  

class CropMonitoringPlantHeight(models.Model):
    date = models.DateField('Monitoring Date')
    #farm = models.ForeignKey(Farm,verbose_name='Farm')
    plotID = models.ForeignKey(Plot,verbose_name='Plot',null=True,blank=True)
    crop_stage = models.CharField('Crop Stage',max_length=50)
    plant_density_per_bed = models.FloatField('Plant density/bed',null=True,blank=True)
    plant_density_per_sqm = models.FloatField('plant density/sq.m',null=True,blank=True)
    number_of_good_plants = models.IntegerField('Number of good plants',null=True,blank=True)
    number_of_bad_plants = models.IntegerField('Number of bad plants',null=True,blank=True)
    plant_number = models.IntegerField('Number of bad plants',null=True,blank=True)
    plant_height = models.FloatField('Plant height(m)',null=True,blank=True)
    plant_canopy_width = models.FloatField('Plant canopy width(m)',null=True,blank=True)
    length_of_crop_stage = models.FloatField('Length of crop stage(days)',null=True,blank=True)
    plant_leave_number = models.IntegerField('Leaves per plant',null=True,blank=True)
    plant_leave_length = models.FloatField('Plant leave length(cm)',null=True,blank=True)
    plant_leave_width = models.FloatField('Plant leave width(cm)',null=True,blank=True)
    
    class Meta:
        ordering = ['date']
        
    def __str__(self):
        return '{}'.format(self.farm)

class YieldRowBedLevel(models.Model):
    date = models.DateField('Harvesting Date')
    #farm = models.ForeignKey(Farm,verbose_name='Farm')
    plotID = models.ForeignKey(Plot,verbose_name='PlotID',null=True,blank=True)
    harvesting_method = models.CharField('Harvesting method',max_length=80)
    fresh_dry = models.CharField('Fresh/Dry',max_length=10,blank=True,null=True)
    area = models.FloatField('area(sq.m)',blank=True,null=True)
    marketable_produced = models.FloatField('Marketable produced',blank=True,null=True)
    ummarketable_produced = models.FloatField('Unmarketable produced',blank=True,null=True)
    marketable_produced_weight = models.FloatField('Weight of marketable produced(kg)',blank=True,null=True)
    unmarketable_produced_weight= models.FloatField(' Weight of unmarketable produced(kg)',blank=True,null=True)

    class Meta:
        ordering = ['date']
        
    def __str__(self):
        return '{}'.format(self.farm)


class YieldPlantLevel(models.Model):
    date = models.DateField('Date')
    #farm = models.ForeignKey(Farm,verbose_name='Farm')
    plotID = models.ForeignKey(Plot,verbose_name='PlotID',null=True,blank=True)
    harvest_method = models.CharField('Harvest Method',max_length=50)
    fresh_dry = models.CharField('Fresh/Dry',max_length=10)
    #dry = models.BooleanField(default=False)
    plant_number = models.IntegerField('Plant number',null=True,blank=True)
    marketable_produced = models.FloatField('Number of marketable produced',null=True,blank=True)
    unmarketable_produced = models.FloatField('Number of unmarketable produced',null=True,blank=True)
    marketable_produced_weight = models.FloatField('Total weight of marketable produced(kg)',null=True,blank=True)
    unmarketable_produced_weight= models.FloatField(' Total weight of unmarketable produced(kg)',null=True,blank=True)
    diameter_width_produced =  models.FloatField('Diameter/width produce',null=True,blank=True)
    length =  models.FloatField('Length produced(cm)',null=True,blank=True)
    #Average_length =  models.FloatField('Average length(cm)')
    #stdev_length =  models.FloatField('Stdev Length(cm)')
    residual_biomass =  models.FloatField('Residual biomass(Kg)',null=True,blank=True)

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
    seed = models.ForeignKey(Seed,verbose_name ='seed')
    technology = models.ForeignKey(Technology,verbose_name='Calibrated Technology',blank=True,null=True)
    date_bed_preparation = models.DateField('Bed Preparation date')
    date_trasplanting = models.DateField('Transplanting date')
    
    class Meta:
        ordering = ['NurseryID']
        
    def __str__(self):
        return '{}'.format(self.NurseryID)


class Transplanting(models.Model):
    date = models.DateField('transplanting date')
    nurseryID = models.ForeignKey(Nursery,verbose_name='nurseryID',null=True,blank=True)
    plotID = models.ForeignKey(Plot,verbose_name='PlotID',null=True,blank=True)
    plantsnumber = models.IntegerField('Total number of plants transplanted')
    plant_spacing_btn_row = models.FloatField('Plant spacing between row(cm)')
    plant_spacing_btn_plants_within_rows = models.FloatField('Plant spacing between plants within rows(cm)')
    plantsnumber_per_row = models.IntegerField('Plant number per row')
    
       
    class Meta:
        ordering =['plotID']
        
    def __str__(self):
        return '{}'.format(self.plotID)   
    

class SeedManagement(models.Model):
    date = models.DateField('Date')
    nursery = models.ForeignKey(Nursery,verbose_name='Nursery planted on')
    seed = models.ForeignKey(Seed,verbose_name='Seed')
    quantity = models.FloatField('Quantity (kg)')
    price_per_unit = models.FloatField('Price per unit (Tsh)')
    total_cost = models.FloatField('Total cost (Tsh)')
    
    
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
    seedling_yield_per_bed = models.FloatField('Seedling yield per bed')
    
    
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
    discharge = models.FloatField('Discharge(m3/s)')
    standard_volume = models.FloatField('Standard Volume (Litre or m3/s)')
    quantity = models.FloatField('Quantity',null=True, blank=True)
    climate = models.CharField('Climate',max_length=30)#choices=CLIMATE_CHOICES
    total_volume = models.FloatField('Total Volume (Litre)')
    
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
    #farm = models.ForeignKey(Farm,verbose_name='Farm')
    plotID = models.ForeignKey(Plot,verbose_name='PlotID',null=True,blank=True)
    soilclass = models.ForeignKey(Soil,verbose_name='Soil class')
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
    
    
    class Meta:
        ordering = ['date']
        
    def __str__(self):
        return '{}'.format(self.soilclass)


class TDRMeasurement(models.Model):
    date = models.DateField('Measurement Date')
    #farm = models.ForeignKey(Farm,verbose_name='Farm')
    plotID = models.ForeignKey(Plot,verbose_name='PlotID',null=True,blank=True)
    measurement = models.FloatField('Measurement(%)')
    
    
    class Meta:
        ordering = ['date']
        
    def __str__(self):
        return '{}'.format(self.measurement)
    
class GravimetricSoilMoisture(models.Model):
    date = models.DateField('Measurement Date')
    #farm = models.ForeignKey(Farm,verbose_name='Farm')
    plotID = models.ForeignKey(Plot,verbose_name='PlotID',null=True,blank=True)
    time = models.TimeField('Time taken',null=True, blank=True)
    depth = models.FloatField('Depth sample',null=True, blank=True)
    volume_core_used = models.FloatField('Volume core used (cm3)',null=True, blank=True)
    weight_core_used = models.FloatField('Weight core used (g)',null=True, blank=True)
    wet_weight = models.FloatField('Wet weight (g)',null=True, blank=True)
    dry_weight = models.FloatField('Dry weight(g)',null=True, blank=True)
    bulk_density = models.FloatField('Bulk density(g/cm3)',null=True, blank=True)
    gravimetric_moisture_content = models.FloatField('Gravimetric moisture content',null=True, blank=True)
    volumetric_moisture_content = models.FloatField('Volumetric moisture content',null=True, blank=True)
    
    class Meta:
        ordering = ['date']
        
    def __str__(self):
        return '{}'.format(self.plotID)



class SoilMoistureProfiler(models.Model):
    date = models.DateField('Measurement Date')
    #farm = models.ForeignKey(Farm,verbose_name='Farm')
    plotID = models.ForeignKey(Plot,verbose_name='PlotID',null=True,blank=True)
    measurement  = models.IntegerField('Measurement number',null=True, blank=True)
    depth_10  = models.FloatField('Measurement at 10cm',null=True, blank=True)
    depth_20  = models.FloatField('VMeasurement at 20cm',null=True, blank=True)
    depth_30  = models.FloatField('Measurement at 30cm',null=True, blank=True)
    depth_40  = models.FloatField('Measurement at 40cm',null=True, blank=True)
    depth_60  = models.FloatField('Measurement at 60cm',null=True, blank=True)
    depth_100 = models.FloatField('Measurement at 100cm',null=True, blank=True)
    #average   = models.FloatField('Average',null=True, blank=True)

    class Meta:
        ordering = ['date']
        
    def __str__(self):
        return '{}'.format(self.farm)

class SoilMoistureMeasurementManagement(models.Model):
    date = models.DateField('Measurement Date')
    #farm = models.ForeignKey(Farm,verbose_name='Farm')
    plotID = models.ForeignKey(Plot,verbose_name='PlotID',null=True,blank=True)
    measurement_option = models.CharField('Soil measurement used(option)',max_length=75)
    
    class Meta:
        ordering = ['date']
        
    def __str__(self):
        return '{}'.format(self.measurement_used)
    

    
class TissueNutrientAnalysis(models.Model):
    date = models.DateField('Measurement Date')
    #farm = models.ForeignKey(Farm,verbose_name='Farm')
    plotID = models.ForeignKey(Plot,verbose_name='PlotID',null=True,blank=True)
    plant_tissue_part = models.CharField('Plant tissue part',max_length=30)
    plantnumber = models.IntegerField('Plant number')
    #rownumber = models.IntegerField('Row number')
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
    date = models.DateField('Measurement Date')
    #farm = models.ForeignKey(Farm,verbose_name='Farm')
    plotID = models.ForeignKey(Plot,verbose_name='PlotID',null=True,blank=True)
    irrigation_event = models.IntegerField('Irrigation Event')
    technology = models.ForeignKey(Technology,verbose_name='Technology')
    start_time = models.TimeField('Start time')
    end_time = models.TimeField('End time')
    total_time = models.FloatField('Total time(mins)')
    quantification_method = models.CharField('Quantification method',max_length=30)
    flume_location = models.CharField('Flume location',max_length=30)
    waterlevel1 = models.FloatField('Water level 1')
    waterlevel2 = models.FloatField('Water level 2',null=True, blank=True)
    furrow_irr_time = models.FloatField('Time to irrigate one furrow (mins)')
    nfurrorws_irrigated_once = models.FloatField('Number of furrow irrigated at once')
    application_rate = models.FloatField('Application rate(m3/s)',null=True, blank=True)
    standardvolume = models.FloatField('Standard volume',null=True, blank=True)
    quantity_of_units = models.IntegerField('Quantity of unit',null=True, blank=True)
    yellow_WFD_before_irrigation = models.IntegerField('Yellow WFD before irrigation',null=True, blank=True)
    red_WFD_before_irrigation= models.IntegerField('Red WFD before irrigation',null=True, blank=True)
    yellow_WFD_time_after_irrigation =  models.FloatField('Yellow WFD time after irrigation',null=True, blank=True)
    red_WFD_time_after_irrigation =  models.FloatField('Red WFD time after irrigation',null=True, blank=True)
    climate = models.CharField('Climate',max_length=20)#choices=CLIMATE_CHOICES
    
    class Meta:
        ordering = ['date']
        
    def __str__(self):
        return '{}'.format(self.plotID)
    

class Weed(models.Model): 
    WEEDING_ACTIVITIES = (
           ('HANDWEEDING','Hand weeding'),
            ('HANDLOOSEN','Hand weeding and loosen the soil manually around plants'),
            ('HOE','Hoe'),
            ('OTHER','Other please specify'),
    )
    date = models.DateField('Weeding date')
    #farm = models.ForeignKey(Farm,verbose_name='Farm')
    plotID = models.ForeignKey(Plot,verbose_name='PlotID',null=True,blank=True)
    weed_activities = models.CharField('What they do',max_length=100)#,choices=WEEDING_ACTIVITIES)
    #crop = models.ForeignKey(Crop,verbose_name='Crop(s)')
    #weeding_personel = models.ManyToManyField(People,verbose_name='Weeding personel(s)',blank=True)
    time = models.FloatField('Time taken')

    class Meta:
        ordering = ['date']
        
    def __str__(self):
        return '{}'.format(self.weed_activities)
    
    
class Harvest(models.Model): 
    date = models.DateField('Harvest date')
    plotID = models.ForeignKey(Plot,verbose_name='Harvested farm',null=True,blank=True)
    time = models.FloatField('Time taken')
    crop = models.ForeignKey(Crop,verbose_name='Harvested crop')
    amount = models.FloatField('Harvest amount')
    amount_for_home = models.FloatField('Harvest amount for home(Kg)')
    amount_for_sell = models.FloatField('Harvest amount for sell(Kg)')
    #price = models.FloatField('Price per unit (Tsh)')
    #harvest_personel = models.ForeignKey(People,verbose_name='Harvest personel',null=True)
    #payement = models.FloatField('Total payement(Tsh)',null=True,blank=True)
    
    class Meta:
        ordering = ['plotID']
        unique_together = (('plotID','date'),)
        
    def __str__(self):
        return '{},{}'.format(self.date,self.plotID)
'''
class HarvestStoreManagement(models.Model):
    date = models.DateField('Harvest date')
    harvest = models.ForeignKey(Harvest,verbose_name='Date,Farm')
    harvested_amount
    amount_sold
    amount_left
    
    def check_balance(self):
       
class Account(models.Model):
    name = models.CharField(max_length=20)
    credit_balance = models.IntegerField(default = 0)
    debit_balance = models.IntegerField(default = 0)
    balance_type = models.CharField(max_length = 10, default = "Z")
    balance = models.IntegerField(default = 0)

    def credit(self, ammount):
        self.credit_balance += ammount
        self.get_balance()
    def debit(self, ammount):
        self.debit_balance +=ammount
        self.get_balance()
    def get_balance(self):
        if self.credit_balance - self.debit_balance > 0:
            self.balance = self.credit_balance - self.debit_balance
            self.balance_type =  "C"
        elif self.debit_balance - self.credit_balance >0:
            self.balance = self.debit_balance - self.credit_balance
            self.balance_type = "D"
        elif self.debit_balance - self.credit_balance == 0:
            self.balance = 0
            self.balance_type = "Z"


class Transaction(models.Model):
    debit_account = models.ForeignKey(Account, related_name ='transaction_debit')
    credit_account = models.ForeignKey(Account, related_name= 'transaction_credit')
    ammount = models.IntegerField()

    def commit(self):
        self.debit_account.debit(self.ammount)
        self.credit_account.credit(self.ammount) 
    
'''
class SaleHarvestedCrop(models.Model): 
    date = models.DateField('Selling date')
    farm = models.ForeignKey(Farm,verbose_name="Farm")
    amount = models.FloatField('Amount sold')
    crop = models.ForeignKey(Crop,verbose_name='crop')
    income = models.FloatField('Total income (Tsh)')
    expenditure = models.FloatField('Expenditure (Tsh)')
    net_income = models.FloatField('Net income (Tsh)')
     
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
    
    class Meta:
        ordering = ['date']
        
    def __str__(self):
        return '{}'.format(self.farm)

class ConsumedCrop(models.Model):
    farm = models.ForeignKey(Farm,verbose_name="Farm",null=True,blank=True)
    date = models.DateField('Sell date')
    crop = models.ForeignKey(Crop,verbose_name='crop')
    amount = models.FloatField('Consumed amount')
    
    class Meta:
        ordering = ['date']
        
    def __str__(self):
        return '{},{}'.format(self.amount)
    

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
    
    date = models.DateField('Date')
    farm = models.ForeignKey(Farm,verbose_name="Farm")
    plotID = models.ForeignKey(Plot,verbose_name='PlotID',null=True,blank=True)
    labour = models.CharField('Labour',max_length=35)
    hired_female_number = models.IntegerField('Numbe of hired female labour')
    hired_male_number = models.IntegerField('Number of hired male labour')
    family_female_number = models.IntegerField('Number of family female labour')
    family_male_number = models.IntegerField('Number of family male labour')
    activity = models.CharField('Performed activity',max_length=100)
    wage = models.FloatField('Daily wage')
    price_unit = models.CharField('Currency',max_length=10,default='Tsh')
    
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
    #farm = models.ForeignKey(Farm,verbose_name="Farm")
    plotID = models.ForeignKey(Plot,verbose_name='PlotID',null=True,blank=True)
    landclearanceoption = models.CharField('Land clearance option',max_length=50)
    
    class Meta:
        ordering = ['plotID']
        
    def __str__(self):
        return '{}'.format(self.plotID)
    
    
class LandPreparation(models.Model):
    date = models.DateField('Land preparation date')
    #farm = models.ForeignKey(Farm,verbose_name="Farm")
    plotID = models.ForeignKey(Plot,verbose_name='PlotID',null=True,blank=True)
    landpreparationtool = models.CharField('Land preparation tool',max_length=50)
    
    class Meta:
        ordering = ['plotID']
        
    def __str__(self):
        return '{}'.format(self.plotID)

    
    
    
    
    
    
