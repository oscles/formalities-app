from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User

# Create your views here.
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import (
	TemplateView, CreateView, DeleteView,
	UpdateView
)

from ..core.mixins import DeleteViewMixin
from .forms import CivilServantForm
from .serializer import CivilServantSerializer
from ..civil_servant.forms import UserForm
from ..core.mixins import ListViewMixin
from ..formality.models import Formality
from ..entity.models import Entity
from ..civil_servant.models import CivilServant


class HomeTemplateView(LoginRequiredMixin, TemplateView):
	template_name = 'base.html'

	def get_context_data(self, **kwargs):
		formalities = Formality.objects_all.all()
		kwargs.update({
			'total_civil_servant': CivilServant.objects_all.count(),
			'total_entities': Entity.objects_all.count(),
			'total_formalities': formalities.count(),
			'formalities_recients': formalities.order_by('-visited')[:10]
		})
		return super().get_context_data(**kwargs)


class CivilServantCreateView(
	SuccessMessageMixin,
	LoginRequiredMixin,
	CreateView
):
	model = CivilServant
	template_name = 'civil_servant/create.html'
	form_class = CivilServantForm
	success_url = reverse_lazy('civil_servant:crear')
	success_message = 'El funcionario %(first_name)s %(last_name)s' \
	                  ' ha sido creado satisfactoriamente'


class CivilServantListView(ListViewMixin):
	template_name = 'civil_servant/list.html'
	model = CivilServant
	context_object_name = 'civil_servants'
	form_class = CivilServantForm
	serializer_class = CivilServantSerializer


class CivilServantDeleteView(DeleteViewMixin, DeleteView):
	model = CivilServant
	success_url = reverse_lazy('civil_servant:crear')


class RegisterUserCreateView(SuccessMessageMixin, CreateView):
	template_name = 'register.html'
	form_class = UserForm
	model = User
	success_url = reverse_lazy('civil_servant:register-user')
	success_message = 'El usuario ha sido creado satisfactoriamente'
