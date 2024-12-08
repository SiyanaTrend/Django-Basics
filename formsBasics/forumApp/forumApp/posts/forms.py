from django import forms
class PersonForm(forms.Form):
    STATUS_CHOICES = (
        (1, 'Draft'),
        (2, 'Published'),
        (3, 'Archived')
    )
    person_name = forms.CharField(
        label='First name',
        help_text='Put your first name',
        max_length=10,
    )
    age = forms.IntegerField(
        help_text='Put your age'
    )
    is_lecturer = forms.BooleanField(
        label='Check if you are lecturer'
    )

    status = forms.ChoiceField(
        choices=STATUS_CHOICES,
    )