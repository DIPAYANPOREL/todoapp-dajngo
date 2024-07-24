from django.shortcuts import render
from django.http import HttpResponse
from . models import Tasks
# Create your views here.

def index(request):

    tasks = Tasks.objects.all()

    context = {'tasks': tasks}

    return render(request, 'tasks.html', context)