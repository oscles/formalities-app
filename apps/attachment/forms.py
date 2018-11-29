from django.forms import ModelForm
from .models import AttachmentFormality


class AttachmentForm(ModelForm):
	class Meta:
		model = AttachmentFormality
		fields = ('formality', 'attachment',)
