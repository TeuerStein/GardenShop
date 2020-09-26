from django.shortcuts import render
from .services.shop_services import take_objects_from_model_by_current_rubric


def view_main_page(request):
    ''' Show main page without any object '''

    context = rubrics_for_shop_page(request)

    return render(request, 'index.html', {})

def show_seeds_by_current_rubric(request, rubric_id):
    ''' Show objects from the Seed model
    with filter by rubric on a page '''

    context = take_objects_from_model_by_current_rubric(request, rubric_id)

    return render(request, 'shop_page.html', context)
