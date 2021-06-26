from django.contrib import admin

# Register your models here.

from fennechpage.models import Entrevista, Departamento, Municipio

admin.site.register(Entrevista)
admin.site.register(Departamento)
admin.site.register(Municipio)