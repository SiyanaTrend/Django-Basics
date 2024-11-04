from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse(f"<h1>You did it!</h1>")
