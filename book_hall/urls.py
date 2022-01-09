from django.urls import path
from .views import *
urlpatterns = [
    path("", HallApplications.as_view(), name="hall_applications"),
    path("add", RegisterHall.as_view(), name="register_hall"),
    path("<str:filterBy>", FilterHallApplication.as_view(), name="filter_applications")
]