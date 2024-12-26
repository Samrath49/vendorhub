from django.db import models
from services.base.models import TimeStampedModel


class Category(TimeStampedModel):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        indexes = [models.Index(fields=['parent'])]