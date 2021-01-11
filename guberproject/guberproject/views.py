from django.http import HttpResponse
from django.template import loader
def index(request): #Index guber.com
    template = loader.get_template('index.html')
    template_loader = template.render()
    return HttpResponse(template_loader)
