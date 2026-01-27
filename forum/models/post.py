from django.db import models
from base import models


class Post(models):
    topic = models.ForeignKey('forum.topic', on_delete=models.CASCADE)
    author = models.ForeignKey('utilisateur.Utilisateur', on_delete=models.CASCADE)
    content = models.TextField()
    is_solution = models.BooleanField(default=False)

    def __str__(self):
        return f"Post #{self.id}"
