from django.forms import ModelForm
from .models import Users
from django import forms

class UserForm(ModelForm):
    class Meta:
        model = Users
        fields = '__all__'

        widgets = {
            'id' : forms.NumberInput(attrs = {'class' : 'form-control'}),
            'name' : forms.TextInput(attrs = {'class' : 'form-control'}),
            'surname' : forms.TextInput(attrs = {'class' : 'form-control'}),
            'dateOfBirth' : forms.DateInput(attrs = {'class' : 'form-control'}),
            'login' : forms.TextInput(attrs = {'class' : 'form-control'}),
            'passwordMd5' : forms.TextInput(attrs = {'class' : 'form-control'}),
            'isDeleted' : forms.TextInput(attrs = {'class' : 'form-control'}),
        }