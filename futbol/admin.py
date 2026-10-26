from django.contrib import admin
from .models import Jugador


@admin.register(Jugador)
class JugadorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'posicion', 'dorsal')
    list_filter = ('posicion',)
    search_fields = ('nombre',)
