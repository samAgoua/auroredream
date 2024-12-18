# Generated by Django 5.1.1 on 2024-11-14 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ModulesManager', '0004_alter_usermodule_unique_together_eventmodule'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='usermodule',
            unique_together=set(),
        ),
        migrations.AddField(
            model_name='modules',
            name='configurable',
            field=models.BooleanField(default=False),
        ),
    ]
