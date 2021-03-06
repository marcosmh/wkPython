from django.shortcuts import render

from .forms import RegForm
from .models import Registrado

# Create your views here.
def inicio(request):
    titulo = "Django"
    if request.user.is_authenticated:
        titulo = "Bienvenido %s " %(request.user)
    form = RegForm(request.POST or None)
    if form.is_valid():
        form_data = form.cleaned_data
        correo = form_data.get("email")
        nomb = form_data.get("nombre")
        obj = Registrado.objects.create(email=correo,nombre=nomb)

    context = {
        "titulo" : titulo,
        "el_form" : form,
    }
    return render(request,"inicio.html",context)
