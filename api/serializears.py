from rest_framework import serializers
from .models import Evento,Participante
  
  #serializer modelo evento
  
class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        filds ='__all__'
        
class ParticipanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participante
        fields ='__all__'
        