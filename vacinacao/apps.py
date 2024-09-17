from django.apps import AppConfig


class VacinacaoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'vacinacao'

    def ready(self):
        import vacinacao.signals
