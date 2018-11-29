"""tramite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

    path('articles/<slug:title>/', views.article, name='article-detail'),
    path('articles/<slug:title>/<int:section>/', views.section, name='article-section'),
"""

from django.contrib import admin
from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from apps.api.router import routes
from apps.civil_servant.views import HomeAnonymousUserTemplateView

handler404 = 'apps.core.view_errors.page_not_found_view'
handler500 = 'apps.core.view_errors.server_error_view'

urlpatterns = [
	path('', HomeAnonymousUserTemplateView.as_view(), name='index'),
	path('login/', LoginView.as_view(template_name='login.html'),
	     name='login'),
	path('logout/', LogoutView.as_view(), name='logout'),
	path('admin/', admin.site.urls),
	path('funcionarios/', include('apps.civil_servant.urls')),
	path('entidades/', include('apps.entity.urls')),
	path('tramites/', include('apps.formality.urls')),
	path('api/', include(routes.urls)),
] + (static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))
