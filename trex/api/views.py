from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Movies
from .serializers import MovieSerializers
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework import generics

class MoviesListCreate(generics.ListCreateAPIView):
    queryset = Movies.objects.all()
    serializer_class = MovieSerializers