from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView, CreateView
from .models import Modules, UserModule
from django.contrib.auth.decorators import login_required

class ModuleListView(ListView):
    model = Modules.objects.all()
    template_name = "module_list.html"
    context_object_name = "modules"

@login_required
def add_user_module(request, module_id):
    module = Modules.objects.get(id=module_id)
    user_module = UserModule(user=request.user, module=module)
    user_module.save()
    return redirect(reverse('dashboard'))
