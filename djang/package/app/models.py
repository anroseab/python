from django.db import models

# Create your models here.
class Package(models.Model):
    name=models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Sub_package(models.Model):
    name=models.CharField(max_length=255)
    package=models.ForeignKey(Package,on_delete=models.CASCADE)