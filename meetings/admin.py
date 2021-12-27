from django.contrib import admin
from .models import Meeting
# Register your models here.


@admin.register(Meeting)
class MeetingAdmin(admin.ModelAdmin):
    list_display = ("title", "description","date_And_Time","venue")