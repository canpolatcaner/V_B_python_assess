from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def anatr(request):
    #return HttpResponse ("Web sitesine hoş geldiniz")
    gidecek = loader.get_template('anasyf.html')
    return HttpResponse(gidecek.render())

def anaen (request):
    return HttpResponse ("Welcome")