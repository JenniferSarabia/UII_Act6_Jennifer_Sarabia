from django.shortcuts import render, redirect, get_object_or_404
from .models import Paciente, Terapeuta, Terapia, Cita, Pago

# Página de inicio
def inicio_live_side(request):
    return render(request, 'inicio.html')

# Agregar paciente
def agregar_paciente(request):
    if request.method == 'POST':
        Paciente.objects.create(
            nom_pac=request.POST.get('nom_pac'),
            ape_pac=request.POST.get('ape_pac'),
            edad_pac=request.POST.get('edad_pac'),
            genero_pac=request.POST.get('genero_pac'),
            tel_pac=request.POST.get('tel_pac'),
            correo_pac=request.POST.get('correo_pac'),
            direccion_pac=request.POST.get('direccion_pac')
        )
        return redirect('ver_pacientes')
    return render(request, 'pacientes/agregar_paciente.html')

# Ver pacientes
def ver_pacientes(request):
    pacientes = Paciente.objects.all()
    return render(request, 'pacientes/ver_pacientes.html', {'pacientes': pacientes})

# Actualizar paciente (mostrar formulario)
def actualizar_paciente(request, id):
    paciente = get_object_or_404(Paciente, pk=id)
    return render(request, 'pacientes/actualizar_paciente.html', {'paciente': paciente})

# Realizar actualización
def realizar_actualizacion_paciente(request, id):
    paciente = get_object_or_404(Paciente, pk=id)
    if request.method == 'POST':
        paciente.nom_pac = request.POST.get('nom_pac')
        paciente.ape_pac = request.POST.get('ape_pac')
        paciente.edad_pac = request.POST.get('edad_pac')
        paciente.genero_pac = request.POST.get('genero_pac')
        paciente.tel_pac = request.POST.get('tel_pac')
        paciente.correo_pac = request.POST.get('correo_pac')
        paciente.direccion_pac = request.POST.get('direccion_pac')
        paciente.save()
        return redirect('ver_pacientes')
    return redirect('ver_pacientes')

# Borrar paciente
def borrar_paciente(request, id):
    paciente = get_object_or_404(Paciente, pk=id)
    if request.method == 'POST':
        paciente.delete()
        return redirect('ver_pacientes')
    return render(request, 'pacientes/borrar_paciente.html', {'paciente': paciente})

# Crear terapeuta
def agregar_terapeuta(request):
    if request.method == 'POST':
        nom = request.POST['nom_tep']
        ape = request.POST['ape_tep']
        esp = request.POST['especialidad_tep']
        tel = request.POST['tel_tep']
        correo = request.POST['correo_tep']
        hor = request.POST['horario_tep']
        exp = request.POST['experiencia_tep']
        Terapeuta.objects.create(
            nom_tep=nom, ape_tep=ape, especialidad_tep=esp,
            tel_tep=tel, correo_tep=correo, horario_tep=hor, experiencia_tep=exp
        )
        return redirect('ver_terapeuta')
    return render(request, 'terapeuta/agregar_terapeuta.html')


# Ver terapeutas
def ver_terapeuta(request):
    terapeutas = Terapeuta.objects.all()
    return render(request, 'terapeuta/ver_terapeuta.html', {'terapeutas': terapeutas})


# Formulario para actualizar terapeuta
def actualizar_terapeuta(request, id):
    terapeuta = get_object_or_404(Terapeuta, id=id)
    return render(request, 'terapeuta/actualizar_terapeuta.html', {'terapeuta': terapeuta})


# Guardar actualización
def realizar_actualizacion_terapeuta(request, id):
    terapeuta = get_object_or_404(Terapeuta, id=id)
    if request.method == 'POST':
        terapeuta.nom_tep = request.POST['nom_tep']
        terapeuta.ape_tep = request.POST['ape_tep']
        terapeuta.especialidad_tep = request.POST['especialidad_tep']
        terapeuta.tel_tep = request.POST['tel_tep']
        terapeuta.correo_tep = request.POST['correo_tep']
        terapeuta.horario_tep = request.POST['horario_tep']
        terapeuta.experiencia_tep = request.POST['experiencia_tep']
        terapeuta.save()
        return redirect('ver_terapeuta')


# Borrar terapeuta
def borrar_terapeuta(request, id):
    terapeuta = get_object_or_404(Terapeuta, id=id)
    if request.method == 'POST':
        terapeuta.delete()
        return redirect('ver_terapeuta')
    return render(request, 'terapeuta/borrar_terapeuta.html', {'terapeuta': terapeuta})

def ver_terapias(request):
    terapias = Terapia.objects.all()
    return render(request, 'terapias/ver_terapias.html', {'terapias': terapias})


def agregar_terapia(request):
    pacientes = Paciente.objects.all()
    terapeutas = Terapeuta.objects.all()
    if request.method == 'POST':
        nom = request.POST.get('nom_ter')
        desc = request.POST.get('desc_ter')
        duracion = request.POST.get('duracion_ter')
        costo = request.POST.get('costo_ter')
        frecuencia = request.POST.get('frecuencia_ter')
        nivel = request.POST.get('nivel_ter')
        fecha = request.POST.get('fecha_inicio')
        paciente_id = request.POST.get('paciente')
        terapeutas_ids = request.POST.getlist('terapeutas')

        terapia = Terapia.objects.create(
            nom_ter=nom,
            desc_ter=desc,
            duracion_ter=duracion,
            costo_ter=costo,
            frecuencia_ter=frecuencia,
            nivel_ter=nivel,
            fecha_inicio=fecha,
            paciente_id=paciente_id
        )
        terapia.terapeutas.set(terapeutas_ids)
        terapia.save()
        return redirect('ver_terapias')

    return render(request, 'terapias/agregar_terapia.html', {
        'pacientes': pacientes,
        'terapeutas': terapeutas
    })


def actualizar_terapia(request, id):
    terapia = get_object_or_404(Terapia, pk=id)
    pacientes = Paciente.objects.all()
    terapeutas = Terapeuta.objects.all()

    if request.method == 'POST':
        terapia.nom_ter = request.POST.get('nom_ter')
        terapia.desc_ter = request.POST.get('desc_ter')
        terapia.duracion_ter = request.POST.get('duracion_ter')
        terapia.costo_ter = request.POST.get('costo_ter')
        terapia.frecuencia_ter = request.POST.get('frecuencia_ter')
        terapia.nivel_ter = request.POST.get('nivel_ter')
        terapia.fecha_inicio = request.POST.get('fecha_inicio')
        terapia.paciente_id = request.POST.get('paciente')
        terapia.save()
        terapeutas_ids = request.POST.getlist('terapeutas')
        terapia.terapeutas.set(terapeutas_ids)
        return redirect('ver_terapias')

    return render(request, 'terapias/actualizar_terapia.html', {
        'terapia': terapia,
        'pacientes': pacientes,
        'terapeutas': terapeutas
    })

def realizar_actualizacion_terapia(request, id):
    terapia = Terapia.objects.get(id=id)
    if request.method == 'POST':
        terapia.nom_ter = request.POST.get('nom_ter')
        terapia.desc_ter = request.POST.get('desc_ter')
        terapia.frecuencia_ter = request.POST.get('frecuencia_ter')
        terapia.nivel_ter = request.POST.get('nivel_ter')
        terapia.fecha_inicio = request.POST.get('fecha_inicio')
        terapia.save()
        return redirect('ver_terapias')


def borrar_terapia(request, id):
    terapia = get_object_or_404(Terapia, pk=id)
    if request.method == 'POST':
        terapia.delete()
        return redirect('ver_terapias')
    return render(request, 'terapias/borrar_terapia.html', {'terapia': terapia})

# --------------------------
# CRUD CITAS
# --------------------------
def ver_citas(request):
    citas = Cita.objects.select_related('paciente', 'terapeuta').all()
    return render(request, 'citas/ver_citas.html', {'citas': citas})

# ➕ Agregar nueva cita
def agregar_cita(request):
    pacientes = Paciente.objects.all()
    terapeutas = Terapeuta.objects.all()

    if request.method == 'POST':
        fecha = request.POST.get('fecha')
        hora = request.POST.get('hora')
        motivo = request.POST.get('motivo')
        estado = request.POST.get('estado')
        paciente_id = request.POST.get('paciente')
        terapeuta_id = request.POST.get('terapeuta')

        # Validar existencia
        paciente = get_object_or_404(Paciente, id=paciente_id)
        terapeuta = get_object_or_404(Terapeuta, id=terapeuta_id)

        # Crear cita
        Cita.objects.create(
            fecha=fecha,
            hora=hora,
            motivo=motivo,
            estado=estado,
            paciente=paciente,
            terapeuta=terapeuta
        )

        return redirect('ver_citas')

    return render(request, 'citas/agregar_cita.html', {
        'pacientes': pacientes,
        'terapeutas': terapeutas
    })

def actualizar_cita(request, id):
    cita = get_object_or_404(Cita, id=id)
    pacientes = Paciente.objects.all()
    terapeutas = Terapeuta.objects.all()

    if request.method == 'POST':
        cita.fecha = request.POST.get('fecha')
        cita.hora = request.POST.get('hora')
        cita.motivo = request.POST.get('motivo')
        cita.estado = request.POST.get('estado')

        paciente_id = request.POST.get('paciente')
        terapeuta_id = request.POST.get('terapeuta')

        cita.paciente = get_object_or_404(Paciente, id=paciente_id)
        cita.terapeuta = get_object_or_404(Terapeuta, id=terapeuta_id)

        cita.save()
        return redirect('ver_citas')

    return render(request, 'citas/actualizar_cita.html', {
        'cita': cita,
        'pacientes': pacientes,
        'terapeutas': terapeutas
    })


def realizar_actualizacion_cita(request, id):
    cita = get_object_or_404(Cita, id=id)
    if request.method == 'POST':
        cita.fecha = request.POST['fecha']
        cita.hora = request.POST['hora']
        cita.paciente = Paciente.objects.get(id=request.POST['paciente'])
        cita.terapia = Terapia.objects.get(id=request.POST['terapia'])
        cita.observaciones = request.POST.get('observaciones', '')
        cita.save()
        return redirect('ver_citas')
    return redirect('ver_citas')


def borrar_cita(request, id):
    cita = get_object_or_404(Cita, id=id)
    if request.method == 'POST':
        cita.delete()
        return redirect('ver_citas')
    return render(request, 'citas/borrar_cita.html', {'cita': cita})




# --------------------------
# CRUD PAGOS
# --------------------------
def ver_pagos(request):
    pagos = Pago.objects.select_related('cita__paciente').all()
    return render(request, 'pagos/ver_pagos.html', {'pagos': pagos})

# Agregar pago
def agregar_pago(request):
    citas = Cita.objects.all()
    if request.method == 'POST':
        fecha_pago = request.POST['fecha_pago']
        monto = request.POST['monto']
        metodo_pago = request.POST['metodo_pago']
        estado = request.POST['estado']
        cita_id = request.POST['cita']

        cita = Cita.objects.get(id=cita_id)
        Pago.objects.create(
            fecha_pago=fecha_pago,
            monto=monto,
            metodo_pago=metodo_pago,
            estado=estado,
            cita=cita
        )
        return redirect('ver_pagos')

    return render(request, 'pagos/agregar_pago.html', {'citas': citas})

# Actualizar pago
def actualizar_pago(request, id):
    pago = get_object_or_404(Pago, id=id)
    citas = Cita.objects.all()
    return render(request, 'pagos/actualizar_pago.html', {'pago': pago, 'citas': citas})

# Guardar actualización
def realizar_actualizacion_pago(request, id):
    pago = get_object_or_404(Pago, id=id)
    if request.method == 'POST':
        pago.fecha_pago = request.POST['fecha_pago']
        pago.monto = request.POST['monto']
        pago.metodo_pago = request.POST['metodo_pago']
        pago.estado = request.POST['estado']
        pago.cita = Cita.objects.get(id=request.POST['cita'])
        pago.save()
        return redirect('ver_pagos')
    return redirect('ver_pagos')

# Borrar pago
def borrar_pago(request, id):
    pago = get_object_or_404(Pago, id=id)
    if request.method == 'POST':
        pago.delete()
        return redirect('ver_pagos')
    return render(request, 'pagos/borrar_pago.html', {'pago': pago})