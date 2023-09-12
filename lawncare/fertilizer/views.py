from django.http import Http404, HttpResponseRedirect
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
    fertilizer =  Fertilizer.objects.get(pk=fert_id)
    bags = request.POST['bags']
    date = request.POST['date']

    fertilizer.application_set.create(bags_applied=bags, date_applied=date)
    return HttpResponseRedirect('/fert')