from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, Welcome to my first app!")