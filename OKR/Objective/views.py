from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django_tables2 import RequestConfig
from .models import Objective, Action
from .tables import ObjectiveTable


# Create your views here.
def index(request):
    objectives = ObjectiveTable(Objective.objects.all())
    RequestConfig(request).configure(objectives)
    return render(request, 'Objective/index.html', {'objectives': objectives})


def objective_detail(request, pk):
    return render(request, 'Objective/objective_detail.html',
                  {'actions': Action.objects.filter(objective_id=pk), 'objective': Objective.objects.get(id=pk)})
