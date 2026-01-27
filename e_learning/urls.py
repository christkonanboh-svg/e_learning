from django.urls import path
from etudiant.views import render_page

urlpatterns = [
    path('<str:page_name>/', render_page, name='render_page'),
]
