
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import patterns,include, url
from django.contrib import admin
admin.autodiscover()
from . import views

urlpatterns = [

    #****************
    url(r'^plant_level_yield/$','iwmi.views.plant_level_yield',name='plant_level_yield'),
    url(r'^bed_level_yield/$','iwmi.views.bed_level_yield',name='bed_level_yield'),
    url(r'^farmyieldlevel/$','iwmi.views.farmyieldlevel',name='farmyieldlevel'),
    url(r'^farmer/$','iwmi.views.farmer',name='farmer'),
    url(r'^landpreparation/$','iwmi.views.landpreparation',name='landpreparation'),
    url(r'^landclearance/$','iwmi.views.landclearance',name='landclearance'),
    url(r'^transplanting/$','iwmi.views.transplanting',name='transplanting'),
    url(r'^nurseryirrigation/$','iwmi.views.nurseryirrigation',name='nurseryirrigation'),    
    url(r'^weeding/$','iwmi.views.weeding',name='weeding'),
    url(r'^farminfo/$','iwmi.views.farminfo',name='farminfo'),
    url(r'^nursery/$','iwmi.views.nursery',name='nursery'),
    url(r'^farmer_detail/$','iwmi.views.farmer_detail',name='farmer_detail'),
    url(r'^fertilizerapplication/$','iwmi.views.fertilizerapplication',name='fertilizerapplication'),
    url(r'^pesticideapplication/$','iwmi.views.pesticideapplication',name='pesticideapplication'),
    url(r'^waterliftingcalibration/$','iwmi.views.waterliftingcalibration',name='waterliftingcalibration'),
    url(r'^applicationcalibration/$','iwmi.views.applicationcalibration',name='applicationcalibration'),
    #url(r'^farm_irrigation/$','iwmi.views.farm_irrigation',name='farm_irrigation'),
    url(r'^farmirrigation/$','iwmi.views.farmirrigation',name='farmirrigation'),
    url(r'^tissuenutrientanalysis/$','iwmi.views.tissuenutrientanalysis',name='tissuenutrientanalysis'),
    url(r'^technology_failure/$','iwmi.views.technology_failure',name='technology_failure'),
    url(r'^cropmonitoring/$','iwmi.views.cropmonitoring',name='cropmonitoring'),
    url(r'^weeding/$','iwmi.views.weeding',name='weeding'),
    url(r'^service_repaire/$','iwmi.views.service_repaire',name='service_repaire'),
    url(r'^soil/$','iwmi.views.soil',name='soil'),
    url(r'^soilmoisture/$','iwmi.views.soilmoisture',name='soilmoisture'),
    url(r'^sale_harvest_crop/$','iwmi.views.sale_harvest_crop',name='sale_harvest_crop'),
    url(r'^consumed_crop_by_household/$','iwmi.views.consumed_crop_by_household',name='consumed_crop_by_household'),
  
    
]# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns +=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)












