from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader


def index(request: WSGIRequest):
    template = loader.get_template('myproject/index.html')
    context = {}
    return HttpResponse(template.render(context, request))
