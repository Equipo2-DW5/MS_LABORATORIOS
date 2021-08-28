from rest_framework import serializers
from .models import Laboratorio

class LaboratorioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Laboratorio
        fields=("lab_id","categoria","descripcion","estado","aforo")

class PostLaboratorioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Laboratorio
        fields=("categoria","descripcion","estado","aforo")