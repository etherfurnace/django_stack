from django.apps import AppConfig


class FrameworkConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.framework'

    def ready(self):
        import apps.framework.signals
