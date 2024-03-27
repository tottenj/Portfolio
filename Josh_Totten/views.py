from django.shortcuts import render
from django.http import HttpResponse
from markdown2 import Markdown
from django import forms

# Create your views here.
def index(request):
    return render(request, "index.html")

def aboutMe(request):
    return render(request, "aboutMe.html")

def projects(request):
    return render(request, "projects.html")

def contact(request):
    return render(request, "contact.html")