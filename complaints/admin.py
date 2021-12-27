from django.contrib import admin
from django.contrib.admin.decorators import display
from .models import *
# Register your models here.
@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    list_display = ('get_member_name','title','description','status','created_At',)

    @display(ordering='Complaint__first_name', description="member")
    def get_member_name(self,obj):
        return obj.member.first_name + " " + obj.member.last_name