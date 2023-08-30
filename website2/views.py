from django.shortcuts import render,HttpResponse,redirect
from lead.models import lead
from contact.models import contact1
from django.http import HttpResponseRedirect
from blog.models import blog
from techteam.models import techteam
from contentteam.models import contentteam
from eventteam.models import eventteam
from gdteam.models import gdteam

def index(request):
    leaddata=lead.objects.all()
    data={
        'leaddata':leaddata
    }
    return render(request,"index.html",data)

def events(request):


    return render(request,"events.html")

def team(request):
    techteamdata=techteam.objects.all()
    contentteamdata=contentteam.objects.all()
    eventteamdata=eventteam.objects.all()
    gdteamdata=gdteam.objects.all()
    data2={
        'techteamdata':techteamdata,
        'contentteamdata':contentteamdata,
        'eventteamdata':eventteamdata,
        'gdteamdata':gdteamdata,

    }
    return render(request,"team.html",data2)

def blogs(request):
    blogsdata=blog.objects.all()
    data1={
        'blogdata': blogsdata
    }
    return render(request,"blogs.html",data1)

def resources(request):
    return render(request,"resources.html")

def contacts(request):
    try:
        if request.method=="POST":
            fname=request.POST.get('first_name')
            lname=request.POST.get('last_name')
            email=request.POST.get('email')
            message=request.POST.get('message')
            en=contact1(first_name=fname,last_name=lname,Email=email,message=message)
            en.save()
            return HttpResponseRedirect('/thankyou')

    except:
        pass        
    return render(request,"contact.html")

def thankyou(request):
    return render(request,"thankyou.html")