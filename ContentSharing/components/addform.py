from django.shortcuts import redirect
from django_unicorn.components import UnicornView

from ContentSharing.models import ContenuGalerie
from Event.models import Evenement
from ..forms import ContenuGalerieForm


class AddformView(UnicornView):
    form_class = ContenuGalerieForm

    evenement = None
    titre = ""
    description = ""
    fichier = None

    def mount(self):
        self.evenement = Evenement.objects.get(numero_uuid=self.component_args[0])
        print(self.evenement)

    def save(self):
        contenu = ContenuGalerie.objects.create(
            evenement=self.evenement,
            utilisateur=self.request.user if self.request.user.is_authenticated else None,
            ip_address=self.request.META.get('REMOTE_ADDR'),
            description=self.description,
            fichier=self.fichier
        )
        contenu.save()
        return redirect('galerie_evenement', uuid=self.evenement.numero_uuid)
