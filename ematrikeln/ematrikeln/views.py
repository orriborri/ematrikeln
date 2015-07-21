from django.shortcuts import render
from django.template.loader import get_template
from django.http import HttpResponse

def index(req):
    return(render(req,'index.html'))

def add(req):
    hometownList = sorted(['Lovisa','Borgå','Sibbo','Kotka'])
    schoolList = sorted(['Aalto Universitet','Helsingfors Universitet','Arcada','Sibelius Akademin'])
    gymnasiumList = sorted(['Kotka svenska samskola','Lovisa Gymnasium','Borgå Gymnasium','Sibbo Gymnasium'])
    return(render(req,'new.html',{'gymnasium':gymnasiumList,'schoolList':schoolList,'hometownList':hometownList}))

def add_member(req):
    return
# Create your views here.
