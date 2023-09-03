from django.shortcuts import render

# Create your views here.

def affichage(request):
	return render(request, 'index.html')

def accueil(request):
    return render(request, 'accueil.html')

def projets(request):
    return render(request, 'projets.html')

def qui_sommes_nous(request):
    return render(request, 'qui_sommes_nous.html')
