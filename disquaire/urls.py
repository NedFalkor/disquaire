
from django.conf import settings
from django.urls import include, re_path, path
from django.contrib import admin

urlpatterns = [
    path('',include('store.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('^_debug_/', include(debug_toolbar.urls)),
    ] + urlpatterns