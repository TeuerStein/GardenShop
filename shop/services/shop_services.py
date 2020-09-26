from shop.models import Seed, Rubric


def rubrics_for_shop_page(request):
    pass

def take_objects_from_model_by_current_rubric(request, rubric_id):
    ''' Take objects from the Seed model
    with filter by rubric and return context for a page '''

    objects = Seed.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)

    context = {
        'objects': objects,
        'rubrics': rubrics,
        'current_rubric': current_rubric,
    }

    return context
