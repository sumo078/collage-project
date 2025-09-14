from django.db import models

# Create your models here.
# class userdetail(models.Model):
#     email=models.EmailField()
#     password=models.IntegerField()
    
    
    
    
class signdetail(models.Model):
    Name=models.CharField(max_length=100)
    Email=models.EmailField()
    Password=models.IntegerField()
    Cpassword=models.IntegerField()
    
class contactdetail(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField()
    text=models.TextField()


class bookingdetail(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.IntegerField()
    appointmentDate=models.DateField()
    services=models.CharField(max_length=400)
    timeSlot=models.CharField(max_length=100)
    
class feedback(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    message=models.TextField()
    
class registerdetail(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    pass1=models.IntegerField()
    
class supplierdetail(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    phone=models.IntegerField()
    address=models.CharField(max_length=40)
class contractordetail(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    phone=models.IntegerField()
    address=models.CharField(max_length=40)
    
    
    