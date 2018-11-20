from rest_framework.routers import DefaultRouter

from .viewset import AttachmentViewSet
from .viewset import CivilServantViewSet, EntityViewSet, FormalityViewSet

routes = DefaultRouter()
routes.register('funcionarios', CivilServantViewSet)
routes.register('entidades', EntityViewSet)
routes.register('tramites', FormalityViewSet)
routes.register('attachments', AttachmentViewSet)