from django.shortcuts import render


def page_not_found_view(request):
	return render(request, template_name='404.html')


def server_error_view(request):
	return render(request, template_name='500.html')
