from django.db import models
from django.utils.text import slugify

from ..core.mixins import TimeStampedModel


# Create your models here.
class Entity(TimeStampedModel):
	slug = models.SlugField(unique=True, blank=True, null=True)
	name = models.CharField(max_length=45)
	nit = models.CharField(max_length=45)
	address = models.CharField(max_length=100)
	telephone = models.CharField(max_length=45)
	website = models.URLField(max_length=100, blank=True, null=True)

	def __str__(self):
		return self.name

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super().save(*args, **kwargs)
