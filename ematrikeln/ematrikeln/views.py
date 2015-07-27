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
    schoolList = sorted(School.objects.all())
    hometownList = sorted(Town.objects.all())
    gymnasiumList = sorted(Gymnasium.School.objects.all())
    #schoolList = sorted(['Aalto Universitet','Helsingfors Universitet','Arcada','Sibelius Akademin'])
    #gymnasiumList = sorted(['Kotka svenska samskola','Lovisa Gymnasium','Borgå Gymnasium','Sibbo Gymnasium'])
    return(render(req,'new.html',{'showdialog':success,'gymnasium':gymnasiumList,'schoolList':schoolList,'hometownList':hometownList}))

def add_member(req):
    firstName   = req.POST['firstName']
    lastName    = req.POST['lastName']
    address     = req.POST['address']
    city        = req.POST['city']
    postcode    = req.POST['postcode']
    epost       = req.POST['email']
    if req.POST['gymnasiumAnnat'] is not None:
        gymnasium = req.POST['gymnasium']
    else:
        gymnasium = req.POST['gymnasiumAnnat']
    hemsida     = req.POST['hometown']
    if req.POST['hometownAnnat'] is '':
        hometown = req.POST['hometown']
    else:
        hometown = req.POST['hometownAnnat']
    if req.POST['schoolAnnat'] is '':
        school = req.POST['school']
    else:
        school = req.POST['schoolAnnat']
    study = req.POST['study']
    # medlemsavgift = req.POST['Betalat']
    newMember = User.objects.create()
    newMember.lastName = lastName
    newMember.address = address
    newMember.city = city
    newMember.email = epost
    newMember.study = study
    newMember.school = School.objects.get_or_create(name=school)
    newMember.hometown = Town.objects.get_or_create(name=hometown)
    newMember.gymnasium = Gymnasium.objects.get_or_create(name=gymnasium)
    newMember.poscode = postcode

    newMember.save()
    return redirect('/add/success')
