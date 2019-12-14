from rest_framework import serializers

from .models import (
    Estudio,
    Collector,
    Estudio,
    Airports,
    BlackList,
    Messages,
    Template,
    Alerts
)


class EstudioSerializer(serializers.ModelSerializer):
  class Meta:
    model= Estudio
    fields= [
        'name'
    ]


class CollectorSerializar(serializers.ModelSerializer):
  class Meta:
    model= Collector
    fields = [
        "name",
        "survey_id",
        "close_date",
    ]
