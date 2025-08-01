from django.db import models

class EcritureComptable(models.Model):
    date = models.DateField()
    libelle = models.CharField(max_length=255)
    montant = models.DecimalField(max_digits=12, decimal_places=2)
    type = models.CharField(max_length=20, choices=[('credit', 'Crédit'), ('debit', 'Débit')])

    def __str__(self):
        return f"{self.date} - {self.libelle} ({self.type})"
