from django.db import models

class Projet(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    date_debut = models.DateField()
    date_fin = models.DateField(null=True, blank=True)
    statut = models.CharField(max_length=30, choices=[('en cours', 'En cours'), ('termine', 'Terminé'), ('suspendu', 'Suspendu')])

    def __str__(self):
        return self.nom
