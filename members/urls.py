from django.urls import  path
from django.conf import  settings
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('profile',views.Profile.as_view(),name='profile'),
    path('edit-profile',views.Edit_Profile.as_view(),name='edit_profile'),
    path('change-password',views.Change_Password.as_view(),name='change_password'),
    path('society-members',views.Society_Members_Information.as_view(),name='society_members_info'),
    path('commitee-members',views.Commitee_Members_Information.as_view(),name='commitee_members_info'),
    path('society-expenses',views.Society_Expenses.as_view(),name='society_expenses'),
    path('society-charges',views.Society_Charges.as_view(),name='society_charges'),
    path('payment_history',views.Payment_History.as_view(),name='payment_history'),
    path('member-complaint',views.Member_Complaint.as_view(),name='member_complaint'),
    path('add-complaint',views.Add_Complaint.as_view(),name='add_complaint'),
    path('society-meeting',views.Society_Meeting.as_view(),name='society_meeting'),
    path('society-events',views.Society_Events.as_view(),name='society_events'),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)