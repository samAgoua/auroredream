# Generated by Django 5.1.1 on 2024-10-01 00:37

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Event', '0002_evenement_cover'),
    ]

    operations = [
        migrations.AddField(
            model_name='evenement',
            name='numero_uuid',
            field=models.UUIDField(blank=True, default=uuid.uuid4, editable=False, unique=True),
        ),
    ]
