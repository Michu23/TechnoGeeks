from django.urls import path
from . import views
from .views import MyTokenObtainPairView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)



urlpatterns = [
    path('signup', views.RegisterView.as_view(), name='signup'),
    path('token', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('view/profile', views.getMyProfile, name='get_profile'),
    path('update/profile', views.updateProfile, name='update_profile'),
    path('view/domain', views.getDomain, name='get_domain'),
    path('create/domain', views.createDomain, name='create_domain'),
    path('delete/domain', views.deleteDomain, name='delete_domain'),
    path('update/domain', views.updateDomain, name='update_domain'),
    path('notification', views.notification, name='notification'),
    path('create/notification', views.createNotifications, name='create_notification'),
    path('delete/notification', views.deleteNotifications, name='delete_notification'),
    path('types', views.getTypes, name='types'),
    path('getLocations', views.getLocations, name='getLocations'),
    path('getBranches', views.getBranches, name='getBranches'),
    path('getBatchStudents', views.getBatchStudents, name='getBatchStudents'),
    path('validate/code', views.isCodeValid, name='is_code_valid'),
]