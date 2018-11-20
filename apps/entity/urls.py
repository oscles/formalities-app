from django.urls import path

from .views import EntityListView, EntityCreateView, EntityDeleteView

app_name = 'entity'

urlpatterns = [
	path('crear/', EntityCreateView.as_view(), name='crear'),
	path('listar/', EntityListView.as_view(), name='listar'),
	path('eliminar/<slug>/', EntityDeleteView.as_view(), name='eliminar'),
]