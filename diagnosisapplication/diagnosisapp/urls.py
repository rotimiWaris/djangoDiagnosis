from django.contrib import admin
from django.urls import path, include, re_path
from . import views
from django.conf import settings
from django.views.static import serve
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    path('admin/', admin.site.urls),
    path('', views.homepage),
    path('diagnosis/', include('diagnosis.urls')),
    path('users/', include('users.urls')),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/docs/', SpectacularSwaggerView.as_view(url_name="schema"))
]

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)