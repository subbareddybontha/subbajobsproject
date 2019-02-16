from django.db import models

# Create your models here.
class Hydjobs(models.Model):
    date=models.DateField()
    company=models.CharField(max_length=100)
    title=models.CharField(max_length=100)
    eiligibility=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    email=models.EmailField()
    phonenumber=models.IntegerField()

class Bangjobs(models.Model):
    date=models.DateField()
    company=models.CharField(max_length=100)
    title=models.CharField(max_length=100)
    eiligibility=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    email=models.EmailField()
    phonenumber=models.IntegerField()

class Chennaijobs(models.Model):
    date=models.DateField()
    company=models.CharField(max_length=100)
    title=models.CharField(max_length=100)
    eiligibility=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    email=models.EmailField()
    phonenumber=models.IntegerField()

class Punejobs(models.Model):
    date=models.DateField()
    company=models.CharField(max_length=100)
    title=models.CharField(max_length=100)
    eiligibility=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    email=models.EmailField()
    phonenumber=models.IntegerField()
