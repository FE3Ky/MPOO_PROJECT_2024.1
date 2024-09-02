from django.shortcuts import render
from django.views.generic import ListView

from vacinacao.models import Paciente


# Create your views here.

def index(request):
    return render(request, "index.html")

class PacienteListView(ListView):
    template_name = "pacienteList.html"
    model = Paciente
    context_object_name = "pacientes"