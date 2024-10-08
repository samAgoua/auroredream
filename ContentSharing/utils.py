import qrcode
from django.conf import settings
import os

def generer_et_sauvegarder_qr_code(chaine, nom_fichier):
    """
    Génère un QR code à partir d'une chaîne et le sauvegarde dans le dossier media.
    
    Args:
    chaine (str): La chaîne à encoder dans le QR code.
    nom_fichier (str): Le nom du fichier pour sauvegarder le QR code.
    
    Returns:
    str: Le chemin relatif du fichier QR code généré.
    """
    # Générer le QR code
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(chaine)
    qr.make(fit=True)
    
    # Créer l'image du QR code
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Définir le chemin de sauvegarde
    chemin_media = settings.MEDIA_ROOT
    chemin_qr = os.path.join(chemin_media, 'qr_codes')
    
    # Créer le dossier s'il n'existe pas
    os.makedirs(chemin_qr, exist_ok=True)
    
    # Chemin complet du fichier
    chemin_fichier = os.path.join(chemin_qr, nom_fichier)
    
    # Sauvegarder l'image
    img.save(chemin_fichier)
    
    # Retourner le chemin relatif pour le stockage en base de données
    return os.path.join('qr_codes', nom_fichier)
