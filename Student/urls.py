from django.urls import path
from . import views



urlpatterns = [

    path('view/students', views.getStudents, name='get_students'),
    path('view/mystudents', views.getMyStudents, name='get_my_students'),
    path('view/placements', views.getPlacements, name='get_placements'),
    path('manage/student', views.manageStudent, name='manage_student'),
    path('request/shift', views.shiftRequest, name='shift_request'),
    path('request/terminate', views.terminateRequest, name='terminate_request'),
]