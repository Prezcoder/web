
from django.http import HttpResponse
from django.shortcuts import render

data = {
	'game': [
		{
			'id': 5,
			'title': 'Pong',
			'year': 2024
		},
		{
			'id': 6,
			'title': 'Ping',
			'year': 2025
		},
		{
			'id': 7,
			'title': 'Pouf',
			'year': 2026
		}

	]

}

def game(request):
	return render(request, 'game/game.html', data)

def home(request):
	return HttpResponse("Hello, world. You're at the home index.")

