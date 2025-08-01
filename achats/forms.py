from django import forms
from .models import Achat

class AchatForm(forms.ModelForm):
    class Meta:
        model = Achat
        fields = ['fournisseur', 'produit', 'quantite', 'prix_unitaire']
