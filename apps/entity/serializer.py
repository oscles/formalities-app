from rest_framework import serializers

from .models import Entity


class EntitySerializer(serializers.ModelSerializer):
	class Meta:
		model = Entity
		fields = ('slug', 'name', 'nit', 'address', 'telephone', 'website')
