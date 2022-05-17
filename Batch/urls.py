from django.urls import path
from . import views



urlpatterns = [
    path('create/batch', views.createBatch, name='create_batch'),
    path('delete/batch', views.deleteBatch, name='delete_batch'),
    path('update/batch', views.updateBatch, name='update_batch'),
]