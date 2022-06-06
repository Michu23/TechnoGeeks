from django.urls import path
from . import views



urlpatterns = [

    path('pay', views.rentPayment, name='rentPayments'),

]