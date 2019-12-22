from rest_framework import serializers
# Models
from .models import Data, StarRating


class StarRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = StarRating
        fields = ['id', 'run', 'rating_value']


class DataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Data
        fields = ['run', 'nombre', 'exam', 'fecha', 'hora_inicio', 'hora_fin', 'sala', 'proctor', 'sede']
