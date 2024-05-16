from django.apps import AppConfig


class PortConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'port'

    def ready(self):
        import port.signals
    
