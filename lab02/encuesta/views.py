from django.shortcuts import render
import math

def index(request):
    context = {
        'titulo': "Formulario",
    }
    return render(request, 'encuesta/formulario.html', context)

def enviar(request):
    context = {
        'titulo': "Respuesta",
        'nombre': request.POST.get('nombre', ''),
        'clave': request.POST.get('password', ''),
        'educacion': request.POST.get('educacion', ''),
        'nacionalidad': request.POST.get('nacionalidad', ''),
        'idiomas': request.POST.getlist('idiomas'),
        'correo': request.POST.get('email', ''),
        'website': request.POST.get('sitioweb', ''),
    }
    return render(request, 'encuesta/respuesta.html', context)

#############################################################################

def formulario_operacion(request):
    return render(request, 'encuesta/operaciones.html')

def calcular_operacion(request):
    if request.method == 'POST':
        num1 = float(request.POST.get('num1', 0))
        num2 = float(request.POST.get('num2', 0))
        operacion = request.POST.get('operacion')
        
        if operacion == 'suma':
            res = num1 + num2
            texto = f"La suma de {num1} + {num2} = {res}"
        elif operacion == 'resta':
            res = num1 - num2
            texto = f"La resta de {num1} - {num2} = {res}"
        elif operacion == 'multiplicacion':
            res = num1 * num2
            texto = f"La multiplicación de {num1} * {num2} = {res}"
        else:
            texto = "Operación no válida"
            
        return render(request, 'encuesta/operaciones.html', {'resultado': texto})
    return render(request, 'encuesta/operaciones.html')

def formulario_cilindro(request):
    return render(request, 'encuesta/cilindro.html')

def calcular_cilindro(request):
    if request.method == 'POST':
        diametro = float(request.POST.get('diametro', 0))
        altura = float(request.POST.get('altura', 0))
        radio = diametro / 2
        
        # V = π * r² * h
        volumen = math.pi * (radio ** 2) * altura
        
        return render(request, 'encuesta/cilindro.html', {'volumen': volumen})
    return render(request, 'encuesta/cilindro.html')
