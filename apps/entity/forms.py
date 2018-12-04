from django import forms

from .models import Entity


class EntityForm(forms.ModelForm):
	class Meta:
		model = Entity
		fields = ('name', 'nit', 'address', 'telephone', 'website')

		labels = {
			'name': 'Nombre',
			'nit': 'NIT',
			'address': 'Dirección',
			'telephone': 'Teléfono',
			'website': 'Página Web'
		}

		widgets = {
			'name': forms.TextInput(attrs={
				'class': 'form-control',
				'placeholder': 'Ministerio de las Tecnologías de la Información'
			}),
			'nit': forms.TextInput(attrs={
				'class': 'form-control',
				'placeholder': 'Ingrese su NIT...'
			}),
			'address': forms.TextInput(attrs={
				'class': 'form-control',
				'placeholder': 'Cartagena - Colombia'
			}),
			'telephone': forms.TextInput(attrs={
				'class': 'form-control',
				'placeholder': 'Ingrese su número telefónico'
			}),
			'website': forms.URLInput(attrs={
				'class': 'form-control',
				'placeholder': 'https://www.mintic.com'
			})
		}
