import datetime
from django.db import models
from userapp.models import Profil
from asosiy.models import Mahsulot


# Create your models here.

class Savat(models.Model):
    profil = models.ForeignKey(Profil, on_delete=models.CASCADE)
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.CASCADE)
    miqdor = models.PositiveSmallIntegerField(default=1)
    umumiy = models.FloatField()
    vaqt = models.DateTimeField(default=datetime.datetime.now())
    arxivda = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        narx = (1-(self.mahsulot.chegirma/100)) * self.mahsulot.narx
        self.umumiy = int(self.miqdor) * float(narx)
        super(Savat, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.profil}:{self.mahsulot}"

class Buyurtma(models.Model):
    savatlar = models.ManyToManyField(Savat)
    sana = models.DateField(auto_now_add=True)
    profil = models.ForeignKey(Profil, on_delete=models.CASCADE)
    manzil = models.CharField(max_length=300)
    zipcode = models.CharField(max_length=7)
    summa  = models.IntegerField(default=0)

    # def save(self, *args, **kwargs):
    #     s = 0
    #     for savat in self.savatlar.all():
    #         s+= savat.umumiy
    #     self.summa = s
    #     super(Buyurtma, self).save(*args, **kwargs)

