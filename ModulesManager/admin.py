from django.contrib import admin
from .models import UserModule, Modules

# Register your models here.

@admin.register(Modules)
class ModulesAdmin(admin.ModelAdmin):
    list_display = ('nom', 'description',)


@admin.register(UserModule)
class UserModuleAdmin(admin.ModelAdmin):
    list_display = ('user', 'module', 'options','statut')
    list_filter = ('user__username',)
    search_fields = ('user__username', 'module__nom')
