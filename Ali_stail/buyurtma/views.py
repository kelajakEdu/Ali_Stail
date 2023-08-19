from django.shortcuts import render, redirect
from django.views import View

from .models import Savat
from .models import *
from asosiy.models import Mahsulot
from asosiy.models import Tanlangan
from userapp.models import Profil


class SavatView(View):
    def get(self, request):
        natija = Savat.objects.filter(profil__user=request.user, arxivda=False)
        s = 0
        chg = 0
        for savat in natija:
            s += (savat.mahsulot.narx) * savat.miqdor
            t = (1-(savat.mahsulot.chegirma/100)) * savat.mahsulot.narx * savat.miqdor
            chg += t

        content = {
            'savatlar': natija,
            'sum': s,
            'chg': s-chg,
            'yakuniy': chg,
        }
        return render(request, 'page-shopping-cart.html', content)

class MiqdorQosh(View):
    def get(self, request, son):
        savat = Savat.objects.get(id=son)
        savat.miqdor += 1
        savat.save()
        return  redirect("/buyurtma/savat")

class MiqdorKamaytir(View):
    def get(self, request, son):
        savat = Savat.objects.get(id=son)
        if savat.miqdor !=1:
            savat.miqdor -= 1
        savat.save()

        return  redirect("/buyurtma/savat")

class BuyurtmaView(View):
    def get(self, request):
        content={
            'buyurtmalar': Buyurtma.objects.filter(profil__user=request.user)
        }
        return render(request, 'page-profile-orders.html', content)

class savatRemoveView(View):
    def get(self, request, pk):
        content = {
            'savatlar': Savat.objects.get(id=pk).delete()
        }
        return redirect('savat')

class AddtanlanganView(View):
    def get(self, request, pk):
        Tanlangan.objects.create(
                mahsulot = Mahsulot.objects.get(id=pk),
                profil = Profil.objects.get(user=request.user)
            )
        return redirect('savat')
class BuyurtmaQoshView(View):
    def get(self, request):
        savatlari = Savat.objects.filter(profil__user = request.user, arxivda=False)
        buyurtma = Buyurtma.objects.create(
            manzil = "Fargona vil. Yozyovon shaxarchasi Mustaqillik ko'chasi",
            zipcode = '3629562',
            profil = Profil.objects.get(user = request.user),
            summa = 120000
        )
        s=0
        for savat in savatlari:
            buyurtma.savatlar.add(savat)
            s+= savat.umumiy
            savat.arxivda=True
            savat.save()
        buyurtma.summa = s
        buyurtma.save()
        return redirect("/buyurtma/buyurtma/")
