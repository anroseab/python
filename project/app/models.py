from django.db import models

# Create your models here.
class Packages(models.Model):
    image=models.ImageField(upload_to='img')
    description=models.CharField(max_length=255)
    
    
class Blog(models.Model):
    image=models.ImageField(upload_to='img')
    description=models.CharField(max_length=255)

class Contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.CharField(max_length=10)
    subject=models.CharField(max_length=50)
    message=models.TextField()


class  Enquiry(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.CharField(max_length=10)
    message=models.TextField()
