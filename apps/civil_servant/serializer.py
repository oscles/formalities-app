from rest_framework import serializers

from .models import CivilServant


class CivilServantBasicInformationSerializer(serializers.ModelSerializer):
	class Meta:
		model = CivilServant
		fields = (
			'slug', 'first_name', 'last_name', 'email',
			'identification_type', 'identification', 'telephone',
			'address', 'entity', 'avatar'
		)


class CivilServantSerializer(serializers.ModelSerializer):
	class Meta:
		model = CivilServant
		fields = (
			'slug', 'first_name', 'last_name', 'email',
			'identification_type', 'identification', 'telephone',
			'address', 'entity', 'username', 'password', 'avatar'
		)
