from django.shortcuts import render

def home(request):
    """Home page view for book management"""
    return render(request, 'book/home.html')
