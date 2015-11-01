from django import forms

class newMember(forms.Form):
    firstname = forms.CharField(max_length=100)
    lastname  = forms.CharField(max_length=100)
    address   = forms.CharField(max_length=100)
    city      = forms.CharField(max_length=100)
    postcode  = forms.CharField(max_length=6)
    email     = forms.EmailField(min_length=3)
    phone     = forms.CharField(max_length=10)
    homeTown  = forms.ModelChoiceField(queryset=Town.objects.all().order_by('name'))
    homeTownAnnat  = forms.ModelChoiceField(queryset=Town.objects.all().order_by('name'))
    gymnasium = forms.ModelChoiceField(queryset=Gymnasium.objects.all().order_by('name'))
    gymnasiumAnnat = forms.CharField(max_length=100)
    school    = forms.ModelChoiceField(queryset=School.objects.all().order_by('name'))
    schoolAnnat = forms.CharField(max_length=100)
    study     = forms.CharField(max_length=50)

