from django.db import IntegrityError
from django.shortcuts import render, redirect
from .models import Egresado, Estudio, Experiencia, Sector, SectoresEgresados
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required
def egresados(request):
    """
    Esta función permite listar los egresados en el sistema. También permite crear, actualizar y eliminar egresados con
    formularios que redirigen a la página con la acción correspondiente.
    @param request: HttpRequest, objeto que contiene la información sobre la solicitud web actual.
    @return: HttpResponse, objeto que contiene la respuesta HTTP que se enviará al navegador web que realizó la
    """
    # Si el usuario es un usuario normal, se redirige a la página de inicio
    if request.user.user_type == 'user':
        return redirect('inicio')
    if request.method == 'GET':
        # Se obtienen los egresados del sistema
        egresados_objects = Egresado.objects.all()[:1000]
        # Renderiza la página de egresados con los egresados obtenidos
        return render(request, 'egresados.html', {
            'egresados': egresados_objects
        })
    elif request.method == 'POST':
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
            egresado.crear_egresado(fecha_nacimiento, nivel_educativo, salario, experiencia_meses, ciudad)
            messages.success(request, 'Egresado creado correctamente')
        except IntegrityError as e:
            messages.error(request, e)
        finally:
            return redirect('egresados')


@login_required
def eliminar_egresado(request, egresado_id):
    """
    Esta función permite eliminar un egresado del sistema.
    @param request: HttpRequest, objeto que contiene la información sobre la solicitud web actual.
    @param egresado_id: Int, identificador del egresado a eliminar.
    @return: HttpResponse, objeto que contiene la respuesta HTTP que se enviará al navegador web que realizó la
    """
    if request.user.user_type == 'user':
        return redirect('inicio')
    if request.method != 'POST':
        return redirect('egresados')

    # Se obtiene el egresado a eliminar
    egresado = Egresado.objects.get(id=egresado_id)
    # Se elimina el egresado
    egresado.eliminar_egresado()

    messages.success(request, 'Egresado eliminado correctamente')
    return redirect('egresados')


@login_required
def editar_egresado(request, egresado_id):
    """
    Esta función permite editar un egresado del sistema.
    @param request: HttpRequest, objeto que contiene la información sobre la solicitud web actual.
    @param egresado_id: Int, identificador del egresado a editar.
    @return: HttpResponse, objeto que contiene la respuesta HTTP que se enviará al navegador web que realizó la
    """
    if request.user.user_type == 'user':
        return redirect('inicio')
    if request.method != 'POST':
        return redirect('egresados')

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
        egresado.actualizar_egresado(fecha_nacimiento, nivel_educativo, salario, experiencia_meses, ciudad)
        messages.success(request, 'Egresado actualizado correctamente')
    except IntegrityError as e:
        messages.error(request, e)
    finally:
        return redirect('egresados')


@login_required
def estudios(request):
    """
    Esta función permite listar los estudios en el sistema. También permite crear, actualizar y eliminar estudios con
    formularios que redirigen a la página con la acción correspondiente.
    @return: HttpResponse, objeto que contiene la respuesta HTTP que se enviará al navegador web que realizó la
    """
    # Si el usuario es un usuario normal, se redirige a la página de inicio
    if request.user.user_type == 'user':
        return redirect('inicio')
    if request.method == 'GET':
        # Se obtienen los estudios del sistema
        estudios_objects = Estudio.objects.all()[:1000]
        # Renderiza la página de estudios con los estudios obtenidos
        return render(request, 'estudios.html', {
            'estudios': estudios_objects
        })
    elif request.method == 'POST':
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
            estudio = Estudio()
            estudio.crear_estudio(titulo=titulo, institucion=institucion, fecha_inicio=fecha_inicio,
                                  fecha_fin=fecha_fin, egresado=egresado)
            messages.success(request, 'Estudio creado correctamente')
        except IntegrityError as e:
            messages.error(request, e)
        finally:
            return redirect('estudios')


@login_required
def eliminar_estudio(request, estudio_id):
    """
    Esta función permite eliminar un estudio del sistema.
    @param request: HttpRequest, objeto que contiene la información sobre la solicitud web actual.
    @param estudio_id: Int, identificador del estudio a eliminar.
    @return: HttpResponse, objeto que contiene la respuesta HTTP que se enviará al navegador web que realizó la
    """
    if request.user.user_type == 'user':
        return redirect('inicio')
    if request.method != 'POST':
        return redirect('estudios')

    # Se obtiene el estudio a eliminar
    estudio = Estudio.objects.get(id=estudio_id)
    # Se elimina el estudio
    estudio.eliminar_estudio()

    messages.success(request, 'Estudio eliminado correctamente')
    return redirect('estudios')


@login_required
def editar_estudio(request, estudio_id):
    """
    Esta función permite editar un estudio del sistema.
    @param request: HttpRequest, objeto que contiene la información sobre la solicitud web actual.
    @param estudio_id: int, identificador del estudio a editar.
    @return: HttpResponse, objeto que contiene la respuesta HTTP que se enviará al navegador web que realizó la
    """
    if request.user.user_type == 'user':
        return redirect('inicio')
    if request.method != 'POST':
        return redirect('estudios')

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
        estudio.actualizar_estudio(titulo=titulo, institucion=institucion, fecha_inicio=fecha_inicio,
                                   fecha_fin=fecha_fin, egresado=egresado)
        messages.success(request, 'Estudio actualizado correctamente')
    except IntegrityError as e:
        messages.error(request, e)
    finally:
        return redirect('estudios')


@login_required
def experiencias(request):
    """
    Esta función permite listar las experiencias en el sistema. También permite crear, actualizar y eliminar
    experiencias con formularios que redirigen a la página con la acción correspondiente.
    @return: HttpResponse, objeto que contiene la respuesta HTTP que se enviará al navegador web que realizó la
    """
    # Si el usuario es un usuario normal, se redirige a la página de inicio
    if request.user.user_type == 'user':
        return redirect('inicio')
    if request.method == 'GET':
        # Se obtienen las experiencias del sistema
        experiencias_objects = Experiencia.objects.all()[:1000]
        # Renderiza la página de experiencias con las experiencias obtenidas
        return render(request, 'experiencias.html', {
            'experiencias': experiencias_objects
        })
    elif request.method == 'POST':
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
            experiencia.crear_experiencia(empresa=empresa, cargo=cargo, fecha_inicio=fecha_inicio,
                                          fecha_fin=fecha_fin, egresado=egresado)
            messages.success(request, 'Experiencia creada correctamente')
        except IntegrityError as e:
            messages.error(request, e)
        finally:
            return redirect('experiencias')


@login_required
def eliminar_experiencia(request, experiencia_id):
    """
    Esta función permite eliminar una experiencia del sistema.
    @param request: HttpRequest, objeto que contiene la información sobre la solicitud web actual.
    @param experiencia_id: Int, identificador de la experiencia a eliminar.
    @return: HttpResponse, objeto que contiene la respuesta HTTP que se enviará al navegador web que realizó la
    """
    if request.user.user_type == 'user':
        return redirect('inicio')
    if request.method != 'POST':
        return redirect('experiencias')

    # Se obtiene la experiencia a eliminar
    experiencia = Experiencia.objects.get(id=experiencia_id)
    # Se elimina la experiencia
    experiencia.eliminar_experiencia()

    messages.success(request, 'Experiencia eliminada correctamente')
    return redirect('experiencias')


@login_required
def editar_experiencia(request, experiencia_id):
    """
    Esta función permite editar una experiencia del sistema.
    @param request: HttpRequest, objeto que contiene la información sobre la solicitud web actual.
    @param experiencia_id: Int, identificador de la experiencia a editar.
    @return: HttpResponse, objeto que contiene la respuesta HTTP que se enviará al navegador web que realizó la
    """
    if request.user.user_type == 'user':
        return redirect('inicio')
    if request.method != 'POST':
        return redirect('experiencias')

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
        experiencia.actualizar_experiencia(empresa=empresa, cargo=cargo, fecha_inicio=fecha_inicio,
                                           fecha_fin=fecha_fin, egresado=egresado)
        messages.success(request, 'Experiencia actualizada correctamente')
    except IntegrityError as e:
        messages.error(request, e)
    finally:
        return redirect('experiencias')


@login_required
def sectores(request):
    """
    Esta función permite listar los sectores en el sistema. También permite crear, actualizar y eliminar sectores con
    formularios que redirigen a la página con la acción correspondiente.
    @return: HttpResponse, objeto que contiene la respuesta HTTP que se enviará al navegador web que realizó la
    """
    # Si el usuario es un usuario normal, se redirige a la página de inicio
    if request.user.user_type == 'user':
        return redirect('inicio')
    if request.method == 'GET':
        # Se obtienen los sectores del sistema
        sectores_objects = Sector.objects.all()[:1000]
        # Renderiza la página de sectores con los sectores obtenidos
        return render(request, 'sectores.html', {
            'sectores': sectores_objects
        })
    elif request.method == 'POST':
        # Se obtienen los datos del formulario
        nombre = request.POST.get('nombre')
        if nombre == '' or nombre == ' ':
            nombre = None

        try:
            # Se crea el sector
            sector = Sector()
            sector.crear_sector(nombre=nombre)
            messages.success(request, 'Sector creado correctamente')
        except IntegrityError as e:
            messages.error(request, e)
        finally:
            return redirect('sectores')


@login_required
def eliminar_sector(request, sector_id):
    """
    Esta función permite eliminar un sector del sistema.
    @param request: HttpRequest, objeto que contiene la información sobre la solicitud web actual.
    @param sector_id: Int, identificador del sector a eliminar.
    @return: HttpResponse, objeto que contiene la respuesta HTTP que se enviará al navegador web que realizó la
    """
    if request.user.user_type == 'user':
        return redirect('inicio')
    if request.method != 'POST':
        return redirect('sectores')

    # Se obtiene el sector a eliminar
    sector = Sector.objects.get(id=sector_id)
    # Se elimina el sector
    sector.eliminar_sector()

    messages.success(request, 'Sector eliminado correctamente')
    return redirect('sectores')


@login_required
def editar_sector(request, sector_id):
    """
    Esta función permite editar un sector del sistema.
    @param request: HttpRequest, objeto que contiene la información sobre la solicitud web actual.
    @param sector_id: Int, identificador del sector a editar.
    @return: HttpResponse, objeto que contiene la respuesta HTTP que se enviará al navegador web que realizó la
    """
    if request.user.user_type == 'user':
        return redirect('inicio')
    if request.method != 'POST':
        return redirect('sectores')

    # Se obtiene el sector a editar
    sector = Sector.objects.get(id=sector_id)

    # Se obtienen los datos del formulario
    nombre = request.POST.get('nombre')
    if nombre == '' or nombre == ' ':
        nombre = None

    try:
        # Se actualiza el sector
        sector.actualizar_sector(nombre=nombre)
        messages.success(request, 'Sector actualizado correctamente')
    except IntegrityError as e:
        messages.error(request, e)
    finally:
        return redirect('sectores')


@login_required
def sectores_egresados(request):
    """
    Esta función permite listar los sectores de egresados en el sistema. También permite crear, actualizar y eliminar sectores de egresados con
    formularios que redirigen a la página con la acción correspondiente.
    @return: HttpResponse, objeto que contiene la respuesta HTTP que se enviará al navegador web que realizó la
    """
    # Si el usuario es un usuario normal, se redirige a la página de inicio
    if request.user.user_type == 'user':
        return redirect('inicio')
    if request.method == 'GET':
        # Se obtienen los sectores de egresados del sistema
        sectores_egresados_objects = SectoresEgresados.objects.all()[:1000]
        # Renderiza la página de sectores de egresados con los sectores de egresados obtenidos
        return render(request, 'sectores_egresados.html', {
            'sectores_egresados': sectores_egresados_objects
        })
    elif request.method == 'POST':
        # Se obtienen los datos del formulario
        sector = request.POST.get('sector')
        sector = Sector.objects.get(id=sector)
        egresado = request.POST.get('egresado')
        egresado = Egresado.objects.get(id=egresado)

        try:
            # Se crea el sector de egresado
            sector_egresado = SectoresEgresados()
            sector_egresado.crear_sectores_egresados(sector=sector, egresado=egresado)
            messages.success(request, 'Sector de egresado creado correctamente')
        except IntegrityError as e:
            messages.error(request, e)
        finally:
            return redirect('sectores_egresados')


@login_required
def eliminar_sector_egresado(request, sector_egresado_id):
    """
    Esta función permite eliminar un sector de egresado del sistema.
    @param request: HttpRequest, objeto que contiene la información sobre la solicitud web actual.
    @param sector_egresado_id: Int, identificador del sector de egresado a eliminar.
    @return: HttpResponse, objeto que contiene la respuesta HTTP que se enviará al navegador web que realizó la
    """
    if request.user.user_type == 'user':
        return redirect('inicio')
    if request.method != 'POST':
        return redirect('sectores_egresados')

    # Se obtiene el sector de egresado a eliminar
    sector_egresado = SectoresEgresados.objects.get(id=sector_egresado_id)
    # Se elimina el sector de egresado
    sector_egresado.eliminar_sectores_egresados()

    messages.success(request, 'Sector de egresado eliminado correctamente')
    return redirect('sectores_egresados')


@login_required
def editar_sector_egresado(request, sector_egresado_id):
    """
    Esta función permite editar un sector de egresado del sistema.
    @param request: HttpRequest, objeto que contiene la información sobre la solicitud web actual.
    @param sector_egresado_id: Int, identificador del sector de egresado a editar.
    @return: HttpResponse, objeto que contiene la respuesta HTTP que se enviará al navegador web que realizó la
    """
    if request.user.user_type == 'user':
        return redirect('inicio')
    if request.method != 'POST':
        return redirect('sectores_egresados')

    # Se obtiene el sector de egresado a editar
    sector_egresado = SectoresEgresados.objects.get(id=sector_egresado_id)

    # Se obtienen los datos del formulario
    sector = request.POST.get('sector')
    sector = Sector.objects.get(id=sector)
    egresado = request.POST.get('egresado')
    egresado = Egresado.objects.get(id=egresado)

    try:
        # Se actualiza el sector de egresado
        sector_egresado.actualizar_sectores_egresados(sector=sector, egresado=egresado)
        messages.success(request, 'Sector de egresado actualizado correctamente')
    except IntegrityError as e:
        messages.error(request, e)
    finally:
        return redirect('sectores_egresados')