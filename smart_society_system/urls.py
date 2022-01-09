from django.contrib import admin
from django.urls import path, include
from .views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path("ajax/expenses/", expenseData , name="expenses" ),
    path("ajax/societyInfo/", societyInfoData, name="societyInfo" ),
    path("ajax/commiteeMembersInfo/", commiteeMembersTabelData, name="commiteeMembers"),
    path("ajax/complaints/", complaintsData, name="complaints" ),


    path("", Home.as_view(), name="home"),
    path("login", MemberLogin.as_view(), name="login"),
    path("logout", MemberLogout.as_view(), name="logout"),
    path("members/", include("members.urls"), name="home"),
    path("book-hall/", include("book_hall.urls")),
    path("society-information/", include("society_information.urls")),
]
