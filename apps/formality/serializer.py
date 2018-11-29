from rest_framework import serializers

from ..attachment.models import AttachmentFormality
from ..attachment.serializer import AttachmentSerializer
from .models import Formality


class FormalitySerializer(serializers.ModelSerializer):
	attachments = serializers.SerializerMethodField()
	civil_get_full_name = serializers.ReadOnlyField(
		source='civil_servant.get_full_name'
	)

	def get_attachments(self, instance):
		query = AttachmentFormality.objects.filter(formality=instance)
		serializer = AttachmentSerializer(query, many=True)
		return serializer.data

	class Meta:
		model = Formality
		fields = (
			'slug',
			'id',
			'name',
			'description',
			'requirements',
			'realization_form',
			'schedule',
			'civil_servant',
			'civil_get_full_name',
			'visited',
			'created_at',
			'attachments'
		)
