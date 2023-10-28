from django.db import models


class Egresado(models.Model):
    fecha_nacimiento = models.DateField(blank=True, null=True)
    nivel_educativo = models.CharField(max_length=250, blank=True, null=True)
    salario = models.FloatField(blank=True, null=True)
    experiencia_meses = models.IntegerField(blank=True, null=True)
    ciudad = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'egresado'


class Estudio(models.Model):
    titulo = models.TextField(blank=True, null=True)
    institucion = models.TextField(blank=True, null=True)
    fecha_inicio = models.DateField(blank=True, null=True)
    fecha_fin = models.DateField(blank=True, null=True)
    egresado = models.ForeignKey(Egresado, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estudio'


class Experiencia(models.Model):
    empresa = models.TextField(blank=True, null=True)
    cargo = models.TextField(blank=True, null=True)
    fecha_inicio = models.DateField(blank=True, null=True)
    fecha_fin = models.DateField(blank=True, null=True)
    egresado = models.ForeignKey(Egresado, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'experiencia'


class Sector(models.Model):
    nombre = models.CharField(max_length=350)

    class Meta:
        managed = False
        db_table = 'sector'


class SectoresEgresados(models.Model):
    sector = models.ForeignKey(Sector, models.DO_NOTHING, blank=True, null=True)
    egresado = models.ForeignKey(Egresado, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sectores_egresados'
