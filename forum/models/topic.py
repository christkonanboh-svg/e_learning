from django.db import models
from django.utils.text import slugify
from base import models


class Topic(models):
    title = models.CharField(max_length=200)
    categorie = models.ForeignKey('forum.Categorie', on_delete=models.CASCADE)
    author = models.ForeignKey('utilisateur.Utilisateur', on_delete=models.CASCADE)
    slug = models.SlugField(blank=True)
    views_count = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
