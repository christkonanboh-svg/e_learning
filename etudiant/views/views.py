from django.shortcuts import render

def render_page(request, page_name):
    return render(request, f"{page_name}.html")
