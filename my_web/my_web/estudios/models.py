from django.contrib.postgres.fields import ArrayField
from django.db import models


class Estudio(models.Model):
  name = models.CharField(max_length=30, null=False, blank=False)
  token = models.CharField(max_length=120, null=False, blank=False)
  blackList = ArrayField(models.CharField(max_length=100), blank=True)

  def __str__(self):
    return self.name
