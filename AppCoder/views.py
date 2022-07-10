from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.models import Curso

def curso (self):
    curso=Curso( nombre = "Django" ,  comision=939393)
    curso.save()
    texto=f"Curso creado :  {curso.nombre} {curso.comision} "
    return HttpResponse(texto)


