from django.http import HttpResponse
from djangoIntroduction.tasks_app.models import Task
from django.shortcuts import render


def index(request):
    filter_title = request.GET.get('filter_title', '')

    tasks = Task.objects.filter(name__icontains=filter_title)

    context = {
        'filter_title': filter_title,
        'tasks': tasks,
    }
    return render(request, 'tasks/index.html', context)


    # tasks = Task.objects.all()
    # output = '\n'.join([
    #     '<h1>TASKS</h1>',
    #     '<ul>',
    #     *[f"<li>{t.name}: {t.description}" for t in tasks],
    #     '</ul>'
    # ])
    # if not output:
    #     output = 'There are no created tasks!'
    #
    # return HttpResponse(output)