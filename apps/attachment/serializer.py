from rest_framework import serializers

from .models import AttachmentFormality


class AttachmentSerializer(serializers.ModelSerializer):
	class Meta:
		model = AttachmentFormality
		fields = ('id', 'formality', 'attachment')
