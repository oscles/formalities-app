from django.urls import path

from ..formality.views import (
	FormalityListView,
	FormalityCreateView,
	FormalityDeleteView,
)

app_name = 'formality'

urlpatterns = [
	path('crear/', FormalityCreateView.as_view(), name='crear'),
	path('listar/', FormalityListView.as_view(), name='listar'),
	path('eliminar/<slug>/', FormalityDeleteView.as_view(), name='eliminar'),
]
