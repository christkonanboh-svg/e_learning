from django.db import models
from base.models import TimeStampedModel, Categorie, Niveau, Langue
from utilisateur.models import Utilisateur

class Parcours(TimeStampedModel):
    titre = models.CharField(max_length=200)
    description = models.TextField()
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    niveau = models.ForeignKey(Niveau, on_delete=models.SET_NULL, null=True)
    langue = models.ForeignKey(Langue, on_delete=models.SET_NULL, null=True)
    instructeur = models.ForeignKey(
        Utilisateur,
        on_delete=models.CASCADE,
        limit_choices_to={'role': 'instructeur'}
    )

    def __str__(self):
        return self.titre
