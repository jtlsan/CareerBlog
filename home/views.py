from django.shortcuts import render
from home.models import DevNews
# Create your views here.

def home(request):
    qs = DevNews.objects.all().first()
    return render(request, "home/home.html", {'tmp': qs})