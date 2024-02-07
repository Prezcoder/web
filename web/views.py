
from django.http import HttpResponse
from django.shortcuts import render
from .models import Game
from django.http import HttpResponseRedirect
from django.http import Http404



def game(request):
	data = Game.objects.all()
	return render(request, 'game/game.html', {'game': data})

def home(request):
	return HttpResponse("Hello, world. You're at the home index.")

def detail(request, id):
	data = Game.objects.get(pk=id)
	return render(request, 'game/detail.html', {'game': data})

def add(request):
	title = request.POST.get('title')
	year = request.POST.get('year')

	if title and year:
		game = Game(title=title, year=year)
		game.save()
		return HttpResponseRedirect('/game/')

	return render(request, 'game/add.html')

def delete(request, id):
	try:
		game = Game.objects.get(pk=id)
	except:
		raise Http404('Game not found')
	game.delete()
	return HttpResponseRedirect('/game/')
	