from django.shortcuts import render,HttpResponse,redirect
from lead.models import lead
from contact.models import contact1
from django.http import HttpResponseRedirect
from blog.models import blog


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