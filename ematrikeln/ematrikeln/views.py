from django.shortcuts import render
from django.template.loader import get_template
from django.http import HttpResponse
from .forms import newMember
from ematrikeln.models import *
from django.shortcuts import redirect


def index(req):
    allMembers = User.objects.all()
    return(render(req,'index.html',{'all':allMembers}))

def add(req):
    success = 'false'
    if req.method == 'POST':
        form = newMember(req.POST)
        if form.is_valid():
            success  = 'true'
    else:
        form = newMember()
    return(render(req,'new.html',{'showdialog':success,'form':form}))

def view_member(req,req_id):
    member =  User.objects.get(id=req_id)
    return(render(req,'medlem.html',{'user':member}))
def delete_member(req,req_id):
    member =  User.objects.get(id= req_id)
    member.delete()
    return redirect('/')
def add_member(req):
    if req.method == 'POST':
        if req.is_valid():
            firstName   = req.POST['firstName']
            lastName    = req.POST['lastName']
            address     = req.POST['address']
            phone       = req.POST['phonenumber']
            city        = req.POST['city']
            postcode    = req.POST['postcode']
            epost       = req.POST['email']
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
            endYear = req.POST['endYear']
            startYear = req.POST['startYear']
            active = req.POST['active']
            # medlemsavgift = req.POST['Betalat']
            studyLine = StudyLine.objects.get_or_create(school = School.objects.get_or_create(name=school)[0], name = study)
            study = Study.objects.create(startYear = startYear,graduated = False,active=active,endYear=endYear, studyLine = studyLine[0])
            newMember = User.objects.create(homeTown = Town.objects.get_or_create(name=hometown)[0], gymnasium = Gymnasium.objects.get_or_create(name=gymnasium)[0], study=study)
            newMember.firstName = firstName
            newMember.lastName = lastName
            newMember.phone = phone
            newMember.adress = address
            newMember.city = city
            newMember.email = epost
            newMember.study = study
            newMember.postcode = postcode
            newMember.save()
            return HttpResponse(200)
        return HttpResponse(500)
    return HttpResponse(404)
