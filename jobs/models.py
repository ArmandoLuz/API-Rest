from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=150, verbose_name="Título")
    description = models.TextField(max_length=1000, verbose_name="Descrição", blank=True, null=True)
    requeriments = models.TextField(max_length=1000, verbose_name="Requisitos", blank=True, null=True)
    salary = models.FloatField(verbose_name="Salário")
    workload = models.CharField(max_length=10, verbose_name="Carga Horária")

    def __str__(self) -> str:
        return self.title