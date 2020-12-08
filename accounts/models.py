from django.db import models

# Create your models here.
class Users(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100, default ='nazwisko')
    dateOfBirth = models.DateField(default = '2019-09-25')
    login = models.CharField(max_length=100, default ='login')
    passwordMd5 = models.CharField(max_length=100, default = 'haslo')
    id_roli = models.IntegerField(default = '1')
    isDeleted = models.BooleanField(default = 'True')

