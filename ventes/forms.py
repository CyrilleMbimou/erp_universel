from django import forms
from .models import Vente

class VenteForm(forms.ModelForm):
    class Meta:
        model = Vente
        fields = ['client', 'montant', 'description']
