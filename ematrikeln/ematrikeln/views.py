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
    if state is '':
        success = 'false'
    else:
        success = 'true'
    schoolList = School.objects.all().extra(order_by=['name'])
    hometownList = Town.objects.all().extra(order_by=['name'])
    gymnasiumList = Gymnasium.objects.all().extra(order_by=['name'])
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
    print(type(req.POST['gymnasium']))

    if req.POST['gymnasium'] != 'Annat':
        gymnasium = req.POST['gymnasium']
    else:
        gymnasium = req.POST['gymnasiumAnnat']
    if req.POST['hometown'] != 'Annat':
        hometown = req.POST['hometown']
    else:
        hometown = req.POST['hometownAnnat']
    if req.POST['school'] != 'Annat':
        school = req.POST['school']
    else:
        school = req.POST['schoolAnnat']
    study = req.POST['study']
    print("home"+hometown)
   # medlemsavgift = req.POST['Betalat'
    
    newMember = User.objects.create(school = School.objects.get_or_create(name=school)[0], homeTown = Town.objects.get_or_create(name=hometown)[0], gymnasium = Gymnasium.objects.get_or_create(name=gymnasium)[0])
    newMember.firstName = firstName
    newMember.lastName = lastName
    newMember.address = address
    newMember.city = city
    newMember.email = epost
    newMember.study = study
    newMember.poscode = postcode

    newMember.save()
    return redirect('/add/success')
