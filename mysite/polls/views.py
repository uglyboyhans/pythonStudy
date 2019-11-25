from django.http import HttpResponse
from .models import Article, Reporter


def index(request):
    return HttpResponse("kon ni chi wa")


def new_reporter(request):
    get = request.GET
    if 'name' not in get:
        return HttpResponse("Invalid param")
    full_name = get['name']
    exist = Reporter.objects.filter(full_name=full_name)
    if len(exist):
        return HttpResponse("exist name")
    reporter = Reporter(full_name=get['name'])
    reporter.save()
    return HttpResponse("new reporter id is " + str(reporter.id))
