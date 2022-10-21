from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse("Hello zuri team, this is my musicapp from my django project songcrud.")
