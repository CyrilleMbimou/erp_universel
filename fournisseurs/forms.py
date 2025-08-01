from django import forms
from .models import Fournisseur

class FournisseurForm(forms.ModelForm):
    class Meta:
        model = Fournisseur
        fields = ['nom', 'email', 'telephone', 'adresse']
