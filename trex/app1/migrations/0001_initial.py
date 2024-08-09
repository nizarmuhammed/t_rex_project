# Generated by Django 5.0 on 2024-01-11 05:04

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=30)),
                ('Description', models.CharField(blank=True, max_length=1000, null=True)),
                ('Created', models.DateTimeField(auto_now_add=True)),
                ('Rate', models.FloatField(max_length=11)),
                ('Uuid', models.UUIDField(default=uuid.uuid4)),
                ('File', models.FileField(upload_to='video')),
                ('Image', models.ImageField(upload_to='img')),
                ('Poster', models.ImageField(upload_to='poster')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('password1', models.IntegerField()),
                ('password2', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Subscribe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('movie', models.ManyToManyField(to='app1.movies')),
            ],
        ),
        migrations.CreateModel(
            name='Watchlists',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Addedat', models.DateTimeField(auto_now_add=True)),
                ('movie', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.movies')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='watchlist', to='app1.profile')),
            ],
        ),
    ]
