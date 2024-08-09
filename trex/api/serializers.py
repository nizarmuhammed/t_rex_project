from rest_framework import serializers
from app1.models import Movies

class MovieSerializers(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = '__all__'