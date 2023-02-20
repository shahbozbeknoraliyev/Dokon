from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Ombor(models.Model):
    nom=models.CharField(max_length=50)
    user=models.OneToOneField(User,on_delete=models.SET_NULL,null=True)
    tel=models.CharField(max_length=13)
    ism=models.CharField(max_length=50)
    manzil=models.CharField(max_length=100)
class Mahsulot(models.Model):
    nom=models.CharField(max_length=50)
    brend=models.CharField(max_length=50)
    narx=models.IntegerField()
    kelgan_sana=models.DateField()
    miqdor=models.IntegerField()
    olchov=models.CharField(max_length=50)
    omborfk=models.ForeignKey(Ombor,on_delete=models.CASCADE)
class Client(models.Model):
    ism=models.CharField(max_length=55)
    nom=models.CharField(max_length=40)
    manzil=models.CharField(max_length=50)
    tel=models.CharField(max_length=13)
    qarz=models.IntegerField()
    omborfk=models.ForeignKey(Ombor,on_delete=models.CASCADE)
