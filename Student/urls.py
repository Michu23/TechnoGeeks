from django.urls import path
from . import views



urlpatterns = [

    path('view/students', views.getStudents, name='get_students'),
    path('view/mystudents', views.getMyStudents, name='get_my_students'),
    path('view/placements', views.getPlacements, name='get_placements'),
    path('view/requests', views.getRequests, name='get_requests'),
    path('manage/student', views.manageStudent, name='manage_student'),
    path('request/shift', views.shiftRequest, name='shift_request'),
    path('request/terminate', views.terminateRequest, name='terminate_request'),
    path('shift/accept', views.shiftAccept, name='shift_accept'),
    path('shift/reject', views.shiftReject, name='shift_reject'),
    path('terminate/accept', views.terminateAccept, name='terminate_accept'),
    path('terminate/reject', views.terminateReject, name='terminate_reject'),
    path('create/placement', views.createPlacement, name='create_placement'),
    path('update/placement', views.updatePlacementProfile, name='update_placement'),
    path('view/placement', views.getPlacement, name='get_placement'),
]