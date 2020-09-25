from django.contrib import admin
from django.urls import path
from shop.views import view_main_page
#ßfrom django.conf import settings
#from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', view_main_page, name="view_main_page"),
]

#if settings.DEBUG:
    #urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    #urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
