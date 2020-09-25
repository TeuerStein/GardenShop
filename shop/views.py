from django.shortcuts import render
from .models import Seed
from .services.shop_services import take_all_objects_from_model


def view_main_page(request):
    ''' Show main page without any object '''

    return render(request, 'index.html', {})

def show_all_seeds(request):
    ''' Show all objects from the Seed model on a page '''

    context = take_all_objects_from_model(request)

    return render(request, 'shop_page.html', context)
