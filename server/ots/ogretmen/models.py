from django.db import models


class Egitmen(models.Model):
  TC = models.CharField(max_length=11)
  AdiSoyadi = models.CharField(max_length=50)
  Dersler = models.CharField(max_length=255)
  Aciklama = models.CharField(max_length=255)
