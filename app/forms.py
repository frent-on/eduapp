from django import forms
from django.forms  import ModelForm

from app.models import *

class ContactForm(forms.Form):
	Email = forms.EmailField(widget = forms.TextInput())
	Titulo = forms.CharField(widget = forms.TextInput())
	Texto = forms.CharField(widget = forms.Textarea())

class LoginForm(forms.Form):
	email = forms.CharField(widget = forms.TextInput())
	password = forms.CharField(widget = forms.PasswordInput(render_value=False))

class RegisterForm(forms.Form):
	email = forms.EmailField(label = "Correo Electronico",widget=forms.TextInput())
	password_one = forms.CharField(label = "Password",widget = forms.PasswordInput(render_value=False))
	password_two = forms.CharField(label = "Confirmar Password",widget = forms.PasswordInput(render_value=False))	

class RegistroEstudianteForm(ModelForm):
	class Meta:
		model = Estudiante
		exclude =("materias","user")
		