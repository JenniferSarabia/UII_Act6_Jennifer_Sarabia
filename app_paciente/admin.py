from django.contrib import admin
from .models import Paciente, Terapeuta, Terapia

# Personalizar la visualización de los modelos en el admin

@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom_pac', 'ape_pac', 'edad_pac', 'genero_pac', 'tel_pac', 'correo_pac', 'fecha_reg_pac')
    search_fields = ('nom_pac', 'ape_pac', 'correo_pac')
    list_filter = ('genero_pac',)

@admin.register(Terapeuta)
class TerapeutaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom_tep', 'ape_tep', 'especialidad_tep', 'tel_tep', 'correo_tep', 'experiencia_tep')
    search_fields = ('nom_tep', 'ape_tep', 'especialidad_tep')
    list_filter = ('especialidad_tep',)

@admin.register(Terapia)
class TerapiaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom_ter', 'duracion_ter', 'costo_ter', 'nivel_ter', 'fecha_inicio')
    search_fields = ('nom_ter', 'nivel_ter')
    list_filter = ('nivel_ter',)