from django.db import models

class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Categorie(TimeStampedModel):
    nom = models.CharField(max_length=150, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.nom


class Niveau(TimeStampedModel):
    nom = models.CharField(max_length=50)

    def __str__(self):
        return self.nom


class Langue(TimeStampedModel):
    code = models.CharField(max_length=10)
    nom = models.CharField(max_length=50)

    def __str__(self):
        return self.nom


class SiteConfiguration(models.Model):
    nom_site = models.CharField(max_length=200)
    email_contact = models.EmailField()
    maintenance = models.BooleanField(default=False)

    def __str__(self):
        return self.nom_site
