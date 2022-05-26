from django.urls import path
from . import views



urlpatterns = [
    path('view/advisors', views.getAdvisors, name='get_advisors'),
    path('view/advisors/names', views.getAdvisorsNames, name='get_advisors_names'),
]