from django.http import HttpResponse
from django.shortcuts import render
from .models import Fertilizer, Application

# Create your views here.
def index(request):
    applications =  Application.objects.all()
    context = {
        'applications': applications
    }

    return render(request, 'fertilizer/index.html', context)

def fertilizers(request):
    fertilizers = Fertilizer.objects.all()
    context = {
        'fertilizers': fertilizers
    }

    return render(request, 'fertilizer/fertilizers.html', context)

def detail(request, fert_id):
    return HttpResponse("Show the fertilizer detail of %s" % fert_id )

def apply(request, fert_id):
    return HttpResponse("Apply fertilizer %s" % fert_id )