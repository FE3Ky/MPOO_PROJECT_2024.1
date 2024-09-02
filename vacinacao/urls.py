from django.urls import path

from vacinacao import views

urlpatterns = [
    path('pacientes', views.PacienteListView.as_view(), name='pacientes'),
]