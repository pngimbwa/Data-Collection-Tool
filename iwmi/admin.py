from django.contrib import admin

from .models import SystemUser,WaterSources,WaterSourceCategory,Transplanting,PlantingMethod,Plot,PumpingSource,RelationManager,PlotManagement,Country,Region, District, Village, Group, LabourManagament, Crop, People, Farm, SoilMoistureMeasurementManagement,PlotOperation, PlotCultivation, Pump, PumpOwnership,Spaire,SpaireManagement,Service,FarmCost,PlotCropProperty,BedPlot,House,Furrow,Technology,TechnologyFailure,TechnologyManagement,TechnologyCalibration,Fertilizer,FertilizerManagement,Pesticide,PesticideManagement,YieldFarmLevel,CropMonitoringPlantHeight,YieldRowBedLevel,Nursery,Seed,SeedManagement,BedNursery,CropPropertyNursery,NurseryIrrigationEvent,Fuel,FuelManagement,Soil,SoilProperty,TDRMeasurement,GravimetricSoilMoisture,TissueNutrientAnalysis,PlotIrrigationEvent,YieldPlantLevel,Weed,Harvest,SaleHarvestedCrop,ResidueManagement,ConsumedCrop,SoilMoistureProfiler

class CountryAdmin(admin.ModelAdmin):
   # prepopulated_fields = {"slug" : ("crop_name",)}
    search_fields = ['name']
    list_display = ('name',)
admin.site.register(Country,CountryAdmin)

class RegionAdmin(admin.ModelAdmin):
   # prepopulated_fields = {"slug" : ("crop_name",)}
    search_fields = ['region']
    list_display = ('country','region',)
admin.site.register(Region,RegionAdmin)

class DistrictAdmin(admin.ModelAdmin):
   # prepopulated_fields = {"slug" : ("crop_name",)}
    search_fields = ['district']
    list_display = ('region','district')
admin.site.register(District,DistrictAdmin)

class VillageAdmin(admin.ModelAdmin):
   # prepopulated_fields = {"slug" : ("crop_name",)}
    search_fields = ['village']
    list_display = ('district','village')
admin.site.register(Village,VillageAdmin)

class GroupAdmin(admin.ModelAdmin):
   # prepopulated_fields = {"slug" : ("crop_name",)}
    search_fields = ['name']
    list_display = ('GroupID','name')
admin.site.register(Group,GroupAdmin)

class CropAdmin(admin.ModelAdmin):
   # prepopulated_fields = {"slug" : ("crop_name",)}
    search_fields = ['name']
    list_display = ('name',)
admin.site.register(Crop,CropAdmin)
'''
class CropVarietyAdmin(admin.ModelAdmin):
   # prepopulated_fields = {"slug" : ("crop_name",)}
    search_fields = ['variety']
    list_display = ('variety',)
admin.site.register(CropVariety,CropVarietyAdmin)
'''
class RelationManagerAdmin(admin.ModelAdmin):
   # prepopulated_fields = {"slug" : ("crop_name",)}
    search_fields = ['farmer','relation']
    list_display = ('farmer','relation')
admin.site.register(RelationManager,RelationManagerAdmin)


class PeopleAdmin(admin.ModelAdmin):
   # prepopulated_fields = {"slug" : ("crop_name",)}
    search_fields = ['personID','firstname','middlename','lastname']
    list_display = ('personID','firstname','middlename','lastname','gender','group','role','village')
admin.site.register(People,PeopleAdmin)

class LabourManagamentAdmin(admin.ModelAdmin):
   # prepopulated_fields = {"slug" : ("crop_name",)}
    search_fields = ['farm']
    list_display = ('date','farm','plotID','labour','hired_female_number','hired_male_number','family_female_number','family_male_number','activity','wage','price_unit')
admin.site.register(LabourManagament,LabourManagamentAdmin)


class FarmAdmin(admin.ModelAdmin):
   # prepopulated_fields = {"slug" : ("crop_name",)}
    search_fields = ['farmID']
    list_display = ('farmID','number','fieldsize','total_irrigated_plots','total_irrigated_plots_land_area')
admin.site.register(Farm,FarmAdmin)

'''
class FarmTotalPlotNumberAdmin(admin.ModelAdmin):
   # prepopulated_fields = {"slug" : ("crop_name",)}
    search_fields = ['number']
    list_display = ('date','number',)
admin.site.register(FarmTotalPlotNumber,FarmTotalPlotNumberAdmin)
'''

class PlotAdmin(admin.ModelAdmin):
   # prepopulated_fields = {"slug" : ("crop_name",)}
    search_fields = ['plotID','farm']
    list_display = ('plotID','farm','village','latitude','longitude')
admin.site.register(Plot,PlotAdmin)

class PlotManagementAdmin(admin.ModelAdmin):
   # prepopulated_fields = {"slug" : ("crop_name",)}
    search_fields = ['plotID','farm']
    list_display = ('date','farm','plotID','elevation','plot_size','crop','water_management_method','water_source','water_application')
admin.site.register(PlotManagement,PlotManagementAdmin)

class PumpingSourceAdmin(admin.ModelAdmin):
   # prepopulated_fields = {"slug" : ("crop_name",)}
    search_fields = ['farm','source',]
    list_display = ('date','farm','source','latitude','longitude','depth','diameter')
admin.site.register(PumpingSource,PumpingSourceAdmin)

'''
class FarmFieldsAdmin(admin.ModelAdmin):
   #prepopulated_fields = {"slug" : ("crop_name",)}
    search_fields = ['farmID']
    list_display = ('farmID',)
admin.site.register(FarmFields,FarmFieldsAdmin)
'''
class PlotOperationAdmin(admin.ModelAdmin):
   # prepopulated_fields = {"slug" : ("crop_name",)}
    search_fields = ['plotID']
    list_display = ('date','plotID','activity','number')
admin.site.register(PlotOperation,PlotOperationAdmin)

class PlotCultivationAdmin(admin.ModelAdmin):
   # prepopulated_fields = {"slug" : ("crop_name",)}
    search_fields = ['farm']
    list_display = ('date','plotID','cultivation_method')
admin.site.register(PlotCultivation,PlotCultivationAdmin)

class PumpAdmin(admin.ModelAdmin):
   # prepopulated_fields = {"slug" : ("crop_name",)}
    search_fields = ['name']
    list_display = ('name',)
admin.site.register(Pump,PumpAdmin)

class PumpOwnershipAdmin(admin.ModelAdmin):
   # prepopulated_fields = {"slug" : ("crop_name",)}
    search_fields = ['size']
    list_display = ('group','name','size','price','date')
admin.site.register(PumpOwnership,PumpOwnershipAdmin)


class SpaireAdmin(admin.ModelAdmin):
   # prepopulated_fields = {"slug" : ("crop_name",)}
    search_fields = ['name']
    list_display = ('name',)
admin.site.register(Spaire,SpaireAdmin)

class SpaireManagementAdmin(admin.ModelAdmin):
   # prepopulated_fields = {"slug" : ("crop_name",)}
    search_fields = ['spaire']
    list_display = ('group','spaire','price','date')
admin.site.register(SpaireManagement,SpaireManagementAdmin)

class ServiceAdmin(admin.ModelAdmin):
   # prepopulated_fields = {"slug" : ("crop_name",)}
    search_fields = ['repaire_type','group']
    list_display = ('date','group','repaire_type','price','total_cost')
admin.site.register(Service,ServiceAdmin)

class FarmCostAdmin(admin.ModelAdmin):
   # prepopulated_fields = {"slug" : ("crop_name",)}
    search_fields = ['farm']
    list_display = ('year','farm','landpreparation','landpulverization','transplanting')
admin.site.register(FarmCost,FarmCostAdmin)

class PlotCropPropertyAdmin(admin.ModelAdmin):
   # prepopulated_fields = {"slug" : ("crop_name",)}
    search_fields = ['name','plotID']
    list_display = ('plotID','name','root_depth','planting_spacing')
admin.site.register(PlotCropProperty,PlotCropPropertyAdmin)

class BedPlotAdmin(admin.ModelAdmin):
   # prepopulated_fields = {"slug" : ("crop_name",)}
    search_fields = ['plotID']
    list_display = ('plotID','length','width','numbers','planting_density')
admin.site.register(BedPlot,BedPlotAdmin)

class HouseAdmin(admin.ModelAdmin):
   # prepopulated_fields = {"slug" : ("crop_name",)}
    search_fields = ['owner']
    list_display = ('latitude','longitude','owner')
admin.site.register(House,HouseAdmin)

class FurrowAdmin(admin.ModelAdmin):
   # prepopulated_fields = {"slug" : ("crop_name",)}
    search_fields = ['plotID']
    list_display = ('plotID','length','width','numbers')
admin.site.register(Furrow,FurrowAdmin)

class TechnologyAdmin(admin.ModelAdmin):
   # prepopulated_fields = {"slug" : ("crop_name",)}
    search_fields = ['name']
    list_display = ('name',)
admin.site.register(Technology,TechnologyAdmin)

class TechnologyManagementAdmin(admin.ModelAdmin):
   # prepopulated_fields = {"slug" : ("crop_name",)}
    search_fields = ['farmer','technology']
    list_display = ('date','technology','farm')
admin.site.register(TechnologyManagement,TechnologyManagementAdmin)

class TechnologyFailureAdmin(admin.ModelAdmin):
   # prepopulated_fields = {"slug" : ("crop_name",)}
    search_fields = ['farmer','technology']
    list_display = ('date','farm','technology','reason')
admin.site.register(TechnologyFailure,TechnologyFailureAdmin)

class TechnologyCalibrationAdmin(admin.ModelAdmin):
   # prepopulated_fields = {"slug" : ("crop_name",)}
    search_fields = ['farm','technology']
    list_display = ('date','farm','technology','repetition','bucketvolume','start_time','end_time','total_time','discharge')
admin.site.register(TechnologyCalibration,TechnologyCalibrationAdmin)

class FertilizerAdmin(admin.ModelAdmin):
   # prepopulated_fields = {"slug" : ("crop_name",)}
    search_fields = ['name']
    list_display = ('name',)
admin.site.register(Fertilizer,FertilizerAdmin)

class FertilizerManagementAdmin(admin.ModelAdmin):
   # prepopulated_fields = {"slug" : ("crop_name",)}
    search_fields = ['fertilizer']
    list_display = ('date','plotID','crop_stage','fertilizer','fertilizer_management','quantity_in_kg','nitrogen','phosphorus','potassium','sulphur','organic_matter','price','price_unit')
admin.site.register(FertilizerManagement,FertilizerManagementAdmin)

class PesticideAdmin(admin.ModelAdmin):
   # prepopulated_fields = {"slug" : ("crop_name",)}
    search_fields = ['name']
    list_display = ('name',)
admin.site.register(Pesticide,PesticideAdmin)

class PesticideManagementAdmin(admin.ModelAdmin):
   # prepopulated_fields = {"slug" : ("crop_name",)}
    search_fields = ['name']
    list_display = ('date','plotID','crop_stage','name','form','quantity_in_litre','quantity_in_kg','price','price_unit')
admin.site.register(PesticideManagement,PesticideManagementAdmin)

class YieldFarmLevelAdmin(admin.ModelAdmin):
   # prepopulated_fields = {"slug" : ("crop_name",)}
    search_fields = ['farm']
    list_display = ('date','farm','area','fresh_dry','marketable_yield','unmarketable_yield','biomas')
admin.site.register(YieldFarmLevel,YieldFarmLevelAdmin)


class CropMonitoringPlantHeightAdmin(admin.ModelAdmin):
   # prepopulated_fields = {"slug" : ("crop_name",)}
    search_fields = ['plotID']
    list_display = ('date','plotID','crop_stage','plant_density_per_bed','plant_density_per_sqm','number_of_good_plants','number_of_bad_plants','plant_number','plant_height','plant_canopy_width','length_of_crop_stage','plant_leave_number','plant_leave_length','plant_leave_width')
admin.site.register(CropMonitoringPlantHeight,CropMonitoringPlantHeightAdmin)


class YieldRowBedLevelAdmin(admin.ModelAdmin):
   # prepopulated_fields = {"slug" : ("crop_name",)}
    search_fields = ['plotID']
    list_display = ('date','plotID','harvesting_method','fresh_dry','area','marketable_produced','ummarketable_produced','marketable_produced_weight','unmarketable_produced_weight')
admin.site.register(YieldRowBedLevel,YieldRowBedLevelAdmin)


class NurseryAdmin(admin.ModelAdmin):
   # prepopulated_fields = {"slug" : ("crop_name",)}
    search_fields = ['farm']
    list_display = ('NurseryID','area','farm','technology','seed','date_bed_preparation','date_trasplanting')
admin.site.register(Nursery,NurseryAdmin)

class SeedAdmin(admin.ModelAdmin):
   # prepopulated_fields = {"slug" : ("crop_name",)}
    search_fields = ['name']
    list_display = ('name',)
admin.site.register(Seed,SeedAdmin)

class SeedManagementAdmin(admin.ModelAdmin):
   # prepopulated_fields = {"slug" : ("crop_name",)}
    search_fields = ['seed']
    list_display = ('date','nursery','seed','quantity','price_per_unit','total_cost')
admin.site.register(SeedManagement,SeedManagementAdmin)


class BedNurseryAdmin(admin.ModelAdmin):
   # prepopulated_fields = {"slug" : ("crop_name",)}
    search_fields = ['nursery']
    list_display = ('length','width','area','nursery','numbers','planting_density_per_bed','seedrate','seedling_yield_per_bed')
admin.site.register(BedNursery,BedNurseryAdmin)

class CropPropertyNurseryAdmin(admin.ModelAdmin):
   # prepopulated_fields = {"slug" : ("crop_name",)}
    search_fields = ['name']
    list_display = ('name','root_depth','planting_spacing','nursery')
admin.site.register(CropPropertyNursery,CropPropertyNurseryAdmin)

class NurseryIrrigationEventAdmin(admin.ModelAdmin):
   # prepopulated_fields = {"slug" : ("crop_name",)}
    search_fields = ['nursery']
    list_display = ('date','nursery','time_started','time_ended','total_time','event','discharge','standard_volume','quantity','climate','total_volume')
admin.site.register(NurseryIrrigationEvent,NurseryIrrigationEventAdmin)

class FuelAdmin(admin.ModelAdmin):
   # prepopulated_fields = {"slug" : ("crop_name",)}
    search_fields = ['name']
    list_display = ('name',)
admin.site.register(Fuel,FuelAdmin)

class FuelManagementAdmin(admin.ModelAdmin):
   # prepopulated_fields = {"slug" : ("crop_name",)}
    search_fields = ['fuel']
    list_display = ('date','fuel','farm','initial_time','final_time','amount_used','refilled_amount')
admin.site.register(FuelManagement,FuelManagementAdmin)

class SoilAdmin(admin.ModelAdmin):
   # prepopulated_fields = {"slug" : ("crop_name",)}
    search_fields = ['name']
    list_display = ('name',)
admin.site.register(Soil,SoilAdmin)


class SoilPropertyAdmin(admin.ModelAdmin):
   # prepopulated_fields = {"slug" : ("crop_name",)}
    search_fields = ['plotID','soilclass']
    list_display = ('date','plotID','soilclass','pH','ec','sand','clay','silt','cec','om','tn','av_p','fe','fc','pwp','k','bulkdensity','zn','se','ca','s','mg','na')
admin.site.register(SoilProperty,SoilPropertyAdmin)


class TDRMeasurementAdmin(admin.ModelAdmin):
   # prepopulated_fields = {"slug" : ("crop_name",)}
    search_fields = ['plotID']
    list_display = ('date','plotID','measurement')
admin.site.register(TDRMeasurement,TDRMeasurementAdmin)

class GravimetricSoilMoistureAdmin(admin.ModelAdmin):
   # prepopulated_fields = {"slug" : ("crop_name",)}
    search_fields = ['plotID']
    list_display = ('date','plotID','time','depth','volume_core_used','weight_core_used','wet_weight','dry_weight','bulk_density','gravimetric_moisture_content','volumetric_moisture_content')
admin.site.register(GravimetricSoilMoisture,GravimetricSoilMoistureAdmin)


class SoilMoistureMeasurementManagementAdmin(admin.ModelAdmin):
   # prepopulated_fields = {"slug" : ("crop_name",)}
    search_fields = ['plotID']
    list_display = ('date','plotID','measurement_option')
admin.site.register(SoilMoistureMeasurementManagement,SoilMoistureMeasurementManagementAdmin)


class TissueNutrientAnalysisAdmin(admin.ModelAdmin):
   # prepopulated_fields = {"slug" : ("crop_name",)}
    search_fields = ['plotID']
    list_display = ('date','plotID','plant_tissue_part','plantnumber','freshweight','dryweight','n','p','k','s','mg','ca','fe','zn')
admin.site.register(TissueNutrientAnalysis,TissueNutrientAnalysisAdmin)


class PlotIrrigationEventAdmin(admin.ModelAdmin):
   # prepopulated_fields = {"slug" : ("crop_name",)}
    search_fields = ['plotID']
    list_display = ('date','plotID','irrigation_event','technology','start_time','end_time','total_time','quantification_method','flume_location','waterlevel1','waterlevel2','furrow_irr_time','nfurrorws_irrigated_once','application_rate','standardvolume','quantity_of_units','yellow_WFD_before_irrigation','red_WFD_before_irrigation','yellow_WFD_time_after_irrigation','red_WFD_time_after_irrigation','climate')
admin.site.register(PlotIrrigationEvent,PlotIrrigationEventAdmin)


class YieldPlantLevelAdmin(admin.ModelAdmin):
   # prepopulated_fields = {"slug" : ("crop_name",)}
    search_fields = ['plotID']
    list_display = ('date','plotID','harvest_method','fresh_dry','plant_number','marketable_produced','unmarketable_produced','marketable_produced_weight','unmarketable_produced_weight','diameter_width_produced','length','residual_biomass')
admin.site.register(YieldPlantLevel,YieldPlantLevelAdmin)


class WeedAdmin(admin.ModelAdmin):
   # prepopulated_fields = {"slug" : ("crop_name",)}
    search_fields = ['plotID']
    list_display = ('date','plotID','weed_activities','time')
admin.site.register(Weed,WeedAdmin)


class HarvestAdmin(admin.ModelAdmin):
   # prepopulated_fields = {"slug" : ("crop_name",)}
    search_fields = ['plotID']
    list_display = ('date','plotID','time','crop','amount','amount_for_home','amount_for_sell')
admin.site.register(Harvest,HarvestAdmin)


class SaleHarvestedCropAdmin(admin.ModelAdmin):
   # prepopulated_fields = {"slug" : ("crop_name",)}
    search_fields = ['farm']
    list_display = ('date','farm','amount','crop','income','expenditure','net_income')
admin.site.register(SaleHarvestedCrop,SaleHarvestedCropAdmin)


class ResidueManagementAdmin(admin.ModelAdmin):
   # prepopulated_fields = {"slug" : ("crop_name",)}
    search_fields = ['farm']
    list_display = ('date','farm','time_taken','burnt','livestock','purpose','crop')
admin.site.register(ResidueManagement,ResidueManagementAdmin)


class ConsumedCropAdmin(admin.ModelAdmin):
   # prepopulated_fields = {"slug" : ("crop_name",)}
    search_fields = ['farm']
    list_display = ('date','amount','farm')
admin.site.register(ConsumedCrop,ConsumedCropAdmin)

class SoilMoistureProfilerAdmin(admin.ModelAdmin):
   # prepopulated_fields = {"slug" : ("crop_name",)}
    search_fields = ['plotID']
    list_display = ('date','plotID','measurement','depth_10','depth_20','depth_30','depth_40','depth_60','depth_100')
admin.site.register(SoilMoistureProfiler,SoilMoistureProfilerAdmin)

class WaterSourcesAdmin(admin.ModelAdmin):
   # prepopulated_fields = {"slug" : ("crop_name",)}
    search_fields = ['name']
    list_display = ('ID','name',)
admin.site.register(WaterSources,WaterSourcesAdmin)

class WaterSourceCategoryAdmin(admin.ModelAdmin):
   # prepopulated_fields = {"slug" : ("crop_name",)}
    search_fields = ['category']
    list_display = ('watersourcetype','category')
admin.site.register(WaterSourceCategory,WaterSourceCategoryAdmin)

class PlantingMethodAdmin(admin.ModelAdmin):
   # prepopulated_fields = {"slug" : ("crop_name",)}
    search_fields = ['plotID']
    list_display = ('plotID','planting_method','planting_date','seeding_date','seeding_rate','seed_spacing_btn_a_row','seed_spacing_within_a_row')
admin.site.register(PlantingMethod,PlantingMethodAdmin)
 
class TransplantingAdmin(admin.ModelAdmin):
   # prepopulated_fields = {"slug" : ("crop_name",)}
    search_fields = ['nurseryID','plotID']
    list_display = ('date','nurseryID','plotID','plantsnumber','plant_spacing_btn_row','plant_spacing_btn_plants_within_rows','plantsnumber_per_row')
admin.site.register(Transplanting,TransplantingAdmin)

class SystemUserAdmin(admin.ModelAdmin):
    #prepopulated_fields = {"slug" : ("crop_name",)}
    search_fields = ['user','firstname','middlename','lastname','role']
    list_display = ('user','firstname','middlename','lastname','role','phone','gender','institution','village','country')
admin.site.register(SystemUser,SystemUserAdmin)
