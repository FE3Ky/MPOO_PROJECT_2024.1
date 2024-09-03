from django.contrib import admin

from vacinacao.models import Funcionario, Paciente, Fabricante, Vacina, Agendamento

# Register your models here.


admin.site.register(Funcionario)
admin.site.register(Fabricante)
admin.site.register(Paciente)
admin.site.register(Vacina)


class AgendamentoAdmin(admin.ModelAdmin):
    list_display = ('paciente', 'vacina', 'data', 'status')


admin.site.register(Agendamento, AgendamentoAdmin)
