from django.contrib import admin
from .models import Categorie, Niveau, Langue

@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ('nom', 'created_at')
    search_fields = ('nom',)

@admin.register(Niveau)
class NiveauAdmin(admin.ModelAdmin):
    list_display = ('nom',)

@admin.register(Langue)
class LangueAdmin(admin.ModelAdmin):
    list_display = ('nom', 'code')
