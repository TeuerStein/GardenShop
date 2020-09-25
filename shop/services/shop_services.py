def take_all_objects_from_model(request):
    ''' Take all objects from the Seed model
    and return context for a page '''

    objects = Seed.objects.all()

    context = {'objects': objects}

    return context
