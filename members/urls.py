from django.conf import  settings
from django.urls import  path
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('profile',views.Profile.as_view(),name='profile'),
    path('edit-profile',views.Edit_Profile.as_view(),name='edit_profile'),
    path('change-password',views.Change_Password.as_view(),name='change_password'),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)