# Generated by Django 5.1.1 on 2024-10-01 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Event', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='evenement',
            name='cover',
            field=models.ImageField(blank=True, upload_to='evenements/'),
        ),
    ]