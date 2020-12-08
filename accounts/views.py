from django.shortcuts import render
from django.http import HttpResponse

from .models import *

b = Users(id= '1', name = 'Justyna', surname = 'Wojsz', dateOfBirth = '2000-08-23', login = 'jus', passwordMd5 = 'u5VC3dR1lkom9', id_roli = '3', isDeleted = 'False')
b.save()
c = Users(id= '2', name = 'Kuba', surname = 'Kowalski', dateOfBirth = '1975-08-13', login = 'kub', passwordMd5 = 'kwiatki453', id_roli = '1', isDeleted = 'True')
d = Users(id= '3', name = 'Paweł', surname = 'Kropka', dateOfBirth = '1999-01-04', login = 'paw', passwordMd5 = 'dom', id_roli = '3', isDeleted = 'False')
c.save()
d.save()
# Create your views here.

def home(request):
	return render(request,'accounts/strona.html')

def products(request):
	return HttpResponse('products')

def customer(request):
	return HttpResponse('customer')

def wizualizacja(request):
	users = Users.objects.all()
	return render(request, 'accounts/strona2.html', {'users' : users})
