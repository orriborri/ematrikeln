from django.shortcuts import render
from django.template.loader import get_template
from django.http import HttpResponse
from .forms import newMember
from ematrikeln.models import *
from django.shortcuts import redirect


def index(req):
    allMembers = User.objects.all()
    return(render(req,'index.html',{'all':allMembers}))

def add(req,state):
    if state is None:
        success = 'false'
    else:
        success = 'true'
    hometownList = sorted(['Lovisa','Borgå','Sibbo','Kotka'])
    schoolList = sorted(['Aalto Universitet','Helsingfors Universitet','Arcada','Sibelius Akademin'])
    gymnasiumList = sorted(['Kotka svenska samskola','Lovisa Gymnasium','Borgå Gymnasium','Sibbo Gymnasium'])
    return(render(req,'new.html',{'showdialog':success,'gymnasium':gymnasiumList,'schoolList':schoolList,'hometownList':hometownList}))

def add_member(req):
    firstName   = req.POST['firstName']
    lastName    = req.POST['lastName']
    address     = req.POST['address']
    city        = req.POST['city']
    postcode    = req.POST['postcode']
    epost       = req.POST['email']
    gymnasium   = req.POST['gymnasium']
    if req.POST['gymnasiumAnnat'] is not None:
        gymnasiumAnnat = req.POST['gymnasiumAnnat']
    hemsida     = req.POST['hometown']
    if req.POST['hometownAnnat'] is not None:
        hometownAnnat = req.POST['hometownAnnat']
    school = req.POST['school']
    if req.POST['schoolAnnat'] is not None:
        schoolAnnat = req.POST['schoolAnnat']
    study = req.POST['study']
    # medlemsavgift = req.POST['Betalat']
    newMember = User.objects.create()
    newMember.firstName = firstName
    newMember.save()
    return redirect('/add/success')
# Create your views here.
