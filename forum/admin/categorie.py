from django.contrib import admin
from forum.models import categorie


@admin.register(categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'ordre', 'created_at', 'updated_at', 'active')
