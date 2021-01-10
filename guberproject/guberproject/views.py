from django.http import HttpResponse

def index(request): #Index guber.com
    return HttpResponse("Index de guber")
