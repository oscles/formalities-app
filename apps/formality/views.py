from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView

from apps.core.mixins import DeleteViewMixin
from .serializer import FormalitySerializer
from .forms import FormalityForm
from .models import Formality
from ..core.mixins import ListViewMixin


class FormalityCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
	template_name = 'formality/create.html'
	model = Formality
	form_class = FormalityForm
	success_url = reverse_lazy('formality:crear')
	success_message = 'El trámite %(name)s ha sido creado satisfactoriamente'

	def post(self, request, *args, **kwargs):
		form = self.get_form()
		print(form)
		if form.is_valid():
			return self.form_valid(form)
		else:
			return self.form_invalid(form)


class FormalityListView(ListViewMixin):
	template_name = 'formality/list.html'
	model = Formality
	context_object_name = 'formalities'
	form_class = FormalityForm
	serializer_class = FormalitySerializer


class FormalityDeleteView(DeleteViewMixin, DeleteView):
	model = Formality
	success_url = reverse_lazy('formality:crear')
