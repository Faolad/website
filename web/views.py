from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "web/index.html", {})
def about(request):
    return render(request, "web/about.html", {})
def contact_us(request):
    return render(request, "web/contact_us.html", {})