from django.contrib import admin

from .models import  MyTestModel,FertilizerSpecification,Remark,ResidualHandling,OtherWaterUsage,SystemUser,CropVarieties,ApplicationCalibration,WaterSources,WaterliftingCalibrations,LandClearance,LandPreparation,WaterManagement,WaterSourceCategory,PlantingMethod,Plot,PumpingSource,RelationManager,PlotCrop,PlotManagement,Country,Region, District, Village, FarmGroup, LabourManagament, Crop, People, Farm, SoilMoistureMeasurementManagement,PlotOperation, PlotCultivation, Pump, PumpOwnership,Spaire,SpaireManagement,Service,FarmCost,PlotCropProperty,BedPlot,House,Furrow,Technology,TechnologyFailure,TechnologyManagement,TechnologyCalibration,Fertilizer,FertilizerManagement,Pesticide,PesticideManagement,YieldFarmLevel,CropMonitoringPlantHeight,YieldRowBedLevel,Nursery,Seed,SeedManagement,BedNursery,CropPropertyNursery,NurseryIrrigationEvent,Fuel,FuelManagement,Soil,SoilProperty,TDRMeasurement,GravimetricSoilMoisture,TissueNutrientAnalysis,PlotIrrigationEvent,YieldPlantLevel,Weed,Harvest,SaleHarvestedCrop,ResidueManagement,ConsumedCrops,SoilMoistureProfiler

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

class FarmGroupAdmin(admin.ModelAdmin):
   # prepopulated_fields = {"slug" : ("crop_name",)}
    search_fields = ['name']
    list_display = ('name','village')
admin.site.register(FarmGroup,FarmGroupAdmin)

class CropAdmin(admin.ModelAdmin):
   # prepopulated_fields = {"slug" : ("crop_name",)}
    search_fields = ['name']
    list_display = ('name',)
admin.site.register(Crop,CropAdmin)

class RelationManagerAdmin(admin.ModelAdmin):
   # prepopulated_fields = {"slug" : ("crop_name",)}
    search_fields = ['farmer','relation']
    list_display = ('farmer','relation','display_family_member')
admin.site.register(RelationManager,RelationManagerAdmin)


class PeopleAdmin(admin.ModelAdmin):
   # prepopulated_fields = {"slug" : ("crop_name",)}
    search_fields = ['personID','firstname','middlename','lastname']
    list_display = ('personID','firstname','middlename','lastname','gender','group','age_group','role','village')
admin.site.register(People,PeopleAdmin)

class LabourManagamentAdmin(admin.ModelAdmin):
   # prepopulated_fields = {"slug" : ("crop_name",)}
    search_fields = ['farm__farmID__personID','enteredpersonel__user__username','labour','areaID']
    list_display = ('date','farm','areaID','areadescription','labour','hired_female_number','hired_male_number','family_female_number','family_male_number','activity','wage','price_unit','family_female_time','family_male_time','hired_female_time','hired_male_time','enteredpersonel')
admin.site.register(LabourManagament,LabourManagamentAdmin)


class FarmAdmin(admin.ModelAdmin):
   # prepopulated_fields = {"slug" : ("crop_name",)}
    search_fields = ['farmID']
    list_display = ('farmID','landownership','fieldsize','number','rented_land','owned_land','total_irrigated_owned_land','total_irrigated_rented_land','irrigated_plots','enteredpersonel')
admin.site.register(Farm,FarmAdmin)

class PlotAdmin(admin.ModelAdmin):
   # prepopulated_fields = {"slug" : ("crop_name",)}
    search_fields = ['plotID','farm']
    list_display = ('farm','plotID','fieldtype','latitude','longitude','landownership','lease_duration','payment_option','payment_monetary','currency','payement_other','enteredpersonel')
admin.site.register(Plot,PlotAdmin)

class PlotCropAdmin(admin.ModelAdmin):
   # prepopulated_fields = {"slug" : ("crop_name",)}
    search_fields = ['farm','plotID']
    list_display = ('farm','plotID','cropping_system','crop1','crop1_variety','crop1_varietytype','crop1_planting_method','crop1_rootdepth','crop1_management_practice','crop1_mulching_type','crop1_mulching_quantity','crop2','crop2_variety','crop2_varietytype','crop2_planting_method','crop2_rootdepth','crop2_management_practice','crop2_mulching_type','crop2_mulching_quantity','enteredpersonel')
admin.site.register(PlotCrop,PlotCropAdmin)


class PlotManagementAdmin(admin.ModelAdmin):
   # prepopulated_fields = {"slug" : ("crop_name",)}
    search_fields = ['plotID','farm']
    list_display = ('date','farm','plotID','display_crop','elevation','plot_size','cropping_system','rootdepth','seasonstart','water_application','enteredpersonel')
admin.site.register(PlotManagement,PlotManagementAdmin)
#croppingpractice

class WaterManagementAdmin(admin.ModelAdmin):
   # prepopulated_fields = {"slug" : ("crop_name",)}
    search_fields = ['plotID','water_management_method']
    list_display = ('farm','plotID','water_management_method','yellow_depth_detector','red_depth_detector','rods_length')
admin.site.register(WaterManagement,WaterManagementAdmin)

class PumpingSourceAdmin(admin.ModelAdmin):
   # prepopulated_fields = {"slug" : ("crop_name",)}
    search_fields = ['farm__farmID__personID','source',]
    list_display = ('date','farm','source','latitude','longitude','elevation','depth','diameter','enteredpersonel')
admin.site.register(PumpingSource,PumpingSourceAdmin)

class PlotOperationAdmin(admin.ModelAdmin):
   # prepopulated_fields = {"slug" : ("crop_name",)}
    search_fields = ['plotID']
    list_display = ('date','farm','plotID','activity','number')
admin.site.register(PlotOperation,PlotOperationAdmin)

class PlotCultivationAdmin(admin.ModelAdmin):
   # prepopulated_fields = {"slug" : ("crop_name",)}
    search_fields = ['farm']
    list_display = ('date','farm','plotID','cultivation_method','enteredpersonel')
admin.site.register(PlotCultivation,PlotCultivationAdmin)

class PumpAdmin(admin.ModelAdmin):
   # prepopulated_fields = {"slug" : ("crop_name",)}
    search_fields = ['name']
    list_display = ('name',)
admin.site.register(Pump,PumpAdmin)

class PumpOwnershipAdmin(admin.ModelAdmin):
   # prepopulated_fields = {"slug" : ("crop_name",)}
    search_fields = ['size']
    list_display = ('group','name','size','price','date','enteredpersonel')
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
    search_fields = ['repaire_type']
    list_display = ('date','farm','repaire_type','total_cost','currency','maintenance_place','technology_broken','distance_to_shop','travel_cost','time_taken','enteredpersonel')
admin.site.register(Service,ServiceAdmin)

class FarmCostAdmin(admin.ModelAdmin):
   # prepopulated_fields = {"slug" : ("crop_name",)}
    search_fields = ['farm']
    list_display = ('year','farm','landpreparation','landpulverization','transplanting')
admin.site.register(FarmCost,FarmCostAdmin)

class PlotCropPropertyAdmin(admin.ModelAdmin):
   # prepopulated_fields = {"slug" : ("crop_name",)}
    search_fields = ['name','plotID']
    list_display = ('farm','plotID','name','root_depth','planting_spacing')
admin.site.register(PlotCropProperty,PlotCropPropertyAdmin)

class BedPlotAdmin(admin.ModelAdmin):
   # prepopulated_fields = {"slug" : ("crop_name",)}
    search_fields = ['plotID__plotID']
    list_display = ('farm','plotID','length','width','numbers')
admin.site.register(BedPlot,BedPlotAdmin)

class HouseAdmin(admin.ModelAdmin):
   # prepopulated_fields = {"slug" : ("crop_name",)}
    search_fields = ['owner']
    list_display = ('latitude','longitude','elevation','owner')
admin.site.register(House,HouseAdmin)

class FurrowAdmin(admin.ModelAdmin):
   # prepopulated_fields = {"slug" : ("crop_name",)}
    search_fields = ['plotID']
    list_display = ('farm','plotID','length','width','numbers')
admin.site.register(Furrow,FurrowAdmin)

class TechnologyAdmin(admin.ModelAdmin):
   # prepopulated_fields = {"slug" : ("crop_name",)}
    search_fields = ['name']
    list_display = ('name',)
admin.site.register(Technology,TechnologyAdmin)

class TechnologyManagementAdmin(admin.ModelAdmin):
   # prepopulated_fields = {"slug" : ("crop_name",)}
    search_fields = ['farmer','technology']
    list_display = ('date','technology','farm','enteredpersonel')
admin.site.register(TechnologyManagement,TechnologyManagementAdmin)

class TechnologyFailureAdmin(admin.ModelAdmin):
   # prepopulated_fields = {"slug" : ("crop_name",)}
    search_fields = ['farmer','technology']
    list_display = ('date','farm','technology','reason','enteredpersonel')
admin.site.register(TechnologyFailure,TechnologyFailureAdmin)

class TechnologyCalibrationAdmin(admin.ModelAdmin):
   # prepopulated_fields = {"slug" : ("crop_name",)}
    search_fields = ['farm','technology']
    list_display = ('date','farm','technology','repetition','bucketvolume','start_time','end_time','total_time','discharge','enteredpersonel')
admin.site.register(TechnologyCalibration,TechnologyCalibrationAdmin)

class FertilizerAdmin(admin.ModelAdmin):
   # prepopulated_fields = {"slug" : ("crop_name",)}
    search_fields = ['name']
    list_display = ('name',)
admin.site.register(Fertilizer,FertilizerAdmin)

class FertilizerManagementAdmin(admin.ModelAdmin):
   # prepopulated_fields = {"slug" : ("crop_name",)}
    search_fields = ['plotID__plotID','fertilizer__name']
    list_display = ('date','farm','plotID','nurseryID','crop_stage','fertilizer','compost_kind','fertilizer_management','quantity_in_kg','price','price_unit','enteredpersonel')
admin.site.register(FertilizerManagement,FertilizerManagementAdmin)

class FertilizerSpecificationAdmin(admin.ModelAdmin):
   # prepopulated_fields = {"slug" : ("crop_name",)}
    search_fields = ['plotID__plotID','fertilizer__name']
    list_display = ('farm','plotID','fertilizer','nitrogen','phosphorus','potassium','sulphur','organic_matter','enteredpersonel')
admin.site.register(FertilizerSpecification,FertilizerSpecificationAdmin)


class PesticideAdmin(admin.ModelAdmin):
   # prepopulated_fields = {"slug" : ("crop_name",)}
    search_fields = ['name']
    list_display = ('name',)
admin.site.register(Pesticide,PesticideAdmin)

class PesticideManagementAdmin(admin.ModelAdmin):
   # prepopulated_fields = {"slug" : ("crop_name",)}
    search_fields = ['name']
    list_display = ('date','farm','plotID','crop_stage','name','form','water_volume','quantity_in_litre','quantity_in_kg','price','price_unit','enteredpersonel')
admin.site.register(PesticideManagement,PesticideManagementAdmin)

class YieldFarmLevelAdmin(admin.ModelAdmin):
   # prepopulated_fields = {"slug" : ("crop_name",)}
    search_fields = ['plotID']
    list_display = ('date','farm','plotID','Crop','fresh_dry','quantity_harvested','marketable_yield','unmarketable_yield','biomas','enteredpersonel')
admin.site.register(YieldFarmLevel,YieldFarmLevelAdmin)

class CropMonitoringPlantHeightAdmin(admin.ModelAdmin):
   # prepopulated_fields = {"slug" : ("crop_name",)}
    search_fields = ['plotID__plotID']#
    list_display = ('date','farm','plotID','Crop','crop_stage','row_number','number_of_good_plants','number_of_bad_plants','plant_number','LAI','plant_height','plant_canopy_width','length_of_crop_stage','plant_leave_number','plant_leave_length','plant_leave_width','plant_number_two','LAI_two','plant_height_two','plant_canopy_width_two','length_of_crop_stage_two','plant_leave_number_two','plant_leave_length_two','plant_leave_width_two','plant_number_three','LAI_three','plant_height_three','plant_canopy_width_three','length_of_crop_stage_three','plant_leave_number_three','plant_leave_length_three','plant_leave_width_three','plant_density_per_sqm','plant_density_per_bed','sub_plot_size','sub_plot_plant_number','total_plant_number','enteredpersonel')
admin.site.register(CropMonitoringPlantHeight,CropMonitoringPlantHeightAdmin)

class YieldRowBedLevelAdmin(admin.ModelAdmin):
   # prepopulated_fields = {"slug" : ("crop_name",)}
    search_fields = ['plotID']
    list_display = ('date','farm','plotID','Crop','row_number','harvesting_method','fresh_dry','marketable_produced','ummarketable_produced','marketable_produced_weight','unmarketable_produced_weight','enteredpersonel')
admin.site.register(YieldRowBedLevel,YieldRowBedLevelAdmin)

class NurseryAdmin(admin.ModelAdmin):
   # prepopulated_fields = {"slug" : ("crop_name",)}
    search_fields = ['farm']
    list_display = ('NurseryID','area','farm','seed','date_bed_preparation','enteredpersonel')
admin.site.register(Nursery,NurseryAdmin)

class SeedAdmin(admin.ModelAdmin):
   # prepopulated_fields = {"slug" : ("crop_name",)}
    search_fields = ['name']
    list_display = ('name',)
admin.site.register(Seed,SeedAdmin)

class SeedManagementAdmin(admin.ModelAdmin):
   # prepopulated_fields = {"slug" : ("crop_name",)}
    search_fields = ['seed']
    list_display = ('date','nursery','seed','quantity','price_per_unit','total_cost','enteredpersonel')
admin.site.register(SeedManagement,SeedManagementAdmin)


class BedNurseryAdmin(admin.ModelAdmin):
   # prepopulated_fields = {"slug" : ("crop_name",)}
    search_fields = ['nursery']
    list_display = ('length','width','area','nursery','numbers','planting_density_per_bed','seed_spacing_within_a_bed','seed_spacing_btn_bed','seedrate','enteredpersonel')
admin.site.register(BedNursery,BedNurseryAdmin)

class CropPropertyNurseryAdmin(admin.ModelAdmin):
   # prepopulated_fields = {"slug" : ("crop_name",)}
    search_fields = ['name']
    list_display = ('name','root_depth','planting_spacing','nursery')
admin.site.register(CropPropertyNursery,CropPropertyNurseryAdmin)

class NurseryIrrigationEventAdmin(admin.ModelAdmin):
   # prepopulated_fields = {"slug" : ("crop_name",)}
    search_fields = ['nursery']
    list_display = ('date','nursery','time_started','time_ended','total_time','event','quantity','climate','total_volume','irrigation_depth','enteredpersonel')
admin.site.register(NurseryIrrigationEvent,NurseryIrrigationEventAdmin)

class FuelAdmin(admin.ModelAdmin):
   # prepopulated_fields = {"slug" : ("crop_name",)}
    search_fields = ['name']
    list_display = ('name',)
admin.site.register(Fuel,FuelAdmin)

class FuelManagementAdmin(admin.ModelAdmin):
   # prepopulated_fields = {"slug" : ("crop_name",)}
    search_fields = ['fuel']
    list_display = ('date','fuel','farm','initial_time','final_time','amount_used','refilled_amount','enteredpersonel')
admin.site.register(FuelManagement,FuelManagementAdmin)

class SoilAdmin(admin.ModelAdmin):
   # prepopulated_fields = {"slug" : ("crop_name",)}
    search_fields = ['name']
    list_display = ('name',)
admin.site.register(Soil,SoilAdmin)


class SoilPropertyAdmin(admin.ModelAdmin):
   # prepopulated_fields = {"slug" : ("crop_name",)}
    search_fields = ['plotID','soilclass']
    list_display = ('date','farm','plotID','soilclass','pH','soil_depth','ec','sand','clay','silt','cec','om','tn','av_p','fe','fc','pwp','k','bulkdensity','zn','se','ca','s','mg','na','enteredpersonel')
admin.site.register(SoilProperty,SoilPropertyAdmin)


class TDRMeasurementAdmin(admin.ModelAdmin):
   # prepopulated_fields = {"slug" : ("crop_name",)}
    search_fields = ['plotID']
    list_display = ('date','farm','plotID','event','measurement_one','measurement_two','measurement_three','measurement_four','measurement_five','measurement_six','measurement_seven','measurement_eigth','measurement_nine','measurement_ten','measurement_depth','enteredpersonel')
admin.site.register(TDRMeasurement,TDRMeasurementAdmin)

class GravimetricSoilMoistureAdmin(admin.ModelAdmin):
   # prepopulated_fields = {"slug" : ("crop_name",)}
    search_fields = ['plotID']
    list_display = ('date','farm','plotID','event','time_taken','depth','volume_core_used','weight_core_used','wet_weight','dry_weight','bulk_density','gravimetric_moisture_content','volumetric_moisture_content','enteredpersonel')
admin.site.register(GravimetricSoilMoisture,GravimetricSoilMoistureAdmin)

class SoilMoistureProfilerAdmin(admin.ModelAdmin):
   # prepopulated_fields = {"slug" : ("crop_name",)}
    search_fields = ['plotID']
    list_display = ('date','farm','plotID','event','depth_10','depth_20','depth_30','depth_40','depth_60','depth_100','enteredpersonel')
admin.site.register(SoilMoistureProfiler,SoilMoistureProfilerAdmin)


class SoilMoistureMeasurementManagementAdmin(admin.ModelAdmin):
   # prepopulated_fields = {"slug" : ("crop_name",)}
    search_fields = ['plotID']
    list_display = ('date','farm','plotID','measurement_option','enteredpersonel')
admin.site.register(SoilMoistureMeasurementManagement,SoilMoistureMeasurementManagementAdmin)


class TissueNutrientAnalysisAdmin(admin.ModelAdmin):
   # prepopulated_fields = {"slug" : ("crop_name",)}
    search_fields = ['plotID']
    list_display = ('date','farm','plotID','Crop','plant_tissue_part','plantnumber','bed_number','freshweight','dryweight','n','p','k','s','mg','ca','fe','zn','enteredpersonel')
admin.site.register(TissueNutrientAnalysis,TissueNutrientAnalysisAdmin)


class PlotIrrigationEventAdmin(admin.ModelAdmin):
   # prepopulated_fields = {"slug" : ("crop_name",)}
    search_fields = ['plotID']
    list_display = ('date','farm','plotID','service_provider','climate','irrigation_event','start_time','end_time','total_time','application_rate','quantity_of_units','water_application','wetteddiameteraroundplant','irrigate_whole_or_per_plant','irrigated_depth','quantification_method','flume_location','waterlevel1','waterlevel2','furrow_irr_time','nfurrorws_irrigated_once','waterheight','topfurrowwidth','buttonfurrowwidth','field_efficiency','conveyance_efficiency','driptank_volume','bucketvolume','bucketnumbers','yellow_WFD_before_irrigation','red_WFD_before_irrigation','yellow_WFD_time_after_irrigation','red_WFD_time_after_irrigation','tanknumber','technology','gender','distance_from_water_source','time_to_fetch_water','water_level_bf_filling','water_level_aftr_filling','time_to_fill_water_tank','fuel','fuelcost','currency','amount_used','refilled_amount','enteredpersonel')
admin.site.register(PlotIrrigationEvent,PlotIrrigationEventAdmin)


class YieldPlantLevelAdmin(admin.ModelAdmin):
   # prepopulated_fields = {"slug" : ("crop_name",)}
    search_fields = ['plotID']
    list_display = ('date','farm','plotID','Crop','harvest_method','fresh_dry','row_number','plant_number','marketable_produced','unmarketable_produced','marketable_produced_weight','unmarketable_produced_weight','diameter_width_produced','length','residual_biomass','enteredpersonel')
admin.site.register(YieldPlantLevel,YieldPlantLevelAdmin)


class WeedAdmin(admin.ModelAdmin):
   # prepopulated_fields = {"slug" : ("crop_name",)}
    search_fields = ['plotID']
    list_display = ('date','farm','plotID','weed_activities','enteredpersonel')
admin.site.register(Weed,WeedAdmin)

class ResidualHandlingAdmin(admin.ModelAdmin):
   # prepopulated_fields = {"slug" : ("crop_name",)}
    search_fields = ['plotID__plotID']
    list_display = ('date','farm','plotID','residual_activities','time','enteredpersonel')
admin.site.register(ResidualHandling,ResidualHandlingAdmin)

class HarvestAdmin(admin.ModelAdmin):
   # prepopulated_fields = {"slug" : ("crop_name",)}
    search_fields = ['plotID']
    list_display = ('date','plotID','time','crop','amount','amount_for_home','amount_for_sell','enteredpersonel')
admin.site.register(Harvest,HarvestAdmin)

class SaleHarvestedCropAdmin(admin.ModelAdmin):
   # prepopulated_fields = {"slug" : ("crop_name",)}
    search_fields = ['plotID__plotID']
    list_display = ('date','plotID','marketprice','amount','income','mode_of_transport','fare','fuel_type','fuel_cost','currency','distance_to_the_market','enteredpersonel')
admin.site.register(SaleHarvestedCrop,SaleHarvestedCropAdmin)

class ResidueManagementAdmin(admin.ModelAdmin):
   # prepopulated_fields = {"slug" : ("crop_name",)}
    search_fields = ['farm']
    list_display = ('date','farm','time_taken','burnt','livestock','purpose','crop','enteredpersonel')
admin.site.register(ResidueManagement,ResidueManagementAdmin)

class ConsumedCropsAdmin(admin.ModelAdmin):
   # prepopulated_fields = {"slug" : ("crop_name",)}
    search_fields = ['plotID']
    list_display = ('date','farm','plotID','where_consumed','how_consumed','quantity','marketprice','totalvalue','currency','enteredpersonel')
admin.site.register(ConsumedCrops,ConsumedCropsAdmin)

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
    search_fields = ['plotID,farm']
    list_display = ('farm','plotID','CroppingSystem','planting_method','date_one','spacing_within_a_row','nurseryID_one','spacing_btn_a_row','seed_quantity','seed_quantity','plantsnumber_per_row_one','date_two','spacing_within_a_row_two','nurseryID_two','plantsnumber_per_row_two','total_plants','total_seed_quantity','seed_quantity2','enteredpersonel')
admin.site.register(PlantingMethod,PlantingMethodAdmin)

'''
class TransplantingAdmin(admin.ModelAdmin):
   # prepopulated_fields = {"slug" : ("crop_name",)}
    search_fields = ['nurseryID','plotID']
    list_display = ('date','nurseryID','plotID','plantsnumber','plant_spacing_btn_row','plant_spacing_btn_plants_within_rows','plantsnumber_per_row','enteredpersonel')
admin.site.register(Transplanting,TransplantingAdmin)
'''
class SystemUserAdmin(admin.ModelAdmin):
    #prepopulated_fields = {"slug" : ("crop_name",)}
    search_fields = ['user','firstname','middlename','lastname','role']
    list_display = ('user','firstname','middlename','lastname','role','phone','gender','institution','village','country')
admin.site.register(SystemUser,SystemUserAdmin)

class LandClearanceAdmin(admin.ModelAdmin):
   # prepopulated_fields = {"slug" : ("crop_name",)}
    search_fields = ['plotID__plotID']
    list_display = ('date','farm','plotID','landclearanceoption','enteredpersonel')
admin.site.register(LandClearance,LandClearanceAdmin)

class LandPreparationAdmin(admin.ModelAdmin):
   # prepopulated_fields = {"slug" : ("crop_name",)}
    search_fields = ['plotID__plotID']
    list_display = ('date','farm','plotID','landpreparationtool','enteredpersonel')
admin.site.register(LandPreparation,LandPreparationAdmin)


class WaterliftingCalibrationsAdmin(admin.ModelAdmin):
   # prepopulated_fields = {"slug" : ("crop_name",)}
    search_fields = ['farm']
    list_display = ('date','farm','technology','event','gender','age_group','waterlevel','start_time','end_time','total_time','bucket_volume','discharge','enteredpersonel')
admin.site.register(WaterliftingCalibrations,WaterliftingCalibrationsAdmin)

class ApplicationCalibrationAdmin(admin.ModelAdmin):
   # prepopulated_fields = {"slug" : ("crop_name",)}
    search_fields = ['plot','water_application']
    list_display = ('date','farm','plot','water_application','bucketdiameter','bucketvolume','calibration_method','dripline_numbers','start_time','end_time','total_time','application_rate','bucketnumbers','waterheight','topfurrowwidth','irrigated_depth','buttonfurrowwidth','buttonfurrowwidth','wetteddiameteraroundplant','irrigate_whole_or_per_plant','field_efficiency','conveyance_efficiency','dripline_length','dripline_spacing','emitter_spacing','driptank_volume','calibrationcup_volume','calibration_cup_time','emitter_wetted_diameter','enteredpersonel')
admin.site.register(ApplicationCalibration,ApplicationCalibrationAdmin)

class CropVarietiesAdmin(admin.ModelAdmin):
    search_fields = ['plotID']
    list_display = ('farm','plotID','cropname','variety','varietytype')
admin.site.register(CropVarieties,CropVarietiesAdmin)

class OtherWaterUsageAdmin(admin.ModelAdmin):
    search_fields = ['plot','farm']
    list_display = ('date','farm','bucketnumber','bucketvolume','technology','usagepurpose','start_time','end_time','total_time','totalvolume','lifting_technology_yes_no')
admin.site.register(OtherWaterUsage,OtherWaterUsageAdmin)

class RemarkAdmin(admin.ModelAdmin):
    search_fields = ['plot']
    list_display = ('start_date','end_date','farm','plot','stress','severness','enteredpersonel')
admin.site.register(Remark,RemarkAdmin)


class MyTestModelAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('name','age','length')
admin.site.register(MyTestModel,MyTestModelAdmin)


'''
 class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('name',)
admin.site.register(Category,CategoryAdmin)

class AuthorAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('name',)
admin.site.register(Author,AuthorAdmin)


class BookAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('name','author','author_email','imported','published','price')
admin.site.register(Book,BookAdmin)

from import_export import resources

class BookResources(resources.ModelResource):
    class Meta:
        model = Book


from import_export.admin import ImportExportModelAdmin

class BookAdmin(ImportExportModelAdmin):
    resource_class = BookResources
   
class PointOfInterestAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('name','position')
admin.site.register(PointOfInterest,PointOfInterestAdmin)

'''



