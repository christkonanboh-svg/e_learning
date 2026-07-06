from django.contrib import admin
from django.urls import path
from etudiant.views import render_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', render_page, name='home'),
]
