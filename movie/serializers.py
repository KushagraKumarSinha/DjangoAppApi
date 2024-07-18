from rest_framework import serializers
from .models import Movie, Suggest

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields='__all__'

class SuggestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suggest
        fields='__all__'