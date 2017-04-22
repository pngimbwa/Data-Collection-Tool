from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
#from iwmi.views import CountryAutocomplete

#from AUTOCOMPLETE.views import CountryAutocomplete

urlpatterns = [
    #url(r'^country-autocomplete/$',CountryAutocomplete.as_view(),name='country-autocomplete',),
    #url(r'^country-autocomplete/$',CountryAutocomplete.as_view(),name='country-autocomplete'),
    #********ADMIN ********
    url(r'^admin/', include(admin.site.urls)),
    
    #********SIGNUP URLS ********
    url(r'^home/$', 'signup.views.home', name='home'),
    url(r'^index/$', 'signup.views.index', name='index'),
    url(r'^$', 'signup.views.index', name='index'),
    url(r'^signup/', include('signup.urls', namespace='signup', app_name='signup')),
    
    #********AUTOCOMPLETE URLS*********
    #url(r'^autocomplete/', include('AUTOCOMPLETE.urls', namespace='autocomplete', app_name='autocomplete')),
    
    #********FARMER URLS ********
    url(r'^iwmiproject/', include('iwmiproject.urls', namespace='iwmiproject', app_name='iwmiproject')),
  
    url(r'^id_region/(?P<country>[-\w^\s]+)/regions/$','iwmiproject.dropdown.region_select',name='region_select'),
    url(r'^id_district/(?P<region>[-\w^\s]+)/districts/$','iwmiproject.dropdown.district_select',name='district_select'),
    url(r'^id_village/(?P<district>[-\w^\s]+)/villages/$','iwmiproject.dropdown.village_select',name='village_select'),
    url(r'^id_crop/(?P<category>[-\w^\s]+)/crops/$','iwmiproject.dropdown.crop_select',name='crop_select'),
    url(r'^id_farmer/(?P<village>[-\w^\s]+)/farmers/$','iwmiproject.dropdown.farmer_select',name='farmer_select'),
    #url(r'^id_plot/(?P<farm>[-\w]+)/plots/$','iwmiproject.dropdown.plot_select',name='plot_select'),
    url(r'^id_pumping_source/(?P<watersource>[-\w^\s]+)/pumping_sources/$','iwmiproject.dropdown.pumping_source_select',name='pumping_source_select'),
    url(r'^id_household_member/(?P<village>[-\w^\s]+)/household_members/$','iwmiproject.dropdown.household_member_select',name='household_member_select'),
    url(r'^farmer/(?P<village>[-\w^\s]+)/farmers/$','iwmiproject.dropdown.farmer_select',name='farmer_select'),
    url(r'^id_nurseryID/(?P<farm>[-\w^\s]+)/nurseryIDs/$','iwmiproject.dropdown.nursery_select',name='nursery_select'),
    url(r'^plot/(?P<farm>[-\w^\s]+)/plots/$','iwmiproject.dropdown.fieldplot_select',name='fieldplot_select'),
    url(r'^technology/(?P<farm>[-\w^\s]+)/technologys/$','iwmiproject.dropdown.technology_select',name='technology_select'),
    url(r'^farm_plot_technology/(?P<farm>[-\w^\s]+)/(?P<plot>[-\w^\s]+)/technologys/$','iwmiproject.dropdown.farm_technology_select',name='farm_technology_select'),
    url(r'^water_application/(?P<plot>[-\w^\s]+)/(?P<farm>[-\w^\s]+)/water_applications/$','iwmiproject.dropdown.water_application_select',name='water_application_select'),
    url(r'^waterapplication/(?P<plot>[-\w^\s]+)/(?P<farm>[-\w^\s]+)/waterapplications/$','iwmiproject.dropdown.waterapplication_select',name='waterapplication_select'),
   # url(r'^nursery/(?P<farm>[-\w]+)/nurseries/$','iwmiproject.dropdown.nurseries_select',name='nurseries_selects'),
    url(r'^nursery_area/(?P<nursery>[-\w^\s]+)/(?P<farm>[-\w]+)/nurseries/$','iwmiproject.dropdown.nurseryarea_select',name='nurseries_selects'),
    
    url(r'^farmergroup/(?P<village>[-\w^\s]+)/farmergroups/$','iwmiproject.dropdown.group_select',name='group_select'),
    url(r'^id_water_application_and_water_management/(?P<plot>[-\w^\s]+)/(?P<farm>[-\w^\s]+)/water_application_and_water_managements/$','iwmiproject.dropdown.water_application_and_water_management_select',name='water_application_and_water_management_select'),
    
    url(r'^pesticide_select/$','iwmiproject.dropdown.pesticide_select',name='pesticide_select'),
    url(r'^fertilizer_select/$','iwmiproject.dropdown.fertilizer_select',name='fertilizer_select'),
    url(r'^crop_select/$','iwmiproject.dropdown.crop_select',name='crop_select'),
    url(r'^crop1_variety/$','iwmiproject.dropdown.crop1_variety',name='crop1_variety'),
    url(r'^crop2_variety/$','iwmiproject.dropdown.crop2_variety',name='crop2_variety'),
    
    url(r'^stress_select/$','iwmiproject.dropdown.stress_select',name='stress_select'),
    
    url(r'^seedtype_select/$','iwmiproject.dropdown.seedtype_select',name='seedtype_select'),

    url(r'^select_all/$','iwmiproject.dropdown.select_all',name='select_all'),
    
    url(r'^plot_croppingsystem/(?P<plot>[-\w]+)/(?P<farm>[-\w]+)/plot_croppingsystem/$','iwmiproject.dropdown.plot_croppingsystem',name='plot_croppingsystem'),
    
    url(r'^get_plot_name/(?P<plot>[-\w]+)/(?P<farm>[-\w]+)/get_plot_name/$','iwmiproject.dropdown.get_plot_name',name='get_plot_name'),
    
    
    url(r'^farm_ownership/(?P<farm>[-\w]+)/farm_ownership/$','iwmiproject.dropdown.farm_ownership',name='farm_ownership'),
    
    url(r'^nursery/(?P<farm>[-\w]+)/nursery/$','iwmiproject.dropdown.farm_nursery',name='nursery'),
    
    url(r'^plotmanagement_info/(?P<farm>[-\w]+)/(?P<plot>[-\w]+)/plotmanagement_info/$','iwmiproject.dropdown.plotmanagement_info',name='plotmanagement_info'),
    
    
    url(r'^get_farmer_name/(?P<farmID>[-\w]+)/get_farmer_name/$','iwmiproject.dropdown.get_farmer_name',name='get_farmer_name'),
    url(r'^get_plot_name/(?P<plotID>[-\w]+)/get_plot_name/$','iwmiproject.dropdown.get_plot_name',name='get_plot_name'),

    url(r'^get_plot_stress/(?P<plotID>[-\w]+)/(?P<farm>[-\w]+)/(?P<start_date>[-\w]+)/(?P<end_date>[-\w]+)/get_plot_stress/$','iwmiproject.dropdown.get_plot_stress',name='get_plot_stress'),
    
    url(r'^get_plot_landpreparationtool/(?P<plotID>[-\w]+)/(?P<farm>[-\w]+)/(?P<date>[-\w]+)/get_plot_landpreparationtool/$','iwmiproject.dropdown.get_plot_landpreparationtool',name='get_plot_landpreparationtool'),
    
    
    url(r'^get_plot_compost_kind/(?P<plotID>[-\w]+)/(?P<farm>[-\w]+)/(?P<date>[-\w]+)/get_plot_compost_kind/$','iwmiproject.dropdown.get_plot_compost_kind',name='get_plot_compost_kind'),
    
    url(r'^get_plot_residual_activities/(?P<plotID>[-\w]+)/(?P<farm>[-\w]+)/(?P<date>[-\w]+)/get_plot_residual_activities/$','iwmiproject.dropdown.get_plot_residual_activities',name='get_plot_residual_activities'),

    url(r'^fertilizerspecification/(?P<farm>[-\w]+)/(?P<plotID>[-\w]+)/fertilizerspecification/$','iwmiproject.dropdown.fertilizerspecification',name='fertilizerspecification'),

    url(r'^edit_fertilizerspecification/(?P<farm>[-\w]+)/(?P<plotID>[-\w]+)/(?P<fertilizer>[-\w^\s]+)/edit_fertilizerspecification/$','iwmiproject.dropdown.edit_fertilizerspecification',name='edit_fertilizerspecification'),

    #url(r'^nursery/(?P<nursery>[-\w]+)/nurseries/$','iwmiproject.dropdown.nursery_info',name='nursery_info'),fertilizer
] #+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns +=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    