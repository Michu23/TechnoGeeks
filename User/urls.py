from django.urls import path
from . import views
from .views import MyTokenObtainPairView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

from django.contrib.auth import views as auth_views



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
    path('view/notifications', views.getNotifications, name='get_notifications'),
    path('create/notification', views.createNotifications, name='create_notification'),
    path('delete/notification', views.deleteNotifications, name='delete_notification'),
    path('update/profilephoto', views.updateProfilephoto, name='update_profilephoto'),
    path('types', views.getTypes, name='types'),
    path('getLocations', views.getLocations, name='getLocations'),
    path('getBranches', views.getBranches, name='getBranches'),
    path('getBatchStudents', views.getBatchStudents, name='getBatchStudents'),
    path('validate/link', views.isLinkValid, name='is_link_valid'),
    path('reset_password/',auth_views.PasswordResetView.as_view(template_name='password_reset.html'),name="reset_password"),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
]