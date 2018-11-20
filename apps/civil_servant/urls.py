from django.urls import path

from ..civil_servant.views import (
	HomeTemplateView,
	CivilServantCreateView,
	CivilServantListView,
	CivilServantDeleteView,
	RegisterUserCreateView
)

app_name = 'civil_servant'

urlpatterns = [
	path('', HomeTemplateView.as_view(), name='home'),
	path('listar/', CivilServantListView.as_view(), name='listar'),
	path('crear/', CivilServantCreateView.as_view(), name='crear'),
	path('eliminar/<slug>/', CivilServantDeleteView.as_view(), name='eliminar'),
	path('register/', RegisterUserCreateView.as_view(), name='register-user'),
]
