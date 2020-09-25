from django.contrib import admin
from django.urls import path
from shop.views import view_main_page


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', view_main_page, name="view_main_page"),
]
