#from django.shortcuts import render
from django.http import	HttpResponse,JsonResponse

# Create your views here.


def myfirstview(request):
	data = {
	'name':'HelloWorld'
	}
	return JsonResponse(data)