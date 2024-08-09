from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

# Create your models here.
class Profile(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    password1=models.CharField(max_length=20)
    password2=models.CharField(max_length=20)

class Movies(models.Model):
    Title = models.CharField(max_length=30)
    Description = models.CharField(max_length=1000, blank=True, null=True)
    Created = models.DateTimeField(auto_now_add=True)
    Rate = models.FloatField(max_length=11)
    Uuid = models.UUIDField(default=uuid.uuid4)
    File = models.FileField(upload_to='video')
    Image = models.ImageField(upload_to='img')
    Poster= models.ImageField(upload_to='poster')
    def __str__(self):
        return self.Title



    

class Watchlists(models.Model):
    user=models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='watchlist')
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE,null=True, blank=True )
    Addedat = models.DateTimeField(auto_now_add=True)

    
    


class History(models.Model):
    movie = models.ManyToManyField(Movies)
    timestamp = models.DateTimeField(auto_now_add=True)
    


class Subscribe(models.Model):
    email = models.EmailField(unique=True)
