from django.db import models

# Create your models here.
from django.utils.text import slugify

from ..core.mixins import TimeStampedModel
from ..civil_servant.models import CivilServant


class Formality(TimeStampedModel):
	slug = models.SlugField(unique=True, blank=True, null=True)
	name = models.CharField(max_length=100)
	description = models.TextField(max_length=1000, blank=True, null=True)
	requirements = models.TextField(max_length=1000)
	realization_form = models.CharField(max_length=100, blank=True, null=True)
	schedule = models.CharField(max_length=100, blank=True, null=True)
	civil_servant = models.ForeignKey(
		CivilServant,
		related_name='formalities',
		on_delete=models.CASCADE
	)
	visited = models.IntegerField(blank=True, null=True, default=0)

	class Meta:
		ordering = ('-created_at',)

	def __str__(self):
		return self.name

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super().save(*args, **kwargs)
