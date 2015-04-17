from django.shortcuts import render_to_response
from django.template import RequestContext
from app.forms import *
from django.core.mail import EmailMultiAlternatives #enviamos html
from django.contrib.auth import login, logout, authenticate
from django.http import  HttpResponseRedirect
def home(request):
	mensaje= "esto es un mensaje desde mi vista"
	ctx = {'msg':mensaje}
	return render_to_response('index.html',ctx,context_instance=RequestContext(request))

def contacto_view(request):
	info_enviado = False #Definir si se envio la infromacion o no
	email =""
	titulo=""
	texto=""
	if request.method == "POST":
		formulario = ContactForm(request.POST)
		if formulario.is_valid():
			info_enviado = True
			email = formulario.cleaned_data['Email']
			titulo = formulario.cleaned_data['Titulo']
			texto = formulario.cleaned_data['Texto']

			#Configuracion enivando mensaje via GMAIL
			to_admin = 'jorge.innovus@gmail.com'
			html_content = "Informacion recibida <br><br><br>***Mensaje****<br><br><br>%s"%(texto)
			#estructura es titulo correo, contenido correo, quien lo envio y para quien va
			msg = EmailMultiAlternatives('Correo de Contacto',html_content,'from@server.com',[to_admin])
			msg.attach_alternative(html_content,'text/html')#definimos el contenido como html
			msg.send() #enciamos el correo
	else:
		formulario = ContactForm()
	ctx = {'form':formulario,'email':email,'titulo':titulo,'texto':texto,'info_enviado':info_enviado}


	#formulario = ContactForm()
	#ctx={'form':formulario}
	return render_to_response('contacto.html',ctx,context_instance=RequestContext(request))

def login_view(request):

	mensaje =""					
	if request.user.is_authenticated():
		return HttpResponseRedirect('/')
	else:
		if request.method == "POST":
			form = LoginForm(request.POST)
			if form.is_valid():
				email = form.cleaned_data['email']
				password = form.cleaned_data['password']
				usuario = authenticate(email=email,password = password)

				if usuario is not None and usuario.is_active:# si e usuario es activo y esta validad

					 login (request, usuario)
					 return HttpResponseRedirect('/')
				else:
					mensaje = "usuario y/o password incorrecto"

		form = LoginForm()
		ctx ={'form':form,'mensaje':mensaje}
		return render_to_response('login.html',ctx,context_instance=RequestContext(request))

def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/')

def register_view(request):
	form = RegisterForm()
	ctx ={'form':form}
	return render_to_response('register.html',ctx,context_instance=RequestContext(request))


def registro_vista(request):
	mensaje= "esto es un mensaje desde mi vista"
	ctx = {'msg':mensaje}
	return render_to_response('formularioregistro.html',ctx,context_instance=RequestContext(request))

def registro_estudiante_view(request):
	form = RegistroEstudianteForm()
	ctx ={'form':form}
	return render_to_response('registropython.html',ctx,context_instance=RequestContext(request))


