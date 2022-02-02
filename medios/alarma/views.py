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