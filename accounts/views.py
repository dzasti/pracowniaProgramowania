from django.shortcuts import render,redirect
from django.http import HttpResponse

from .models import *
from .forms import UserForm

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
	form_class = UserForm
	if form.is_valid():
		form.save()
		return redirect('/proba')
	return render(request, 'accounts/updateAdd.html', {'form': form})

def updateAdd2(request,pk):
	order = Users.objects.get(id=pk)
	form = UserForm(instance = order)
	if request.method == 'POST':
		form = UserForm(request.POST, instance = order)
		if form.is_valid():
			form.save()
			return redirect('/proba')
	return render(request, 'accounts/updateAdd.html', {'form': form})