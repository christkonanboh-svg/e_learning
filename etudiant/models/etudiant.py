from django.db import models
from django.conf import settings


class Etudiant(models.Model):   # ✅ TOUJOURS models.Model
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='etudiant'
    )

    matricule = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.matricule
