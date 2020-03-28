from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    s="<button type='button'> <a href = 'http://127.0.0.1:8000/app_search'>App_Searcher</a></button> <br> <br>"  \
      "<button type='button'> <a href = 'http://127.0.0.1:8000/key_finder'>Key Word Finder</a></button>"
    return HttpResponse(s)

def keyword_finder(request):
    return HttpResponse("Hi, Key Word Finder!")