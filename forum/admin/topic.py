from django.contrib import admin
from forum.models import topic


@admin.register(topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('title', 'categorie', 'author', 'views_count', 'created_at', 'active')
