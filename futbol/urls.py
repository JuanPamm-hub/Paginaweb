from django.urls import path
from .views import lista_jugadores

app_name = 'futbol'

urlpatterns = [
    path('', lista_jugadores, name='home'),
]
