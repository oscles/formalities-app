from django.db import models


class ManagerMain(models.Manager):
	def get_queryset(self):
		return super(ManagerMain, self) \
			.get_queryset() \
			.filter(deleted_at__isnull=True)


class ManagerAllMain(models.Manager):
	def get_queryset(self):
		return super(ManagerAllMain, self).get_queryset()


