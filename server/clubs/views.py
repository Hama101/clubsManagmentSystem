from django.shortcuts import render
from django.http import HttpResponse
from .models import Clubs as c
from .models import Events as e
from .models import Members as m

# Create your views here.
def home(request):
    return render(request,'home.html')


def clublist(request):
    clubs = c.objects.all()
    return render(request,'clublist.html',
                    {'clubs' : clubs})

def events(request):
    events = e.objects.all()
    return render(request , 'events.html' ,
                    {'events': events} )


def eventDetails(response , title):
    ed = e.objects.get(title=title)
    return render(response , 'eventdetails.html' , {'ed':   ed})

def members(request):
    members = m.objects.all()
    return render(request , 'members.html' ,
                    {'members': members} )