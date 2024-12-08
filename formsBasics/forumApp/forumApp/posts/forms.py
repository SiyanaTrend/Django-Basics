from django import forms
class PersonForm(forms.Form):
    person_name = forms.CharField(
        label='Put your first name',
        max_length=10,
    )
    age = forms.IntegerField(
        label='Put your age'
    )
