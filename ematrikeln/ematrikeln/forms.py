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
            to_field_name="name",
            required = False,
            )
    homeTownAnnat  = forms.CharField(max_length=100, required = False)
    gymnasium = forms.ModelChoiceField(
            queryset=Gymnasium.objects.all().order_by('name'),
            empty_label = "Annat",
            to_field_name="name",
            required = False,
            )
    gymnasiumAnnat = forms.CharField(max_length=100, required = False)
    school    = forms.ModelChoiceField(
            queryset=School.objects.all().order_by('name'),
            empty_label = "Annat",
            to_field_name="name",
            required = False,
            )
    schoolAnnat = forms.CharField(max_length=100, required = False)
    study     = forms.CharField(max_length=50)
    startYear =forms.CharField(max_length=4)
    medlemsTyp = forms.ChoiceField([('studerande','studerande'),('äldre medlem','äldre medlem')])

    def  clean(self):
        cleaned_data = super(newMember, self).clean()
        msg = "Detta fält är obligatorisk"
        def validateOthers(choice,other,data,self,msg):
            if not data.get(choice):
                if not data.get(other):
                    self.add_error(other, msg)
        validateOthers('school','schoolAnnat',cleaned_data,self,msg)
        validateOthers('gymnasium','gymnasiumAnnat',cleaned_data,self,msg)
        validateOthers('homeTown','homeTownAnnat',cleaned_data,self,msg)
#        homeTown = cleaned_data.get('homeTown')

#        if homeTown == "None":
#        homeTownAnnat = cleaned_data.get('homeTownAnnat')
#            if homeTownAnnat == "None":
#
#        print(homeTown)
#        gymnasium = cleaned_data.get('gymnasium')
#        school = cleaned_data.get('school')
#    def __init__(self,req):
#       super(newMember, self).__init__()
#      choices=[(x,x) for x in range(1900, datetime.now().year+1)]
#      self.fields['startYear'].choices = choices

