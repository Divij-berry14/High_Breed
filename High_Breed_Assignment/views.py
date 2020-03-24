from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    s="<button type='button'> <a href = 'http://127.0.0.1:8000/apsearch'>App_Searcher</a></button>"
    return HttpResponse(s)

def App_searcher(request):
    return HttpResponse("Hi, App Searcher!")