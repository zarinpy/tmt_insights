from django.apps import AppConfig


class CommonAppConfig(AppConfig):
    name = "apps.common"
    verbose_name = "Common"

    def ready(self):
        """
        Common system checks
        Common signal registration
        """
        try:
            import apps.common.receivers  # noqa F401
        except ImportError:
            pass
