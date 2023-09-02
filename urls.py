from django.urls import path
from . import views

#URL CONF
urlpatterns =[
	path('hello/', views.affichage),
	path('acceuil/', views.accueil, name='accueil'),
    path('projets/', views.projets, name='projets'),
    path('qui_sommes_nous/', views.qui_sommes_nous, name='qui_sommes_nous'),

]