from django.urls import path
from .views import (
    generer_code_qr,
    afficher_code_qr,
    galerie_evenement
)

urlpatterns = [
    path('generer-code-qr/<uuid>/', generer_code_qr, name='generer_code_qr'),
    path('afficher-code-qr/<uuid>/', afficher_code_qr, name='afficher_code_qr'),
    path('galerie/<uuid>/', galerie_evenement, name='galerie_evenement'),
]