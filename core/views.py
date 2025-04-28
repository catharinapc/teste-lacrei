from rest_framework import viewsets
from .models import Profissional, Consulta
from .serializers import ProfissionalSerializer, ConsultaSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

class ProfissionalViewSet(viewsets.ModelViewSet):
    queryset = Profissional.objects.all()
    serializer_class = ProfissionalSerializer

class ConsultaViewSet(viewsets.ModelViewSet):
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer

    @action(detail=False, methods=["get"], url_path="buscar-por-profissional/(?P<profissional_id>[^/.]+)")
    def buscar_por_profissional(self, request, profissional_id=None):
        consultas = self.queryset.filter(profissional_id=profissional_id)
        serializer = self.get_serializer(consultas, many=True)
        return Response(serializer.data)
