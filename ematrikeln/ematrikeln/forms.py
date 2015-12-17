from django import forms
from ematrikeln.models import *

class newMember(forms.Form):
    firstname = forms.CharField(max_length=100, min_length=2)
    lastname  = forms.CharField(max_length=100, min_length=2)
    address   = forms.CharField(max_length=100)
    city      = forms.CharField(max_length=100)
    postcode  = forms.CharField(max_length=6)
    email     = forms.EmailField(min_length=3)
    phone     = forms.CharField(max_length=10)
    homeTown  = forms.ModelChoiceField(
            queryset=Town.objects.all().order_by('name'),
            empty_label="Annat",
            required = False
            )
    homeTownAnnat  = forms.CharField(max_length=100, required = False)
    gymnasium = forms.ModelChoiceField(
            queryset=Gymnasium.objects.all().order_by('name'),
            empty_label = "Annat",
            required = False
            )
    gymnasiumAnnat = forms.CharField(max_length=100, required = False)
    school    = forms.ModelChoiceField(
            queryset=School.objects.all().order_by('name'),
            empty_label = "Annat",
            required = False
            )
    schoolAnnat = forms.CharField(max_length=100, required = False)
    study     = forms.CharField(max_length=50)
    medlemsTyp = forms.ChoiceField(MedlemsTyp.medlemsTyper)

    def clean(self):
        cleanData = super(newMember, self).clean()
        if cleanData.get('homeTown') == None:
            if cleanData.get('homeTownAnnat') == "":
                self.add_error('homeTownAnnat', 'Ifall du har valt annat bör du spesifiera vilket')
        if cleanData.get('gymnasium') == None:
            if cleanData.get('gymnasiumAnnat') == "":
                self.add_error('gymnasiumAnnat', 'Ifall du har valt annat bör du spesifiera vilket')
        if cleanData.get('school') == None:
            if cleanData.get('schoolAnnat') == "":
                self.add_error('schoolAnnat', 'Ifall du har valt annat bör du spesifiera vilket')
