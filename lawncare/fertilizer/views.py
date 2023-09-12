from django.http import HttpResponse
from django.template import loader
from .models import Fertilizer, Application

# Create your views here.
def index(request):
    applications =  Application.objects.all()
    template = loader.get_template('fertilizer/index.html')

    context = {
        'applications': applications
    }

    return HttpResponse(template.render(context, request))

def fertilizers(request):
    fertilizers = Fertilizer.objects.all()
    template = loader.get_template('fertilizer/fertilizers.html')

    context = {
        'fertilizers': fertilizers
    }

    return HttpResponse(template.render(context, request))

def detail(request, fert_id):
    return HttpResponse("Show the fertilizer detail of %s" % fert_id )

def apply(request, fert_id):
    return HttpResponse("Apply fertilizer %s" % fert_id )