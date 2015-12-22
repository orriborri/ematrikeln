from django import forms
from datetime import datetime, time, date
from ematrikeln.models import *

class newMember(forms.Form):


    firstname = forms.CharField(max_length=100)
    lastname  = forms.CharField(max_length=100)
    address   = forms.CharField(max_length=100)
    city      = forms.CharField(max_length=100)
    postcode  = forms.CharField(max_length=6)
    email     = forms.EmailField(min_length=3)
    phone     = forms.CharField(max_length=10)
    homeTown  = forms.ModelChoiceField(
            queryset = Town.objects.all().order_by('name'),
            empty_label="Annat",
            required=True)
    homeTownAnnat  = forms.CharField(max_length=100)
    gymnasium = forms.ModelChoiceField(
            queryset=Gymnasium.objects.all().order_by('name'),
            empty_label = "Annat",
            required=True)
    gymnasiumAnnat = forms.CharField(max_length=100)
    school    = forms.ModelChoiceField(
            queryset=School.objects.all().order_by('name'),
            empty_label = "Annat",
            required=True)
    schoolAnnat = forms.CharField(max_length=100)
    study     = forms.CharField(max_length=50)
    medlemsTyp = forms.ChoiceField(MedlemsTyp.medlemsTyper)
    startYear =forms.CharField(widget=forms.Select())
    def __init__(self):
        super(newMember, self).__init__()
        choices=[(x,x) for x in range(1900, datetime.now().year+1)]
        self.fields['startYear'].choices = choices

