from django.contrib import admin
from models import parcours

@admin.register(parcours)
class ParcoursAdmin(admin.ModelAdmin):
    list_display = ('titre', 'categorie', 'niveau', 'langue')
    list_filter = ('categorie', 'niveau', 'langue')
