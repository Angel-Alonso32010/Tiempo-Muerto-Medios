from multiprocessing import context
from django import template
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader



def vista1(request):
    template=loader.get_template('v1a1.html')
    suma = 56+56
    context ={
        'vista': 'vista1',
        'app': 'aplicacion 1',
        'suma': suma,
    }
   
    return HttpResponse(template.render(context,request))


def aluminio(request):
    template=loader.get_template('aluminio.html')
    context={
        
    }
    
    return HttpResponse(template.render(context,request))

def dt (request):
    return render (request, 'templates/dt.html', {})

def Empalme (request):
    return render (request, 'templates/Empalme.html', {})


def logout (request):
    return render (request, 'templates/logout', {})

def PrensaManual (request):
    return render (request, 'templates/PrensaManual.html', {})

def Principal (request):
    return render (request, 'templates/principal.html', {})

def welding (request):
    return render (request, 'templates/welding.html', {})

def wl (request):
    return render (request, 'templates/wl.html', {})

def coax (request):
    return render (request, 'templates/coaxial.html', {})

def prepCoaxial (request):
    return render (request, 'templates/prepCoaxial.html', {})

def kawa (request):
    return render (request, 'templates/kawa.html', {})

