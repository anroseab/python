from django.db import models

# Create your models here.
class Packages(models.Model):
    image=models.ImageField(upload_to='img')
    description=models.CharField(max_length=255)
    
    def __str__(self):
        return str(self.image) 



class Subpackage(models.Model):
    description=models.CharField(max_length=255)
    image=models.ForeignKey(Packages,on_delete=models.CASCADE)
    test1=models.CharField(max_length=255)
    test2=models.CharField(max_length=255)
    test3=models.CharField(max_length=255)
    test4=models.CharField(max_length=255)
    test5=models.CharField(max_length=255)
    cost=models.CharField(max_length=255)

