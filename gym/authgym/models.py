from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField()
    phonenumber = models.CharField(max_length=12)
    description = models.TextField()
    
    def __str__(self):
        return self.email
    
    
    
class Enrollment(models.Model):
    FullName = models.CharField(max_length=25)
    Email = models.EmailField()
    Gender = models.CharField(max_length=25)
    PhoneNumber = models.CharField(max_length=12)
    DOB = models.CharField(max_length=50)
    SelectMemberShipplan = models.CharField(max_length=200)
    SelectTrainer = models.CharField(max_length=55)
    Reference = models.CharField(max_length=55)
    Address = models.TextField()
    paymentStatus = models.CharField(max_length=55, blank=True, null=True)
    Price = models.IntegerField(max_length=55, blank=True, null=True)
    DueDate = models.DateTimeField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)
    
    def __str__(self):
        return self.FullName
    
    
    
class Trainer(models.Model):
    name = models.CharField(max_length=25)
    gender = models.CharField(max_length=25)
    phone = models.CharField(max_length=12)
    salary = models.IntegerField(max_length=25)
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)
    
    
    def __str__(self):
        return self.name
    
    
class Membershipplan(models.Model):
    plan = models.CharField(max_length=185)
    price = models.IntegerField(max_length=55)
    
    def __int__(self):
        return self.id