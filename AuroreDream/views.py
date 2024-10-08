from Event.models import Evenement
from django.views.generic import TemplateView

class ProfileView(TemplateView):
    template_name = "registration/profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['events'] = Evenement.objects.filter(organisateur_id=self.request.user.id)
        return context
