from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from Event.models import Evenement

# Create your models here.

class ContenuGalerie(models.Model):
    TYPES_CONTENU = [
        ('IMAGE', 'Image'),
        ('VIDEO', 'Vidéo'),
    ]

    def get_upload_path(instance, filename):
        return f"galerie/{instance.evenement.numero_uuid}/{filename}"

    evenement = models.ForeignKey(Evenement, on_delete=models.CASCADE, related_name='contenus')
    type_contenu = models.CharField(max_length=5, choices=TYPES_CONTENU)
    fichier = models.FileField(upload_to=get_upload_path)
    description = models.TextField(blank=True)
    date_ajout = models.DateTimeField(auto_now_add=True)
    utilisateur = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)

    def __str__(self):
        return f"{self.get_type_contenu_display()} pour {self.evenement.titre}"
    
    def save(self, *args, **kwargs):
        super.save(*args, **kwargs)

    class Meta:
        verbose_name = "Contenu de galerie"
        verbose_name_plural = "Contenus de galerie"

class CodeQR(models.Model):

    def get_upload_path(instance, filename):
        return f"codes_qr/{instance.evenement.numero_uuid}/{filename}"
    
    def generate_unique_code():
        import random
        import string
        code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
        return code
    
    def generate_qr_code(self,url, filename):
        import qrcode
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(url)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img.save(filename)

    evenement = models.OneToOneField(Evenement, on_delete=models.CASCADE, related_name='code_qr')
    code = models.CharField(max_length=100, unique=True, default=generate_unique_code)
    img = models.ImageField(upload_to=get_upload_path, blank=True)
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Code QR pour {self.evenement.titre}"

    class Meta:
        verbose_name = "Code QR"
        verbose_name_plural = "Codes QR"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.img:
            url_galere = f'{settings.BASE_URL}/galerie/{self.evenement.numero_uuid}/'
            nom_fichier = f'qr_code_{self.evenement.numero_uuid}.png'
            chemin_fichier = f'{settings.MEDIA_ROOT}/{self.get_upload_path(nom_fichier)}'
            self.generate_qr_code(url_galere, chemin_fichier)
            self.img = chemin_fichier
            super().save(*args, **kwargs)
