# Generated by Django 5.0 on 2024-01-15 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='password1',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='profile',
            name='password2',
            field=models.CharField(max_length=20),
        ),
    ]
