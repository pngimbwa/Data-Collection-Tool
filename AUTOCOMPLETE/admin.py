from django.contrib import admin
from .models import Country,Person,CompanyStation,Car,PointOfInterest
from .forms import PersonForm

class CountryAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('name',)
admin.site.register(Country,CountryAdmin)

'''
class PersonAdmin(admin.ModelAdmin):
    form = PersonForm
admin.site.register(Person, PersonAdmin)
'''

class PersonAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('name','personID','birth_country')
admin.site.register(Person,PersonAdmin)


class CompanyStationAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('name',)
admin.site.register(CompanyStation,CompanyStationAdmin)

class CarAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('name','photo')
admin.site.register(Car,CarAdmin)

class PointOfInterestAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('name','position')
admin.site.register(PointOfInterest,PointOfInterestAdmin)

