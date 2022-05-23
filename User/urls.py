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
    path('view/profile', views.getProfile, name='get_profile'),
    path('update/profile', views.updateProfile, name='update_profile'),
    path('view/domain', views.getDomain, name='get_domain'),
    path('create/domain', views.createDomain, name='create_domain'),
    path('delete/domain', views.deleteDomain, name='delete_domain'),
    path('update/domain', views.updateDomain, name='update_domain'),
    path('notification', views.notification, name='notification'),
]