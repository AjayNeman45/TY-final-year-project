from django.contrib.postgres import fields
from django.db.models.base import Model
from django.forms import ModelForm, models
from .models import Complaint

class ComplaintCreateForm(ModelForm):
    class Meta:
        model = Complaint
        fields = ['member','title','description','created_At']