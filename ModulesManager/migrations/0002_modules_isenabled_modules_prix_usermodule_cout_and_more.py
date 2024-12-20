# Generated by Django 5.1.1 on 2024-11-12 21:38

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ModulesManager', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='modules',
            name='isEnabled',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='modules',
            name='prix',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='usermodule',
            name='cout',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='usermodule',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='modules', to=settings.AUTH_USER_MODEL),
        ),
    ]
