from django.urls import path
from .views import (
    EvenementCreateView, 
    DashboardView
    )

urlpatterns = [
    path('creer-evenement/', EvenementCreateView.as_view(), name='evenement_create'),
    path('dashboard/<int:pk>/', DashboardView.as_view(), name='dashboard'),
]
