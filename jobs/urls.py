from django.urls import path
from jobs.views import JobsView

urlpatterns = [
    path('jobs/', JobsView.as_view(), name='jobs_create_list'),
]
