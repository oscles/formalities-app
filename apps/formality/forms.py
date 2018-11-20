from django import forms

from .models import Formality


class FormalityForm(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields.get('civil_servant').empty_label = '- Seleccione -'

	class Meta:
		model = Formality
		fields = (
			'name',
			'description',
			'requirements',
			'realization_form',
			'schedule',
			'civil_servant'
		)

		widgets = {
			'name': forms.TextInput(attrs={
				'class': 'form-control',
				'placeholder': 'Ingrese nombre de la entidad...'
			}),
			'description': forms.Textarea(attrs={
				'class': 'form-control',
				'placeholder': 'Descripción del trámite...',
				'rows': '3'
			})
			,
			'requirements': forms.Textarea(attrs={
				'class': 'form-control',
				'placeholder': 'Descripción de los requisitos...',
				'rows': '3'
			}),
			'realization_form': forms.TextInput(attrs={
				'class': 'form-control',
				'placeholder': 'Ingrese la forma de realizacíon...'
			}),
			'schedule': forms.TextInput(attrs={
				'class': 'form-control',
				'placeholder': 'Ingrese el horario...'
			}),
			'civil_servant': forms.Select(attrs={
				'class': 'form-control'
			})

		}
