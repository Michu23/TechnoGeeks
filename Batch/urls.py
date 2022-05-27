from django.urls import path
from . import views



urlpatterns = [
    path('view/batches', views.getBatches, name='get_batches'),
    path('create/batch', views.createBatch, name='create_batch'),
    path('delete/batch', views.deleteBatch, name='delete_batch'),
    path('update/batch', views.updateBatch, name='update_batch'),
    path('view/groups', views.getGroups, name='get_groups'),
    path('view/mygroups', views.getMyGroups, name='get_my_groups'),
    path('view/group/less', views.getGroupLess, name='get_group_less'),
    path('view/group/details', views.getGroupDetails, name='get_group_details'),
    path('view/mygroup/details', views.getMyGroupDetails, name='get_my_group_details'),
    path('add/group', views.addInGroup, name='add_in_group'),
    path('remove/group', views.removeFromGroup, name='remove_from_group'),
    path('create/group', views.createGroup, name='create_group'),
    path('delete/group', views.deleteGroup, name='delete_group'),
    path('update/group', views.updateGroup, name='update_group'),
]