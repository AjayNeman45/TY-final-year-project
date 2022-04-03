from django import forms
from django.contrib import admin

from .forms import incomeForm

from .models import *

# Register your models here.

class IncomeAdmin(admin.ModelAdmin):
    readonly_fields = ('totalCharges', )
    list_display = ('id','member','member_Bank_Name','society_Bank_Name','check_Number', 'createdAt', 'totalCharges')
  

admin.site.register(Income,IncomeAdmin)
@admin.register(Expense)
class  ExpenseAdmin(admin.ModelAdmin):
    list_display = ('id','title','description','amount','createdAt')

@admin.register(Charges)
class  ChargesAdmin(admin.ModelAdmin):
    list_display = ('id','charges_Type','amount')