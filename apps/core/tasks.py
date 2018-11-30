from django.template.loader import render_to_string

from tramite.settings import EMAIL_HOST_PASSWORD, EMAIL_ADMIN
from django.core.mail import EmailMultiAlternatives
from celery import current_app

app = current_app


def base_send_email(from_email, html_content, subject, text_content, to):
	email = EmailMultiAlternatives(
		subject=subject,
		body=text_content,
		from_email=from_email,
		to=[to]
	)
	email.attach_alternative(html_content, "text/html")
	email.send(fail_silently=True)


@app.task
def send_email(formality_name, username, to):
	subject = 'Ud has sido asignado a un nuevo trámite.'
	from_email = EMAIL_HOST_PASSWORD
	text_content = 'Tu Trámite'
	html_content = render_to_string(
		template_name='emails.html',
		context={
			'is_formality': True,
			'formality_name': formality_name,
			'username': username,
			'url': f'http://localhost:8000/tramites/listar/'
		}
	)
	base_send_email(from_email, html_content, subject, text_content, to)


@app.task
def send_message(*args, **kwargs):
	subject = 'Hay un nuevo mensaje'
	from_email = EMAIL_HOST_PASSWORD
	to = EMAIL_ADMIN
	text_content = 'Tu Trámite'
	html_content = render_to_string(
		template_name='emails.html',
		context={
			'is_message': True,
			'full_name': kwargs.get('name', None),
			'telephone': kwargs.get('phone', None),
			'email': kwargs.get('email', None),
			'message': kwargs.get('message', None),
		}
	)
	base_send_email(from_email, html_content, subject, text_content, *to)


@app.task
def send_subscription(email):
	subject = 'Hay una nueva subscripción'
	from_email = EMAIL_HOST_PASSWORD
	to = [*EMAIL_ADMIN]
	text_content = 'Tu Trámite'
	html_content = render_to_string(
		template_name='emails.html',
		context={
			'is_subscription': True,
			'sender': email
		}
	)
	base_send_email(from_email, html_content, subject, text_content, to)
