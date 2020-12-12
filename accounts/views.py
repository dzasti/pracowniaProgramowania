from django.shortcuts import render,redirect
from django.http import HttpResponse

from .models import *
from .forms import UserForm

b = Users(id= '1', name = 'Justyna', surname = 'Wojsz', dateOfBirth = '2000-08-23', login = 'jus', passwordMd5 = 'u5VC3dR1lkom9', isDeleted = 'False')
b.save()
c = Users(id= '2', name = 'Kuba', surname = 'Kowalski', dateOfBirth = '1975-08-13', login = 'kub', passwordMd5 = 'kwiatki453', isDeleted = 'True')
d = Users(id= '3', name = 'Paweł', surname = 'Kropka', dateOfBirth = '1999-01-04', login = 'paw', passwordMd5 = 'dom',isDeleted = 'False')
c.save()
d.save()
# Create your views here.

def home(request):
	return render(request,'accounts/strona.html')

def proba(request):
	users = Users.objects.all()
	return render(request, 'accounts/proba.html', {'users' : users})

def error(request):
	return render(request, 'accounts/error.html')

def updateAdd(request):
	form = UserForm
	form = UserForm(request.POST)
	if form.is_valid():
		form.save()
		return redirect('/proba')
	return render(request, 'accounts/updateAdd.html', {'form': form})