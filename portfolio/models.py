from django.db import models

class Portfolio(models.Model):
    benutzername = models.CharField(max_length=50)
    e_Mail = models.TextField(max_length=50)
    profilbild = models.ImageField(upload_to ='profilbild', null=True, blank=True)

class Kategorie(models.Model):
    name = models.CharField(max_length=50)
    beschreibung = Beschreibung = models.TextField(max_length=10000)
    kategorie_bild = models.ImageField(upload_to ='kategoriebild', null=True, blank=True)


class Projekt(models.Model):
    titel = models.CharField(max_length=50)
    beschreibung = models.TextField(max_length=10000)
    url = models.URLField(max_length=200)
    projekt_bild = models.ImageField(upload_to ='projektbild', null=True, blank=True)
    erstellungsdatum = models.DateTimeField(null=True, blank=True)
    kategorie = models.ForeignKey(Kategorie, related_name= 'kategorie_project' ,on_delete=models.CASCADE) # so dass wenn ich ein kategorie lösche bleibt das project

NIVEAU_CHOICES = [
    ("Anfänger", "Anfänger"),
    ("Fortgeschrittener", "Fortgeschrittener"),
    ("Experte", "Experte"),
]

class Skill(models.Model):
    name = models.CharField(max_length=50)
    niveau = models.CharField(max_length=20, choices=NIVEAU_CHOICES)
    beschreibung = models.TextField(max_length=10000)
