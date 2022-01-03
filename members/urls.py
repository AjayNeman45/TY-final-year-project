from django.conf import  settings
from django.urls import  path
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('profile/<int:id>',views.Profile.as_view(),name='profile'),
    path('edit-profile/<int:id>',views.Edit_Profile.as_view(),name='edit_profile'),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)