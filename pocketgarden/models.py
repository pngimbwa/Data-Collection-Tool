'''
from django.db import models

from iwmi.models import Country, Crop, District, Farm, CropVariety, Group, People, Region, Row, Seed, Soil, Technology, Village, Weed, Pesticide, Fertilizer

class BedNurseryInitialActivities(models.Model):
    ACTIVITY_CHOICES =(
        ('FA','Fertilizer application'),
        ('PA','Pesticide application'), 
        )
    date = models.DateField('Date activity was performed')
    farmer_name = models.ForeignKey(People,verbose_name="Farmer's name")
    activity = models.CharField('Activity',max_length=200,choices=ACTIVITY_CHOICES)
    cost = models.FloatField('Costs')
    
    class Meta:
        ordering = ['date']
        
    def __str__(self):
        return '{}'.format(farmer_name)
    
class LandPreparation(models.Model):
    date = models.DateField('Date activity was performed')
    farmer_name = models.ForeignKey(People,verbose_name="Farmer's name")
    amount = models.FloatField('Amount')
    unit = models.FloatField('Unit')
    cost_per_unit = models.FloatField('Cost per unit')
    total_cost = models.FloatField('Total cost')

    class Meta:
        ordering = ['date']
        
    def __str__(self):
        return '{}'.format(farmer_name)
    
class ConventionalGardenPreparationCost(models.Model):
    date = models.DateField('Date activity was performed')
    farmer_name = models.ForeignKey(People,verbose_name="Farmer's name")
    plot_size = models.FloatField('Ploat size')
    material_used =  models.CharField('Material used', max_length=30)
    unit = models.FloatField('Unit')
    amount = models.FloatField('Amount')
    total_cost = models.FloatField('Total cost')
    
    class Meta:
        ordering = ['date']
        
    def __str__(self):
        return '{}'.format(farmer_name)
    
class SoilNutrientAnalysis(models.Model):
    
    STAGE_CHOICES =(
        ('early','early'),
        ('mid','mid'),
        ('end','end'),
    )
    SAMPLE_POINT_CHOICES =(
        ('top','top'),
        ('mid','mid'),
        ('bottom','bottom'),
    )
    date = models.DateField('Date activity was performed')
    farmer_name = models.ForeignKey(People,verbose_name="Farmer's name")
    stage = models.CharField('Activity',max_length=200,choices=STAGE_CHOICES)
    point_sample = models.CharField('Activity',max_length=200,choices=SAMPLE_POINT_CHOICES)
    
    class Meta:
        ordering = ['date']
        
    def __str__(self):
        return '{}'.format(farmer_name)
    

class WaterApplicationMethod(models.Model):
    IRRIGATION_METHOD_CHOICES =(
        ('1','Bucket'),
        ('2','Water hose'),
        ('3','Other,please specify'),
    )
    date = models.DateField('Date activity was performed')
    farmer_name = models.ForeignKey(People,verbose_name="Farmer's name")
    start_time = models.TimeField('Start time')
    end_time = models.TimeField('End time')
    method_used = models.CharField('Method used',max_length=200,choices=IRRIGATION_METHOD_CHOICES)
    number_of_bucket =  models.FloatField('number of bucket ')
    water_discharge =  models.FloatField('water discharge')

    class Meta:
        ordering = ['date']
        
    def __str__(self):
        return '{}'.format(farmer_name)
    
class MoistureLevel(models.Model):
    date = models.DateField('Date activity was performed')
    farmer_name = models.ForeignKey(People,verbose_name="Farmer's name")
    depth_one = models.FloatField('Depth one')
    depth_two = models.FloatField('Depth two')
    depth_three = models.FloatField('Depth three')
    before_irrigation  = models.BooleanField(default=False)
    after_irrigation  = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['date']
        
    def __str__(self):
        return '{}'.format(farmer_name)
    
class PesticideApplication(models.Model):
    date = models.DateField('Date activity was performed')
    farmer_name = models.ForeignKey(People,verbose_name="Farmer's name")
    pesticide = models.ForeignKey(Pesticide,verbose_name="Pesticide")
    amount = models.FloatField('Amount')
    pocket = models.CharField('Pocket',max_length=30)
    cost = models.FloatField('cost')
    time = models.FloatField('Time taken(mins)')
     
    class Meta:
        ordering = ['date']
        
    def __str__(self):
        return '{}'.format(farmer_name)


    
class FertilizerApplication(models.Model):
    date = models.DateField('Date activity was performed')
    farmer_name = models.ForeignKey(People,verbose_name="Farmer's name")
    fertilizer = models.ForeignKey(Fertilizer,verbose_name="Fertilizer")
    quantity= models.FloatField('Quantity')
    unit  = models.FloatField('Unit')
    pocket = models.CharField('Pocket',max_length=30)
    cost = models.FloatField('cost')
    time = models.FloatField('Time taken(mins)')
     
    class Meta:
        ordering = ['date']
        
    def __str__(self):
        return '{}'.format(farmer_name)
    
class Weed(models.Model):
    EQUIPEMENT_CHOICES=(
        ('Hand','Hand'),
        ('Hoe','Hoe'),
    )
    date = models.DateField('Date activity was performed')
    farmer_name = models.ForeignKey(People,verbose_name="Farmer's name")
    equipment_used =  models.CharField('Equipment used',max_length=200,choices=EQUIPEMENT_CHOICES)


class Labour(models.Model):
    date = models.DateField('Date activity was performed')
    farmer_name = models.ForeignKey(People,verbose_name="Farmer's name")
    activity =  models.CharField('Acitivity',max_length=50)
    number_of_people = models.IntegerField('Number of people')
    rate = models.FloatField('rate')
    total_cost = models.FloatField('total cost')
    

class Harvesting(models.Model):
    date = models.DateField('Date activity was performed')
    practice = models.CharField('practice',max_length=50)
    farmer_name = models.ForeignKey(People,verbose_name="Farmer's name")
    days = models.FlatField('Number of days')
    top = models.FloatField('Top')
    mid = models.FloatField('Mid')
    bottom = models.FloatField('Bottom')
    number_leaves_harvested = models.FloatField('number of leaves harvested')
    cumulative_leaves = models.FloatField('Cumulative leaves')
    

class HarvestSale(models.Model):
    date = models.DateField('Date activity was performed')
    practice = models.CharField('practice',max_length=50)
    farmer_name = models.ForeignKey(People,verbose_name="Farmer's name")
    quantity = models.FloatField('Quantity')
    leaves_per_unit = models.FloatField('leaves per unit')
    unit_sale_market_price = models.FloatField('unit sale market price')
    total_income = models.FloatField('total income')
    related_expenditure = models.FloatField('related expenditure')
    netincome = models.FloatField('Net income')
    
class ConsumedCrop(models.model):
    date = models.DateField('Date activity was performed')
    practice = models.CharField('practice',max_length=50)
    farmer_name = models.ForeignKey(People,verbose_name="Farmer's name")
    quantity= models.FloatField('Quantity')
    values= models.FloatField('values(Tsh)')
    
    
'''
