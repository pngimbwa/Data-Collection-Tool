from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import patterns,include, url
from django.contrib import admin
admin.autodiscover()
from . import views

urlpatterns = [

    #****************
    url(r'^car/$','AUTOCOMPLETE.views.car',name='car'),
    
    url(r'^location/$','AUTOCOMPLETE.views.location',name='location'),
    
]# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns +=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)












