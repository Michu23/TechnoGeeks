from django.urls import path
from . import views



urlpatterns = [
    path('view/advisors', views.getAdvisors, name='get_advisors'),
    path('view/reviewers', views.getReviewers, name='get_reviewers'),
    path('view/advisors/names', views.getAdvisorsNames, name='get_advisors_names'),
]