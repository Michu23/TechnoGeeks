from django.urls import path
from . import views



urlpatterns = [

    path('pay', views.rentPayments, name='rentPayments'),
    path('upfrontpay', views.upfrontPayments, name='upfrontPayments'),
    path('shiftpay', views.shiftPayments, name='shiftPayments'),
    path('paying', views.paying, name='paying'),
    path('myPayments', views.myPayments, name='myPayments'),

]