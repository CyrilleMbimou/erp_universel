from django.db import models

class Document(models.Model):
    titre = models.CharField(max_length=255)
    fichier = models.FileField(upload_to='documents/')
    date_upload = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titre
