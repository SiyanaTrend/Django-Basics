from django import forms


class PersonForm(forms.Form):
    STATUS_CHOICES = (
        (1, 'Draft'),
        (2, 'Published'),
        (3, 'Archived')
    )
    person_name = forms.CharField(
        label='',
        # initial='Hi, I am',
        help_text='Put your first name',
        widget=forms.TextInput(attrs={'placeholder': 'Search'}),
        # widget=forms.Textarea(attrs={'placeholder': 'Search'}),
        error_messages={
            'required': 'Please enter a value',
        },
        required=True,
        max_length=10,
    )
    age = forms.IntegerField(
        help_text='Put your age'
    )
    email = forms.CharField(
        label='',
        # widget=forms.EmailInput(attrs={'placeholder': 'email address'}),
        widget=forms.URLInput(attrs={'placeholder': 'URL'}),
    )
    is_lecturer = forms.BooleanField(
        label='Check if you are lecturer',
        required=False,
    )

    # using ChoiceField => returns the object as a string, no matter if it is int, etc.
    # status = forms.ChoiceField(
    #     choices=STATUS_CHOICES,
    # )

    # using IntegerField with widget/Select => returns the object as int
    # status = forms.IntegerField(
    #     widget=forms.Select(choices=STATUS_CHOICES),
    # )

    checkboxes = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=STATUS_CHOICES,
    )

    file = forms.FileField(
        required=False,
    )
