from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.views import APIView
from candidature.models import Candidature
from candidature.serializers import CandidatureSerializer
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from profiles.serializers import CustomUserSerializer
from rest_framework.response import Response
from rest_framework import status

def get_candidature(context):
    candidature_key = context.kwargs.get('pk')
    return get_object_or_404(Candidature, pk=candidature_key)

class RetrieveCandidatureView(RetrieveAPIView):
    def get(self, request, **kwargs):
        candidature = get_candidature(self)
        serialized_candidature = CandidatureSerializer(candidature)

        return Response(serialized_candidature.data)

class ListCandidatureView(ListAPIView):
    queryset = Candidature.objects.all()
    serializer_class = CandidatureSerializer

class CreateCandidatureView(CreateAPIView):
    permission_classes = (IsAuthenticated, IsAdminUser,)
    serializer_class = CandidatureSerializer

class CandidatesPerJobView(ListAPIView):
    permission_classes = (IsAuthenticated, IsAdminUser,)
    serializer_class = CustomUserSerializer

    def get_queryset(self):
        candidature = get_candidature(self)
        
        return candidature.candidates.all() if candidature else None
    
class RegisterCadidateInJob(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, **kwargs):
        user = request.user
        candidature = get_candidature(self)
        candidature.candidates.add(user)

        return Response(status=status.HTTP_200_OK)
