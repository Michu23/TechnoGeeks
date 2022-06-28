from django.urls import path
from . import views, chart



urlpatterns = [
    path('view/tasklist', views.getTaskslist, name='get_taskslist'),
    path('view/manifest', views.getManifest, name='get_manifest'),
    path('view/chartdata', chart.getChartdata, name='get_chartdata'),
    path('view/pendings', views.getPendings, name='get_pendings'),
    path('delete/pendings', views.deletePendings, name='delete_pendings'),
    path('review/passed', views.reviewPassed, name='review_passed'),
    path('review/repeated', views.reviewRepeated, name='review_repeated'),
    path('add/task', views.addTask, name='add_task'),
    path('complete/task', views.completeTask, name='complete_task'),
    path('delete/task', views.delete_task, name='complete_task'),
    path('folder/submit', views.folderSubmit, name='folder_submit'),
]