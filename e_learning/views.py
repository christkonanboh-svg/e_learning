from django.shortcuts import render

def render_page(request):
    return render(request, 'fixed-instructor-dashboard.html')
