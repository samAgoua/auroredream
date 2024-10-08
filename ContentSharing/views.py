from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.core.exceptions import PermissionDenied
from .models import ContenuGalerie, CodeQR
from Event.models import Evenement
from .forms import ContenuGalerieForm
from .utils import generer_et_sauvegarder_qr_code
import qrcode

def galerie_evenement(request, uuid):
    evenement = get_object_or_404(Evenement, numero_uuid=uuid)
    contenus = ContenuGalerie.objects.filter(evenement=evenement).order_by('-date_ajout')
    form = ContenuGalerieForm()
    
    if request.method == 'POST':
        form = ContenuGalerieForm(request.POST, request.FILES)
        if form.is_valid():
            contenu = form.save(commit=False)
            contenu.evenement = evenement
            contenu.utilisateur = request.user if request.user.is_authenticated else None
            contenu.ip_address = request.META.get('REMOTE_ADDR')
            contenu.save()
            return redirect('galerie_evenement', uuid=uuid)
    
    context = {
        'evenement': evenement,
        'contenus': contenus,
        'form': form,
    }
    return render(request, 'services/contentsharing/galerie.html', context)

@login_required
@require_POST
def supprimer_contenu(request, contenu_id):
    contenu = get_object_or_404(ContenuGalerie, id=contenu_id)
    if request.user == contenu.utilisateur or request.user == contenu.evenement.organisateur:
        contenu.delete()
        return JsonResponse({'success': True})
    else:
        raise PermissionDenied

def generer_code_qr(request, uuid):
    evenement = get_object_or_404(Evenement, numero_uuid=uuid)
    if request.user != evenement.organisateur:
        raise PermissionDenied
    
    # Générer l'URL de la galerie de l'événement
    url_galerie = request.build_absolute_uri(f'/galerie/{uuid}/')
    
    # Générer un nom de fichier unique pour le QR code
    nom_fichier = f'qr_code_{uuid}.png'
    
    # Utiliser la fonction utilitaire pour générer et sauvegarder le QR code
    chemin_relatif = generer_et_sauvegarder_qr_code(url_galerie, nom_fichier)
    
    # Créer ou mettre à jour l'objet CodeQR
    code_qr, cree = CodeQR.objects.update_or_create(
        evenement=evenement,
        defaults={'img': chemin_relatif}
    )
    
    return JsonResponse({'success': True, 'qr_code_url': code_qr.img.url})

def afficher_code_qr(request, uuid):
    evenement = get_object_or_404(Evenement, numero_uuid=uuid)
    code_qr = get_object_or_404(CodeQR, evenement=evenement)
    return render(request, 'ContentSharing/afficher_code_qr.html', {'code_qr': code_qr})
