from django.contrib import admin
from forum.models import post


@admin.register(post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('topic', 'author', 'is_solution', 'created_at', 'active')
