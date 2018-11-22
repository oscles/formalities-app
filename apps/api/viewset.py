from django.db.models import Count
from rest_framework import viewsets, renderers
from rest_framework.decorators import action
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.response import Response

from apps.attachment.serializer import AttachmentSerializer
from ..attachment.models import AttachmentFormality
from ..formality.models import Formality
from ..formality.serializer import FormalitySerializer
from ..entity.models import Entity
from ..entity.serializer import EntitySerializer
from ..civil_servant.models import CivilServant
from ..civil_servant.serializer import CivilServantSerializer, \
	CivilServantBasicInformationSerializer


class CivilServantViewSet(viewsets.ModelViewSet):
	queryset = CivilServant.objects_all.all()
	serializer_class = CivilServantSerializer
	lookup_field = 'slug'

	def update(self, request, *args, **kwargs):
		instance = self.get_object()
		serializer = CivilServantBasicInformationSerializer(
			instance, data=request.data
		)
		serializer.is_valid(raise_exception=True)
		self.perform_update(serializer)
		return Response(serializer.data)


class EntityViewSet(viewsets.ModelViewSet):
	queryset = Entity.objects_all.all()
	serializer_class = EntitySerializer
	lookup_field = 'slug'


class AttachmentViewSet(viewsets.ModelViewSet):
	queryset = AttachmentFormality.objects.all()
	serializer_class = AttachmentSerializer


class FormalityViewSet(viewsets.ModelViewSet):
	queryset = Formality.objects_all.all()
	serializer_class = FormalitySerializer
	parser_classes = (MultiPartParser, FormParser,)
	lookup_field = 'slug'

	@action(detail=False)
	def counter(self, request, *args, **kwargs):
		response = self._get_response(formalities=Formality)
		return Response(response)

	def _get_response(self, *args, **kwargs):
		response = {}
		is_superuser = self.request.user.is_superuser
		if is_superuser:
			for attr, value in kwargs.items():
				response.update({attr: self._get_for_month(value.objects_all)})
		else:
			for attr, value in kwargs.items():
				response.update({attr: self._get_for_month(value.objects)})
		return response

	def _get_for_month(self, model_manager):
		return model_manager.values('created_at__month') \
			.annotate(total=Count('created_at__month')) \
			.order_by('created_at__month')

	def list(self, request, *args, **kwargs):
		if self.request.query_params:
			query_params = self.request.query_params
			slug = query_params.get('slug', None)
			if 'visited' in query_params and 'slug' in query_params:
				serializer = self.get_serializer(self.increment_visit(slug))
				return Response(serializer.data)
		return super().list(request, *args, **kwargs)

	def increment_visit(self, slug):
		instance = Formality.objects_all.get(slug=slug)
		serializer = self.serializer_class(
			instance,
			data={'visited': instance.visited + 1},
			partial=True
		)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		return instance

	def update(self, request, *args, **kwargs):
		print(request.data)
		# print(self.request.FILES['file'].size)
		return super().update(request, *args, **kwargs)
