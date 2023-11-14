from django.views import View
from django.db import IntegrityError
from django.shortcuts import render, redirect
from .models import Egresado, Estudio, Experiencia, Sector, SectoresEgresados
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from abc import abstractmethod


@method_decorator(login_required, name='dispatch')
class ObjetosView(View):
    template_name = ''

    @abstractmethod
    def obtener_objetos(self):
        """
        Esta función permite obtener los objetos a mostrar en la página. Esta función debe ser implementada por las
        clases hijas.
        """
        pass

    @abstractmethod
    def obtener_contexto(self, elementos):
        """
        Esta función permite obtener el contexto para renderizar la página.

        @param elementos: Lista de elementos a mostrar en la página.
        """
        pass

    def get(self, request):
        """
        Esta función permite listar los objetos en el sistema.
        @param request: HttpRequest, objeto que contiene la información sobre la solicitud web actual.
        @return: HttpResponse, objeto que contiene la respuesta HTTP que se enviará al navegador web que realizó la
        """
        objetos = self.obtener_objetos()
        return render(request, self.template_name, self.obtener_contexto(objetos))

    @abstractmethod
    def post(self, request):
        """
        Esta función permite crear un objeto en el sistema.
        @param request: HttpRequest, objeto que contiene la información sobre la solicitud web actual.
        @return: HttpResponse, objeto que contiene la respuesta HTTP que se enviará al navegador web que realizó la
        """
        pass


@method_decorator(login_required, name='dispatch')
class ObjetosEliminarView(View):
    @abstractmethod
    def post(self, request, objeto_id):
        """
        Esta función permite eliminar un objeto del sistema.
        @param request: HttpRequest, objeto que contiene la información sobre la solicitud web actual.
        @param objeto_id: Int, identificador del objeto a eliminar.
        @return: HttpResponse, objeto que contiene la respuesta HTTP que se enviará al navegador web que realizó la
        """
        pass


@method_decorator(login_required, name='dispatch')
class ObjetosEditarView(View):
    @abstractmethod
    def post(self, request, objeto_id):
        """
        Esta función permite editar un objeto del sistema.
        @param request: HttpRequest, objeto que contiene la información sobre la solicitud web actual.
        @param objeto_id: Int, identificador del objeto a editar.
        @return: HttpResponse, objeto que contiene la respuesta HTTP que se enviará al navegador web que realizó la
        """
        pass


@method_decorator(login_required, name='dispatch')
class EgresadosView(ObjetosView):
    template_name = 'egresados.html'

    def obtener_objetos(self):
        """
        Esta función permite obtener los egresados a mostrar en la página.
        """
        return Egresado.objects.all()[:1000]

    def obtener_contexto(self, elementos):
        """
        Esta función permite obtener el contexto para renderizar la página.

        @param elementos: Lista de elementos a mostrar en la página.
        @return: Lista de egresados a mostrar en la página.
        """
        return {
            'egresados': elementos
        }

    def post(self, request):
        """
        Esta función permite crear un egresado en el sistema.
        @param request: HttpRequest, objeto que contiene la información sobre la solicitud web actual.
        @return: HttpResponse, objeto que contiene la respuesta HTTP que se enviará al navegador web que realizó la
        """
        # Se obtienen los datos del formulario
        fecha_nacimiento = request.POST.get('fecha_nacimiento')
        if fecha_nacimiento == '' or fecha_nacimiento == ' ':
            fecha_nacimiento = None
        nivel_educativo = request.POST.get('nivel_educativo')
        if nivel_educativo == '' or nivel_educativo == ' ':
            nivel_educativo = None
        salario = request.POST.get('salario')
        if salario == '' or salario == ' ':
            salario = None
        experiencia_meses = request.POST.get('experiencia_meses')
        if experiencia_meses == '' or experiencia_meses == ' ':
            experiencia_meses = None
        ciudad = request.POST.get('ciudad')
        if ciudad == '' or ciudad == ' ':
            ciudad = None

        try:
            # Se crea el egresado
            egresado = Egresado()
            egresado.crear(fecha_nacimiento=fecha_nacimiento, nivel_educativo=nivel_educativo, salario=salario,
                           experiencia_meses=experiencia_meses, ciudad=ciudad)
            messages.success(request, 'Egresado creado correctamente')
        except IntegrityError as e:
            messages.error(request, e)
        finally:
            return redirect('egresados')


@method_decorator(login_required, name='dispatch')
class EgresadosEliminarView(ObjetosEliminarView):
    def post(self, request, egresado_id):
        """
        Esta función permite eliminar un egresado del sistema.
        @param request: HttpRequest, objeto que contiene la información sobre la solicitud web actual.
        @param egresado_id: Int, identificador del egresado a eliminar.
        @return: HttpResponse, objeto que contiene la respuesta HTTP que se enviará al navegador web que realizó la
        """

        # Se obtiene el egresado a eliminar
        egresado = Egresado.objects.get(id=egresado_id)
        # Se elimina el egresado
        egresado.eliminar()

        messages.success(request, 'Egresado eliminado correctamente')
        return redirect('egresados')


@method_decorator(login_required, name='dispatch')
class EgresadosEditarView(ObjetosEditarView):
    def post(self, request, egresado_id):
        """
        Esta función permite editar un egresado del sistema.
        @param request: HttpRequest, objeto que contiene la información sobre la solicitud web actual.
        @param egresado_id: Int, identificador del egresado a editar.
        @return: HttpResponse, objeto que contiene la respuesta HTTP que se enviará al navegador web que realizó la
        """

        # Se obtiene el egresado a editar
        egresado = Egresado.objects.get(id=egresado_id)

        # Se obtienen los datos del formulario
        fecha_nacimiento = request.POST.get('fecha_nacimiento')
        if fecha_nacimiento == '' or fecha_nacimiento == ' ':
            fecha_nacimiento = None
        nivel_educativo = request.POST.get('nivel_educativo')
        if nivel_educativo == '' or nivel_educativo == ' ':
            nivel_educativo = None
        salario = request.POST.get('salario')
        if salario == '' or salario == ' ':
            salario = None
        experiencia_meses = request.POST.get('experiencia_meses')
        if experiencia_meses == '' or experiencia_meses == ' ':
            experiencia_meses = None
        ciudad = request.POST.get('ciudad')
        if ciudad == '' or ciudad == ' ':
            ciudad = None

        try:
            # Se actualiza el egresado
            egresado.actualizar(fecha_nacimiento=fecha_nacimiento, nivel_educativo=nivel_educativo, salario=salario,
                                experiencia_meses=experiencia_meses, ciudad=ciudad)
            messages.success(request, 'Egresado actualizado correctamente')
        except IntegrityError as e:
            messages.error(request, e)
        finally:
            return redirect('egresados')


@method_decorator(login_required, name='dispatch')
class EstudiosView(ObjetosView):
    template_name = 'estudios.html'

    def obtener_objetos(self):
        """
        Esta función permite obtener los estudios a mostrar en la página.
        """
        return Estudio.objects.all()[:1000]

    def obtener_contexto(self, elementos):
        """
        Esta función permite obtener el contexto para renderizar la página.

        @param elementos: Lista de elementos a mostrar en la página.
        @return: Lista de estudios a mostrar en la página.
        """
        return {
            'estudios': elementos
        }

    def post(self, request):
        """
        Esta función permite crear un estudio en el sistema.
        @param request: HttpRequest, objeto que contiene la información sobre la solicitud web actual.
        @return: HttpResponse, objeto que contiene la respuesta HTTP que se enviará al navegador web que realizó la
        """
        # Se obtienen los datos del formulario
        titulo = request.POST.get('titulo')
        if titulo == '' or titulo == ' ':
            titulo = None
        institucion = request.POST.get('institucion')
        if institucion == '' or institucion == ' ':
            institucion = None
        fecha_inicio = request.POST.get('fecha_inicio')
        if fecha_inicio == '' or fecha_inicio == ' ':
            fecha_inicio = None
        fecha_fin = request.POST.get('fecha_fin')
        if fecha_fin == '' or fecha_fin == ' ':
            fecha_fin = None
        egresado = request.POST.get('egresado')
        egresado = Egresado.objects.get(id=egresado)

        try:
            # Se crea el estudio
            estudio = Estudio()
            estudio.crear(titulo=titulo, institucion=institucion, fecha_inicio=fecha_inicio,
                          fecha_fin=fecha_fin, egresado=egresado)
            messages.success(request, 'Estudio creado correctamente')
        except IntegrityError as e:
            messages.error(request, e)
        finally:
            return redirect('estudios')


@method_decorator(login_required, name='dispatch')
class EstudiosEliminarView(ObjetosEliminarView):
    def post(self, request, estudio_id):
        """
        Esta función permite eliminar un estudio del sistema.
        @param request: HttpRequest, objeto que contiene la información sobre la solicitud web actual.
        @param estudio_id: Int, identificador del estudio a eliminar.
        @return: HttpResponse, objeto que contiene la respuesta HTTP que se enviará al navegador web que realizó la
        """

        # Se obtiene el estudio a eliminar
        estudio = Estudio.objects.get(id=estudio_id)
        # Se elimina el estudio
        estudio.eliminar()

        messages.success(request, 'Estudio eliminado correctamente')
        return redirect('estudios')


@method_decorator(login_required, name='dispatch')
class EstudiosEditarView(ObjetosEditarView):
    def post(self, request, estudio_id):
        """
        Esta función permite editar un estudio del sistema.
        @param request: HttpRequest, objeto que contiene la información sobre la solicitud web actual.
        @param estudio_id: Int, identificador del estudio a editar.
        @return: HttpResponse, objeto que contiene la respuesta HTTP que se enviará al navegador web que realizó la
        """

        # Se obtiene el estudio a editar
        estudio = Estudio.objects.get(id=estudio_id)

        # Se obtienen los datos del formulario
        titulo = request.POST.get('titulo')
        if titulo == '' or titulo == ' ':
            titulo = None
        institucion = request.POST.get('institucion')
        if institucion == '' or institucion == ' ':
            institucion = None
        fecha_inicio = request.POST.get('fecha_inicio')
        if fecha_inicio == '' or fecha_inicio == ' ':
            fecha_inicio = None
        fecha_fin = request.POST.get('fecha_fin')
        if fecha_fin == '' or fecha_fin == ' ':
            fecha_fin = None
        egresado = request.POST.get('egresado')
        egresado = Egresado.objects.get(id=egresado)

        try:
            # Se actualiza el estudio
            estudio.actualizar(titulo=titulo, institucion=institucion, fecha_inicio=fecha_inicio,
                               fecha_fin=fecha_fin, egresado=egresado)
            messages.success(request, 'Estudio actualizado correctamente')
        except IntegrityError as e:
            messages.error(request, e)
        finally:
            return redirect('estudios')


@method_decorator(login_required, name='dispatch')
class ExperienciasView(ObjetosView):
    template_name = 'experiencias.html'

    def obtener_objetos(self):
        """
        Esta función permite obtener las experiencias a mostrar en la página.
        """
        return Experiencia.objects.all()[:1000]

    def obtener_contexto(self, elementos):
        """
        Esta función permite obtener el contexto para renderizar la página.

        @param elementos: Lista de elementos a mostrar en la página.
        @return: Lista de experiencias a mostrar en la página.
        """
        return {
            'experiencias': elementos
        }

    def post(self, request):
        """
        Esta función permite crear una experiencia en el sistema.
        @param request: HttpRequest, objeto que contiene la información sobre la solicitud web actual.
        @return: HttpResponse, objeto que contiene la respuesta HTTP que se enviará al navegador web que realizó la
        """
        # Se obtienen los datos del formulario
        empresa = request.POST.get('empresa')
        if empresa == '' or empresa == ' ':
            empresa = None
        cargo = request.POST.get('cargo')
        if cargo == '' or cargo == ' ':
            cargo = None
        fecha_inicio = request.POST.get('fecha_inicio')
        if fecha_inicio == '' or fecha_inicio == ' ':
            fecha_inicio = None
        fecha_fin = request.POST.get('fecha_fin')
        if fecha_fin == '' or fecha_fin == ' ':
            fecha_fin = None
        egresado = request.POST.get('egresado')
        egresado = Egresado.objects.get(id=egresado)

        try:
            # Se crea la experiencia
            experiencia = Experiencia()
            experiencia.crear(empresa=empresa, cargo=cargo, fecha_inicio=fecha_inicio,
                              fecha_fin=fecha_fin, egresado=egresado)
            messages.success(request, 'Experiencia creada correctamente')
        except IntegrityError as e:
            messages.error(request, e)
        finally:
            return redirect('experiencias')


@method_decorator(login_required, name='dispatch')
class ExperienciasEliminarView(ObjetosEliminarView):
    def post(self, request, experiencia_id):
        """
        Esta función permite eliminar una experiencia del sistema.
        @param request: HttpRequest, objeto que contiene la información sobre la solicitud web actual.
        @param experiencia_id: Int, identificador de la experiencia a eliminar.
        @return: HttpResponse, objeto que contiene la respuesta HTTP que se enviará al navegador web que realizó la
        """

        # Se obtiene la experiencia a eliminar
        experiencia = Experiencia.objects.get(id=experiencia_id)
        # Se elimina la experiencia
        experiencia.eliminar()

        messages.success(request, 'Experiencia eliminada correctamente')
        return redirect('experiencias')


@method_decorator(login_required, name='dispatch')
class ExperienciasEditarView(ObjetosEditarView):
    def post(self, request, experiencia_id):
        """
        Esta función permite editar una experiencia del sistema.
        @param request: HttpRequest, objeto que contiene la información sobre la solicitud web actual.
        @param experiencia_id: Int, identificador de la experiencia a editar.
        @return: HttpResponse, objeto que contiene la respuesta HTTP que se enviará al navegador web que realizó la
        """

        # Se obtiene la experiencia a editar
        experiencia = Experiencia.objects.get(id=experiencia_id)

        # Se obtienen los datos del formulario
        empresa = request.POST.get('empresa')
        if empresa == '' or empresa == ' ':
            empresa = None
        cargo = request.POST.get('cargo')
        if cargo == '' or cargo == ' ':
            cargo = None
        fecha_inicio = request.POST.get('fecha_inicio')
        if fecha_inicio == '' or fecha_inicio == ' ':
            fecha_inicio = None
        fecha_fin = request.POST.get('fecha_fin')
        if fecha_fin == '' or fecha_fin == ' ':
            fecha_fin = None
        egresado = request.POST.get('egresado')
        egresado = Egresado.objects.get(id=egresado)

        try:
            # Se actualiza la experiencia
            experiencia.actualizar(empresa=empresa, cargo=cargo, fecha_inicio=fecha_inicio,
                                   fecha_fin=fecha_fin, egresado=egresado)
            messages.success(request, 'Experiencia actualizada correctamente')
        except IntegrityError as e:
            messages.error(request, e)
        finally:
            return redirect('experiencias')


@method_decorator(login_required, name='dispatch')
class SectoresView(ObjetosView):
    template_name = 'sectores.html'

    def obtener_objetos(self):
        """
        Esta función permite obtener los sectores a mostrar en la página.
        """
        return Sector.objects.all()[:1000]

    def obtener_contexto(self, elementos):
        """
        Esta función permite obtener el contexto para renderizar la página.

        @param elementos: Lista de elementos a mostrar en la página.
        @return: Lista de sectores a mostrar en la página.
        """
        return {
            'sectores': elementos
        }

    def post(self, request):
        """
        Esta función permite crear un sector en el sistema.
        @param request: HttpRequest, objeto que contiene la información sobre la solicitud web actual.
        @return: HttpResponse, objeto que contiene la respuesta HTTP que se enviará al navegador web que realizó la
        """
        # Se obtienen los datos del formulario
        nombre = request.POST.get('nombre')
        if nombre == '' or nombre == ' ':
            nombre = None

        try:
            # Se crea el sector
            sector = Sector()
            sector.crear(nombre=nombre)
            messages.success(request, 'Sector creado correctamente')
        except IntegrityError as e:
            messages.error(request, e)
        finally:
            return redirect('sectores')


@method_decorator(login_required, name='dispatch')
class SectoresEliminarView(ObjetosEliminarView):
    def post(self, request, sector_id):
        """
        Esta función permite eliminar un sector del sistema.
        @param request: HttpRequest, objeto que contiene la información sobre la solicitud web actual.
        @param sector_id: Int, identificador del sector a eliminar.
        @return: HttpResponse, objeto que contiene la respuesta HTTP que se enviará al navegador web que realizó la
        """

        # Se obtiene el sector a eliminar
        sector = Sector.objects.get(id=sector_id)
        # Se elimina el sector
        sector.eliminar()

        messages.success(request, 'Sector eliminado correctamente')
        return redirect('sectores')


@method_decorator(login_required, name='dispatch')
class SectoresEditarView(ObjetosEditarView):
    def post(self, request, sector_id):
        """
        Esta función permite editar un sector del sistema.
        @param request: HttpRequest, objeto que contiene la información sobre la solicitud web actual.
        @param sector_id: Int, identificador del sector a editar.
        @return: HttpResponse, objeto que contiene la respuesta HTTP que se enviará al navegador web que realizó la
        """

        # Se obtiene el sector a editar
        sector = Sector.objects.get(id=sector_id)

        # Se obtienen los datos del formulario
        nombre = request.POST.get('nombre')
        if nombre == '' or nombre == ' ':
            nombre = None

        try:
            # Se actualiza el sector
            sector.actualizar(nombre=nombre)
            messages.success(request, 'Sector actualizado correctamente')
        except IntegrityError as e:
            messages.error(request, e)
        finally:
            return redirect('sectores')


@method_decorator(login_required, name='dispatch')
class SectoresEgresadosView(ObjetosView):
    template_name = 'sectores_egresados.html'

    def obtener_objetos(self):
        """
        Esta función permite obtener los sectores de egresados a mostrar en la página.
        """
        return SectoresEgresados.objects.all()[:1000]

    def obtener_contexto(self, elementos):
        """
        Esta función permite obtener el contexto para renderizar la página.

        @param elementos: Lista de elementos a mostrar en la página.
        @return: Lista de sectores de egresados a mostrar en la página.
        """
        return {
            'sectores_egresados': elementos
        }

    def post(self, request):
        """
        Esta función permite crear un sector de egresado en el sistema.
        @param request: HttpRequest, objeto que contiene la información sobre la solicitud web actual.
        @return: HttpResponse, objeto que contiene la respuesta HTTP que se enviará al navegador web que realizó la
        """
        # Se obtienen los datos del formulario
        sector = request.POST.get('sector')
        sector = Sector.objects.get(id=sector)
        egresado = request.POST.get('egresado')
        egresado = Egresado.objects.get(id=egresado)

        try:
            # Se crea el sector de egresado
            sector_egresado = SectoresEgresados()
            sector_egresado.crear(sector=sector, egresado=egresado)
            messages.success(request, 'Sector de egresado creado correctamente')
        except IntegrityError as e:
            messages.error(request, e)
        finally:
            return redirect('sectores_egresados')


@method_decorator(login_required, name='dispatch')
class SectoresEgresadosEliminarView(ObjetosEliminarView):
    def post(self, request, sector_egresado_id):
        """
        Esta función permite eliminar un sector de egresado del sistema.
        @param request: HttpRequest, objeto que contiene la información sobre la solicitud web actual.
        @param sector_egresado_id: Int, identificador del sector de egresado a eliminar.
        @return: HttpResponse, objeto que contiene la respuesta HTTP que se enviará al navegador web que realizó la
        """

        # Se obtiene el sector de egresado a eliminar
        sector_egresado = SectoresEgresados.objects.get(id=sector_egresado_id)
        # Se elimina el sector de egresado
        sector_egresado.eliminar()

        messages.success(request, 'Sector de egresado eliminado correctamente')
        return redirect('sectores_egresados')


@method_decorator(login_required, name='dispatch')
class SectoresEgresadosEditarView(ObjetosEditarView):
    def post(self, request, sector_egresado_id):
        """
        Esta función permite editar un sector de egresado del sistema.
        @param request: HttpRequest, objeto que contiene la información sobre la solicitud web actual.
        @param sector_egresado_id: Int, identificador del sector de egresado a editar.
        @return: HttpResponse, objeto que contiene la respuesta HTTP que se enviará al navegador web que realizó la
        """

        # Se obtiene el sector de egresado a editar
        sector_egresado = SectoresEgresados.objects.get(id=sector_egresado_id)

        # Se obtienen los datos del formulario
        sector = request.POST.get('sector')
        sector = Sector.objects.get(id=sector)
        egresado = request.POST.get('egresado')
        egresado = Egresado.objects.get(id=egresado)

        try:
            # Se actualiza el sector de egresado
            sector_egresado.actualizar(sector=sector, egresado=egresado)
            messages.success(request, 'Sector de egresado actualizado correctamente')
        except IntegrityError as e:
            messages.error(request, e)
        finally:
            return redirect('sectores_egresados')