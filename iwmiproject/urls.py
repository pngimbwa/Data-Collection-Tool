
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import patterns,include, url
from django.contrib import admin
admin.autodiscover()
from . import views

urlpatterns = [

    #****************
    url(r'^plant_level_yield/$','iwmiproject.views.plant_level_yield',name='plant_level_yield'),
    url(r'^bed_level_yield/$','iwmiproject.views.bed_level_yield',name='bed_level_yield'),
    url(r'^plantingmethod/$','iwmiproject.views.plantingmethod',name='plantingmethod'),
    url(r'^residue_handling/$','iwmiproject.views.residue_handling',name='residue_handling'),
    url(r'^otherwaterusage/$','iwmiproject.views.otherwaterusage',name='otherwaterusage'),
    url(r'^farmyieldlevel/$','iwmiproject.views.farmyieldlevel',name='farmyieldlevel'),
    url(r'^farmer/$','iwmiproject.views.farmer',name='farmer'),
    url(r'^landpreparation/$','iwmiproject.views.landpreparation',name='landpreparation'),
    url(r'^landclearance/$','iwmiproject.views.landclearance',name='landclearance'),
    #url(r'^transplanting/$','iwmiproject.views.transplanting',name='transplanting'),
    url(r'^nurseryirrigation/$','iwmiproject.views.nurseryirrigation',name='nurseryirrigation'),    
    url(r'^weeding/$','iwmiproject.views.weeding',name='weeding'),
    url(r'^farminfo/$','iwmiproject.views.farminfo',name='farminfo'),
    url(r'^nursery/$','iwmiproject.views.nursery',name='nursery'),
    url(r'^farmer_detail/$','iwmiproject.views.farmer_detail',name='farmer_detail'),
    url(r'^fertilizerapplication/$','iwmiproject.views.fertilizerapplication',name='fertilizerapplication'),
    url(r'^pesticideapplication/$','iwmiproject.views.pesticideapplication',name='pesticideapplication'),
    url(r'^waterliftingcalibration/$','iwmiproject.views.waterliftingcalibration',name='waterliftingcalibration'),
    url(r'^applicationcalibration/$','iwmiproject.views.applicationcalibration',name='applicationcalibration'),
    #url(r'^farm_irrigation/$','iwmi.views.farm_irrigation',name='farm_irrigation'),
    url(r'^farmirrigation/$','iwmiproject.views.farmirrigation',name='farmirrigation'),
    url(r'^tissuenutrientanalysis/$','iwmiproject.views.tissuenutrientanalysis',name='tissuenutrientanalysis'),
    url(r'^technology_failure/$','iwmiproject.views.technology_failure',name='technology_failure'),
    url(r'^cropmonitoring/$','iwmiproject.views.cropmonitoring',name='cropmonitoring'),
    url(r'^weeding/$','iwmiproject.views.weeding',name='weeding'),
    url(r'^service_repaire/$','iwmiproject.views.service_repaire',name='service_repaire'),
    url(r'^soil/$','iwmiproject.views.soil',name='soil'),
    url(r'^soilmoisture/$','iwmiproject.views.soilmoisture',name='soilmoisture'),
    url(r'^sale_harvest_crop/$','iwmiproject.views.sale_harvest_crop',name='sale_harvest_crop'),
    url(r'^consumed_crop_by_household/$','iwmiproject.views.consumed_crop_by_household',name='consumed_crop_by_household'),
    url(r'^remarks/$','iwmiproject.views.remarks',name='remarks'),
    url(r'^fertilizerspecification/$','iwmiproject.views.fertilizerspecification',name='fertilizerspecification'),

    #url(r'^pointofinterest/$','iwmiproject.views.point_of_interest',name='pointofinterest'),
    url(r'^upload_excel/$','iwmiproject.views.upload_excel',name='upload_excel'),
    url(r'^download_excel/$','iwmiproject.views.download_csv',name='download_excel'),
    
    
    #view data ,
    url(r'^edit_farmer_detail/(?P<plotID>[-\w^\s]+)/(?P<personID>[-\w^\s]+)/$','iwmiproject.views_display_edit_delete.edit_farmer_detail',name='edit_farmer_detail'),
    
    url(r'^list_farmers/$','iwmiproject.views_display_edit_delete.list_farmers',name='list_farmers'),
    url(r'^list_crop_production/$','iwmiproject.views_display_edit_delete.list_crop_production',name='list_crop_production'),
    #start_date,end_date
    url(r'^edit_remark_detail/(?P<plotID>[-\w^\s]+)/(?P<personID>[-\w^\s]+)/$','iwmiproject.views_display_edit_delete.edit_remark_detail',name='edit_remark_detail'),
    url(r'^edit_remark_specific_detail/(?P<plotID>[-\w^\s]+)/(?P<personID>[-\w^\s]+)/(?P<start_date>[-\w]+)/(?P<end_date>[-\w]+)/$','iwmiproject.views_display_edit_delete.edit_remark_specific_detail',name='edit_remark_specific_detail'),
    url(r'^delete_remark_specific_detail/(?P<plotID>[-\w^\s]+)/(?P<personID>[-\w^\s]+)/(?P<start_date>[-\w]+)/(?P<end_date>[-\w]+)/$','iwmiproject.views_display_edit_delete.delete_remark_specific_detail',name='delete_remark_specific_detail'),
    url(r'^delete_remark_detail/(?P<plotID>[-\w^\s]+)/(?P<personID>[-\w^\s]+)/$','iwmiproject.views_display_edit_delete.delete_remark_detail',name='delete_remark_detail'),
    
    
    url(r'^edit_detail/(?P<plotID>[-\w^\s]+)/(?P<personID>[-\w^\s]+)/$','iwmiproject.views_display_edit_delete.edit_detail',name='edit_detail'),
    
    url(r'^delete_detail/(?P<plotID>[-\w^\s]+)/(?P<personID>[-\w^\s]+)/$','iwmiproject.views_display_edit_delete.delete_detail',name='delete_detail'),
    
    #edit land clearance
    url(r'^edit_Landclearance_detail/(?P<plotID>[-\w^\s]+)/(?P<personID>[-\w^\s]+)/$','iwmiproject.views_display_edit_delete.land_clearance_detail',name='edit_Landclearance_detail'),
    url(r'^edit_landclearance_detail/(?P<plotID>[-\w^\s]+)/(?P<personID>[-\w^\s]+)/(?P<date>[-\w]+)/$','iwmiproject.views_display_edit_delete.edit_landclearance_detail',name='edit_landclearance_detail'),
    
    #delete land clearance
    url(r'^delete_landclearance_specific_detail/(?P<plotID>[-\w^\s]+)/(?P<personID>[-\w^\s]+)/(?P<date>[-\w]+)/$','iwmiproject.views_delete.delete_landclearance_specific_detail',name='delete_landclearance_specific_detail'),
    url(r'^delete_land_clearance_detail/(?P<plotID>[-\w^\s]+)/(?P<personID>[-\w^\s]+)/$','iwmiproject.views_delete.delete_land_clearance_detail',name='delete_land_clearance_detail'),
  
    #edit land preparation
    url(r'^edit_land_preparation/(?P<plotID>[-\w^\s]+)/(?P<personID>[-\w^\s]+)/$','iwmiproject.views_display_edit_delete.edit_land_preparation',name='edit_land_preparation'),
    url(r'^edit_landpreparation_specific_detail/(?P<plotID>[-\w^\s]+)/(?P<personID>[-\w^\s]+)/(?P<date>[-\w]+)/$','iwmiproject.views_display_edit_delete.edit_landpreparation_specific_detail',name='edit_landpreparation_specific_detail'),
    
    #delete land preparation
    url(r'^delete_landpreparation_specific_detail/(?P<plotID>[-\w^\s]+)/(?P<personID>[-\w^\s]+)/(?P<date>[-\w]+)/$','iwmiproject.views_delete.delete_landpreparation_specific_detail',name='delete_landpreparation_specific_detail'),
    url(r'^delete_landpreparation_detail/(?P<plotID>[-\w^\s]+)/(?P<personID>[-\w^\s]+)/$','iwmiproject.views_delete.delete_landpreparation_detail',name='delete_landpreparation_detail'),
  
    #edit fertilizermanagament
    url(r'^edit_plot_fertilizermanagement/(?P<plotID>[-\w^\s]+)/(?P<personID>[-\w^\s]+)/$','iwmiproject.views_display_edit_delete.edit_plot_fertilizermanagement',name='edit_plot_fertilizermanagement'),
    url(r'^edit_fertilizermanagement_specific_detail/(?P<plotID>[-\w^\s]+)/(?P<personID>[-\w^\s]+)/(?P<date>[-\w]+)/(?P<fertilizer>[-\w^\s]+)/$','iwmiproject.views_display_edit_delete.edit_fertilizermanagement_specific_detail',name='edit_fertilizermanagement_specific_detail'),
    
    #delelte fertilizermanagament
    url(r'^delete_fertilizermanagement_detail/(?P<plotID>[-\w^\s]+)/(?P<personID>[-\w^\s]+)/$','iwmiproject.views_delete.delete_fertilizermanagement_detail',name='delete_fertilizermanagement_detail'),
    url(r'^delete_fertilizermanagement_specific_detail/(?P<plotID>[-\w^\s]+)/(?P<personID>[-\w^\s]+)/(?P<date>[-\w]+)/$','iwmiproject.views_delete.delete_fertilizermanagement_specific_detail',name='delete_fertilizermanagement_specific_detail'),
    
    #edit pesticidemanagement
    url(r'^edit_pesticidemanagement_specific_detail/(?P<plotID>[-\w^\s]+)/(?P<personID>[-\w^\s]+)/(?P<date>[-\w]+)/(?P<pesticide>[-\w^\s]+)/$','iwmiproject.views_display_edit_delete.edit_pesticidemanagement_specific_detail',name='edit_pesticidemanagement_specific_detail'),
    url(r'^edit_plot_pestcidemanagement/(?P<plotID>[-\w^\s]+)/(?P<personID>[-\w^\s]+)/$','iwmiproject.views_display_edit_delete.edit_plot_pestcidemanagement',name='edit_plot_pestcidemanagement'),
    
    #delete pesticidemanagement
    url(r'^delete_pesticidemanagement_detail/(?P<plotID>[-\w^\s]+)/(?P<personID>[-\w^\s]+)/$','iwmiproject.views_delete.delete_pesticidemanagement_detail',name='delete_pesticidemanagement_detail'),
    url(r'^delete_pesticidemanagement_specific_detail/(?P<plotID>[-\w^\s]+)/(?P<personID>[-\w^\s]+)/(?P<date>[-\w]+)/$','iwmiproject.views_delete.delete_pesticidemanagement_specific_detail',name='delete_pesticidemanagement_specific_detail'),
    
    #edit weeding
    url(r'^edit_plot_weeding_specific_detail/(?P<plotID>[-\w^\s]+)/(?P<personID>[-\w^\s]+)/(?P<date>[-\w]+)/$','iwmiproject.views_display_edit_delete.edit_plot_weeding_specific_detail',name='edit_plot_weeding_specific_detail'),
    url(r'^edit_plot_weeding/(?P<plotID>[-\w^\s]+)/(?P<personID>[-\w^\s]+)/$','iwmiproject.views_display_edit_delete.edit_plot_weeding',name='edit_plot_weeding'),
    
    #delete weeding
    url(r'^delete_weeding_detail/(?P<plotID>[-\w^\s]+)/(?P<personID>[-\w^\s]+)/$','iwmiproject.views_delete.delete_weeding_detail',name='delete_weeding_detail'),
    url(r'^delete_weeding_specific_detail/(?P<plotID>[-\w^\s]+)/(?P<personID>[-\w^\s]+)/(?P<date>[-\w]+)/$','iwmiproject.views_delete.delete_weeding_specific_detail',name='delete_weeding_specific_detail'),
    
    #edit yieldfarmlevel
    url(r'^edit_yieldfarmlevel_specific_detail/(?P<plotID>[-\w^\s]+)/(?P<personID>[-\w^\s]+)/(?P<date>[-\w]+)/$','iwmiproject.views_display_edit_delete.edit_yieldfarmlevel_specific_detail',name='edit_yieldfarmlevel_specific_detail'),
    url(r'^edit_yieldfarmlevel/(?P<plotID>[-\w^\s]+)/(?P<personID>[-\w^\s]+)/$','iwmiproject.views_display_edit_delete.edit_yieldfarmlevel',name='edit_yieldfarmlevel'),
    
    #edit residualhandling
    url(r'^edit_plot_residualhandling/(?P<plotID>[-\w^\s]+)/(?P<personID>[-\w^\s]+)/$','iwmiproject.views_display_edit_delete.edit_plot_residualhandling',name='edit_plot_residualhandling'),
    url(r'^edit_plot_residualhandling_specific_detail/(?P<plotID>[-\w^\s]+)/(?P<personID>[-\w^\s]+)/(?P<date>[-\w]+)/$','iwmiproject.views_display_edit_delete.edit_plot_residualhandling_specific_detail',name='edit_plot_residualhandling_specific_detail'),
    
    #edit_plot_yieldrowbedlevel
    url(r'^edit_plot_yieldrowbedlevel/(?P<plotID>[-\w^\s]+)/(?P<personID>[-\w^\s]+)/$','iwmiproject.views_display_edit_delete.edit_plot_yieldrowbedlevel',name='edit_plot_yieldrowbedlevel'),
    url(r'^edit_yieldrowbedlevel_specific_detail/(?P<plotID>[-\w^\s]+)/(?P<personID>[-\w^\s]+)/(?P<date>[-\w]+)/(?P<Crop>[-\w^\s]+)/$','iwmiproject.views_display_edit_delete.edit_yieldrowbedlevel_specific_detail',name='edit_yieldrowbedlevel_specific_detail'),
    
    
    #edit_plot_yieldplantlevel_specific_detail
    url(r'^edit_plot_yieldplantlevel/(?P<plotID>[-\w^\s]+)/(?P<personID>[-\w^\s]+)/$','iwmiproject.views_display_edit_delete.edit_plot_yieldplantlevel',name='edit_plot_yieldplantlevel'),
    url(r'^edit_plot_yieldplantlevel_specific_detail/(?P<plotID>[-\w^\s]+)/(?P<personID>[-\w^\s]+)/(?P<date>[-\w]+)/(?P<Crop>[-\w^\s]+)/$','iwmiproject.views_display_edit_delete.edit_plot_yieldplantlevel_specific_detail',name='edit_plot_yieldplantlevel_specific_detail'),
    
    #edit soil
    url(r'^edit_plot_soilproperty/(?P<plotID>[-\w^\s]+)/(?P<personID>[-\w^\s]+)/$','iwmiproject.views_display_edit_delete.edit_plot_soilproperty',name='edit_plot_soilproperty'),
    url(r'^edit_plot_soilproperty_specific_detail/(?P<plotID>[-\w^\s]+)/(?P<personID>[-\w^\s]+)/(?P<date>[-\w]+)/$','iwmiproject.views_display_edit_delete.edit_plot_soilproperty_specific_detail',name='edit_plot_soilproperty_specific_detail'),
    
    #edit otherwaterusage
    #url(r'^edit_plot_otherwaterusage/(?P<personID>[-\w]+)/$','iwmiproject.views_display_edit_delete.edit_plot_otherwaterusage',name='edit_plot_otherwaterusage'),
    #url(r'^edit_plot_otherwaterusage_specific_detail/(?P<personID>[-\w]+)/(?P<date>[-\w]+)/(?P<start_time>[-\w]+)/$','iwmiproject.views_display_edit_delete.edit_plot_otherwaterusage_specific_detail',name='edit_plot_otherwaterusage_specific_detail'),
    
    #edit tissuenutrientanalyis#
    url(r'^edit_plot_tissuenutrientanalysis/(?P<plotID>[-\w^\s]+)/(?P<personID>[-\w^\s]+)/$','iwmiproject.views_display_edit_delete.edit_plot_tissuenutrientanalysis',name='edit_plot_tissuenutrientanalysis'),
    url(r'^edit_plot_tissuenutrientanalysis_specific_detail/(?P<plotID>[-\w^\s]+)/(?P<personID>[-\w^\s]+)/(?P<date>[-\w]+)/(?P<plantnumber>[-\w]+)/(?P<Crop>[-\w^\s]+)/(?P<bed_number>[-\w]+)/$','iwmiproject.views_display_edit_delete.edit_plot_tissuenutrientanalysis_specific_detail',name='edit_plot_tissuenutrientanalysis_specific_detail'),
    
    
    #edit edit_plot_saleharvestedcrop
    url(r'^edit_plot_saleharvestedcrop/(?P<plotID>[-\w^\s]+)/(?P<personID>[-\w^\s]+)/$','iwmiproject.views_display_edit_delete.edit_plot_saleharvestedcrop',name='edit_plot_saleharvestedcrop'),
    url(r'^edit_plot_saleharvestedcrop_specific_detail/(?P<plotID>[-\w^\s]+)/(?P<personID>[-\w^\s]+)/(?P<date>[-\w]+)/$','iwmiproject.views_display_edit_delete.edit_plot_saleharvestedcrop_specific_detail',name='edit_plot_saleharvestedcrop_specific_detail'),
    
    
    #edit edit_plot_cropmonitoringplantheight
    url(r'^edit_plot_cropmonitoringplantheight/(?P<plotID>[-\w^\s]+)/(?P<personID>[-\w^\s]+)/$','iwmiproject.views_display_edit_delete.edit_plot_cropmonitoringplantheight',name='edit_plot_cropmonitoringplantheight'),
    url(r'^edit_plot_cropmonitoringplantheight_specific_detail/(?P<plotID>[-\w^\s]+)/(?P<personID>[-\w^\s]+)/(?P<date>[-\w]+)/(?P<crop_stage>[-\w]+)/(?P<row_number>[-\w]+)/(?P<Crop>[-\w^\s]+)/$','iwmiproject.views_display_edit_delete.edit_plot_cropmonitoringplantheight_specific_detail',name='edit_plot_cropmonitoringplantheight_specific_detail'),
    
    #edit_cropmonitoringplantheight
    url(r'^edit_cropmonitoringplantheight/(?P<plotID>[-\w^\s]+)/(?P<personID>[-\w^\s]+)/$','iwmiproject.views_display_edit_delete.edit_cropmonitoringplantheight',name='edit_cropmonitoringplantheight'),
    url(r'^edit_consumedcropbyhousehold_specific_detail/(?P<plotID>[-\w^\s]+)/(?P<personID>[-\w^\s]+)/(?P<date>[-\w]+)/$','iwmiproject.views_display_edit_delete.edit_consumedcropbyhousehold_specific_detail',name='edit_consumedcropbyhousehold_specific_detail'),
    
    
    #edit_technologyfailure
    url(r'^edit_technologyfailure/(?P<personID>[-\w^\s]+)/$','iwmiproject.views_display_edit_delete.edit_technologyfailure',name='edit_technologyfailure'),
    url(r'^edit_technologyfailure_specific_detail/(?P<personID>[-\w^\s]+)/(?P<date>[-\w^\s]+)/$','iwmiproject.views_display_edit_delete.edit_technologyfailure_specific_detail',name='edit_technologyfailure_specific_detail'),
    
    
    #edit edit_plot_fertilizer_specification
    url(r'^edit_plot_fertilizer_specification/(?P<personID>[-\w^\s]+)/(?P<plotID>[-\w^\s]+)/$','iwmiproject.views_display_edit_delete.edit_plot_fertilizer_specification',name='edit_plot_fertilizer_specification'),
    url(r'^edit_fertilizer_specification_specific_detail/(?P<personID>[-\w^\s]+)/(?P<plotID>[-\w^\s]+)/(?P<fertilizer>[-\w^\s]+)/$','iwmiproject.views_display_edit_delete.edit_fertilizer_specification_specific_detail',name='edit_fertilizer_specification_specific_detail'),
    
    
    
]# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns +=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)












