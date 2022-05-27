from django.urls import path
from . import views



urlpatterns = [

    path('view/students', views.getStudents, name='get_students'),
    path('view/mystudents', views.getMyStudents, name='get_my_students'),

]