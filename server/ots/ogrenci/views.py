from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect
from django.shortcuts import render
from django import forms
from .models import Talebe

# # Create your views here.

def ana_ogrenci(request):
    #return HttpResponse ("Web sitesine hoş geldiniz")
    # gidecek = loader.get_template('ogrenci_sf.html')
    #return HttpResponse(gidecek.render())

#def ogrencilist(request):
    ogrenciliste = Talebe.objects.all()
    template = loader.get_template('ogrenci_sf.html')
    gidecek ={
        'ogrencilistesi' : ogrenciliste,
    }
    return HttpResponse(template.render(gidecek, request))



class OgrenciForm(forms.ModelForm):
    class Meta:
        model = Talebe
        fields = ['TC', 'AdiSoyadi',
                  'Aciklama']  
# Kullanmak istediğiniz alanları buraya ekleyin
def ekle(request):
    if request.method == 'POST': # POST = Gönderme işlemi
        form = OgrenciForm(request.POST)
        if form.is_valid():
            # Form verileri işleme
            form.save()  # Veritabanına kaydetme
            return redirect('ogrenciler')  #url name
    else: # GET işlemi
        form = OgrenciForm()
    return render(request, 'ekle.html', {'form': form})

def detay(request, gelenid):
  secilen = Talebe.objects.get(id=gelenid)
  sayfa = loader.get_template('detay.html')
  gidecek = {
    'giden': secilen,
  }
  return HttpResponse(sayfa.render(gidecek, request))


def sil(request, gelenid):
  secilen = Talebe.objects.get(id=gelenid)
  
  secilen.delete()
  return redirect('ogrenciler') 


def guncelle(request, gelenid):
    ogrenci = Talebe.objects.get(id=gelenid)
    if request.method == 'POST':
        form = OgrenciForm(request.POST, instance=ogrenci)
        if form.is_valid():
            # Form verileri işleme
            form.save()  # Veritab. kaydetme
            return redirect('ogrenciler')#url adı
    else:
        form = OgrenciForm(instance=ogrenci)
    return render(request, 'ekle.html', {'form': form}) 

