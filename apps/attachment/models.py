from datetime import datetime

from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.
from ..formality.models import Formality


class AttachmentFormality(models.Model):
	formality = models.ForeignKey(
		Formality,
		related_name='attachments',
		on_delete=models.CASCADE
	)
	attachment = models.FileField(
		upload_to='formality_docs/',
		validators=[FileExtensionValidator(
			allowed_extensions=[
				'xls', 'xlsx', 'pdf',
				'doc', 'docx', 'odt',
				'pptx'
			]
		)],
		max_length=45
	)

	def save(self, *args, **kwargs):
		ext = self.attachment.name.split('.')[-1]
		self.attachment.name = f'{datetime.today()}.{ext}'
		super().save(*args, **kwargs)

	def delete(self, using=None, keep_parents=False):
		self.attachment.delete(save=False)
		return super().delete(using, keep_parents)

	def __str__(self):
		extension, name = self.attachment.name.split('/')
		return name
