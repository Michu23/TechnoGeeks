from django.urls import path
from . import views



urlpatterns = [
    path('view/advisors', views.getAdvisors, name='get_advisors'),
]