from typing import Any
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView, CreateView
from .models import Modules, UserModule, EventModule
from django.contrib.auth.decorators import login_required
from Event.models import Evenement as Event
from loguru import logger

class ModuleListView(ListView):
    model = Modules.objects.all()
    template_name = "module_list.html"
    context_object_name = "modules"

    # def get(self,request,pk=None, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['evennement'] = None
    #     if pk is not None:
    #         logger.info(f"Event ID: {self.kwargs['pk']}")
    #         self.get_context_data()['evennement'] = Event.objects.get(id=self.kwargs['pk'])
    #     else:
    #         self.get_context_data()['evennement'] = 1
    #     return context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['evennement'] = "aurore"
        return context

@login_required
def add_user_module(request, module_id):
    module = Modules.objects.get(id=module_id)
    user_module = UserModule(user=request.user, module=module)
    user_module.save()
    return redirect(reverse('dashboard'))

@login_required
def add_event_module(request, module_id, event_id):
    module = Modules.objects.get(id=module_id)
    event = Event.objects.get(id=event_id)
    event_module = EventModule(event=event, module=module)
    event_module.save()
    return redirect(reverse('dashboard', kwargs={'pk': event_id}))
