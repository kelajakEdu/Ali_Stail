from django.contrib.auth.models import User
from django.db import models

class Profil(models.Model):
    ism = models.CharField(max_length=50,null=True)
    jins = models.CharField(max_length=50)
    shahar = models.CharField(max_length=50)
    viloyat = models.CharField(max_length=50)
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.ism