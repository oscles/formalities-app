from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import models
from django.http import JsonResponse, HttpResponseRedirect
from django.utils import timezone
from django.views.generic import ListView

from .manager import ManagerMain, ManagerAllMain


class TimeStampedModel(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	deleted_at = models.DateTimeField(blank=True, null=True)
	objects = ManagerMain()
	objects_all = ManagerAllMain()

	class Meta:
		abstract = True


class ListViewMixin(LoginRequiredMixin, ListView):
	form_class = None
	serializer_class = None
	model = None

	def get(self, request, *args, **kwargs):
		if request.is_ajax():
			slug = self.request.GET.get('slug', None)
			visited = self.request.GET.get('visited', None)
			instance = self.model.objects.get(slug=slug)
			if visited:
				self._update_visited(request, instance, visited, *args, **kwargs)
			serializer = self.serializer_class(instance=instance)
			return JsonResponse(serializer.data)
		return super().get(request, *args, **kwargs)

	def _update_visited(self, request, instance, *args, **kwargs):
		instance.visited += 1
		instance.save()
		return super().get(request, *args, **kwargs)

	def get_context_data(self, object_list=None, *args, **kwargs):
		kwargs.update({
			'form': self.form_class,
			'total': self.model.objects.count()
		})
		return super().get_context_data(object_list=object_list, **kwargs)


class DeleteViewMixin:
	success_url = None

	def post(self, request, *args, **kwargs):
		return self.delete(request, *args, **kwargs)

	def delete(self, request, *args, **kwargs):
		instance = self.get_object()
		instance.deleted_at = timezone.now()
		instance.save()
		return HttpResponseRedirect(self.success_url)
