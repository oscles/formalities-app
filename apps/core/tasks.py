from django.template import Context
from django.template.loader import render_to_string

from tramite.settings import EMAIL_HOST_PASSWORD
from django.core.mail import EmailMultiAlternatives, EmailMessage
from celery import current_app

app = current_app


@app.task
def send_email(formality_name, username, to):
	subject = 'Ud has sido asignado a un nuevo trámite.'
	from_email = EMAIL_HOST_PASSWORD
	text_content = 'Tu Trámite'
	html_content = render_to_string(
		template_name='emails.html',
		context={
			'formality_name': formality_name,
			'username': username,
			'url': f'http://localhost:8000/tramites/listar/'
		}
	)
	email = EmailMultiAlternatives(
		subject=subject,
		body=text_content,
		from_email=from_email,
		to=[to]
	)
	email.attach_alternative(html_content, "text/html")
	email.send(fail_silently=True)
