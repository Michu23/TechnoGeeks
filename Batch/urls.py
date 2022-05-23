from django.urls import path
from . import views



urlpatterns = [
    path('view/batch', views.getBatch, name='get_batch'),
    path('create/batch', views.createBatch, name='create_batch'),
    path('delete/batch', views.deleteBatch, name='delete_batch'),
    path('update/batch', views.updateBatch, name='update_batch'),
    path('view/group', views.getGroup, name='get_group'),
    path('create/group', views.createGroup, name='create_group'),
    path('delete/group', views.deleteGroup, name='delete_group'),
    path('update/group', views.updateGroup, name='update_group'),
]