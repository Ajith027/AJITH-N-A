# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from . models import place,team


def demo(request):
    obj=place.objects.all()
    team_obj=team.objects.all()
    return render(request,"index.html",{'result':obj,'result1':team_obj})
