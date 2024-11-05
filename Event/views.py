from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView, TemplateView, DetailView
from .models import Evenement

# Create your views here.

class EvenementCreateView(CreateView):
    model = Evenement
    fields = ['titre','cover','description','date','lieu','type_evenement']
    template_name = 'Event/creer_evenement.html'

    def form_valid(self, form):
        form.instance.organisateur = self.request.user
        return super().form_valid(form)
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titre_page'] = "Créer un événement"
        return context
    
    def get_success_url(self):
        return reverse('dashboard', kwargs={'pk': self.object.pk})


class DashboardView(DetailView):
    """ doc """
    model = Evenement
    template_name = 'Event/dashboard.html'
    context_object_name = 'evenement'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titre_page'] = "Dashboard"
        return context

