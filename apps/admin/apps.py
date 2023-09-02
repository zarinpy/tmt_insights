from django.contrib.admin import apps as adminApps
from django.utils.translation import gettext_lazy
from django.contrib.admin.sites import AdminSite as BaseAdmin
from django.contrib.admin.options import ModelAdmin


class AdminSite(BaseAdmin):
    # Text to put at the end of each page's <title>.
    site_title = gettext_lazy("django admin site")

    # Text to put in each page's <h1>.
    site_header = gettext_lazy("django admin panel")

    # Text to put at the top of the admin index page.
    index_title = gettext_lazy("django administration")

    def admin_view(self, view, cacheable=False):
        def wrapper(func):
            def wrapped(*args, **kwargs):
                instance = getattr(func, '__self__', None)
                if isinstance(instance, ModelAdmin):
                    new_instance = type(instance)(instance.model, instance.admin_site)
                    return func.__func__(new_instance, *args, **kwargs)
                return func(*args, **kwargs)

            return wrapped

        return super().admin_view(wrapper(view), cacheable=False)


class AdminConfig(adminApps.AdminConfig):
    default_site = 'apps.admin.apps.AdminSite'
    label = 'admin'
