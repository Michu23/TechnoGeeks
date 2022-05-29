from django.urls import path
from . import views



urlpatterns = [
    path('view/tasklist', views.getTaskslist, name='get_taskslist'),
    path('view/manifest', views.getManifest, name='get_manifest'),
]