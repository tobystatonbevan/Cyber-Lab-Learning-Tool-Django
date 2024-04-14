from django.shortcuts import render

def home(request):
    return render(request, "pages/home.html",{})

def admin_details(request):
    return render(request, "pages/admin_details.html",{})