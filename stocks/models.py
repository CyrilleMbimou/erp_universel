from django.db import models
from produits.models import Produit

class Stock(models.Model):
    produit = models.OneToOneField(Produit, on_delete=models.CASCADE, related_name='stock')
    quantite = models.PositiveIntegerField(default=0)
    seuil_alerte = models.PositiveIntegerField(default=5)

    def __str__(self):
        return f"Stock de {self.produit}: {self.quantite} unités"
