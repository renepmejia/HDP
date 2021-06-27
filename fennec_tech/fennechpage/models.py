# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Departamento(models.Model):
    id_depa = models.IntegerField(primary_key=True)
    nombre_depa = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'departamento'


class Municipio(models.Model):
    id_muni = models.IntegerField(primary_key=True)
    nombre_muni = models.CharField(max_length=50)
    id_depart = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'municipio'

class Usuario(models.Model):
    id_usuario = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    contraseña =  models.CharField(max_length=10)

    class Meta:
        verbose_name='Usuario'

class Vacuna(models.Model):
    id_vacuna = models.IntegerField(primary_key= True)
    dosis1 = models.BooleanField(default=False)
    dosis2 = models.BooleanField(default=False)

    class Meta:
        verbose_name='Vacuna'

class Entrevista(models.Model):
    id_usuario = models.CharField('Nombre entrevistador',max_length=5, null=False, blank=False)
    id_depa = models.CharField('Departamento', max_length=15, null=False, blank=False)
    id_muni = models.CharField('Municipio', max_length=50, null=False, blank=False)
    id_vacuna = models.BooleanField('Dosis 1', default=True)
    id_vacuna = models.BooleanField('Dosis 2')

    class Meta:
        verbose_name='Entrevista'