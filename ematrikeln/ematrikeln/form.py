from django import forms

class medlemForm(forms.Form):
    firstName.form.CharField(max_length = 30)
    lastName.form.CharField(max_length = 30)
    address.form.CharField(max_length = 30)
    phone.form.IntegerField()
    city.form.CharField(max_length = 30)
    postcode.form.IntegerField()
    gymnasium.form.CharField(max_length = 30)
    gymnasiumAnnat.form.CharField(max_length = 30)
    school.form.CharField(max_length = 30)
    schoolAnnat.form.CharField(max_length = 30)
    study.form.CharField(max_length = 30)
    endYear.form.IntegerForm()
    startYear.form.IntegerForm()
    active.form.BooleanField()
