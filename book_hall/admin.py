from django.contrib import admin
from .models import BookHall
from django.contrib.admin.decorators import display

# Register your models here.
@admin.register(BookHall)
class BookHallAdmin(admin.ModelAdmin):
    list_display = ("get_member_name","event_Name","date","start_Time","end_Time")
    @display(ordering='BookHall__first_name', description="member")
    def get_member_name(self,obj):
        return obj.member.first_name +  " " + obj.member.last_name