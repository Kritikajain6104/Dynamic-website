from django.shortcuts import render,HttpResponse
from lead.models import lead


def index(request):
    leaddata=lead.objects.all()
    data={
        'leaddata':leaddata
    }
    return render(request,"index.html",data)

def events(request):
    return render(request,"events.html")

def team(request):
    return render(request,"team.html")

def blogs(request):
    return render(request,"blogs.html")

def resources(request):
    return render(request,"resources.html")

def contact(request):
    return render(request,"contact.html")
