from django.urls import *
from .views import *
urlpatterns = [
    path("", SocietyInfo, name="society-info")
]