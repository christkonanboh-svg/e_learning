from django.contrib import admin
from etudiant.models import Etudiant

@admin.register(Etudiant)
class EtudiantAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'niveau',
        'date_inscription',
        'created_at',
        'updated_at',
        'active'
    )
    search_fields = (
        'user__username',
        'user__email'
    )
