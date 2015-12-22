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
    success = "false"
    if req.method == 'POST':
        form = newMember(req.POST)
        firstname = form['firstname']
        lastname = form['lastname']
        address = form['address']
        city = form['city']
        postcode = form['postcode']
        email = form['email']
        phone = form['phone']
        hometown = form['homeTown']
        startYear = 2010
       # startYear = form['startYear']
        if form['gymnasium'] == '':
            print('it twerks')
            gymnasium = form['gymnasium']
        else:
            gymnasium = form['gymnasiumAnnat']
        if form['homeTown'] != 'Annat':
            hometown = form['homeTown']
        else:
            hometown = form['homeTownAnnat']
        if form['school'] != 'Annat':
            school = form['school']
        else:
            school = form['schoolAnnat']
        study = form['study']
        active = True
        endYear = None
        studyLine = StudyLine.objects.get_or_create(school = School.objects.get_or_create(name=school)[0], name = study)
        study = Study.objects.create(startYear = startYear,graduated = False,active=active,endYear=endYear, studyLine = studyLine[0])
        member = User.objects.create(homeTown = Town.objects.get_or_create(name=hometown)[0], gymnasium = Gymnasium.objects.get_or_create(name=gymnasium)[0], study=study)
        member.firstname = firstname
        member.lastname = lastname
        member.phone = phone
        member.adress = address
        member.city = city
        member.email = email
        member.study = study
        member.postcode = postcode
        member.save()

        if form.is_valid():
            success = "true"
            form = newMember()
    else:
        success = 'true'
    schoolList = School.objects.all().extra(order_by=['name'])
    hometownList = Town.objects.all().extra(order_by=['name'])
    gymnasiumList = Gymnasium.objects.all().extra(order_by=['name'])
    return(render(req,'new.html',{'showdialog':success,'gymnasium':gymnasiumList,'schoolList':schoolList,'hometownList':hometownList}))
def view_member(req,req_id):
    member =  User.objects.get(id=req_id)
    return(render(req,'medlem.html',{'user':member}))
def delete_member(req,req_id):
    member =  User.objects.get(id= req_id)
    member.delete()
    return redirect('/')
