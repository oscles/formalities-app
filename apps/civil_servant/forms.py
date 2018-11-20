from django.contrib.auth.models import User
from django import forms

from .models import CivilServant


class CivilServantForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields.get('entity').empty_label = '- Seleccione -'

	class Meta:
		model = CivilServant
		fields = (
			'first_name', 'last_name', 'email',
			'identification_type', 'identification', 'telephone',
			'address', 'entity', 'username', 'password', 'avatar'
		)

		widgets = {
			'username': forms.TextInput(attrs={'class': 'form-control'}),
			'first_name': forms.TextInput(attrs={'class': 'form-control'}),
			'last_name': forms.TextInput(attrs={'class': 'form-control'}),
			'email': forms.EmailInput(attrs={'class': 'form-control'}),
			'password': forms.PasswordInput(attrs={'class': 'form-control'}),
			'identification_type': forms.Select(
				attrs={'class': 'form-control'}
			),
			'identification': forms.TextInput(attrs={'class': 'form-control'}),
			'telephone': forms.TextInput(attrs={'class': 'form-control'}),
			'address': forms.TextInput(attrs={'class': 'form-control'}),
			'entity': forms.Select(attrs={
				'class': 'form-control',
				'data-live-search': 'true',
				'data-size': '6',
			}),
			'avatar': forms.FileInput()
		}


class UserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('username', 'email', 'password')

	def clean_email(self):
		email = self.cleaned_data.get('email', None)
		if email is None:
			self.add_error('email', 'Este campo es obligatorio')
		if User.objects.filter(email=email).exists():
			self.add_error('email', 'Hay un usuario que usa este email')
		return email
