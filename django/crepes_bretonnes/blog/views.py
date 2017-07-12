from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
# Create your views here.
def home(request: HttpRequest) -> HttpResponse:
    text = """<h1>Bienvenue sur le blog !</h1>
              <p> Les crêpes bretonnes ça tue des mouettes en plein vole ! </p>"""
    return HttpResponse(text)