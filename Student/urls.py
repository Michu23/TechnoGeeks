from django.urls import path
from . import views



urlpatterns = [
    path('view/mystudents', views.getMyStudents, name='get_my_students'),
]