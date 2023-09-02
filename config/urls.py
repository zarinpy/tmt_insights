from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path(
        'swagger',
        SpectacularSwaggerView.as_view(url_name='schema'), 
        name='swagger-ui',
    ),
    path('admin/', admin.site.urls),
]
