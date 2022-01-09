from django.shortcuts import render
from django.views import View

from .models import SocietyInformation
# Create your views here.
def SocietyInfo(request):
    societyInfo = SocietyInformation.objects.get(id=1)
    context = {"societyInfo": societyInfo}
    return render(request, "societyInfo.html", context)
    
