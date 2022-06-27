from django.urls import path
from . import views



urlpatterns = [

    path('pay', views.rentPayments, name='rentPayments'),
    path('upfrontpay', views.upfrontPayments, name='upfrontPayments'),
    path('shiftpay', views.shiftPayments, name='shiftPayments'),
    path('FinePayments', views.FinePayments, name='FinePayments'),
    path('paying', views.paying, name='paying'),
    path('myPayments', views.myPayments, name='myPayments'),
    path('start_payment', views.start_payment, name='start_payment'),
    path('pending', views.allPendingPayments, name='pending'),
    path('cashpaid', views.cashPaid, name='cashpaid'),
    path('sendform', views.sendForm, name='sendform'),
    path('completed', views.allCompletedPayments, name='completed'),

]