from django.shortcuts import render
from django.views.generic import ListView


def HomeView(request):
	"""Index"""
	return render(request, 'index.html')