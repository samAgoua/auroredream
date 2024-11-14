from django.urls import path
from . import views

urlpatterns = [
    path('add/<int:module_id>', views.add_user_module, name='add_user_module'),
    path('add/<int:module_id>/<int:event_id>', views.add_event_module, name='add_event_module'),
]