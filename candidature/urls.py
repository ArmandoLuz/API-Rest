from django.urls import path
from candidature.views import (
    CreateCandidatureView,
    ListCandidatureView, 
    CandidatesPerJobView, 
    RegisterCadidateInJob,
    RetrieveCandidatureView,
)

urlpatterns = [
    path('candidature/', ListCandidatureView.as_view(), name='candidature'),
    path('candidature/create/', CreateCandidatureView.as_view(), name='create_candidature'),
    path('candidature/<int:pk>/', RetrieveCandidatureView.as_view(), name='detail_candidature'),
    path('candidature/<int:pk>/register/', RegisterCadidateInJob.as_view(), name='register_cadidate_in_job'),
    path('candidature/<int:pk>/candidates/', CandidatesPerJobView.as_view(), name='candidates_per_view'),
]