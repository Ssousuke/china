from django.db import models
from apps.utils.base_models import Base


class TypeJob(Base):
    type = models.CharField(max_length=50)

    def __str__(self):
        return self.type

    class Meta:
        verbose_name = 'Tipo de Trabalho'
        verbose_name_plural = 'Tipo de Trabalho'
        ordering = ['type']


class Job(Base):
    job = models.CharField(max_length=255)
    description = models.TextField(max_length=450)
    initial_date = models.DateField()
    finish_date = models.DateField(blank=True, null=True)
    type = models.ForeignKey(TypeJob, on_delete=models.CASCADE)
    link = models.URLField(blank=True, null=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.job

    class Meta:
        verbose_name = 'Trabalho'
        verbose_name_plural = 'Trabalhos'
        ordering = ['-created_at']
