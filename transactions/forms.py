from django.forms import ModelForm
from django import forms
from .models import *

months = (
    ("1", "january"),
    ("1", "january"),
    ("1", "january"),
    ("1", "january"),
)
class incomeForm(ModelForm):
    month = forms.ChoiceField(choices=months)
    class Meta:
        model = Income
        fields = '__all__'