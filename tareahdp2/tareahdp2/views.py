from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template.loader import get_template

def saludo(request):
	return HttpResponse("Hola mundo")
	
def despedida (request):
	return HttpResponse(pagina)

def fecha (request):
	fecha_actual = datetime.datetime.now()
	pagina = """<html>
				<body>
					<h1>fecha y hora actuales %s</h1>
				</body>
			</html>""" % fecha_actual
	return HttpResponse(pagina)

class persona(object):
	"""docstring for persona"""
	def __init__(self, nombre, apellido):
		self.nombre = nombre
		self.apellido = apellido
		
def paginita (request):

	doc_externo=open("/home/guille/Documentos/tareahdp2/tareahdp2/pagina.html")

	dia_actual = datetime.datetime.now()

	p1= persona("Alexander","Amaya")

	#nombre="Guillermo"

	#apellido="Lovo"

	plt=Template(doc_externo.read())

	doc_externo.close()

	ctx=Context({"mi_nombre":p1.nombre, "mi_apellido": p1.apellido, "fechita": dia_actual})

	documento=plt.render(ctx)

	return HttpResponse(documento)

def inicio_sesion(request):
	iniciar_sesion=get_template('iniciosesion')
	sesion=iniciar_sesion.render()
	return HttpResponse(sesion)

def formulario(request):
	formula=get_template('formulario')
	formu=formula.render()
	return HttpResponse(formu)