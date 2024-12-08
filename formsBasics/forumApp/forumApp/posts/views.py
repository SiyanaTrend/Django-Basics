from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render

from forumApp.posts.forms import PersonForm


def index(request):
    form = PersonForm(request.POST or None)

    if request.method == 'POST':
        print(request.POST['person_name'])

    if form.is_valid():
        print(form.cleaned_data['person_name'])

    context = {
        "my_form": form,
    }
    return render(request, 'base.html', context)


def dashboard(request):
    context = {
        "posts": [
            {
                "title": "How to create Django project",
                "author": "Maria Kirilova",
                "content": "",
                "created_at": datetime.now(),
            },
            {
                "title": "How to create HTML file ",
                "author": "Ivan Abadjiev",
                "content": "It is the **most easiest** <i>thing</i> to do",
                "created_at": datetime.now(),
            },
            {
                "title": "How to create CSS file",
                "author": "",
                "content": "### You should follow my steps",
                "created_at": datetime.now(),
            },
        ]
    }

    return render(request, 'posts/dashboard.html', context)
