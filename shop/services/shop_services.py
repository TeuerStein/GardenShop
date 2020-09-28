from shop.models import Seed, Rubric
from django.core.paginator import Paginator


def rubrics_for_shop_page(request):
    rubrics = Rubric.objects.all()

    context = {'rubrics': rubrics}

    return context

def take_objects_from_model_by_current_rubric(request, rubric_id):
    ''' Take objects from the Seed model
    with filter by rubric and pagination
    return context for a page '''

    objects = Seed.objects.filter(rubric=rubric_id)

    paginator = Paginator(objects, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)

    context = {
        'page_obj': page_obj,
        'rubrics': rubrics,
        'current_rubric': current_rubric,
    }

    return context
