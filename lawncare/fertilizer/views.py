from django.http import HttpResponse, Http404
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
    try:
       fertilizer = Fertilizer.objects.get(pk=fert_id)
       context = {
           'fertilizer': fertilizer
       } 
    except Fertilizer.DoesNotExist:
        raise Http404("Fertilizer with id: %s does not exist" % fert_id)

    return render(request, 'fertilizer/fertilizer.html', context)

def apply(request, fert_id):
    return HttpResponse("Apply fertilizer %s" % fert_id )