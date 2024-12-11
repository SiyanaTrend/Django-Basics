from django import forms

from forumApp.posts.choices import LanguageChoice
from forumApp.posts.models import Post


class PostBaseForm(forms.ModelForm):
    # lecturer = forms.BooleanField(
    #     required=True,
    # )
    class Meta:
        model = Post
        fields = "__all__"
        # fields = ('title', 'content')
        # exclude = ['content']
        # widgets = {
        #     'title': forms.NumberInput,
        # }
        # help_texts = {
        #     'title': 'Put a title'
        # }
        # labels = {
        #     'title': 'This is title'
        # }
        error_messages = {
            'title': {
                'required': 'Please enter the title of the post',
                'max_length': f'The title is too long. Please keep it under {Post.TITLE_MAX_LENGTH} characters.'
            },
        }


class PostCreateForm(PostBaseForm):
    pass


class PostEditForm(PostBaseForm):
    pass


class PostDeleteForm(PostBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:       # disabled all fields at once
            self.fields[field].disabled = True


class SearchForm(forms.Form):
    query = forms.CharField(
        label='',
        required=False,
        # required=True,
        # error_messages={
        #     'required': 'Please write something',
        # },
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Search for a post...',
            }
        )
    )



# instead of:
# class PostForm(forms.Form):
#     title = forms.CharField(
#         max_length=100,
#     )
#     content = forms.CharField(
#         widget=forms.Textarea,
#     )
#     author = forms.CharField(
#         max_length=30,
#     )
#     created_at = forms.DateTimeField()
#     languages = forms.ChoiceField(
#         choices=LanguageChoice.choices,
#     )