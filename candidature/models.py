from django.db import models
from jobs.models import Job
from profiles.models import CustomUser

class Candidature(models.Model):
    job = models.ForeignKey(Job, on_delete=models.PROTECT, related_name='job', verbose_name='Vaga')
    candidates = models.ManyToManyField(CustomUser, related_name='candidates', verbose_name='Cadidatos', blank=True)
    date_init = models.DateTimeField(auto_now_add=True, verbose_name='Data de início')
    date_end = models.DateTimeField(verbose_name='Data de término')

    def __str__(self) -> str:
        return self.job.__str__()
