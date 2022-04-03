from django.urls import path
from . import views
urlpatterns = [
    path("/", views.create_payment),
    path("home/", views.HomePageView.as_view(), name="payment-home"),
    path('config/', views.stripe_config),
    path('create-checkout-session/', views.create_checkout_session),
    path('success/', views.SuccessView.as_view()), 
    path('cancelled/', views.CancelledView.as_view()), 
]