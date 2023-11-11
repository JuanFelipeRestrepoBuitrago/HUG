from django.db import models


class Egresado(models.Model):
    fecha_nacimiento = models.DateField(blank=True, null=True)
    nivel_educativo = models.CharField(max_length=250, blank=True, null=True)
    salario = models.FloatField(blank=True, null=True)
    experiencia_meses = models.IntegerField(blank=True, null=True)
    ciudad = models.CharField(max_length=250, blank=True, null=True)

    @staticmethod
    def crear_egresado(fecha_nacimiento, nivel_educativo, salario, experiencia_meses, ciudad):
        """
        Esta funcion permite crear un egresado en el sistema

        @param fecha_nacimiento: fecha de nacimiento del egresado
        @param nivel_educativo: nivel educativo del egresado
        @param salario: salario del egresado
        @param experiencia_meses: experiencia en meses del egresado
        @param ciudad: ciudad del egresado
        @return: retorna el egresado creado
        """
        egresado = Egresado(fecha_nacimiento=fecha_nacimiento, nivel_educativo=nivel_educativo, salario=salario,
                            experiencia_meses=experiencia_meses, ciudad=ciudad)
        egresado.save()

        return egresado

    def actualizar_egresado(self, fecha_nacimiento=None, nivel_educativo=None, salario=None, experiencia_meses=None, ciudad=None):
        """
        Esta funcion permite actualizar un egresado en el sistema

        @param fecha_nacimiento: fecha de nacimiento del egresado
        @param nivel_educativo: nivel educativo del egresado
        @param salario: salario del egresado
        @param experiencia_meses: experiencia en meses del egresado
        @param ciudad: ciudad del egresado
        """
        self.fecha_nacimiento = fecha_nacimiento
        self.nivel_educativo = nivel_educativo
        self.salario = salario
        self.experiencia_meses = experiencia_meses
        self.ciudad = ciudad

        self.save()

        return self

    def eliminar_egresado(self):
        """
        Esta funcion permite eliminar un egresado en el sistema
        """
        self.delete()

    class Meta:
        managed = False
        db_table = 'egresado'


class Estudio(models.Model):
    titulo = models.TextField(blank=True, null=True)
    institucion = models.TextField(blank=True, null=True)
    fecha_inicio = models.DateField(blank=True, null=True)
    fecha_fin = models.DateField(blank=True, null=True)
    egresado = models.ForeignKey(Egresado, models.DO_NOTHING, blank=True, null=True)

    @staticmethod
    def crear_estudio(titulo, institucion, fecha_inicio, fecha_fin, egresado):
        """
        Esta funcion permite crear un estudio en el sistema

        @param titulo: titulo del estudio
        @param institucion: institucion del estudio
        @param fecha_inicio: fecha de inicio del estudio
        @param fecha_fin: fecha de fin del estudio
        @param egresado: egresado del estudio
        @return: retorna el estudio creado
        """
        estudio = Estudio(titulo=titulo, institucion=institucion, fecha_inicio=fecha_inicio, fecha_fin=fecha_fin, egresado=egresado)
        estudio.save()

        return estudio

    def actualizar_estudio(self, titulo=None, institucion=None, fecha_inicio=None, fecha_fin=None, egresado=None):
        """
        Esta funcion permite actualizar un estudio en el sistema

        @param titulo: titulo del estudio
        @param institucion: institucion del estudio
        @param fecha_inicio: fecha de inicio del estudio
        @param fecha_fin: fecha de fin del estudio
        @param egresado: egresado del estudio
        """
        self.titulo = titulo
        self.institucion = institucion
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.egresado = egresado

        self.save()

        return self

    def eliminar_estudio(self):
        """
        Esta funcion permite eliminar un estudio en el sistema
        """
        self.delete()

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
