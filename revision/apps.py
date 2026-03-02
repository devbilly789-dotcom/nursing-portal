from django.apps import AppConfig


class RevisionConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'revision'

    def ready(self):
        import revision.signals