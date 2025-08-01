from django.db import models

class Produit(models.Model):
    nom = models.CharField(max_length=100)
    reference = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)
    prix_unitaire = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.nom} ({self.reference})"
