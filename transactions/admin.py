from django.contrib import admin

from .models import *

# Register your models here.

@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    list_display = ('id','member','member_Bank_Name','society_Bank_Name','check_Number','amount','createdAt')


@admin.register(Expense)
class  ExpenseAdmin(admin.ModelAdmin):
    list_display = ('id','title','description','amount','createdAt')

@admin.register(Charges)
class  ChargesAdmin(admin.ModelAdmin):
    list_display = ('id','charges_Type','amount')