from django.contrib import admin
from django.urls import path
from . import views


#con el nombre de la url podemos acceder a ella sin meter toda la ruta, es decir, name='templateName'

urlpatterns = [
    path('<int:id>', views.todo, name='todos'),
    path('all/', views.get_all, name='all')
]
