from django.shortcuts import render

from rest_framework import viewsets
from .models import Evento, Participante
from .serializears import EventoSerializer 

class EventoViewSet(viewsets.ModelViewSet):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer
    
class ParticipanteViewSet(viewsets.ModelViewSet):
    queryset = Participante.objects.all()
    serializer_class = ParticipanteSerializer
# Create your views here.
