from django.db import models

# Create your models here.

class  Vivo(models.Model):
    name=models.CharField(max_length=255)

class  Oppo(models.Model):
    name=models.CharField(max_length=255)
