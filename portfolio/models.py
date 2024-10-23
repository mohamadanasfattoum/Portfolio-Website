from django.db import models

class Portfolio(models.Model):
    Benutzername = models.CharField(max_length=50)
    E_Mail = models.TextField(max_length=50)
    Profilbild = models.ImageField(upload_to ='Profilbild', null=True, blank=True)


