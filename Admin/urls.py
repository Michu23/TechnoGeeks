from django.urls import path
from . import views



urlpatterns = [
    path('view/advisors', views.getAdvisors, name='get_advisors'),
    path('view/reviewers', views.getReviewers, name='get_reviewers'),
    path('delete/advisor', views.deleteAdvisor, name='delete_reviewers'),
    path('view/advisors/names', views.getAdvisorsNames, name='get_advisors_names'),
    path('view/leads', views.getLeads, name='get_leads'),
    path('create/lead', views.createLead, name='create_leads'),
    path('delete/lead', views.deleteLead, name='delete_leads'),
]