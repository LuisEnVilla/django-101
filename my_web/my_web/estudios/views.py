from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework import filters

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

from .serializers import (
    EstudioSerializer,
    CollectorSerializar
)


class EstudioViewSet(viewsets.ModelViewSet):
    queryset = Estudio.objects.all()
    serializer_class = EstudioSerializer
    filter_backends = [filters.SearchFilter]
    filterset_fields = ['name', ]


class CollectoresViewSet(viewsets.ModelViewSet):
  queryset = Collector.objects.all()
  serializer_class = CollectorSerializar
  filter_backends = [filters.SearchFilter]
  filterset_fields = ['name', ]
