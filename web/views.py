
from django.http import HttpResponse

def game(request):
	return HttpResponse("Hello, world. You're at the game index.")

def home(request):
	return HttpResponse("Hello, world. You're at the home index.")

//test