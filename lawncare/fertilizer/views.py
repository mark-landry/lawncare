from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Show all the applied fertilizers")

def fertilizers(request):
    return HttpResponse("List all available fertilizers")

def detail(request, fert_id):
    return HttpResponse("Show the fertilizer detail of %s" % fert_id )

def apply(request, fert_id):
    return HttpResponse("Apply fertilizer %s" % fert_id )