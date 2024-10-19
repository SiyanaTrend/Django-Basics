from django.shortcuts import render
from django.http import HttpResponse

from urlsAndViews.department.models import Department


def index(request):
    return HttpResponse('Hello Django!')


def view_with_int_pk(request, pk):
    return HttpResponse(f'<h1>Int pk: {pk} </h1>')


def view_with_slug(request, slug):
    department = Department.objects.get(slug=slug)
    return HttpResponse(f'<h1>Department from slug: {department} </h1>')

def view_with_pk_slug(request, pk, slug):
    department = Department.objects.get(pk=pk, slug=slug)
    return HttpResponse(f'<h1>ID: {pk} Department: {department} </h1>')

def view_with_name(request, variable):
    return HttpResponse(f'<h1>View with name: {variable} </h1>')

def view_with_path(request, variable):
    return HttpResponse(f'<h1>View with path: {variable} </h1>')

def view_with_regex(request, archive_year):
    return HttpResponse(f'The year is: {archive_year}')
