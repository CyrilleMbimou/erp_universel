from django.db import models
from core.models import Client

class Vente(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='ventes')
    date_vente = models.DateTimeField(auto_now_add=True)
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Vente #{self.id} - {self.client} - {self.montant} €"
