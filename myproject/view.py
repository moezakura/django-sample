from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader


def index(request: WSGIRequest):
    template = loader.get_template('myproject/index.html')
    return HttpResponse(template.render({}, request))


def post(request: WSGIRequest):
    if request.method != 'POST':
        return HttpResponse("not allow method", status=405)

    template = loader.get_template('myproject/index.html')
    return HttpResponse(template.render({
        'error_message': '',
    }, request))
