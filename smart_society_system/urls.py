from django.contrib import admin
from django.urls import path, include
from .views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path("ajax/expenses/", expenseData , name="expenses" ),
    path("ajax/societyInfo/", societyInfoData, name="societyInfo" ),
    path("ajax/commiteeMembersInfo/", commiteeMembersTabelData, name="commiteeMembers"),
    path("ajax/complaints/", complaintsData, name="complaints" ),

    # path("",include('members.urls'))
]
