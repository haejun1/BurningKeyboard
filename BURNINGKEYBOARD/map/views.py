from django.shortcuts import render, redirect, get_object_or_404
from .models import *

# Create your views here.
def index(request):
    return render(request, 'map/index.html')