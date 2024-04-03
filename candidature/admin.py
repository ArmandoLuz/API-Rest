from django.contrib import admin
from candidature.models import Candidature

@admin.register(Candidature)
class CandidatureAdmin(admin.ModelAdmin):
    list_display = ("id", "job", "date_init", "date_end",)
    search_fields = ("job",)