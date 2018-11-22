from tramite.settings import EMAIL_HOST_PASSWORD
from django.core.mail import EmailMultiAlternatives, EmailMessage
from celery import current_app

app = current_app


@app.task(bind=True)
def send_email(self, *args, **kwargs):
	subject, from_email, to = 'hello', EMAIL_HOST_PASSWORD, 'osnaiderluis94@hotmail.com'
	text_content = 'This is an important message.'
	html_content = '<p>This is an <strong>important</strong> message.</p>'
	email = EmailMultiAlternatives(subject, text_content, from_email, [to])
	email.attach_alternative(html_content, "text/html")
	email.send(fail_silently=False)
