from django.shortcuts import render, redirect
from itertools import chain
from .models import Resultados, Red_VHF, Criptografia, Red_HF, Mensajero , Mtrr, Codigo_Morse, Radioaficionados
from .forms import ResultadosForm, Red_VhForm, CriptografiaForm, Red_HForm, MensajeroForm, MtrrForm, Codigo_MorseForm, RadioaficionadosForm


def principal(request):
    resultados = Resultados.objects.all()
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
        return redirect('principal')
    
   
    context = {'formularios': formularios, 'resultados':resultados}
    return render(request, 'vistas/index.html', context)


def crear(request, id):
    resultado = Resultados.objects.get(id=id)
    uno = Red_VHF.objects.filter(id=id)
    context = { 'resultado':resultado, 'uno':uno}
    return render(request, 'vistas/index.html', context)
    
    
    