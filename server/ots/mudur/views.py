from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def ana_mudur(request):
    #return HttpResponse ("Web sitesine hoş geldiniz")
    gidecek = loader.get_template('mudur_sf.html')
    return HttpResponse(gidecek.render())