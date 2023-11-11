from django.db import models


class CRUDBase(models.Model):
    """
    Esta clase permite crear un modelo base para los modelos de la épica de CRUD de egresados
    """

    class Meta:
        abstract = True

    def crear(self, **kwargs):
        """
        Esta funcion permite crear un modelo en el sistema

        @param kwargs: parametros del modelo
        @return: retorna el modelo creado
        """
        for field, value in kwargs.items():
            setattr(self, field, value)
        self.save()

        return self

    def actualizar(self, **kwargs):
        """
        Esta funcion permite actualizar un modelo en el sistema

        @param kwargs: parametros del modelo
        """
        for field, value in kwargs.items():
            setattr(self, field, value)
        self.save()

        return self

    def eliminar(self):
        """
        Esta funcion permite eliminar un modelo en el sistema
        """
        self.delete()


class Egresado(CRUDBase):
    """
    Esta clase permite crear un modelo de egresado
    """
    fecha_nacimiento = models.DateField(blank=True, null=True)
    nivel_educativo = models.CharField(max_length=250, blank=True, null=True)
    salario = models.FloatField(blank=True, null=True)
    experiencia_meses = models.IntegerField(blank=True, null=True)
    ciudad = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'egresado'


class Estudio(CRUDBase):
    """
    Esta clase permite crear un modelo de estudio
    """
    titulo = models.TextField(blank=True, null=True)
    institucion = models.TextField(blank=True, null=True)
    fecha_inicio = models.DateField(blank=True, null=True)
    fecha_fin = models.DateField(blank=True, null=True)
    egresado = models.ForeignKey(Egresado, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'estudio'


class Experiencia(CRUDBase):
    """
    Esta clase permite crear un modelo de experiencia
    """
    empresa = models.TextField(blank=True, null=True)
    cargo = models.TextField(blank=True, null=True)
    fecha_inicio = models.DateField(blank=True, null=True)
    fecha_fin = models.DateField(blank=True, null=True)
    egresado = models.ForeignKey(Egresado, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'experiencia'


class Sector(CRUDBase):
    """
    Esta clase permite crear un modelo de sector
    """
    nombre = models.CharField(max_length=350)

    class Meta:
        managed = False
        db_table = 'sector'


class SectoresEgresados(CRUDBase):
    """
    Esta clase permite crear un modelo de sector de egresado
    """
    sector = models.ForeignKey(Sector, models.DO_NOTHING)
    egresado = models.ForeignKey(Egresado, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'sectores_egresados'
