from django.shortcuts import render, render_to_response, redirect
from .models import Socio
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request, id):
    socio = Socio.objects.filter(id=id)
    return  render_to_response('sosios/index.html', {'socio': socio})