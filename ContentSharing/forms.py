from django import forms
from django.forms import ModelForm

from .models import ContenuGalerie

class ContenuGalerieForm(ModelForm):
    class Meta:
        model = ContenuGalerie
        fields = ['type_contenu', 'fichier', 'description']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['type_contenu'].widget.attrs.update({'class': 'form-control'})
        self.fields['fichier'].widget.attrs.update({'class': 'form-control-file'})
        self.fields['description'].widget.attrs.update({'class': 'form-control', 'rows': 3})
        
    def clean_fichier(self):
        fichier = self.cleaned_data.get('fichier')
        if fichier:
            if fichier.size > 10 * 1024 * 1024:  # 10 Mo
                raise forms.ValidationError("Le fichier ne doit pas dépasser 10 Mo.")
        return fichier
