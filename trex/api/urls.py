from django.urls import path
from .views import MoviesListCreate
from api import views

urlpatterns = [
   path('', MoviesListCreate.as_view(), name='movies-list-create'),


]