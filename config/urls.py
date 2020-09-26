from django.contrib import admin
from django.urls import path
from shop.views import (
    view_main_page,
    show_seeds_by_current_rubric,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', view_main_page, name="view_main_page"),
]
