from django.shortcuts import render

from nopims.models import Master

# Create your views here.
def index(request):
    masters= Master.objects.all()
    
    return render(request, 'masters/index.html', {"masters":masters})
    #return HttpResponse("test")