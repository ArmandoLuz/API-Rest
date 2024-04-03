from django.contrib import admin
from jobs.models import Job

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "description",
        "requeriments",
        "salary",
        "workload",
    )

    search_fields = ("title",)
