from django.contrib import admin

from vacinacao.choices import STATUS_CHOICES
from vacinacao.models import Funcionario, Paciente, Fabricante, Vacina, Agendamento, Registro

# Register your models here.


admin.site.register(Funcionario)
admin.site.register(Fabricante)
admin.site.register(Paciente)
admin.site.register(Vacina)


class AgendamentoAdmin(admin.ModelAdmin):
    list_display = ('paciente', 'vacina', 'data', 'status')

    def has_change_permission(self, request, obj=None):
        return obj.status == STATUS_CHOICES[0][0] if obj is not None else False


class RegistroAdmin(admin.ModelAdmin):
    list_display = ('paciente', 'vacina', 'funcionario', 'agendamento', 'data')
    list_filter = ('paciente__nome', 'vacina__tipo', 'funcionario__nome', 'data')

    def has_change_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(Agendamento, AgendamentoAdmin)
admin.site.register(Registro, RegistroAdmin)
