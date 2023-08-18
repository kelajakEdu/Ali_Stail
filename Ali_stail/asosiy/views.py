from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View
from .models import *

class HomeView(View):
    def get(self, request):
        if request.user.is_authenticated:
            content = {
                'bolimlar': Bolim.objects.all()
            }
            return render(request, 'page-index.html',content)

class HomeLoginsizView(View):
    def get(self, request):
        return render(request, 'page-index-2.html')

class BolimlarView(View):
    def get(self, request):
        content = {
            'bolimlar': Bolim.objects.all()
        }
        return render(request, 'page-category.html', content)

class BolimMahsulotlar(View):
    def get(self, request,soz):
        natija = Mahsulot.objects.filter(bolim__id=soz)
        kom = request.GET.get('k')
        dav = request.GET.get('d')
        mi = request.GET.get('kichik')
        ma = request.GET.get('katta')
        if kom:
            natija=natija.filter(brend=kom)
        if dav:
            natija=natija.filter(brend=dav)
        if mi and ma:
            natija=natija.filter(narx__gt=mi, narx__lt=ma)
        content = {
            'mahsulot':natija
        }
        return render(request, 'page-listing-grid.html', content)

class MahsulotDetails(View):
    def get(self, request, pk):
        chegirma_narx = Mahsulot.objects.get(id=pk).narx * (100 - Mahsulot.objects.get(id=pk).chegirma) // 100
        data = {
            'mahsulot': Mahsulot.objects.get(id=pk),
            'chegirma_narx': chegirma_narx,
            'izohlar': Izoh.objects.filter(mahsulot__id=pk)
        }
        return  render(request, 'page-detail-product.html', data)

class TanlanganView(View):
    def get(self, request):
        content = {
            'tanlangan': Tanlangan.objects.all()
        }
        return render(request, 'page-profile-wishlist.html', content)

class RemovtanlanganView(View):
    def get(self, request, pk):
        content = {
            'tanlangan': Tanlangan.objects.get(id=pk).delete()
        }
        return redirect('tanlangan')

