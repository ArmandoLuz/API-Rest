from rest_framework.serializers import ModelSerializer, SerializerMethodField
from candidature.models import Candidature

class CandidatureSerializer(ModelSerializer):
    n_candidates = SerializerMethodField()
    
    class Meta:
        model = Candidature
        fields = (
            "id",
            "date_init",
            "date_end",
            "job",
            "n_candidates",
        )

    def get_n_candidates(self, obj):
        return obj.candidates.all().count()