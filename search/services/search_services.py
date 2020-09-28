from art.models import Seed
from django.db.models import Q


def get_objects_from_model_with_filter(self):
	''' Take a object from the Seed.model '''

	return Seed.objects.filter(name__icontains = self.request.GET.get('q'))
