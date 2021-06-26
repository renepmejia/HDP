from django.shortcuts import render, HttpResponse

# Create your views here.

'''def inicio(request):

	return render(request, "plantilla.html")'''

def sesion(request):

	return render(request, "iniciosesion.html")

def formulario(request):

	return render(request, "formulario.html")

