from django.shortcuts import render
from django.http import HttpResponse

def app_searcher(request):
    return render(request,'App_Searcher/form.html')
