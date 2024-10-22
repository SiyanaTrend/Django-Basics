from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponse, Http404


from urlsAndViews.department.models import Department


def index(request):
    # url = reverse('redirect-view')
    # return HttpResponse(f'<h1>{url}</h1>')
    url_lazy = reverse('redirect-view')
    return HttpResponse(f'<h1>reverse lazy</h1>')


def view_with_int_pk(request, pk):
    return HttpResponse(f'<h1>Int pk: {pk} </h1>')


def view_with_slug(request, slug):
    department = Department.objects.get(slug=slug)
    return HttpResponse(f'<h1>Department from slug: {department} </h1>')

def view_with_pk_slug(request, pk, slug):
    # # Option 1 for error 404
    department = Department.objects.filter(pk=pk, slug=slug)
    #
    if not department:
        raise Http404
    # return HttpResponse(f'<h1>ID: {pk} Department: {department.first()} </h1>')

    # # Option 2
    # department = get_object_or_404(Department, pk=pk, slug=slug)
    # return HttpResponse(f'<h1>ID: {pk} Department: {department} </h1>')

    # # Option 3
    # return HttpResponseNotFound()


def view_with_name(request, variable):
    # return HttpResponse(f'<h1>View with name: {variable} </h1>')
    return render(request,'departments/name_template.html', {'variable': variable})

def view_with_path(request, variable):
    return HttpResponse(f'<h1>View with path: {variable} </h1>')

def view_with_regex(request, archive_year):
    return HttpResponse(f'The year is: {archive_year}')

def redirect_to_softuni(request):
    return redirect('https://softuni.bg')

def redirect_to_view(request):
    # # option 1 - breaks abstractions
    # return redirect('http://localhost:8000')

    # # option 2 breaks single responsibility if view is from another app
    # return redirect(index)

    # option 3 - best option => put a name in urls path: path('', views.index, name='home')
    return redirect('home')

