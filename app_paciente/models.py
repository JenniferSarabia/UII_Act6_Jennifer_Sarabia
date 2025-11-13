from django.db import models

# ==========================================
# MODELO: PACIENTE
# ==========================================
class Paciente(models.Model):
    nom_pac = models.CharField(max_length=100)
    ape_pac = models.CharField(max_length=100)
    edad_pac = models.PositiveIntegerField()
    genero_pac = models.CharField(max_length=20)
    tel_pac = models.CharField(max_length=15)
    correo_pac = models.EmailField(max_length=80, unique=True)
    direccion_pac = models.CharField(max_length=120)
    fecha_reg_pac = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nom_pac} {self.ape_pac}"

# ==========================================
# MODELO: TERAPEUTA
# ==========================================
class Terapeuta(models.Model):
    nom_tep = models.CharField(max_length=100)
    ape_tep = models.CharField(max_length=100)
    especialidad_tep = models.CharField(max_length=100, choices=[
        ('Física', 'Física'),
        ('Psicológica', 'Psicológica'),
        ('Ocupacional', 'Ocupacional'),
        ('Lenguaje', 'Lenguaje'),
        ('Otra', 'Otra'),
    ])
    tel_tep = models.CharField(max_length=15)
    correo_tep = models.EmailField(max_length=80, unique=True)
    horario_tep = models.CharField(max_length=50, default='Lunes a Viernes')
    experiencia_tep = models.PositiveIntegerField(help_text="Años de experiencia")

    def __str__(self):
        return f"{self.nom_tep} {self.ape_tep} - {self.especialidad_tep}"

# ==========================================
# MODELO: TERAPIA
# ==========================================
class Terapia(models.Model):
    nom_ter = models.CharField(max_length=100)
    desc_ter = models.TextField(blank=True, null=True)
    duracion_ter = models.PositiveIntegerField(help_text="Duración en minutos")
    costo_ter = models.DecimalField(max_digits=8, decimal_places=2)
    frecuencia_ter = models.CharField(max_length=50)
    nivel_ter = models.CharField(max_length=50, choices=[
        ('Física', 'Física'),
        ('Psicológica', 'Psicológica'),
        ('Ocupacional', 'Ocupacional'),
        ('Lenguaje', 'Lenguaje'),
    ])
    fecha_inicio = models.DateField()
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name="terapias")
    terapeutas = models.ManyToManyField(Terapeuta, related_name="terapias")

    def __str__(self):
        return self.nom_ter

# --------------------------
# MODELO: CITA
# --------------------------
class Cita(models.Model):
    fecha = models.DateField()
    hora = models.TimeField()
    motivo = models.CharField(max_length=200)
    estado = models.CharField(max_length=50, choices=[
        ('pendiente', 'Pendiente'),
        ('confirmada', 'Confirmada'),
        ('cancelada', 'Cancelada'),
        ('finalizada', 'Finalizada'),
    ])
    paciente = models.ForeignKey('Paciente', on_delete=models.CASCADE)
    terapeuta = models.ForeignKey('Terapeuta', on_delete=models.CASCADE)

    def __str__(self):
        return f"Cita de {self.paciente} con {self.terapeuta} el {self.fecha}"


# --------------------------
# MODELO: PAGO
# --------------------------
class Pago(models.Model):
    fecha_pago = models.DateField()
    monto = models.DecimalField(max_digits=8, decimal_places=2)
    metodo_pago = models.CharField(max_length=50, choices=[
        ('efectivo', 'Efectivo'),
        ('tarjeta', 'Tarjeta'),
        ('transferencia', 'Transferencia'),
    ])
    estado = models.CharField(max_length=50, choices=[
        ('pendiente', 'Pendiente'),
        ('pagado', 'Pagado'),
        ('cancelado', 'Cancelado'),
    ])
    cita = models.ForeignKey('Cita', on_delete=models.CASCADE, related_name='pagos')

    def __str__(self):
        return f"Pago de ${self.monto} - {self.cita.paciente.nom_pac}"

    class Meta:
        verbose_name = "Pago"
        verbose_name_plural = "Pagos"

