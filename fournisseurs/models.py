from django.db import models

class Fournisseur(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    telephone = models.CharField(max_length=20, blank=True)
    adresse = models.TextField(blank=True)

    def __str__(self):
        return self.nom
