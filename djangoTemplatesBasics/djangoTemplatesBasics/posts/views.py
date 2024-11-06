from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {
        "current_time": datetime.now()
    }
    return render(request, 'base.html', context)
