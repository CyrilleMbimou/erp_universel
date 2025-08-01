from django.db import models
from fournisseurs.models import Fournisseur
from produits.models import Produit

class Achat(models.Model):
    fournisseur = models.ForeignKey(Fournisseur, on_delete=models.CASCADE, related_name='achats')
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE, related_name='achats')
    date_achat = models.DateTimeField(auto_now_add=True)
    quantite = models.PositiveIntegerField()
    prix_unitaire = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Achat {self.produit} x{self.quantite} à {self.fournisseur}"
