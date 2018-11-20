from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from django.db import models

# Create your models here.
from django.utils.text import slugify

from ..core.mixins import TimeStampedModel
from ..entity.models import Entity


def civil_servant_path(instance, filename):
	extension = filename.split('.')[-1]
	return f'avatars/{instance.identification}.{extension}'


class CivilServant(User, TimeStampedModel):
	IDENTIFICATION_TYPE = (
		('', '- Seleccione -'),
		('cc', 'Cédula de ciudadania'),
		('ce', 'Cédula de extranjería'),
		('pasaporte', 'Pasaporte')
	)
	slug = models.SlugField(unique=True, blank=True, null=True)
	identification_type = models.CharField(
		max_length=45,
		choices=IDENTIFICATION_TYPE
	)
	identification = models.CharField(
		max_length=45,
		unique=True,
		verbose_name='N° ID'
	)
	telephone = models.CharField(max_length=45)
	address = models.CharField(max_length=100)
	avatar = models.ImageField(
		upload_to=civil_servant_path,
		validators=[
			FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg'])
		],
		blank=True,
		null=True
	)
	entity = models.ForeignKey(
		Entity,
		related_name='civil_servants',
		on_delete=models.CASCADE
	)

	def __str__(self):
		return self.get_full_name()

	def save(self, *args, **kwargs):
		self.slug = slugify(self.get_full_name())
		self.set_password(self.password)
		super().save(*args, **kwargs)
