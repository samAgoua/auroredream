from typing import Collection
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from Event.models import Evenement


class Modules(models.Model):
    nom = models.CharField(max_length=100)
    code = models.CharField(max_length=255) # Application Name
    description = models.TextField()
    prix = models.IntegerField(default=0)
    isEnabled = models.BooleanField(default=True)
    options = models.JSONField(default=None, blank=True, null=True)
    configurable = models.BooleanField(default=False)

    def __str__(self):
        return self.nom
    
    @property
    def user_has_module(self):
        user = get_user_model().objects.get(username='admin')
        return UserModule.objects.filter(user_id=user.pk, module=self).exists()
    
    def event_has_module(self, event_id) -> bool:
        event = Evenement.objects.get(id=event_id)
        return EventModule.objects.filter(event=event, module=self).exists()


class UserModule(models.Model):
    UserModuleStatut = (
        ('ACTIF', 'Actif'),
        ('INACTIF', 'Inactif'),
        ('INDISPONIBLE', 'Indisponible')
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="modules")
    module = models.ForeignKey(Modules, on_delete=models.CASCADE)
    statut = models.CharField(max_length=20, choices=UserModuleStatut, default="INACTIF")
    options = models.JSONField(default=None, blank=True, null=True)
    cout = models.IntegerField(null=True, blank=True)

class EventModule(models.Model):
    event = models.ForeignKey('Event.Evenement', on_delete=models.CASCADE)
    module = models.ForeignKey(Modules, on_delete=models.CASCADE)
    options = models.JSONField(default=None, blank=True, null=True)
    cout = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.event} - {self.module}"
    class Meta:
        unique_together = [['event', 'module']]
    

