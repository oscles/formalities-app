# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView

from .serializer import EntitySerializer
from .forms import EntityForm
from ..core.mixins import ListViewMixin, DeleteViewMixin
from .models import Entity


class EntityCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
	template_name = 'entity/create.html'
	model = Entity
	form_class = EntityForm
	success_message = 'La entidad %(name)s ha sido creada satisfactoriamente'
	success_url = reverse_lazy('entity:crear')


class EntityListView(ListViewMixin):
	template_name = 'entity/list.html'
	model = Entity
	context_object_name = 'entities'
	form_class = EntityForm
	serializer_class = EntitySerializer


class EntityDeleteView(DeleteViewMixin, DeleteView):
	model = Entity
	success_url = reverse_lazy('entity:crear')

