from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template.loader import get_template



def inicio_sesion(request):
	iniciar_sesion=get_template('iniciosesion')
	sesion=iniciar_sesion.render()
	return HttpResponse(sesion)

def formulario(request):
	formula=get_template('formulario')
	formu=formula.render()
	return HttpResponse(formu)

def inicio(request):
	iniciar=get_template('covid19vacunados.html')
	inic=iniciar.render()
	return HttpResponse(inic)