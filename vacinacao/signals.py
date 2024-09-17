from django.db.models.signals import post_save
from django.dispatch import receiver

from vacinacao.choices import STATUS_CHOICES
from vacinacao.models import Agendamento, Registro


@receiver(post_save, sender=Agendamento)
def create_registro(sender, instance, created, **kwargs):
    if not created and instance.status == STATUS_CHOICES[1][0]:
        Registro.objects.create(
            paciente=instance.paciente,
            vacina=instance.vacina,
            funcionario=instance.funcionario,
            agendamento=instance,
        )

