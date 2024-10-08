from django.contrib import admin
from .models import ContenuGalerie, CodeQR

# Register your models here.
@admin.register(ContenuGalerie)
class ContenuGalerieAdmin(admin.ModelAdmin):
    list_display = ('evenement', 'type_contenu', 'fichier', 'date_ajout', 'utilisateur', 'ip_address')
    list_filter = ('type_contenu', 'date_ajout', 'utilisateur')
    search_fields = ('evenement__titre', 'description')
    date_hierarchy = 'date_ajout'
    ordering = ('date_ajout', 'evenement')
    fields = ('evenement', 'type_contenu', 'fichier', 'description', 'date_ajout', 'utilisateur', 'ip_address')
    readonly_fields = ('date_ajout', 'ip_address')


@admin.register(CodeQR)
class CodeQRAdmin(admin.ModelAdmin):
    list_display = ('evenement', 'code', 'img', 'date_creation')
    list_filter = ('date_creation',)
    search_fields = ('evenement__titre',)
    date_hierarchy = 'date_creation'
    ordering = ('date_creation', 'evenement')
    fields = ('evenement', 'code', 'img', 'date_creation')
    readonly_fields = ('date_creation',)
