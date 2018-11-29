from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView

from apps.core.mixins import DeleteViewMixin
from ..attachment.models import AttachmentFormality
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
		form_class = self.get_form_class()
		form = self.get_form(form_class)
		files = request.FILES.getlist('file')
		if form.is_valid():
			instance = form.save()
			for file in files:
				AttachmentFormality(formality=instance, attachment=file).save()
			messages.success(request, self.success_message % request.POST)
			return HttpResponseRedirect(reverse_lazy('formality:crear'))
		else:
			return render(request, self.template_name, {'form': form})


class FormalityListView(ListViewMixin):
	template_name = 'formality/list.html'
	model = Formality
	context_object_name = 'formalities'
	form_class = FormalityForm
	serializer_class = FormalitySerializer


class FormalityDeleteView(DeleteViewMixin, DeleteView):
	model = Formality
	success_url = reverse_lazy('formality:crear')
