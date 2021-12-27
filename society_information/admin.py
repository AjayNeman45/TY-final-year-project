from django.contrib import admin
from .models import SocietyInformation

# Register your models here.
@admin.register(SocietyInformation)
class SocietyInformationAdmin(admin.ModelAdmin):
    list_display = ('id','name','address','number_of_Flats','number_of_Residents','number_of_Tenants','number_of_Wings')

