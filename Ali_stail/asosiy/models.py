import datetime

from django.db import models
from userapp.models import Profil

class Bolim(models.Model):
    nom = models.CharField(max_length=100)
    rasm = models.FileField()
    def __str__(self):
        return self.nom

class Mahsulot(models.Model):
    nom = models.CharField(max_length=100)
    narx = models.PositiveIntegerField()
    chegirma = models.PositiveIntegerField(default=0)
    batafsil = models.TextField()
    brend = models.CharField(max_length=30)
    kafolat = models.CharField(max_length=30)
    yetkazish = models.CharField(max_length=30)
    mavjud = models.BooleanField(default=True)
    bolim = models.ForeignKey(Bolim, on_delete=models.CASCADE)
    ishlab_chiqaruvchi = models.CharField(max_length=30, default='Uzb')

    def __str__(self):
        return self.nom

class Media(models.Model):
    rasm = models.FileField()
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.CASCADE, related_name='rasmlar')


class Izoh(models.Model):
    matn = models.TextField()
    sana = models.DateField()
    baho = models.PositiveSmallIntegerField()
    mahsulot = models.ForeignKey(Mahsulot,on_delete=models.CASCADE)
    profil = models.ForeignKey(Profil,on_delete=models.CASCADE)

    def str(self):
        return f"{self.mahsulot} ga izoh"

class Tanlangan(models.Model):
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.CASCADE)
    profil = models.ForeignKey(Profil, on_delete=models.CASCADE)