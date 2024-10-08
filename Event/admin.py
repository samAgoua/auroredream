from django.contrib import admin
from .models import Evenement

# Register your models here.

@admin.register(Evenement)
class EvenementAdmin(admin.ModelAdmin):
    list_display = ('titre','cover', 'date', 'lieu', 'type_evenement', 'organisateur', 'date_creation', 'date_modification')
    list_filter = ('type_evenement', 'organisateur', 'date_creation', 'date_modification')
    search_fields = ('titre', 'description', 'lieu')
    date_hierarchy = 'date'
    ordering = ('date', 'titre')
    fields = ('titre','cover', 'description', 'date', 'lieu', 'type_evenement', 'organisateur')
    readonly_fields = ('date_creation', 'date_modification')
