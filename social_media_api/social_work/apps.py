from django.apps import AppConfig


class SocialWorkConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'social_work'

    def ready(self):
        import social_work.signals
