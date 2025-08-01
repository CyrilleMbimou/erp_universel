from django import forms
from .models import EcritureComptable

class EcritureComptableForm(forms.ModelForm):
    class Meta:
        model = EcritureComptable
        fields = ['date', 'libelle', 'montant', 'type']
