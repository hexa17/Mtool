from django.shortcuts import render
from django.http import HttpResponse
from .ahrefs import AhrefsData

# Create your views here.

def index(request):
    return HttpResponse(AhrefsData.get_ahrefs_backlinks())