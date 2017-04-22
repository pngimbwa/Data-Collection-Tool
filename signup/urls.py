
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import patterns,include, url
from django.contrib import admin
admin.autodiscover()
from . import views

urlpatterns = [
    
    #********LOGIN/LOGOUT/HOME ********
    url(r'^login/$','signup.views.LoginRequest',name='login'),
    url(r'^logout','signup.views.LogoutRequest',name='logout'),
    url(r'^home/$', 'signup.views.home', name='home'),
    url(r'^register/$', 'signup.views.register', name='register'),
    url(r'^registerUser/$', 'signup.views.registeruser', name='registerUser'),
    
    #********PASSWORD RESERT/PASSWORD CHANGE********
    url(r'^passwordchange','django.contrib.auth.views.password_change',name='passwordchange'),
    url(r'^password_change_done','django.contrib.auth.views.password_change_done',name='password_change_done'),
    url(r'^reserpassword/passwordsent','django.contrib.auth.views.password_reset_done',name='password_reset_done'),
    url(r'^resetpassword','django.contrib.auth.views.password_reset',name='reset_password'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z]+)/(?P<token>.+)/$', 'django.contrib.auth.views.password_reset_confirm', name='password_reset_confirm'),
    url(r'^reset/done','django.contrib.auth.views.password_reset_complete',name='password_reset_complete'),
    
    #********HELP********
    url(r'^help/$', 'signup.views.help', name='help'),
    
]# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns +=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)












