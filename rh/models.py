from django.db import models

class Employe(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    poste = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    telephone = models.CharField(max_length=20, blank=True)
    date_embauche = models.DateField()

    def __str__(self):
        return f"{self.nom} {self.prenom}"
