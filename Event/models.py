from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.

class Evenement(models.Model):
    TYPES_EVENEMENT = [
        ('MARIAGE', 'Mariage'),
        ('ANNIVERSAIRE', 'Anniversaire'),
        ('REUNION', 'Réunion'),
        ('AUTRE', 'Autre'),
    ]

    titre = models.CharField(max_length=200)
    cover = models.ImageField(upload_to='evenements/', blank=True)
    description = models.TextField(blank=True)
    date = models.DateTimeField(null=True, blank=True)
    lieu = models.CharField(max_length=200, blank=True)
    type_evenement = models.CharField(max_length=20, choices=TYPES_EVENEMENT, default='AUTRE')
    organisateur = models.ForeignKey(User, on_delete=models.CASCADE, related_name='evenements_organises')
    date_creation = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)
    numero_uuid = models.UUIDField(unique=True, editable=False, default=uuid.uuid4, blank=True)

    def __str__(self):
        return str(self.titre) 
    

    class Meta:
        verbose_name = "Événement"
        verbose_name_plural = "Événements"
