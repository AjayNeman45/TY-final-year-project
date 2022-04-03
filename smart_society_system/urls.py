from django.contrib import admin
from django.urls import path, include, NoReverseMatch
from .views import *
from django.conf.urls.static import static
from django.conf.urls import handler404
from django.conf import  settings


handler404 = 'smart_society_system.views.error_404_view'

urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),
    path("ajax/expenses/", expenseData , name="expenses" ),
    path("ajax/societyInfo/", societyInfoData, name="societyInfo" ),
    path("ajax/commiteeMembersInfo/", commiteeMembersTabelData, name="commiteeMembers"),
    path("ajax/complaints/", complaintsData, name="complaints" ),


    path("", Home.as_view(), name="home"),
    path("saidham-co-op-society/", MainPage.as_view(), name="main-page"),
    path("login/", MemberLogin.as_view(), name="login"),
    path("logout/", MemberLogout.as_view(), name="logout"),
    path("members/", include("members.urls"), name="members"),
    path("book-hall/", include("book_hall.urls")),
    path("society-information/", include("society_information.urls")),
    path("payment/", include("transactions.urls"))
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


handler404 = 'smart_society_system.views.handle_not_found'
