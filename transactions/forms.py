from dataclasses import field, fields
from django.forms import ModelForm
from django import forms
from .models import *


class incomeForm(ModelForm):
    charges = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                 choices=Charges.objects.all(), label="charges for")
    class Meta:
        fields = ['charges']