from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls', namespace='main'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = 'pages.views.page_404'
handler500 = 'pages.views.page_500'
handler502 = 'pages.views.page_502'
handler503 = 'pages.views.page_503'
