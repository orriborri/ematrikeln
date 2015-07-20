from django.shortcuts import render
from django.template.loader import get_template
from django.http import HttpResponse

def index(req):
    return(render(req,'index.html'))

def add(req):
    return(render(req,'new.html'))

def add_member(req):
    return
# Create your views here.
