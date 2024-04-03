from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from jobs.models import Job
from jobs.serializers import JobSerializer

class JobsView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, IsAdminUser,)
    queryset = Job.objects.all()
    serializer_class = JobSerializer
