from django.apps import AppConfig

class RandomapplicationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'randomApplication'

    def ready(self):
        import randomApplication.signals
