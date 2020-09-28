from .services.search_services import get_objects_from_model_with_filter
from django.shortcuts import render
from django.views.generic.list import ListView


class Search(ListView):
	''' Controller class for search line '''

	template_name = 'search.html'

	def get_queryset(self):
		return get_objects_from_model_with_filter(self)

	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(*args, **kwargs)
		context['q'] = self.request.GET.get('q')
		return context
