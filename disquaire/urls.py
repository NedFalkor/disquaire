
from django.conf import settings
from django.urls import include, re_path, path  # Remarquez l'importation corrigée ici
from django.contrib import admin

urlpatterns = [
    path('store/',include('store.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        re_path(r'^_debug_/', include(debug_toolbar.urls)),
    ] + urlpatterns