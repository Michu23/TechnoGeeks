from django.urls import path
from . import views



urlpatterns = [
    path('view/tasklist', views.getTaskslist, name='get_taskslist'),
    path('view/manifest', views.getManifest, name='get_manifest'),
    path('review/passed', views.reviewPassed, name='review_passed'),
    path('review/repeated', views.reviewRepeated, name='review_repeated'),
    path('add/task', views.addTask, name='add_task'),
    path('complete/task', views.completeTask, name='complete_task'),
]