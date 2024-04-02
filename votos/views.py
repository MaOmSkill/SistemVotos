from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.template.loader import get_template
from django.template.loader import render_to_string
from django.db.models import Count
from datetime import datetime
from django.contrib import messages
import os
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders
from django.db.models import F 
from .models import Resultados, Red_VHF, Criptografia, Red_HF, Mensajero , Mtrr, Codigo_Morse, Radioaficionados
from .forms import ResultadosForm, Red_VhForm, CriptografiaForm, Red_HForm, MensajeroForm, MtrrForm, Codigo_MorseForm, RadioaficionadosForm


def principal(request):
    resultados = Resultados.objects.all().order_by(F('resta').desc())
    cripto = Criptografia.objects.all()
    vhf = Red_VHF.objects.all()
    hf = Red_HF.objects.all()
    mensaje = Mensajero.objects.all()
    mtrr = Mtrr.objects.all()
    morse = Codigo_Morse.objects.all()
    radio = Radioaficionados.objects.all()
    
   

    formularios = {
        'resultados': ResultadosForm(request.POST or None),
        'red_vh': Red_VhForm(request.POST or None),
        'criptografia': CriptografiaForm(request.POST or None),
        'red_h': Red_HForm(request.POST or None),
        'mensajero': MensajeroForm(request.POST or None),
        'mtrr': MtrrForm(request.POST or None),
        'codigo_morse': Codigo_MorseForm(request.POST or None),
        'radioaficionados': RadioaficionadosForm(request.POST or None),
    }

    if request.method == 'POST':
        for form in formularios.values():
            if form.is_valid():
                form.save()
                messages.success(request, 'Se efectuo el Registro de los Datos con Exito')
                return redirect('principal')
        else:
            messages.error(request, 'Faltaron campos por rellenar en el Formulario')
   
    context = {'formularios': formularios, 'resultados':resultados, 'cripto':cripto , 
               'vhf':vhf, 'hf':hf, 'mensaje':mensaje, 'mtrr':mtrr, 'morse':morse, 
               'radio':radio}
    return render(request, 'vistas/index.html', context)


def campeon(request, id):
    titulo = Resultados.objects.filter(id=id)
    vhf = Red_VHF.objects.filter(id=id)
    cripto = Criptografia.objects.filter(id=id)
    hf = Red_HF.objects.filter(id=id)
    mensaje = Mensajero.objects.filter(id=id)
    mtrr = Mtrr.objects.filter(id=id)
    morse = Codigo_Morse.objects.filter(id=id)
    radio = Radioaficionados.objects.filter(id=id)
    context = {'vhf':vhf, 'cripto':cripto, 'hf':hf, 'mensaje':mensaje, 'mtrr':mtrr, 'morse':morse, 'radio':radio, 'titulo':titulo}
    return render(request, 'vistas/campeon.html', context)


def mostrar(request, id):
    titulo = Resultados.objects.filter(id=id)
    vhf = Red_VHF.objects.filter(id=id)
    cripto = Criptografia.objects.filter(id=id)
    hf = Red_HF.objects.filter(id=id)
    mensaje = Mensajero.objects.filter(id=id)
    mtrr = Mtrr.objects.filter(id=id)
    morse = Codigo_Morse.objects.filter(id=id)
    radio = Radioaficionados.objects.filter(id=id)
    context = {'vhf':vhf, 'cripto':cripto, 'hf':hf, 'mensaje':mensaje, 'mtrr':mtrr, 'morse':morse, 'radio':radio, 'titulo':titulo}
    return render(request, 'vistas/crear.html', context)
    
def muybueno(request, id):
    titulo = Resultados.objects.filter(id=id)
    vhf = Red_VHF.objects.filter(id=id)
    cripto = Criptografia.objects.filter(id=id)
    hf = Red_HF.objects.filter(id=id)
    mensaje = Mensajero.objects.filter(id=id)
    mtrr = Mtrr.objects.filter(id=id)
    morse = Codigo_Morse.objects.filter(id=id)
    radio = Radioaficionados.objects.filter(id=id)
    context = {'vhf':vhf, 'cripto':cripto, 'hf':hf, 'mensaje':mensaje, 'mtrr':mtrr, 'morse':morse, 'radio':radio, 'titulo':titulo}
    return render(request, 'vistas/muybueno.html', context)  

def bueno(request, id):
    titulo = Resultados.objects.filter(id=id)
    vhf = Red_VHF.objects.filter(id=id)
    cripto = Criptografia.objects.filter(id=id)
    hf = Red_HF.objects.filter(id=id)
    mensaje = Mensajero.objects.filter(id=id)
    mtrr = Mtrr.objects.filter(id=id)
    morse = Codigo_Morse.objects.filter(id=id)
    radio = Radioaficionados.objects.filter(id=id)
    context = {'vhf':vhf, 'cripto':cripto, 'hf':hf, 'mensaje':mensaje, 'mtrr':mtrr, 'morse':morse, 'radio':radio, 'titulo':titulo}
    return render(request, 'vistas/bueno.html', context)  

def suficiente(request, id):
    titulo = Resultados.objects.filter(id=id)
    vhf = Red_VHF.objects.filter(id=id)
    cripto = Criptografia.objects.filter(id=id)
    hf = Red_HF.objects.filter(id=id)
    mensaje = Mensajero.objects.filter(id=id)
    mtrr = Mtrr.objects.filter(id=id)
    morse = Codigo_Morse.objects.filter(id=id)
    radio = Radioaficionados.objects.filter(id=id)
    context = {'vhf':vhf, 'cripto':cripto, 'hf':hf, 'mensaje':mensaje, 'mtrr':mtrr, 'morse':morse, 'radio':radio, 'titulo':titulo}
    return render(request, 'vistas/suficiente.html', context)

def deficiente(request, id):
    titulo = Resultados.objects.filter(id=id)
    vhf = Red_VHF.objects.filter(id=id)
    cripto = Criptografia.objects.filter(id=id)
    hf = Red_HF.objects.filter(id=id)
    mensaje = Mensajero.objects.filter(id=id)
    mtrr = Mtrr.objects.filter(id=id)
    morse = Codigo_Morse.objects.filter(id=id)
    radio = Radioaficionados.objects.filter(id=id)
    context = {'vhf':vhf, 'cripto':cripto, 'hf':hf, 'mensaje':mensaje, 'mtrr':mtrr, 'morse':morse, 'radio':radio, 'titulo':titulo}
    return render(request, 'vistas/deficiente.html', context) 



def pdf(request):
    try:
        resultados = Resultados.objects.all()
        fecha = datetime.now().date()
        img_uno = settings.STATIC_ROOT + '/imagenes/img_uno.png'
        img_dos = settings.STATIC_ROOT + '/imagenes/img_dos.png'
        template = 'pdf/pdf.html'
        context = {'resultados':resultados, 'fecha':fecha , 'img_uno':img_uno, 'img_dos':img_dos}
        template = get_template(template)
        html = template.render(context)
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="reporte.pdf"'
        pisa_status = pisa.CreatePDF(html, dest=response)
        if pisa_status.err:
            messages.error(request, 'Error al generar el PDF')
            return HttpResponse('We had some errors <pre>' + html + '</pre>')
        return response
    except Resultados.DoesNotExist:
        messages.error(request, 'PDF de Resultados no Encontrada')
        return redirect('servicio')
    