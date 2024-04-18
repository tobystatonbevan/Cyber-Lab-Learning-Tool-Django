from django.shortcuts import render
from pages.models import Vulnerability

def home(request):
    return render(request, "pages/home.html",{})

def admin_details(request):
    return render(request, "pages/admin_details.html",{})

def vulnerabilities(request):
    vulnerabilities = Vulnerability.objects.all()
    context = {
        "vulnerabilities": vulnerabilities
    }
    return render(request, "pages/vulns.html",context)
