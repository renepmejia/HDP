from django.shortcuts import render, HttpResponse

from fennechpage.models import Departamento
from fennechpage.models import Municipio

# Create your views here.

'''def inicio(request):

	return render(request, "plantilla.html")'''

def sesion(request):

	return render(request, "iniciosesion")

def formulario(request):

	departamentos = Departamento.objects.all()
	municipios = Municipio.objects.all()
	return render(request, "formulario", {"departamentos":departamentos,"municipios":
		municipios})

def inicio(request):
	return render(request, "covid19vacunados.html")

